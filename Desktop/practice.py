def in_file(name):
    path = "./src/" + name
    return path + ".html"
    
path = in_file("home")
html = open(path).read()
