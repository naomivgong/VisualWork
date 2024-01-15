from db import SQLHandler

#create instance of SQLHandler/Helpers to handle database actions
VisualWork_db_handler = SQLHandler("VisualWork.db")

#converts a list into a string
def listToString(list):
    listToStr = ','.join(map(str, list))
    return listToStr


def calculateGrade():
    className = input("What is the name of the class")
    catNum = int(input("How many weighted categories?: "))
    categoryList = []
    weightList = []
    #ask the user for how their class is graded
    for i in range(catNum):
        category = input("What is the category name ")
        categoryList.append(category)
        weight = input("What is the weight of the category (ex. 20%)? ")
        #removes percentage sign
        weight = int(weight[:-1])
        weightList.append(weight/100)
    #ask the user for their grade in each category
    gradeInCategory = []
    for i in categoryList:
        gradeInCategory.append(int(input("(Do not put %) What is your grade in " + i + " ")))

    #multiplies their grade in each category times the weight
    result = [x * y for x, y in zip(weightList, gradeInCategory)]
    total = 0
    for i in range(0, len(result)):
        total += result[i]
    print("Your grade is " + str(total) + " ")

    rowID = VisualWork_db_handler.insert_class(className, listToString(categoryList), listToString(weightList))
    # Retrieve and print data from the "students" table

    select_query = "SELECT * FROM Classes"
    result = VisualWork_db_handler.execute_query(select_query)
    for row in result:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
     # Close the database connection
    VisualWork_db_handler.close_connection()



userquit = False
while (not userquit):
    print("calculate grade [c]")
    print("log study session [l]")
    print("predict my score on an exam [p]")
    print("Load a new class [N]")
    print("Quit[q]")
    command = input("Please enter a command: ")

    if command == 'c':
        calculateGrade()
    if command == 'q':
        userquit = True