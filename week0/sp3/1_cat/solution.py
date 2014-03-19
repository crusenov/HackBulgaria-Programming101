import sys

def main():
    if len(sys.argv) > 1:
        fname  = sys.argv[1]
        file = open(sys.argv[1], "r")
        content = file.read()
        file.close()
        return content
    else:
        return ("No arguments given!")

if __name__ == '__main__':
    main()
