# 5(C). Create a Cassandra table using python, and insert everything from xml to the db table called 'movies'

# Parse Data from movies.xml and insert them into Cassandara table. ( Keyspace = 'movie_keyspace' and Table = 'movies') 

from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()

cluster = Cluster(['localhost'])
session = cluster.connect()

session.execute("CREATE KEYSPACE IF NOT EXISTS movie_keyspace WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}")
session.set_keyspace("movie_keyspace")

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


session.shutdown()
cluster.shutdown()