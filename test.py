import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('movies.xml')
root = tree.getroot()

# initialize a variable to rount movies with 'R' Rating
r_count = 0


for movie in root.findall('movie'):
    rating = movie.find('rating').text
    if rating == 'R':
        r_count += 1


# Print the count of movies with an "R" rating
print(f"Number of movies rated as 'R': {r_count}")
