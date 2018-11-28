
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
#print(pages)


#Now, concatenate the dictionary items to create a webpage for every html file in the content dir. (This also uses templating to sub in the content info and page titles.)      
        

def main():
    for item in pages:
        template = open("templates/base.html").read()
        content = open(item["filepath"]).read()
        finished_page = template.replace("{{content}}", content).replace("{{title}}", item["title"])
        open(item["output"], "w+").write(finished_page)
main()







