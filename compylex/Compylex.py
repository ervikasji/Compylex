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
        self.create_file()

    def create_file(self):
        """Function to create the code and input files.

        Args:
            None

        Returns:
            None

        """
        if(self.lang == "PYTHON"):
            pass
        elif(self.lang == "C"):
            pass
        elif(self.lang == 'CPP'):
            pass

    def compile_python(self, code, input):
        """Function to compile python code and return output.

        Args:
            code file
            input file

        Returns:
            output of compiled code or error message to be displayed

        """
        pass

    def compile_C(self, code, input):
        """Function to compile C code and return output.

        Args:
            code file
            input file

        Returns:
            output of compiled code or error message to be displayed

        """
        pass

    def compile_cpp(self, code, input):
        """Function to compile C++ code and return output.

        Args:
            code file
            input file

        Returns:
            output of compiled code or error message to be displayed

        """
        pass
