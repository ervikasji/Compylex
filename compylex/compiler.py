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
        self.id = id
        self.output = ""
        self.compile_status
        self.create_file()

    def create_file(self):
        """Function to create the code and input files.
        Args:
            None
        Returns:
            None
        """
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

    def compile_python(self):
        """Function to compile python code and return output.
        Args:
            None
        Returns:
            None
        """
        pass

    def compile_C(self):
        """Function to compile C code and return output.
        Args:
            None
        Returns:
            None
        """
        pass

    def compile_cpp(self):
        """Function to compile C++ code and return output.
        Args:
            None
        Returns:
            None
        """
        pass

    def output(self):
        """Function to return output of the code
        Args:
            None
        Returns:
            Output of the compiled code
        """
        pass

    def compile_status(self):
        """Function to return compilation status code
        Args:
            None
        Returns:
            Compilation status code
        """
        pass