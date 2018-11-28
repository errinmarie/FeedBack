# This is the example of reading in the book, and writing it to a json file.
text = open('wonderland.txt').read()
lines = text.splitlines()

paragraphs = []
current_chapter = ''
current_paragraph = ''
chapters = []
for line in lines:
    line = line.strip()
    if line.startswith('CHAPTER'):
        current_chapter = line
        paragraphs = []
        chapters.append((current_chapter, paragraphs))
        continue

    if not current_chapter:
        continue

    current_paragraph += ' ' + line

    if line == 'THE END':
        break

    if not line:
        current_paragraph = current_paragraph.strip(' *')
        if current_paragraph:
            paragraphs.append(current_paragraph)
        current_paragraph = ''

print(chapters[0])

import json
open('wonderland.json', 'w+').write(json.dumps(chapters, indent=4))

# Now, lets loop through the chapters again and output HTML
f = open('wonderland.html', 'w+')
f.write('''
<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Alice in Wonderland</title>
    <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura.css" type="text/css">
</head>
<body>
<h1>Alice in Wonderland</h1>
''')
for chapter_title, contents in chapters:
    f.write('<h2>' + chapter_title + '</h2>')
    for paragraph in contents:
        f.write('<p>' + paragraph + '</p>')
    f.write('<hr />')


f.write('''
</body>
''')
