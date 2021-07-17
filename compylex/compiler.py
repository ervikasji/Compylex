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
    """

    def __init__(self, code="", lang="", input="", id=0):
        self.code = code
        self.lang = lang
        self.input = input
        self.id = id
        self.output = ""
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
            code file
            input file

        Returns:
            output of compiled code or error message to be displayed

        """
        pass

    def compile_C(self):
        """Function to compile C code and return output.

        Args:
            code file
            input file

        Returns:
            output of compiled code or error message to be displayed

        """
        pass

    def compile_cpp(self):
        """Function to compile C++ code and return output.

        Args:
            code file
            input file

        Returns:
            output of compiled code or error message to be displayed

        """
        pass
