import operator
import builtins
import types
import dis
import filecmp
import sys
import os
from contextlib import redirect_stdout
from os.path import isfile, join


class Frame(object):
    def __init__(self):
        self.data_stack = []
        self.block_stack = []
        self.locals_ = {}


class Executor(object):
    #def __init__(self, instruction, instructions, data_stack, block_stack,
                #locals_):
    def __init__(self,  instruction, instructions, frame):
        self.argval = instruction.argval  # value manipulate with
        self.offset = instruction.offset
        self.instructions = instructions

        self.stack = frame.data_stack
        self.block_stack = frame.block_stack
        self.locals = frame.locals_

    def LOAD_NAME(self):  # incomplete, add globals
        #         print("To load:", self.argval)
        if self.argval in dir(builtins):
            self.stack.append(
                getattr(builtins, self.argval))  # на стек добавится
            # built-in функция
        elif self.argval in self.locals:
            self.stack.append(self.locals[self.argval])
        elif self.argval in globals():
            self.stack.append(globals()[self.argval])
        else:
            raise NameError()

    def LOAD_GLOBAL(self):
        if self.argval in globals():
            self.stack.append(globals()[self.argval])
        else:
            self.stack.append(getattr(builtins, self.argval))

    def DELETE_FAST(self):
        if self.argval in self.locals:
            del self.locals[self.argval]
        else:
            raise NameError(
                "No name {} found in local variables".format(self.locals))

    def STORE_ATTR(self):
        object_to_set_attr = self.stack.pop()
        attr_value = self.stack.pop()
        setattr(object_to_set_attr, self.argval, attr_value)

    def DELETE_ATTR(self):
        object_to_del_attr = self.stack.pop()
        delattr(object_to_del_attr, self.argval)

    def STORE_FAST(self):
        self.locals[self.argval] = self.stack.pop()

    def DELETE_NAME(self):
        if self.argval in self.locals:
            del self.locals[self.argval]
        else:
            del globals()[self.argval]

    def DELETE_GLOBAL(self):
        if self.argval in globals():
            del globals()[self.argval]
        else:
            raise NameError

    def DELETE_SUBSCR(self):
        attr_to_del = self.stack.pop()
        object_to_del_attr = self.stack.pop()
        del object_to_del_attr[attr_to_del]

    def GET_ITER(self):
        self.stack[-1] = iter(self.stack[-1])

    def FOR_ITER(self):
        try:
            self.stack.append(next(self.stack[-1]))
        except StopIteration:
            self.stack.pop()  # pop iterator
            return self.instructions[self.argval]

    def SETUP_LOOP(self):
        self.block_stack.append(('for loop', self.argval))

    def BREAK_LOOP(self):
        instr_to_jump = self.instructions[self.block_stack[-1][1]]
        self.block_stack.pop()
        return instr_to_jump

    def POP_BLOCK(self):  # incompleted
        self.block_stack.pop()

    def DUP_TOP(self):
        self.stack.append(self.stack[-1])

    def DUP_TOP_TWO(self):
        self.stack.append(self.stack[-2])
        self.stack.append(self.stack[-2])

    def POP_JUMP_IF_TRUE(self):
        bool_value = self.stack.pop()
        if bool_value:
            return self.instructions[self.argval]

    def POP_JUMP_IF_FALSE(self):
        bool_value = self.stack.pop()
        if not bool_value:
            return self.instructions[self.argval]

    def JUMP_IF_TRUE_OR_POP(self):
        bool_value = self.stack[-1]
        if bool_value:
            return self.instructions[
                self.argval]  # returns number of command to jump
        else:
            self.stack.pop()

    def JUMP_IF_FALSE_OR_POP(self):
        bool_value = self.stack[-1]
        if (not bool_value):
            return self.instructions[self.argval]
        else:
            self.stack.pop()

    def JUMP_ABSOLUTE(self):
        return self.instructions[self.argval]

    def JUMP_FORWARD(self):
        return self.instructions[self.argval]

    def ROT_TWO(self):
        self.stack[-2], self.stack[-1] = self.stack[-1], self.stack[-2]

    def ROT_THREE(self):

        self.stack[-2], self.stack[-1], self.stack[-3] = \
            self.stack[-3], self.stack[-2], self.stack[-1]

    def UNARY_POSITIVE(self):
        self.stack[-1] = abs(self.stack[-1])

    def UNARY_NEGATIVE(self):
        self.stack[-1] = -abs(self.stack[-1])

    def UNARY_NOT(self):
        self.stack[-1] = not self.stack[-1]

    def UNARY_INVERT(self):
        self.stack[-1] = ~self.stack[-1]

    def LOAD_CONST(self):
        self.stack.append(self.argval)

    def LOAD_FAST(self):
        if self.argval in self.locals:
            self.stack.append(self.locals[self.argval])
        else:
            raise NameError(
                "No name {} found in local variables".format(self.locals))

    def STORE_NAME(self):
        self.locals[self.argval] = self.stack.pop()

    def STORE_GLOBAL(self):
        globals()[self.argval] = self.stack.pop()

    def BUILD_TUPLE(self):
        lst = []
        for _ in range(self.argval):
            lst.append(self.stack.pop())
        lst.reverse()
        self.stack.append(tuple(lst))

    def BUILD_TUPLE_UNPACK(self):
        lst = []
        for _ in range(self.argval):
            tmp_lst = []
            obj_to_unpack = self.stack.pop()
            for elem in obj_to_unpack:
                tmp_lst.append(elem)
            tmp_lst.reverse()
            lst += tmp_lst
        lst.reverse()
        self.stack.append(tuple(lst))

    def BUILD_LIST_UNPACK(self):
        lst = []
        for _ in range(self.argval):
            tmp_lst = []
            obj_to_unpack = self.stack.pop()
            for elem in obj_to_unpack:
                tmp_lst.append(elem)
            tmp_lst.reverse()
            lst += tmp_lst
        lst.reverse()
        self.stack.append(lst)

    def BUILD_SLICE(self):
        if self.argval == 2:
            TOS = self.stack.pop()
            TOS1 = self.stack.pop()
            self.stack.append(slice(TOS1, TOS))
        elif self.argval == 3:
            TOS = self.stack.pop()
            TOS1 = self.stack.pop()
            TOS2 = self.stack.pop()
            self.stack.append(slice(TOS2, TOS1, TOS))

    def BUILD_LIST(self):
        lst = []
        for _ in range(self.argval):
            lst.append(self.stack.pop())
        lst.reverse()
        self.stack.append(lst)

    def CONTINUE_LOOP(self):
        return self.instructions[self.argval]

    # new and INCOMPLETE

    def LOAD_BUILD_CLASS(self):
        self.stack.append(builtins.__build_class__())

    def UNPACK_SEQUENCE(self):
        TOS = self.stack[-1]
        self.stack.pop()
        for x in reversed(TOS):
                self.stack.append(x)

    def STORE_MAP(self):
        map_, val, key = self.stack[-3:]
        self.stack[-2:] = []
        map_[key] = val

    def STORE_SUBSCR(self):
        subscr = self.stack[-1]
        self.stack.pop()
        obj = self.stack[-1]
        self.stack.pop()
        val = self.stack[-1]
        self.stack.pop()
        obj[subscr] = val

    def MAP_ADD(self):
        key = self.stack[-1]
        value = self.stack[-2]
        the_map = self.stack[-self.argval]
        the_map[key] = value

    def SET_ADD(self):
        val = self.stack[-1]
        the_set = self.stack[-self.argval]
        the_set.add(val)

    def LIST_APPEND(self):
        element_to_add = self.stack[-1]
        the_list = self.stack[-self.argval]
        the_list.append(element_to_add)
    # new

    def BUILD_MAP(self):
        map_to_push = {}
        for _ in range(self.argval):
            TOS = self.stack.pop()
            TOS1 = self.stack.pop()
            map_to_push[TOS1] = TOS
        self.stack.append(map_to_push)

    def BUILD_MAP_UNPACK(self):
        dict_to_push = {}
        for _ in range(self.argval):
            current_dict = self.stack.pop()
            for key in current_dict:
                if key not in dict_to_push:  # to avoid collisions, incomplete
                    dict_to_push[key] = current_dict[key]
                    #         print(dict_to_push)
        self.stack.append(dict_to_push)

    def BUILD_SET(self):
        lst = []
        for _ in range(self.argval):
            lst.append(self.stack.pop())
        lst.reverse()
        self.stack.append(set(lst))

    def BUILD_SET_UNPACK(self):
        set_to_push = set()
        for _ in range(self.argval):
            iterable_object = self.stack.pop()
            for elem in iterable_object:
                set_to_push.add(elem)
        self.stack.append(set_to_push)

    def LOAD_ATTR(self):
        self.stack[-1] = getattr(self.stack[-1], self.argval)

    def CALL_FUNCTION(self):
        kw_args_number = self.argval // 256
        pos_args_number = self.argval % 256

        kw_args = {}
        for i in range(kw_args_number):
            kw_args[self.stack[-2]] = self.stack[-1]
            self.stack.pop()
            self.stack.pop()

        pos_args = []
        for i in range(pos_args_number):
            pos_args.append(self.stack[-1])
            self.stack.pop()
        # print('pos args are', pos_args)
        pos_args.reverse()
        function_to_call = self.stack.pop()
        if "print" in str(function_to_call):
            (__builtins__).__dict__['print'](*pos_args, **kw_args)
            self.stack.append(None)
        else:
            self.stack.append(function_to_call(*pos_args, **kw_args))

    def COMPARE_OP(self):
        b = self.stack.pop()
        a = self.stack.pop()

        operations = {
            '<': operator.lt,
            '<=': operator.le,
            '>': operator.gt,
            '>=': operator.ge,
            '==': operator.eq,
            '!=': operator.ne,
            'is': operator.is_,
            'is not': operator.is_not,
            'in': lambda x, y: x in y,
            'not in': lambda x, y: x not in y,
            'not': operator.not_
        }

        self.stack.append(operations[self.argval](a, b))

    def POP_TOP(self):
        self.stack.pop()

    def RETURN_VALUE(self):
        return self.stack.pop()


