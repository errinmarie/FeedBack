import requests

print('------------ Challenge 1')
# Challenge 1
# Examine the following code. Can you understand what it is doing? Can
# you predict the sort of data it will print out? Get it functioning.
# You will need to use pipenv to install requests.
response = requests.get('https://en.wikipedia.org/wiki/Main_Page')
html_code = response.text
for line in html_code.splitlines():
    if '<title>' in line:
        print(line)





print('------------ Challenge 2')
# Challenge 2
# Go to the website in your browser.  Using the top code as a guide,
# write code that will look for the topic of today's featured article,
# and print out the text surrounding that.
response = requests.get('https://en.wikipedia.org/wiki/Main_Page')
html_code = response.text
for line in html_code.splitlines():
    # Would have to be different based on what is today
    if 'King Island emu' in line:
        print(line)






print('------------ Bonus')

# Bonus Challenge 1
response = requests.get('https://news.ycombinator.com')
html_code = response.text
for line in html_code.splitlines():
    # Using "not in" and continue lets us skip ones that don't have the word
    # "storylink" (which indicates a story link, based on inspection of the source code)
    if 'storylink' not in line:
        continue
    #print(line)


# Bonus Challenge 2 + 3
results = []
for line in html_code.splitlines():
    if 'storylink' not in line:
        continue

    split = line.split('"')
    # Using print to figure out where the heck the link is in this split list.
    # Turns out it seems to always be at index 15
    #for i, line in enumerate(split):
    #    print(i, line)

    # Extract URL
    url = split[15]

    # All URLs should have HTTP, skip ones that don't
    if 'http' not in url:
        continue

    # The news caption is in index 18: fetch & remove cruft
    messy_caption = split[18]
    split = messy_caption.split('<')
    caption = split[0]
    caption = caption.strip('>')

    print(caption, '(URL at:', url, ')')

    # Now, let's put the URL and caption into the results list
    results.append({
        'url': url,
        'caption': caption,
    })


#####################################
# Bonus Challenge #3
import json
output_file = open('3_bonus_output.json', 'w+')
json.dump(results, output_file, indent=4)


