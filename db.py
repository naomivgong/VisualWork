import sqlite3

#This data table is for my classes
CREATE_CLASSES_TABLE = """CREATE TABLE IF NOT EXISTS Classes (
                        pk TEXT PRIMARY KEY,
                        class_name TEXT, 
                        category_list TEXT,
                        weight_list TEXT);
                        """

INSERT_CLASSES = "INSERT INTO Classes (class_name, category_list, weight_list) VALUES (?, ?, ?);"

GET_ALL_CLASSES = "SELECT * FROM Classes"
GET_CLASSES_BY_NAME = "SELECT * FROM Classes WHERE class_name = ?;"

REMOVE_DUPLICATE_CLASS = "SELECT DISTINCT class_name from Classes"

#Danger removing entitre table
DELETE_ENTIRE_TABLE = "DROP TABLE IF EXISTS Classes"

def connect():
    return sqlite3.connect("VisualWork.db")

def create_classes_table(connection):
    with connection:
        connection.execute(CREATE_CLASSES_TABLE)

def add_classes(connection, class_name, category_list, rating):
    with connection:
        connection.execute(INSERT_CLASSES, (class_name, category_list, rating))

def get_all_classes(connection):
    with connection:
        return connection.execute(GET_ALL_CLASSES).fetchall()

#fetchall gets the entire column of name
def get_classes_by_name(connection, class_name):
    with connection:
       return  connection.execute(GET_CLASSES_BY_NAME, (class_name,)).fetchall()
    
def find_class(connection, class_name):
    with connection:
        result = connection.execute(GET_CLASSES_BY_NAME, (class_name,)).fetchone()
        return result is not None
    
#removes duplicate classes
def removes_duplicates(connection):
    with connection:
        connection.execute("SELECT DISTINCT class_name from Classes")

def remove_table(connection):
    with connection:
        connection.execute(DELETE_ENTIRE_TABLE)
        connection.execute("VACUUM")


