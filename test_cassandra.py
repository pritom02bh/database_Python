from cassandra.cluster import Cluster

# Connect to the Cassandra cluster (adjust host and port as needed)
cluster = Cluster(['localhost'])
session = cluster.connect()

# Set the keyspace (make sure it matches the keyspace you used when creating the table)
session.set_keyspace("movie_keyspace")

# Define a CQL query to select all data from the 'movies' table
select_query = "SELECT * FROM movies"

# Execute the query and print the results
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

# Close the Cassandra session and cluster
session.shutdown()
cluster.shutdown()
