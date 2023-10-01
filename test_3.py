from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider

auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')

# Connect to your Cassandra cluster (replace with your actual Cassandra cluster's IP addresses)
cluster = Cluster(['localhost'])  # Use your Cassandra cluster's IP address or hostname

# Connect to the keyspace (replace 'movie_keyspace' with your keyspace name)
session = cluster.connect('movie_keyspace')  # Use your keyspace name

# Define your CQL query to select all rows from the 'Rating' table
cql_query = "SELECT Rating FROM movies"


# Execute the query
result = session.execute(cql_query)

print(result)
