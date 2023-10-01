import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()

r_count = 0


for movie in root.findall('movie'):
    rating = movie.find('rating').text
    if rating == 'R':
        r_count += 1

print(f"Number of movies rated as 'R': {r_count}")
