# a. read movies.xml from python and print out all the movies, and count how many movies in the list are rated as ‘R’.
# b. print out root node's attribute

import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()

r_rated_count = 0

for movie in root.findall('movie'):
    title = movie.get('title')
    rating = movie.find('rating').text
    
    print(f"Title: {title}")
    print(f"Rating: {rating}")
    print(f"Title: {title}")
    print('    ')
    
    if rating == 'R':
        r_rated_count += 1

print(f"Total 'R' rated movies: {r_rated_count}")


# Print out the root attribute
root_attribute = root.get('shelf')
print('    ')
print(f"Root Attribute: {root_attribute}")
