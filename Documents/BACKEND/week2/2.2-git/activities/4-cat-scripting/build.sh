mkdir docs

cat templates/top.html content/index.html templates/bottom.html > docs/index.html

cat templates/top.html content/projects.html templates/bottom.html > docs/projects.html

cat templates/top.html content/contact.html templates/bottom.html > docs/contact.html

mv css/style.css docs

mv img/funky-lines.png docs

mv img/profile.jpg docs

mv img/sunset.jpg docs
