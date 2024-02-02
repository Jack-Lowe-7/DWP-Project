import databaseComms as dc

def consoleChoice():
  choice = int(input("[1] Add a student\n[2] Award Stamps\n[3] View a student\n"))
  if choice == 1:
    name = input("Enter student's name: ")
    form = input("Enter student's form: ")
    stamps = input("Enter student's current stamps: ")
    emailPre = input("Enter student's email prefix (e.g. 19lowe.j): ")
    mainClass = input("Enter student's class: ")
    dc.add_student(name, form, stamps, emailPre, mainClass)
  elif choice == 2:
    name = input("Enter student name: ")
    stamps = input("Enter stapms to add: ")
    dc.award_stamps(name, stamps)
  elif choice == 3:
    emailPre = input("Enter student's email prefix (e.g. 19lowe.j): ")
    print(dc.view_student(emailPre))
  else:
    print("Please enter a vaild option")
    consoleChoice()

consoleChoice()