class VirtualMachine(object):
    def __init__(self):
        self.call_stack = [Frame()]
        self.data_stack = []
        self.block_stack = []
        self.locals = {}

    def prepare_codeobject(self, codeobject):
        instructions = {}
        instructions_list = []
        for instruction in dis.get_instructions(codeobject):
            instructions[instruction.offset] = len(instructions_list)
            instructions_list.append(instruction)
        return instructions, instructions_list

    def execute(self, instruction, instructions):
        stack = self.call_stack[-1].data_stack
        #stack = self.data_stack

        #executor = Executor(instruction, instructions, self.data_stack,
                            # self.block_stack, self.locals)
        executor = Executor(instruction, instructions, self.call_stack[-1])

        #         print(instruction.opname)
        if "BINARY" in instruction.opname:
            b = stack.pop()
            a = stack.pop()
            operations = {
                'BINARY_POWER': operator.pow,
                'BINARY_MULTIPLY': operator.mul,
                'BINARY_FLOOR_DIVIDE': operator.floordiv,
                'BINARY_TRUE_DIVIDE': operator.truediv,
                'BINARY_MODULO': operator.mod,
                'BINARY_ADD': operator.add,
                'BINARY_SUBTRACT': operator.sub,
                'BINARY_SUBSCR': operator.getitem,
                'BINARY_LSHIFT': operator.lshift,
                'BINARY_RSHIFT': operator.rshift,
                'BINARY_AND': operator.and_,
                'BINARY_XOR': operator.xor,
                'BINARY_OR': operator.or_,
            }
            stack.append(operations[instruction.opname](a, b))
        elif 'INPLACE' in instruction.opname:
            a = stack.pop()
            operations = {
                'INPLACE_POWER': operator.ipow,
                'INPLACE_MULTIPLY': operator.imul,
                'INPLACE_FLOOR_DIVIDE': operator.ifloordiv,
                'INPLACE_TRUE_DIVIDE': operator.itruediv,
                'INPLACE_MODULO': operator.imod,
                'INPLACE_ADD': operator.iadd,
                'INPLACE_SUBTRACT': operator.isub,
                'INPLACE_LSHIFT': operator.ilshift,
                'INPLACE_RSHIFT': operator.irshift,
                'INPLACE_AND': operator.iand,
                'INPLACE_XOR': operator.ixor,
                'INPLACE_OR': operator.ior,
            }
            stack[-1] = operations[instruction.opname](stack[-1], a)
        elif (instruction.opname in dir(Executor)):
            return getattr(executor, instruction.opname)()  # () нужны,
            # чтобы выполнился метод у executor
            # incomplete
        else:
            raise NameError("No method {} found".format(instruction.opname))

    def run_code(self, codeobject):
        instructions, instructions_list = self.prepare_codeobject(codeobject)
        index = 0
        while index < len(instructions_list):
            execute_return = self.execute(instructions_list[index],
                                          instructions)

            while type(execute_return) is int:
                index = execute_return
                execute_return = self.execute(instructions_list[index],
                                              instructions)
                # for jumps
            index += 1
        # print(self.data_stack)

        self.data_stack = []
