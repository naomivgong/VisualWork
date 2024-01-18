import db
from studySessions import studySessions


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
        db.update_weights(connection, className, listToString(categoryList), listToString(weightList))
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
        listOfCategories = stringToList(listOfCategories)
        listOfWeight = stringToList(listOfWeight)
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
def loadClass():
    newClassName = input("What is the new class name? ")
    if searchClass(connection, newClassName) == True:
        db.add_classes(connection, newClassName)
        #adds a key into the Python Dictionary
        print(f"new key {newClassName}")
        studySession[newClassName] = []
    else:
        print("this class already exists")

def logSession():
    date = input("Date (format: June 6, 2022): ")
    #print out a menu for the class names
    classList = db.get_all_classes(connection)
    print("Select class")
    tempClassList = []
    #prints out the menu of the classes menu, the menu will continue to be printed
    #if user doesnt enter valid number
    classSelected = False
    while (not classSelected):
        for n, classes in enumerate(classList):
            className = classes[0]
            tempClassList.append(className)
            print(f"{className} [{n+1}]")
        classNameSelected = int(input("Select a class from the list: "))
        #returns the user if the entered an invalid option
        if (classNameSelected >= 1 or classNameSelected <= len(tempClassList)):
            classSelected = True
        else:
            print("Try Again")
    classNameSelected = tempClassList[classNameSelected - 1]
    print('---')
    print(classNameSelected)
    print('---')
    print("Enter the duration")
    hours = int(input("How many hours: "))
    minutes = int(input("How many minutes: "))
    material = input("What did you study for ex. Physics Midterm 1: ")
    notes = input("Any Notes? (ex. did chapter 5 problems): ")

    duration = hours * 60 + minutes

    #creates a study session object
    newStudySession = studySessions(date,className,duration, material, notes)
    studySession[classNameSelected].append(newStudySession)
    print(studySession)

db.remove_table(connection)
#will create a list of dictionaries
studySession = {}
db.create_classes_table(connection)
userquit = False
while (not userquit):
    print("------")
    '''
    classes = db.get_all_classes(connection)
    for aclass in classes:
        print(aclass)
    '''
    print("Select Menu")
    print("-------------------")
    print("calculate grade [1]")
    print("log study session [2]")
    print("predict my score on an exam [3]")
    print("Load a new class [4]")
    print("View All Classes [5]")
    print("Quit[6]")
    print("-------------------")
    command = input("Please enter a command: ")

    if command == '1':
        calculateGrade()
    elif command == '2':
        logSession()
    elif command == '4':
        loadClass()
    elif command == '6':
        userquit = True
    else:
        print("Please select a valid option")