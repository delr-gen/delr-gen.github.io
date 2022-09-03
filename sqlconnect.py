from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy


# configure Cloud SQL Python Connector properties
def getconn():
    connector = Connector()
    return connector.connect(
        "bacons-recipe-app:us-west2:baconsrecipes",
        "pymysql",
        user="root",
        password="Georginaggiraffe0803!",
        db="bacon_recipe"
    )


# create connection pool to re-use connections
def create_pool():
    return sqlalchemy.create_engine(
        "mysql+mysqlconnector://",
        creator=getconn,
    )
    


# query or insert into Cloud SQL database
if __name__ == "__main__":
    with create_pool().connect() as db_conn:
        # query database
        result = db_conn.execute("SELECT * from Recipe").fetchall()

        # Do something with the results
        for row in result:
            print(row)
