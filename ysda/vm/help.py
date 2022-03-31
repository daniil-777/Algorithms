import dis


codeobj = compile('print(2 * 3)', '<test>', 'exec')
print(list(dis.get_instructions(codeobj)))
