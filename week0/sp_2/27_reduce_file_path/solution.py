def reduce_file_path(path):
	final = ""
	new = path.split("/")
	for i in new:
		if i == '..':
			p = new.index(i)
			new.pop(p-1)
			new.pop(p-2)
			new.pop(p-1)
	final += "/".join(x for x in new if x != "" and x != "." and x != "..")
	return "/" + final




def main():
	print(reduce_file_path("/"))
	print(reduce_file_path("/srv/../"))
	print(reduce_file_path("/srv/www/htdocs/wtf/"))
	print(reduce_file_path("/srv/www/htdocs/wtf"))
	print(reduce_file_path("/srv/./././././"))
	print(reduce_file_path("/etc//wtf/"))
	print(reduce_file_path("/etc/../etc/../etc/../"))
	print(reduce_file_path("//////////////"))
	print(reduce_file_path("/../"))

if __name__ == '__main__':
	main()