

#The 'pages' list consists of dictionaries, each of which contains the elements for a full webpage.

pages = [
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Feedback",
    },
    {
        "filename": "content/find_food.html",
        "output": "docs/find_food.html",
        "title": "Find Food",
    },
    {
        "filename": "content/donate_food.html",
        "output": "docs/donate_food.html",
        "title": "Donate Food",
    },
]     


#The page_create function concatenates the dictionary items to create each webpage. There's also templating here to add in the page title.       
        

def main():
    for item in pages:
        template = open("templates/base.html").read()
        content = open(item["filename"]).read()
        finished_page = template.replace("{{content}}", content).replace("{{title}}", item["title"])
        open(item["output"], "w+").write(finished_page)
main()






