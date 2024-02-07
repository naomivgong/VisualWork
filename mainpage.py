import db
from studySessions import studySessions
import helpers


connection = db.connect()
db.create_classes_table(connection)

def weightTimesCategoryGrade(weightList, gradeInCategory):
    #multiplies their grade in each category times the weight
    result = [x * y for x, y in zip(weightList, gradeInCategory)]
    total = 0
    for i in range(0, len(result)):
        total += result[i]
    return total

def calculateGrade():
    
    className = input("What is the name of the class ")
    #if the class name  doesnt exists or if it does exist but no weights
    if (searchClass(connection, className) == True):
        print("you need to add the class first")
        loadClass()
    elif (db.check_if_columns_null(connection, className) == False):
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
            gradeInCategory.append(float(input("(Do not put %) What is your grade in " + i + " ")))

        total = weightTimesCategoryGrade(weightList, gradeInCategory)
        print("Your grade is " + total + " ")
        #adds the class into my database
        db.update_weights(connection, className, helpers.listToString(categoryList), helpers.listToString(weightList))
        #prints my classes
        classes = db.get_all_classes(connection)
        print("hi")
        for aclass in classes:
            print(aclass) 
    else:
        #fectch the weight and category of the class name 
        print("The class has been loaded")
        getWeightResults = db.get_weights(connection, className)
        listOfCategories, listOfWeight = getWeightResults
        #converts to current string digit list into a list of ints
        listOfCategories = helpers.stringToList(listOfCategories)
        listOfWeight = helpers.stringToList(listOfWeight)
        #converts the list of weight to ints
        listOfWeight =  [float(num) for num in listOfWeight]
        #ask the user for their input in each category
        grades = []
        for category in listOfCategories:
            categoryGrade = float(input(f"What is your grade in {category} ex. (90)"))
            grades.append(categoryGrade)
        total = weightTimesCategoryGrade(listOfWeight, grades)
        print(f"Your grade is {total}")


#adds a class into your system
def loadClass(studySession):
    newClassName = input("What is the new class name? ")
    if searchClass(connection, newClassName) == True:
        db.add_classes(connection, newClassName)
        #adds a key into the Python Dictionary
        formattedClassName = f"'{newClassName}'"
        print(f"new key {formattedClassName}")
        studySession[formattedClassName] = []
    else:
        print("this class already exists")

def searchClass(connection, className):
    if db.find_class(connection, className):
        return True
    return False


def viewAllClasses(connection):
    classes = db.get_all_classes(connection)
    print("Here is a list of the loaded classes")
    print("------------------------------------")
    for aclass in classes:
        print(str(aclass)[2:-3])
        print("----------")

#will create a list of dictionaries
studySession = {}
# Update the study session dictionary
newStudySession = studySessions.construct_studySession(connection, studySession)
studySession.update(newStudySession)
userquit = False

while (not userquit):
    print("------")
    
    classes = db.get_all_classes(connection)
    for aclass in classes:
        print(aclass)
    print("Select Menu")
    print("-------------------")
    print("calculate grade [1]")
    print("log study session [2]")
    print("predict my score on an exam [3]")
    print("Load a new class [4]")
    print("View All Classes [5]")
    print ("Direct me to Study Sessions[6]")
    print("Quit[7]")
    print("-------------------")
    command = input("Please enter a command: ")

    if command == '1':
        helpers.clearTerminal()
        calculateGrade(connection)
    elif command == '2':
        studySessions.logSession(connection)
    elif command == '4':
        helpers.clearTerminal()
        input("Press Enter to continue...")
        loadClass(studySession)
    elif command == '5':
        helpers.clearTerminal()
        viewAllClasses(connection)
        input("Press Enter to continue...")
    elif command == '7':
        userquit = True
    else:
        print("Please select a valid option")