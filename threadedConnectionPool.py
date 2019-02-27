from psycopg2.pool import ThreadedConnectionPool
from multiprocessing.pool import ThreadPool
import time

queries = ['asdf', 'fghj', ...]

pool = ThreadedConnectionPool(0, 6,
                           dbname="bizops",
                           host="bizops-cluster.cvppsscrmyqr.us-east-1.redshift.amazonaws.com",
                           port="5439",
                           user="akalloo",
                           password=p)

def execute_query(query):
    conn = pool.getconn(query)
    with conn.cursor() as cur:
        cur.execute(query)
        value = pd.DataFrame(cur.fetchall())
    pool.putconn(conn, query)
    return value

thread_pool = ThreadPool(len(queries))
results = thread_pool.map(execute_query, queries)
pool.closeall()

for tb in range(len(table_names)):
    exec(table_names[tb] + " = results["+str(tb)+"]")
