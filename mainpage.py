import db


connection = db.connect()
db.create_classes_table(connection)
    

#converts a list into a string
def listToString(list):
    listToStr = ','.join(map(str, list))
    return listToStr

#converts a string to a list
def stringToList(str):
    strToList = list(str.split(','))
    return strToList

def searchClass(connection, className):
    if db.find_class(connection, className):
        return True
    return False


def calculateGrade():
    
    className = input("What is the name of the class ")
    if (searchClass(connection, className) == False):
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
        #adds the class into my database
        db.add_classes(connection, className, listToString(categoryList), listToString(weightList))
        #prints my classes
        classes = db.get_all_classes(connection)
        for aclass in classes:
            print(aclass) 
    else:
        #fectch the weight and category of the class name 
        stringToList()
        

def loadClass():
    newClassName = input("What is the new class name")

userquit = False
while (not userquit):
    print("calculate grade [1]")
    print("log study session [2]")
    print("predict my score on an exam [3]")
    print("Load a new class [4]")
    print("Quit[5]")
    command = input("Please enter a command: ")

    if command == '1':
        calculateGrade()
    if command == '5':
        userquit = True