import sys


def main():
	if len(sys.argv) > 1:
		content = ""
		for i in range(1,len(sys.argv)):
			fname  = sys.argv[i]
			file = open(fname, "r")
			content += file.read()
			file.close()
		return content
	else:
		return ("No arguments given!")

if __name__ == '__main__':
	main()
