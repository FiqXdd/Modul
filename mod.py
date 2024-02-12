import os

# Extract the file path to a variable
file_path = '/sdcard/PP.txt'

#check if the file exists with path.exists()
if os.path.exists(file_path):
    os.remove('/sdcard/PP.txt')