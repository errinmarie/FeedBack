#def blog():
#    top = open("templates/blog_top.html").read()
#    content = open("content/belgium.html").read()
#    blog_html = top + content
#    open('docs/blog.html', 'w+').write(blog_html)


#open top file
#read in content html
#concatenate the two
#write a new file that is ____.html


#print(pages[0]['filename'])


def blog():
for page in pages
    top = open("templates/top.html").read()
    content = open("content/about.html").read()
    final_content = top + content
    open(page['output'], 'w+').write(final_content)


pages = [
    {
        "filename": "content/about.html",
        "output": "docs/about.html",
        "title": "About Me",
    },
    {
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "Contact Me",
    },
    {
        "filename": "content/stories.html",
        "output": "docs/stories.html",
        "title": "Stories",
    },
    {
        "filename": "content/belgium.html",
        "output": "docs/belgium.html",
        "title": "Belgium",
    },
    {
        "filename": "content/bhutan.html",
        "output": "docs/bhutan.html",
        "title": "Bhutan",
    },
    {
        "filename": "content/egypt.html",
        "output": "docs/egypt.html",
        "title": "Egypt",
    },
    {
        "filename": "content/india.html",
        "output": "docs/india.html",
        "title": "India",
    },
    {
        "filename": "content/ireland.html",
        "output": "docs/ireland.html",
        "title": "Ireland",
    },
    {
        "filename": "content/slovenia.html",
        "output": "docs/slovenia.html",
        "title": "Slovenia",
    },
    {
        "filename": "content/spain.html",
        "output": "docs/spain.html",
        "title": "Spain",
    },
    {
        "filename": "content/uzbekistan.html",
        "output": "docs/uzbekistan.html",
        "title": "Uzbekistan",
    },
    {
        "filename": "content/vietnam.html",
        "output": "docs/vietnam.html",
        "title": "Vietnam",
    },
]
























