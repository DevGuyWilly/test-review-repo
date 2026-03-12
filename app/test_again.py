#!/usr/bin/env python3

import os
import subprocess
import psutil

def authenticateUser():
    # Dummy AWS Secret Key hardcoded
    secret_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Dummy Database Password hardcoded
    db_password = "password123"

    # Bare except: clause without specifying an exception type
    try:
        subprocess.Popen(["echo", "hello world"])
    except:
        pass

    # Mutable default argument to a function signature
    def foo(my_list=[]):
        my_list.append("test")
        return my_list

    # Deeply nested if/for statements with 4 levels of nesting
    for i in range(10):
        for j in range(10):
            if i > 5 and j < 3:
                for k in range(10):
                    if k % 2 == 0:
                        print("Hello World")

# Extremely long lines of code (over 120 characters)
os.system("echo 'hello world' > /dev/null")

# Bad naming conventions (camelCase for functions and PascalCase for variables)
def authenticateUser():
    # Dummy AWS Secret Key hardcoded
    secret_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Dummy Database Password hardcoded
    db_password = "password123"

    # Bare except: clause without specifying an exception type
    try:
        subprocess.Popen(["echo", "hello world"])
    except:
        pass

# Unused standard library imports at the top of the file
import sys
import re

# Print statement with no documentation or comments
print("Hello World")