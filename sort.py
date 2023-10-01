from cassandra.cluster import Cluster

# Connect to your Cassandra cluster (replace with your actual Cassandra cluster's IP addresses)
cluster = Cluster(['127.0.0.1'])  # Use your Cassandra cluster's IP address or hostname

# Connect to the keyspace (replace 'mykeyspace' with your keyspace name)
session = cluster.connect('movie_keyspace')  # Use your keyspace name

# Define your CQL query
cql_query = "SELECT * FROM Rating WHERE Rating = 'PG' ORDER BY rating"

# Execute the query
result = session.execute(cql_query)

# Process the results
for Rating in result:
    print(result)  # Replace this with your desired processing logic
