from compylex.compiler import Compile
code = Compile("print('hello)", "PYTHON", "", 0)
print(code.get_status())
