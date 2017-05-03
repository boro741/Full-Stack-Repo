
import os

i = 1

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"/Users/pavanboro/Downloads/prank")
    print(file_list)
    # (2) for each file, rename filename
    for file_list in os.listdir(r"/Users/pavanboro/Downloads/prank"):
        print("i: %d"% i )
        i = i+1
rename_files()
