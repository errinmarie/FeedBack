
#First, create a list of all the html files (filepaths) in the content dir:

import glob
all_html_files = glob.glob("content/*.html")
#print(all_html_files)    


#Next, isolate the pieces of the filepaths into filename & title. Create an 'output' filepath that will route into the docs dir. Then populate the 'pages' list with dictionaries that define keys and values for each desired webpage.
        
import os
pages = []
for file_path in all_html_files:
    file_name = os.path.basename(file_path)
    name_only, extension = os.path.splitext(file_name)
    output = 'docs/' + file_name
    pages.append({
        "filepath": file_path,
        "filename": file_name,
        "title": name_only,
        "output": output,
    })
print(pages)


#Now, concatenate the dictionary items to create a webpage for every html file in the content dir:

def page_create():
    for page in pages:
        top = open("templates/top.html").read()
        content = open(page["filepath"]).read()
        fullpage = top + content
        open(page["output"], "w+").write(fullpage)
page_create()


#I think this part was supposed to auto-update my page titles, but it didn't work so I hashed it out.

#from jinja2 import Template
#for page in pages:
#    page_title = open(item["output"]).read()
#    template = Template("""{{ title }}""")
#    result = template.render(page["title"])
#    print(result)


#I think this part was supposed to auto-update my page navigation, but it didn't work so I hashed it out.

#from jinja2 import Template
#{% for page in pages %}
#    <a href="{{ nav.filename }}">{{ nav.title }}</a>
#{% endfor %}

#template.render(pages=pages) 
    
    
    
    
    
    
    
