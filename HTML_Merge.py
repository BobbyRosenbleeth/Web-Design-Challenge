#Insert table into Page 7 file.

with open('my_file.html', 'r') as f:
    table_html = f.read()

with open('page7.temp.html', 'r') as g:
    main_html = g.read()

insert_location = main_html.find('<div id="table-placeholder"></div>')
new_html = main_html[:insert_location] + table_html + main_html[insert_location:]

with open('page7.html', 'w') as h:
    h.write(new_html)