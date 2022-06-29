import sqlite3
from sqlite3 import Cursor

class DbContext:
    """
    Father class that contains common methods for database connection between models
    """
    def __init__(self) -> None:
        """
        Method that defines the constructor of the class
        """
        self.__db_name = "database\\app_restaurante_database.db"
    
    def run_query(self,
                  query: str,
                  parameters = ()) -> Cursor:
        """
        Method that runs a query in the database with parameters given
        """
        try:
            with sqlite3.connect(self.__db_name) as connection:
                cursor = connection.cursor()
                result = cursor.execute(query,
                                        parameters)
                connection.commit()
        except Exception as ex:
            raise ex
        return result