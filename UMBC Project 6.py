################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None

  return val

################ Main Program ################

##Set needed functions 

#Blank dictionary 
studentGrades = {}

#Add a student to dictionary function
def addStudent():
  print()
  student = input("Enter a student name: ")
  studentGrades[student] = []
  print()
  print(f"{student} added!")

#Remove a student funcition 
def removeStudent():
  print()
  student = input("Enter a stduent name: ")
  if student not in studentGrades:
    print()
    print(f"{student} not in our records")
  else:
    studentGrades.pop(student)
    print()
    print(f"{student} removed!")

#Add quiz grade function 
def addGrade():
  print()
  student = input("Enter a student: ")
  if student not in studentGrades:
    print()
    print(f"{student} not in our records")
  else: 
    print()
    grade = getNumberGradeFromUser()
    studentGrades[student].append(grade)
    print()
    print(f"{grade} added to {student} grades")

#List quiz grades 
def listGrades():
  print()
  student = input("Enter a student: ")
  if student not in studentGrades:
    print()
    print(f"{student} not in our records")
  else: 
    #for grades in studentGrades[student]:
    print()
    print(f"{student} current grades are: ")
    for grades in studentGrades[student]:
      print(grades)      
    

#Calculate Letter Grade
def getLetterGrade(grade):
  if(grade >= 90):
    return "A"
  elif(grade >= 80):
    return "B"
  elif(grade >= 70):
    return "C"
  else:
    return "F"

#Calculate Letter Grade
def studentLetterGrade():
  totalGrade = 0
  print()
  student = input("Enter a student: ")
  if student not in studentGrades:
    print(f"{student} not in our records")
  else: 
    for grades in studentGrades[student]:
      totalGrade = totalGrade + grades
    finalGrade = totalGrade/len(studentGrades[student])
  letterGrade = getLetterGrade(finalGrade)
  print()
  print(f"{student} current letter grade is: {letterGrade}")

## Application Loop

#Blank Values
userInput = ""

#Valid input list
validInput = ["1", "2", "3", "4", "5", "6"]

#App Loop, while not equal to exit, continue loop 
while(userInput != 6):

  # Prompt the user to select an option
  print()
  displayMenu()

  #user input
  userInput = input("Select and Option: ")
  #userInput = int(userInput)

  #See if input is integer
  if userInput not in validInput:
    print()
    print("Invalid Input")

  else:
     userInput = int(userInput)

  #if option 1, add studnet 
  if(userInput == 1):
    addStudent()

  #elif option 2, remove student
  elif(userInput == 2):
    removeStudent()

  #elif option 3, add grade
  elif(userInput == 3):
    addGrade()

  #elif option 4, list grades
  elif(userInput == 4):
    listGrades()

  #elif option 5, get letter grade
  elif(userInput == 5): 
    studentLetterGrade()



