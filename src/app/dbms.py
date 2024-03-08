from datetime import datetime
from typing import Any, Tuple, Union

from pytz import BaseTzInfo
import psycopg2


# Connect to the default database
def create_db(dbname: str):
    conn = psycopg2.connect(dbname="postgres")
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Check if the database exists
    cursor.execute(
        "SELECT 1 \
         FROM pg_database \
         WHERE datname = %s;", 
        (dbname,)
    )
    exists = cursor.fetchone()

    if exists:
        print("Database already exists.")
    else:
        # Create a new database
        cursor.execute(f"CREATE DATABASE {dbname};")

        cursor.close()
        conn.close()
        conn = psycopg2.connect(dbname=dbname)
        cursor = conn.cursor()

        with open("app/dump.sql", "r") as file:
            sql_commands = file.read()
            cursor.execute(sql_commands)
        print("Database created.")

    cursor.close()
    conn.close()


class DBMS:
    def __init__(
        self, 
        dbname: str,
        user: str,
        # password: str,
        host: str,
        port: int,
        local_tz: BaseTzInfo
    ) -> None:
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            # password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()
        self.local_tz = local_tz

    def add_user_and_pasport(
        self,
        user_tg_id: Union[int, str]
    ) -> None:
        """Adding user to base"""
        date = datetime.now(self.local_tz)
        join_date = date.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute(
            "INSERT INTO users \
             (user_tg_id, join_date) \
             VALUES (%s, %s)",
            (user_tg_id, join_date)
        )
        self.conn.commit()

    def get_user(self, user_tg_id: Union[int, str]) -> Union[Tuple[Any], None]:
        self.cursor.execute(
            "SELECT * \
             FROM users \
             WHERE user_tg_id = %s",
            (user_tg_id,)
        )
        result = self.cursor.fetchone()
        if not result:
            return
        return result

    def user_exists(self, user_tg_id: Union[int, str]) -> bool:
        self.cursor.execute(
            "SELECT user_tg_id \
             FROM users \
             WHERE user_tg_id = %s",
            (user_tg_id,)
        )
        result = self.cursor.fetchall()
        if not result:
            return False
        return bool(result[0])

    def close(self) -> None:
        self.conn.close()
