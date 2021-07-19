#!/usr/bin/env python3
import subprocess
import os
from os import path
from pathlib import Path


class Compile():
    """Compile class for compiling code and returning output

        Attributes:
        code  (string): code to be compiled
        lang (string): programming language used
        input (string): user input
        id (integer): user id
        output (string): output of code
        compile status (string): compilation status code
    """

    def __init__(self, code="", lang="", input="", id=0):
        self.code = code
        self.lang = lang
        self.input = input
        self.id = str(id)
        self.output = ""
        self.status = ""
        self.create_file()

    def create_file(self):
        """Function to create the code and input files.
        Args:
            None
        Returns:
            None
        """
        dir = os.path.join(str(Path.home()), ".data")
        if(path.isdir(dir)):
            pass
        else:
            os.mkdir(dir)
        os.chdir(dir)

        if(self.lang == "PYTHON"):
            file = open(self.id+".py", "w")
            file.write(self.code)
            file.close()
        elif(self.lang == "C"):
            file = open(self.id+".c", "w")
            file.write(self.code)
            file.close()
        elif(self.lang == 'CPP'):
            file = open(self.id+".cpp", "w")
            file.write(self.code)
            file.close()
        file = open(self.id+"-input.txt", "w")
        file.write(self.input)
        file.close()

    def delete_file(self):
        """Function to delete the code and input files.
        Args:
            None
        Returns:
            None
        """
        subprocess.call(["rm", self.id+"-input.txt"])
        if(self.lang == "PYTHON"):
            subprocess.call(["rm", self.id+".py"])
        elif(self.lang == "C"):
            subprocess.call(["rm", self.id+".c"])
        elif(self.lang == 'CPP'):
            subprocess.call(["rm", self.id+".cpp"])

    def compile_python(self):
        """Function to compile python code and return output.
        Args:
            None
        Returns:
            None
        """
        if(self.input == ""):
            stdout = subprocess.run(
                ["python3", self.id+".py"], stdout=subprocess.PIPE).stdout.decode('utf-8')
            stderr = subprocess.run(
                ["python3", self.id+".py"], stderr=subprocess.PIPE).stderr.decode('utf-8')
            self.output = stdout
            self.status = stderr

        else:
            pass

    def compile_C(self):
        """Function to compile C code and return output.
        Args:
            None
        Returns:
            None
        """
        if(self.input == ""):
            pass
        else:
            pass

    def compile_cpp(self):
        """Function to compile C++ code and return output.
        Args:
            None
        Returns:
            None
        """
        if(self.input == ""):
            pass
        else:
            pass

    def get_output(self):
        """Function to return output of the code
        Args:
            None
        Returns:
            Output of the compiled code
        """
        return self.output

    def get_status(self):
        """Function to return compilation status code
        Args:
            None
        Returns:
            Compilation status code
        """
        return self.status
