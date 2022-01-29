from psycopg2 import connect
from psycopg2.errors import DuplicateDatabase, DuplicateTable, OperationalError

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"

db_create = "CREATE DATABASE workshop"
users_table_create = """CREATE TABLE users (
              id serial primary key,
              username varchar(255) unique,
              hashed_password varchar(80)
              );
              """
messages_table_create = """CREATE TABLE messages (
              id serial primary key,
              from_id integer references users(id) ON DELETE CASCADE,
              to_id integer references users(id) ON DELETE CASCADE,
              creation_date timestamp default current_timestamp,
              text varchar(255)
              );"""

try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True # ustawiamy autocommit żeby nie zatwierdzać za każdym razem
    cursor = cnx.cursor() # utworzenie kursora
    try:
        cursor.execute(db_create)
        print("Baza danych 'workshop' została utworzona")
    except DuplicateDatabase as e:
        print(f"Błąd {e}: podana baza danych już istnieje.")
    cnx.close()
except OperationalError as e:
    print(f"Błąd {e}: Błąd połączenia")

try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST, database="warsztat")
    cnx.autocommit = True # ustawiamy autocommit żeby nie zatwierdzać za każdym razem
    cursor = cnx.cursor() # utworzenie kursora
    try:
        cursor.execute(users_table_create)
        print("Tabela 'users' została utworzona")
    except DuplicateTable as e:
        print(f"Błąd {e}: podana tabela już istnieje.")

    try:
        cursor.execute(messages_table_create)
        print("Tabela 'messages' została utworzona")
    except DuplicateTable as e:
        print(f"Błąd {e}: podana tabela już istnieje.")
    cnx.close()
except OperationalError as e:
    print(f"Błąd {e}: Błąd połączenia")

