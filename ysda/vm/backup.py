import types
import builtins
import dis


class VirtualMachineError(Exception):
    """For raising errors in the operation of the VM."""
    pass


class Frame(object):

    def __init__(self, code, global_names, local_names, prev_frame=None, next_instr=0):
        self.code = code
        self.frame = None
        self.next_instr = next_instr
        self.global_names = global_names
        self.local_names = local_names
        self.prev_frame = prev_frame
        self.stack = []
        self.block_stack = []
        self.call_stack = []
        self.return_value = None
        if prev_frame:
            self.builtin_names = prev_frame.builtin_names
        else:
            self.builtin_names = local_names['__builtins__']
            if hasattr(self.builtin_names, '__dict__'):
                self.builtin_names = self.builtin_names.__dict__

    def make_frame(self, code, callargs={}, global_names=None, local_names=None, next_instr = 0):
        if global_names is not None:
            global_names = local_names
            if local_names is None:
                local_names = global_names
        elif self.call_stack:
            global_names = self.frame.global_names
            local_names = {}
        else:
            global_names = local_names = {}
            global_names['__buildints__'] = __builtins__
            local_names['__buildints__'] = __builtins__

        local_names.update(callargs)
        frame = Frame(code, global_names, local_names, self.frame, next_instr)
        return frame

    def top(self):
        """Return the value at the top of the stack, with no changes."""
        return self.frame.stack[-1]

    def push_frame(self, frame):
        self.call_stack.append(frame)
        self.frame = frame

    def pop_frame(self):
        self.call_stack.pop()
        if self.call_stack:
            self.frame = self.call_stack[-1]
        else:
            self.frame = None
        return self.frame

    def run_frame(self, frame):
        """Run a frame until it returns (somehow).
        Exceptions are raised, the return value is returned.
        """
        self.push_frame(frame)
        instructions = list(dis.get_instructions(frame.code))
        while frame.next_instr < len(instructions):
            instr = instructions[self.frame.next_instr]
            why = self.dispatch_instruction(instr)
            while why and frame.block_stack:
                why = self.и(why)
            if why:
                break
        self.pop_frame()
        return self.return_value

    def dispatch_instruction(self, instruction):
        """ Dispatch by bytename to the corresponding methods.
        Exceptions are caught and set on the virtual machine."""
        why = None
        operation = instruction.opname
        args = {'arg' : instruction.arg,
                'argval' : instruction.argval}
        try:
            self.frame.next_instr +=1
            if operation.startswith('INPLACE_'):
                self.inplaceOperator(operation)
            else:
                op = getattr(self, operation, None)
                why = op(args)
        except VirtualMachineError as e:
            print(e)
        why = 'vm_exception'
        return why

    def manage_block_stack(self, why):
        """ Manage a frame's block stack.
        Manipulate the block stack and data stack for looping,
        exception handling, or returning."""
        assert why != 'yield'

        block = self.frame.block_stack[-1]
        if block.type == 'loop' and why == 'continue':
            self.jump(self.return_value)
            why = None
            return why
        if block.type == 'loop' and why == 'break':
            why = None
            self.jump(block.handler)
            return why
        return why

    def peek(self, n):
        """Get a value `n` entries down in the stack, without changing the stack."""
        return self.frame.stack[-n]

    def jump(self, jump):
        """Move the bytecode pointer to `jump`, so it will execute next."""
        self.frame.f_lasti = jump

    def pop_block(self):
        return self.frame.block_stack.pop()

    def run(self, code, global_names=None, local_names = None):
        frame = self.make_frame(code, callargs={}, global_names = global_names,
                                local_names = local_names, next_instr = 0)
        val = self.run_frame(frame)
        return val

    """def parse_argument(self, instruction, argument, what_to_execute):
        numbers = ["LOAD_VALUE"]
        names = ["LOAD_NAME", "STORE_NAME"]

        if instruction in numbers:
            argument = what_to_execute["numbers"][argument]
        elif instruction in names:
            argument = what_to_execute["names"][argument]

        return argument """
