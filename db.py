import sqlite3

#This data table is for my classes
CREATE_CLASSES_TABLE = """CREATE TABLE IF NOT EXISTS Classes (
                        pk TEXT PRIMARY KEY,
                        class_name TEXT, 
                        category_list TEXT,
                        weight_list TEXT
                        study_session TEXT);
                        """

INSERT_CLASSES = "INSERT INTO Classes (class_name) VALUES (?);"
INSERT_WEIGHTS =  "INSERT INTO Classes (category_list, weight_list) VALUES (?, ?);"

#used for if the class is already in the system but not the weights
INSERT_WEIGHTS_CATEGORY = "UPDATE Classes SET category_list = ?, weight_list = ? WHERE class_name = ?;"

FIND_VALUE_BY_CONDITION = "SELECT category_list, weight_list FROM Classes WHERE class_name = ?;"
CHECK_IF_NULL = "SELECT weight_list IS NOT NULL, category_list IS NOT NULL FROM Classes WHERE class_name = ?;"



GET_ALL_CLASSES = "SELECT class_name FROM Classes"
GET_CLASSES_BY_NAME = "SELECT * FROM Classes WHERE class_name = ?;"

REMOVE_DUPLICATE_CLASS = "SELECT DISTINCT class_name from Classes"



#Danger removing entitre table
DELETE_ENTIRE_TABLE = "DROP TABLE IF EXISTS Classes"

def connect():
    return sqlite3.connect("VisualWork.db")

def create_classes_table(connection):
    with connection:
        connection.execute(CREATE_CLASSES_TABLE)

def add_classes(connection, class_name):
    with connection:
        connection.execute(INSERT_CLASSES, (class_name,))

def add_weights(connection, category_list, weight_list):
    with connection:
        connection.execute(INSERT_WEIGHTS, (category_list, weight_list))

def update_weights(connection, class_name, category_list, weight_list):
    with connection:
        connection.execute(INSERT_WEIGHTS_CATEGORY, (category_list, weight_list, class_name) )

def get_all_classes(connection):
    with connection:
        return connection.execute(GET_ALL_CLASSES).fetchall()

#fetchall gets the entire column of name
def get_classes_by_name(connection, class_name):
    with connection:
       return  connection.execute(GET_CLASSES_BY_NAME, (class_name,)).fetchall()
    
def get_weights(connection, class_name):
    with connection:
        result = connection.execute(FIND_VALUE_BY_CONDITION, (class_name,)).fetchone()
        return result

#finds class name in the data base
def find_class(connection, class_name):
    with connection:
        result = connection.execute(GET_CLASSES_BY_NAME, (class_name,)).fetchone()
        return result is None
    
def check_if_columns_null(connection, condition):
    with connection:
        result = connection.execute(CHECK_IF_NULL, (condition,)).fetchone()
        # returns a tuple (weight_list_is_not_null, category_list_is_not_null)
        if (result[0] == False or result[1] == False):
            return False
        return True

#removes duplicate classes
def removes_duplicates(connection):
    with connection:
        connection.execute("SELECT DISTINCT class_name from Classes")

#removes the entire table
def remove_table(connection):
    with connection:
        connection.execute(DELETE_ENTIRE_TABLE)
        connection.execute("VACUUM")


