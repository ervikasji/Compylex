from compylex.compiler import Compile
code = Compile("print(2+3)", "PYTHON", "", 0)
print(code.get_status())
