# Read movie_data from Cassandra, Keyspace = "movie_keyspace", Table = 'movies'

from cassandra.cluster import Cluster

cluster = Cluster(['localhost'])
session = cluster.connect()


session.set_keyspace("movie_keyspace")


select_query = "SELECT * FROM movies"


rows = session.execute(select_query)

for row in rows:
    print("Title:", row.title)
    print("Type:", row.type)
    print("Format:", row.format)
    print("Year:", row.year)
    print("Rating:", row.rating)
    print("Stars:", row.stars)
    print("Description:", row.description)
    print("-------------------")

session.shutdown()
cluster.shutdown()
