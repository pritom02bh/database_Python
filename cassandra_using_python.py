from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import xml.etree.ElementTree as ET

# Load the XML data from the file
tree = ET.parse('movies.xml')
root = tree.getroot()

# Connect to the Cassandra cluster (adjust host and port as needed)
cluster = Cluster(['localhost'])
session = cluster.connect()

# Create a keyspace and set it as the current keyspace
session.execute("CREATE KEYSPACE IF NOT EXISTS movie_keyspace WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}")
session.set_keyspace("movie_keyspace")

# Define a CQL query to create the 'movies' table
create_table_query = """
CREATE TABLE IF NOT EXISTS movies (
    title TEXT PRIMARY KEY,
    type TEXT,
    format TEXT,
    year INT,
    rating TEXT,
    stars INT,
    description TEXT
)
"""
session.execute(create_table_query)

# Iterate through each <movie> element and insert data into the 'movies' table
for movie in root.findall('movie'):
    title = movie.get('title')
    movie_type = movie.find('type').text
    format = movie.find('format').text
    year = int(movie.find('year').text)
    rating = movie.find('rating').text
    stars = int(movie.find('stars').text)
    description = movie.find('description').text

    insert_query = """
    INSERT INTO movies (title, type, format, year, rating, stars, description)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    session.execute(insert_query, (title, movie_type, format, year, rating, stars, description))

# Close the Cassandra session and cluster
session.shutdown()
cluster.shutdown()