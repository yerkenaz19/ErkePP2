import os

name = r"/Users/erkenazsagynbaeva/ErkePP2/lab6/directories.py"

print(os.access(name, os.F_OK)) # Existence
print(os.access(name, os.R_OK)) # Readability
print(os.access(name, os.W_OK)) # Writeability
print(os.access(name, os.X_OK)) # Executeability