import types
import dis


class VirtualMachine:
    def __init__(self):
        self.stack = []
        self.locals = {}
        self.functions = []
        self.where_to_go = 0
        self.is_jump = False
        self.block_stack = []

    def run(self, code: types.CodeType) -> None:
        for instruction in dis.get_instructions(code):
            if (not self.is_jump) or (self.is_jump and instruction.offset == self.where_to_go):
                if instruction.opname == 'LOAD_NAME':
                    if instruction.argval not in self.locals:
                        self.functions.append(instruction.argval)
                    else:
                        self.stack.append(self.locals[instruction.argval])
                elif instruction.opname == 'DELETE_NAME':
                    self.DELETE_NAME(instruction.argval)
                elif instruction.opname == 'LOAD_CONST':
                    self.stack.append(instruction.argval)
                elif instruction.opname == 'CALL_FUNCTION':
                    self.call_function(instruction.argval)
                elif instruction.opname == 'POP_TOP':
                    self.stack.pop()
                elif instruction.opname == 'STORE_NAME':
                    self.locals[instruction.argval] = self.stack.pop()
                elif instruction.opname == 'RETURN_VALUE':
                    if len(self.stack):
                        return self.stack.pop()
                elif 'BINARY' in instruction.opname:
                    self.call_binary(instruction.opname)

                elif 'INPLACE' in instruction.opname:
                    self.call_inplace(instruction.opname)

                elif 'UNARY' in instruction.opname:
                    self.call_unary(instruction.opname)

                elif instruction.opname == 'COMPARE_OP':
                    self.COMPARE_OP(instruction.argval)
                elif instruction.opname == 'BUILD_TUPLE':
                    self.BUILD_TUPLE(instruction.argval)
                elif instruction.opname == 'BUILD_LIST':
                    self.BUILD_LIST(instruction.argval)
                elif instruction.opname == 'BUILD_SET':
                    self.BUILD_SET(instruction.argval)
                elif instruction.opname == 'ROT_TWO':
                    self.ROT_TWO()
                elif instruction.opname == 'ROT_THREE':
                    self.ROT_THREE()
                elif instruction.opname == 'STORE_SUBSCR':
                    self.STORE_SUBSCR()
                elif instruction.opname == 'JUMP_IF_TRUE_OR_POP':
                    x = self.stack[-1]
                    if not x:
                        self.stack.pop()
                    else:
                        self.is_jump = True
                        self.where_to_go = instruction.argval
                elif instruction.opname == 'JUMP_IF_FALSE_OR_POP':
                    x = self.stack[-1]
                    if x:
                        self.stack.pop()
                    else:
                        self.is_jump = True
                        self.where_to_go = instruction.argval

    def call_function(self, n_args):
        f_name = self.functions.pop()
        args = self.stack[-n_args:]
        self.stack = self.stack[:-n_args]
        if f_name == 'print':
            self.stack.append(print(*args))

    def JUMP_ABSOLUTE(self, op):
        return self.stack[op]

    def JUMP_FORWARD(self, op):
        return self.stack[op]




    def call_binary(self, op_name):
        y = self.stack.pop()
        x = self.stack.pop()
        z = 0
        if op_name == "BINARY_ADD":
            z = x + y
        if op_name == "BINARY_AND":
            z = x & y
        if op_name == "BINARY_FLOOR_DIVIDE":
            z = x // y
        if op_name == "BINARY_LSHIFT":
            z = x << y
        if op_name == "BINARY_MODULO":
            z = x % y
        if op_name == "BINARY_MULTIPLY":
            z = x * y
        if op_name == "BINARY_OR":
            z = x | y
        if op_name == "BINARY_POWER":
            z = x ** y
        if op_name == "BINARY_RSHIFT":
            z = x >> y
        if op_name == "BINARY_SUBSCR":
            z = x[y]
        if op_name == "BINARY_SUBTRACT":
            z = x - y
        if op_name == "BINARY_TRUE_DIVIDE":
            z = x / y
        if op_name == "BINARY_XOR":
            z = x ^ y
        self.stack.append(z)

    def call_inplace(self, op):
        x = self.stack.pop()
        y = self.stack.pop()
        if op == 'INPLACE_POWER':
            x **= y
        elif op == 'INPLACE_MULTIPLY':
            x *= y
        elif op in ['INPLACE_DIVIDE', 'INPLACE_FLOOR_DIVIDE']:
            x //= y
        elif op == 'INPLACE_TRUE_DIVIDE':
            x /= y
        elif op == 'INPLACE_MODULO':
            x %= y
        elif op == 'INPLACE_ADD':
            x += y
        elif op == 'INPLACE_SUBTRACT':
            x -= y
        elif op == 'INPLACE_LSHIFT':
            x <<= y
        elif op == 'INPLACE_RSHIFT':
            x >>= y
        elif op == 'INPLACE_AND':
            x &= y
        elif op == 'INPLACE_XOR':
            x ^= y
        elif op == 'INPLACE_OR':
            x |= y
        self.stack.append(x)

    def call_unary(self, op):
        x = self.stack.pop()
        if op == 'UNARY_POSITIVE':
            x = +x
        elif op == 'UNARY_NEGATIVE':
            x = -x
        elif op == 'UNARY_NOT':
            x = not x
        elif op == 'UNARY_INVERT':
            x = ~x
        self.stack.append(x)


    def COMPARE_OP(self, op):
        b = self.stack.pop()
        a = self.stack.pop()
        if op == '<':
            self.stack.append(a < b)
        elif op == '<=':
            self.stack.append(a <= b)
        elif op == '==':
            self.stack.append(a == b)
        elif op == '!=':
            self.stack.append(a != b)
        elif op == '>':
            self.stack.append(a > b)
        elif op == '>=':
            self.stack.append(a >= b)

    def popn(self, n):
        """Pop a number of values from the value stack.

        A list of `n` values is returned, the deepest value first.

        """
        if n:
            ret = self.stack[-n:]
            self.stack[-n:] = []
            return ret
        else:
            return []

    def push(self, *vals):
        """Push values onto the value stack."""
        self.stack.extend(vals)

    def BUILD_TUPLE(self, count):
        elts = self.popn(count)
        self.push(tuple(elts))

    def BUILD_LIST(self, count):
        elts = self.popn(count)
        self.push(elts)

    def BUILD_SET(self, count):
        # TODO: Not documented in Py2 docs.
        elts = self.popn(count)
        self.push(set(elts))

    def DELETE_NAME(self, name):
        del self.stack[name]
    def ROT_TWO(self):
        a, b = self.popn(2)
        self.push(b, a)

    def ROT_THREE(self):
        a, b, c = self.popn(3)
        self.push(c, a, b)

    def pop_block(self):
        return self.block_stack.pop()

    def STORE_SUBSCR(self):
        val, obj, subscr = self.popn(3)
        obj[subscr] = val

    def BUILD_SLICE(self, op):
        if op == 2:
            TOS = self.stack.pop()
            TOS1 = self.stack.pop()
            self.stack.append(slice(TOS1, TOS))
        elif op == 3:
            TOS = self.stack.pop()
            TOS1 = self.stack.pop()
            TOS2 = self.stack.pop()
            self.stack.append(slice(TOS2, TOS1, TOS))

    def BUILD_MAP(self, op):
        map_to_push = {}
        for _ in range(op):
            TOS = self.stack.pop()
            TOS1 = self.stack.pop()
            map_to_push[TOS1] = TOS
        self.stack.append(map_to_push)

    def BUILD_MAP_UNPACK(self, op):
        dict_to_push = {}
        for _ in range(op):
            current_dict = self.stack.pop()
            for key in current_dict:
                if key not in dict_to_push:  # to avoid collisions, incomplete
                    dict_to_push[key] = current_dict[key]
                    #         print(dict_to_push)
        self.stack.append(dict_to_push)


    def BUILD_TUPLE_UNPACK(self, op):
        lst = []
        for _ in range(op):
            tmp_lst = []
            obj_to_unpack = self.stack.pop()
            for elem in obj_to_unpack:
                tmp_lst.append(elem)
            tmp_lst.reverse()
            lst += tmp_lst
        lst.reverse()
        self.stack.append(tuple(lst))

    def BUILD_LIST_UNPACK(self, op):
        lst = []
        for _ in range(op):
            tmp_lst = []
            obj_to_unpack = self.stack.pop()
            for elem in obj_to_unpack:
                tmp_lst.append(elem)
            tmp_lst.reverse()
            lst += tmp_lst
        lst.reverse()
        self.stack.append(lst)

    def SET_ADD(self, op):
        val = self.stack[-1]
        the_set = self.stack[-op]
        the_set.add(val)

    def LIST_APPEND(self, op):
        element_to_add = self.stack[-1]
        the_list = self.stack[-op]
        the_list.append(element_to_add)



    #def DUP_TOP(self):
        #self.stack.push(self.stack.top())



    #def pop_block(self):
        #return self.stack.pop()'

"""
    def byte_GET_ITER(self):
        self.stack.push(iter(self.pop()))

    def byte_FOR_ITER(self, jump):
        iterobj = self.top()
        try:
            v = next(iterobj)
            self.push(v)
        except StopIteration:
            self.pop()
            self.jump(jump)

        def CALL_FUNCTION_KW(self, arg):
            kwargs = self.stack.pop()
            return self.call_function(arg, [], kwargs)

        def FUNCTION_VAR_KW(self, arg):
            args, kwargs = self.popn(2)
            return self.call_function(arg, args, kwargs)
        """







