#Lets create a folder for website

"""This program will take site name, author, and file types
and then create a folder for the site."""

site = input("Enter the site name: ")
author = input("Enter the author's name: ")
js_reqd = input("Do you need folder for javascript file? (y/n): ")
css_reqd = input("Do you need folder for css file? (y/n): ")

import os

os.mkdir(site)
print(f"Created {os.path.dirname}")
os.chdir(site)

with open('index.html', 'w') as f:
    f.write(f'<!DOCTYPE html>\n<html>\n<head>{site}</head>\n<meta>{author}</meta>\n</html>')

#os.chdir('..')
if js_reqd == 'y': 
    os.makedirs('js')
    print(f"Created {os.path.dirname}")
if css_reqd == 'y':
    os.makedirs('css')
    print(f"Created {os.path.dirname}")