#builtins__.__dict__
    """def run(self, code: types.CodeType) -> None:
        self.byte_code = list(code.co_code)
        self.names = list(code.co_names)
        self.consts = list(code.co_consts)
        self.stack = []
        self.vars = {}
        self.byte_code_counter = 0
        self.builtins_names = __builtins__
        if hasattr(self.builtins_names, '__dict__'):
            self.builtins_names = self.builtins_names.__dict__
        instructions = list(dis.get_instructions(code))
        for instruction in instructions:
            if instruction.opname == 'LOAD_NAME':
                #self.stack.append(instruction.argval)
                self.LOAD_NAME(instruction.argval)
            elif instruction.opname == 'LOAD_CONST':
                self.LOAD_CONST(instruction.argval)
            elif instruction.opname == 'POP_TOP':
                self.POP_TOP(instruction.argval)
            elif instruction.opname == 'BINARY_ADD':
                self.BINARY_ADD()
            elif instruction.opname == 'BINARY_AND':
                self.BINARY_AND()
            elif instruction.opname == 'BINARY_FLOOR_DIVIDE':
                self.BINARY_FLOOR_DIVIDE()
            elif instruction.opname == 'BINARY_MULTIPLY':
                self.BINARY_MULTIPLY()
            elif instruction.opname == 'CALL_FUNCTION':
                self.CALL_FUNCTION(instruction.argval)
            elif instruction.opname == 'PRINT_EXPR':
                self.PRINT_EXPR()
            elif instruction.opname == 'BINARY_POWER':
                self.BINARY_POWER()
            elif instruction.opname == 'BINARY_SUBTRACT':
                self.BINARY_SUBTRACT()
            elif instruction.opname == 'COMPARE_OP':
                self.COMPARE_OP(instruction.argval)
            elif instruction.opname == 'BUILD_LIST':
                self.BUILD_LIST(instruction.argval)
            elif instruction.opname == 'BUILD_TUPLE':
                self.BUILD_TUPLE(instruction.argval)
            elif instruction.opname == 'BUILD_SLICE':
                self.BUILD_SLICE(instruction.argval)
            elif instruction.opname.startswith == 'INPLACE_':
                self.inplaceOperator(instruction.opname[8:])
                """

    def PRINT_EXPR(self):
        answer = self.stack.pop()
        print(answer)


    def LOAD_NAME(self, arg):
        if arg in self.builtins_names.keys():  # здесь мы храним названия встроенных функций
            name = self.builtins_names[arg]  #здесь мы уже достаем реальную функцию
        else:
            name = self.names[arg]
        if self.vars.get(name) is not None:
            name = self.vars[name]
        self.stack.append(name) #положили саму print

    def byte_LOAD_NAME(self, name):
        frame = self.frame
        if name in frame.f_locals:
            val = frame.f_locals[name]
        elif name in frame.f_globals:
            val = frame.f_globals[name]
        elif name in frame.f_builtins:
            val = frame.f_builtins[name]
        else:
            raise NameError("name '%s' is not defined" % name)
        self.push(val)

    def LOAD_CONST(self, arg):
        self.stack.append(arg)  #кладем само значение

    def POP_TOP(self, arg):
        self.stack.pop()

    def RETURN_VALUE(self, arg):
        pass

    def STORE_NAME(self, name):
        self.frame.f_locals[name] = self.pop_frame()

    def STORE_FAST(self, arg):
        self.vars[self.names[arg]] = self.stack.pop()

    def LOAD_VALUE(self):
        pass
    def BINARY_AND(self):
        first = self.frame.stack.pop()
        second = self.frame.stack.pop()
        total = first + second
        self.frame.stack.append(total)

    def BINARY_FLOOR_DIVIDE(self):
        first = self.stack.pop()
        second = self.stack.pop()
        total = first // second
        self.stack.append(total)
    def BINARY_MULTIPLY(self):
        first = self.stack.pop()
        second = self.stack.pop()
        multiplication = first * second
        self.stack.append(multiplication)
    def CALL_FUNCTION(self, arg):
        a = []
        for i in range(arg):
            a.append(self.stack.pop())
        name = self.stack[len(self.stack) - 1]
        res = name(*a)
        #if res is not None:
        self.stack.append(res)

    def BINARY_ADD(self, arg):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    def BINARY_FLOOR_DIVIDE(self, arg):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a // b)

    def BINARY_SUBTRACT(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)

    def BINARY_MULTIPLY(self, arg):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a * b)

    def BINARY_POWER(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a ** b)

    def BINARY_TRUE_DIVIDE(self, arg):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a / b)

    def BINARY_MODULO(self, arg):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a % b)

    def COMPARE_OP(self, arg):
        b = self.stack.pop()
        a = self.stack.pop()
        op = dis.cmp_op[arg]
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

    def BUILD_TUPLE(self, count):
        elts = self.popn(count)
        self.push(tuple(elts))

    def BUILD_LIST(self, count):
        elts = self.popn(count)
        self.push(elts)

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

    def BUILD_SLICE(self, count):
        if count == 2:
            x, y = self.popn(2)
            self.push(slice(x, y))
        elif count == 3:
            x, y, z = self.popn(3)
            self.push(slice(x, y, z))
        else:  # pragma: no cover
            raise VirtualMachineError("Strange BUILD_SLICE count: %r" % count)
    def inplaceOperator(self, op):
        x, y = self.popn(2)
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
        else:           # pragma: no cover
            raise VirtualMachineError("Unknown in-place operator: %r" % op)
        self.push(x)

    def JUMP_FORWARD(self, jump):
        self.jump(jump)

    def JUMP_ABSOLUTE(self, jump):
        self.jump(jump)

    def JUMP_IF_TRUE(self, jump):
        val = self.top()
        if val:
            self.jump(jump)

    def JUMP_IF_FALSE(self, jump):
        val = self.top()
        if not val:
            self.jump(jump)

    def LOAD_NAME(self, name):
        frame = self.frame
        if name in frame.f_locals:
            val = frame.f_locals[name]
        elif name in frame.f_globals:
            val = frame.f_globals[name]
        elif name in frame.f_builtins:
            val = frame.f_builtins[name]
        else:
            raise NameError("name '%s' is not defined" % name)
        self.push(val)

    def STORE_NAME(self, name):
        self.frame.f_locals[name] = self.pop_frame()

    def DELETE_NAME(self, name):
        del self.frame.f_locals[name]

    def LOAD_FAST(self, name):
        if name in self.frame.f_locals:
            val = self.frame.f_locals[name]
        else:
            raise UnboundLocalError(
                "local variable '%s' referenced before assignment" % name
            )
        self.push_frame(val)

    def STORE_FAST(self, name):
        self.frame.f_locals[name] = self.pop_frame()

    def DELETE_FAST(self, name):
        del self.frame.f_locals[name]

    def LOAD_GLOBAL(self, name):
        f = self.frame
        if name in f.f_globals:
            val = f.f_globals[name]
        elif name in f.f_builtins:
            val = f.f_builtins[name]
        else:
            raise NameError("global name '%s' is not defined" % name)
        self.push_frame(val)

    def STORE_GLOBAL(self, name):
        f = self.frame
        f.f_globals[name] = self.pop_frame()

    def LOAD_DEREF(self, name):
        self.push(self.frame.cells[name].get())

    def STORE_DEREF(self, name):
        self.frame.cells[name].set(self.pop_frame())

    def LOAD_LOCALS(self):
        self.push(self.frame.f_locals)












