import types
import dis


class VirtualMachine:
    def __init__(self):
        self.stack = []
        self.locals = {}
        self.functions = []
        self.where_to_go = 0
        self.is_jump = False

    def run(self, code: types.CodeType) -> None:
        for i in dis.get_instructions(code):
            if (not self.is_jump) or (self.is_jump and i.offset == self.where_to_go):
                if i.opname == 'LOAD_NAME':
                    if i.argval not in self.locals:
                        self.functions.append(i.argval)
                    else:
                        self.stack.append(self.locals[i.argval])
                elif i.opname == 'LOAD_CONST':
                    self.stack.append(i.argval)
                elif i.opname == 'CALL_FUNCTION':
                    self.call_function(i.argval)
                elif i.opname == 'POP_TOP':
                    self.stack.pop()
                elif i.opname == 'STORE_NAME':
                    self.locals[i.argval] = self.stack.pop()
                elif i.opname == 'RETURN_VALUE':
                    if len(self.stack):
                        return self.stack.pop()
                elif 'BINARY' in i.opname:
                    self.call_binary(i.opname)
                elif i.opname == 'JUMP_IF_TRUE_OR_POP':
                    x = self.stack[-1]
                    if not x:
                        self.stack.pop()
                    else:
                        self.is_jump = True
                        self.where_to_go = i.argval
                elif i.opname == 'JUMP_IF_FALSE_OR_POP':
                    x = self.stack[-1]
                    if x:
                        self.stack.pop()
                    else:
                        self.is_jump = True
                        self.where_to_go = i.argval

    def call_function(self, n_args):
        f_name = self.functions.pop()
        args = self.stack[-n_args:]
        self.stack = self.stack[:-n_args]
        if f_name == 'print':
            self.stack.append(print(*args))

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
