import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()

movie_names = []
for movie in root.findall('movie'):
    title = movie.get('title')
    movie_names.append(title)

for name in movie_names:
    print(name)


    r_count = 0

    for movie in root.findall('movie'):
        rating = movie.find('rating').text
        if rating == 'R':
            r_count += 1

print(f"Number of movies rated as 'R': {r_count}")