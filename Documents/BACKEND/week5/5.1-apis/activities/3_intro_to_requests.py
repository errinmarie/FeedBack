import requests

print('------------ Challenge 1')
# Challenge 1
# 1. Examine the following code. Can you understand what it is doing? Can
# you predict the sort of data it will print out?
# 2. Get it functioning. You will need to use pipenv to install requests.
response = requests.get('https://en.wikipedia.org/wiki/Main_Page')
html_code = response.text
#print(html_code)
#for line in html_code.splitlines():
#    if '<title>' in line:
#        print(line)





print('------------ Challenge 2')
# Challenge 2
# 1. Go to that website in your browser.
# 2. Using the code from Challenge 1 as a guide, write code that will search
# for mentions of a certain article title, such as today's featured article.
# 3. Have it print the text surrounding this.







print('------------ Bonus')
# Bonus Challenge
# - The Bonus Challenges involve writing a Hacker News "scraper".
# - A "scraper" is a piece of software that does what we've been doing: Looking
# through website HTML code for data that is interesting or useful
# 1. Uncomment the following code
# 2. Dig into the source code of hacker news. Can you establish a pattern? What
# is true about the code that is for each headline?
# 3. Modify it to *only* print out the code for each headline (e.g. like the
# previous code with Wikipedia)

#response = requests.get('https://news.ycombinator.com')
#html_code = response.text
#for line in html_code.splitlines():
#    print(line)








#####################################
# Bonus Challenge 2:
# Building on the previous challenge, modify your code to now output the title
# and URL, "extracted" from the HTML code.

# Note: This is a challenging exercise in using Python strings! Below is some
# code that can be used as a hint on how to access only certain parts of Python
# strings that might contain HTML or other code.

html_line = '<a href="http://something.com">Something</a>'

split = html_line.split('"')
# Spit becomes: ['<a href=', 'http://something.com', '>Something</a>']
#print(split)
url = split[1]
#print('URL:', url)

# Let's get rid of the '</a>'
link_caption = split[2]
split_link_caption = link_caption.split('<')
# Spit becomes: ['>Something', '/a>']
caption = split_link_caption[0]

# Finally, we must remove the '>' from the caption -- strip removes the given
# character(s) from the beginning or end of the string
caption = caption.strip('>')
#print('Caption:', caption)







#####################################
# Bonus Challenge 3:
# 1. Finally, take these "extracted" components and put them into a list. You
# should store a dictionary for each URL and caption pair.
# 2. Use the json package from the standard library to output this list into a
# file.












#####################################
# Advanced Bonus Challenge:
# Scrapy is one of the most popular web-scraping frameworks.
# Can you read it's documentation and learn how to write a Hacker News scraper
# using Scrapy?

# (No solution)

