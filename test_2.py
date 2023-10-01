import xml.etree.ElementTree as ET

# Load the XML data from the file
tree = ET.parse('movies.xml')
root = tree.getroot()

# Iterate through each <movie> element and extract the title
movie_names = []
for movie in root.findall('movie'):
    title = movie.get('title')
    movie_names.append(title)

# Print the list of movie names
for name in movie_names:
    print(name)


# initialize a variable to rount movies with 'R' Rating
    r_count = 0

    for movie in root.findall('movie'):
        rating = movie.find('rating').text
        if rating == 'R':
            r_count += 1


# Print the count of movies with an "R" rating
print(f"Number of movies rated as 'R': {r_count}")