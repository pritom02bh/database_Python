from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider
import xml.etree.ElementTree as ET

auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')

cluster = Cluster(['localhost'])

session = cluster.connect('movie_keyspace') 


query = "SELECT * FROM movies WHERE rating = 'PG' ALLOW FILTERING"
result = session.execute(query)


root = ET.Element("movies")


for row in result:
    movie = ET.SubElement(root, "movie")
    ET.SubElement(movie, "title").text = row.title
    ET.SubElement(movie, "year").text = str(row.year)
    ET.SubElement(movie, "rating").text = row.rating
    


tree = ET.ElementTree(root)
tree.write("sorted_movie.xml", encoding="utf-8", xml_declaration=True)


session.shutdown()
cluster.shutdown()