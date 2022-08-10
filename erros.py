#!/usr/bin/env python3

import os
import sys

# EAFP - Easy to ASK Forgiveness than permission
# (E mais facil pedir perdao do que permissao)

try:
    names = open("names.txt").readlines() # FileNotFoundError
    # FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
