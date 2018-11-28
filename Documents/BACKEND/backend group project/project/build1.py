index_top = open('templates/top.html').read()
index_content = open('content/index.html').read()
index_bottom = open('templates/bottom.html').read()
index_html = index_top + index_content + index_bottom
open('docs/index.html', 'w+').write(index_html)


find_food_top = open('templates/top.html').read()
find_food_content = open('content/find_food.html').read()
find_food_bottom = open('templates/bottom.html').read()
find_food_html = find_food_top + find_food_content + find_food_bottom
open('docs/find_food.html', 'w+').write(find_food_html)


donate_food_top = open('templates/top.html').read()
donate_food_content = open('content/donate_food.html').read()
donate_food_bottom = open('templates/bottom.html').read()
donate_food_html = donate_food_top + donate_food_content + donate_food_bottom
open('docs/donate_food.html', 'w+').write(donate_food_html)
