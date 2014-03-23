import os
from subprocess import call
import sys


def main():
    if len(sys.argv) > 2:
        print ("Too many arguments")
    elif len(sys.argv) < 2:
        print ("No given arguments")
    else:
        directory = sys.argv[1]
        dir_content = os.listdir(directory)
        for file in dir_content:
            if "." not in file:
                os.chdir(directory + '/' + file)
                new_dir = (directory + '/' +file)
                new_content = os.listdir(new_dir)
                for new in new_content:
                    if "." not in new and new != '7_pizza':
                        os.chdir(new_dir + '/' + new)
                        print("Testing function " + new)
                        call("python3.3 tests.py", shell = True)
                        os.chdir(new_dir)



if __name__ == '__main__':
    main()
