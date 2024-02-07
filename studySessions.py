import db
import helpers

class studySessions:

    def __init__(self, date, className, duration, material, notes):
        self.date = date
        self.className = className
        self.duration = duration
        self.material = material
        self.notes = notes

    @staticmethod
    def logSession(connection, studySession):
        #checks if there are any classes
        classList = db.get_all_classes(connection)
        if classList == []:
            print("Please load a class first")
            return
        date = input("Date (format: June 6, 2022): ")
        #print out a menu for the class names
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

        #creates a study session object and adds it into the studySessions dictionary
        newStudySession = studySessions(date,classNameSelected,duration, material, notes)
        dictObj = newStudySession.__dict__
        formattedClassName = f"'{classNameSelected}'"
        print("the class name selected is " + formattedClassName)
        studySession[formattedClassName].append(dictObj)
        #now extract the list of study sessions of the classNameSelected
        allOfClassStudySession = studySession[formattedClassName]
        #update the study session to the database
        allOfClassStudySession = helpers.listToString(allOfClassStudySession)
        db.update_studysession(connection,allOfClassStudySession, classNameSelected)
        print(studySession)

    @staticmethod
    def construct_studySession(connection):
        # tuples are immutable, so create a new dictionary
        studySessionInfo = db.get_all_studysessions(connection)
        classes = db.get_all_classes(connection)

        newStudySession = {}
        for className, session in zip(classes, studySessionInfo):
            # Initialize an empty list for each class
            newStudySession[str(className)[1:-2]] = []

        print("construct study sessions")
        return newStudySession
    
    @staticmethod
    def printAllStudySession(connection):
        helpers.clearTerminal()
        exit = False
        while (not exit):
            print("Welcome to your Study Sessions!")
            print("Menu: please select a number")

            #displays graphs of hours studied over time
            print("see study progress [1] ")
            print("view all study sessions [2]")
            print("I want to select a particular class's study session [3]")

    def selectParticularStudySession(connection):
        helpers.clearTerminal()
        print("options: ")
        tempClassList = []
        classList = db.get_all_classes(connection)
        for n, classes in enumerate(classList):
                className = classes[0]
                tempClassList.append(className)
                print(f"{className} [{n+1}]")
        print("")
        








