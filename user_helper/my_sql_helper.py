from sqlalchemy.engine import create_engine
import psycopg2
engine = create_engine('postgresql://postgres:example@0.0.0.0:5432/postgres') # postgresql - назва драйвера,
# логін, а друге пароль,@ - ip і port server(0.0.0.0:5432)#mydatabase - назва бд потрібно створити
connection = engine.connect()
connection.execute(
    """
    CREATE TABLE usersdata(
	    user_id serial PRIMARY KEY,
        username VARCHAR (50) NOT NULL,
        password VARCHAR (50) NOT NULL
    """)

