from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider

auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')

cluster = Cluster(['localhost'])

session = cluster.connect('movie_keyspace') 

cql_query = "SELECT * FROM movies WHERE rating = 'PG'"

result = session.execute(cql_query)

for row in result:
    print(row)