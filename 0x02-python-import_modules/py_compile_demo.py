#!/usr/bin/python3
import os
import py_compile

def compile_script(filepath):
    filename, _ = os.path.splitext(filepath)
    print("\n")
    print(f"filename is {filename}")
    pyc_path = os.path.join(os.path.dirname(filepath), f"{filename}.pyc")
    print(pyc_path)
    
    py_compile.compile(filepath, cfile=pyc_path)
    print(f"Compiled: {filepath} to {pyc_path}")

compile_script("/home/alson-kali/PROGRAMMING/ALX/alx-higher_level_programming/0x02-python-import_modules/demo.py")
