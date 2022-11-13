import sys
import time

def loading():
    loading = "\n...\n...\n...\n"
    for i in loading:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.09),
    print()

def hello():
    hello = "\nWelcome to Contact Tracer!\n"
    for i in hello:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.07),
    print()

def optionOne():
    global inputName, contact, age, gender, address, number, vaccine, booster, comorbidity
    print("\nYou have selected: Option 1. Kindly fill up the information below.")
    time.sleep(0.5)
    inputName = input("\nName: ")
    contact = inputName.upper()
    age = int(input("\nAge: "))
    gender = input("\nGender (F/M/Transman/Transwoman/Rather not disclose): ")
    address = input("\nAddress: ")
    number = int(input("\nContact Number: "))
    vaccine = input("\nHave you been fully vaccinated againts COVID-19? (Yes/No): ")
    booster = input("\nHave you completed your booster shots against COVID-19? (Yes/No): ")
    comorbidity = input("\nDo you have any existing health conditions? (If yes, please state them. If no, type none.): ")
    loading()
    print("\nYour personal information has been saved. Thank you for your cooperation.\n\n")
    time.sleep(1)

def saveInfo():
    global userContact
    userContact = {
        contact:    {"Name" : inputName,
                    "Age" : age,
                    "Gender": gender,
                    "Address" : address,
                    "Number" : number,
                    "Vaccine" : vaccine,
                    "Booster" : booster,
                    "Comorbidity" : comorbidity
                    }
                }

def optionTwo():
    global contactInfo
    print("\nYou have selected: Option 2.")
    loading()
    searchInfo = input("\nEnter the full name of the contact you wish to search: ")
    contactInfo = searchInfo.upper()
    print()
    loading()
    if contactInfo in userContact:
        show = "\nThis is what we retrieved:\n"
        for i in show:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05),
        print()
        for key, value in userContact.items():
            print("Name: ",value["Name"], "\nAge: ",value["Age"], "\nGender: ",value["Gender"], "\nAddress: ",value["Address"], "\nContact Number: ",value["Number"], "\nFully vaccinated?: ",value["Vaccine"], "\nBooster shots complete?: ",value["Booster"], "\nComorbidities: ",value["Comorbidity"])
        print("")
    if contactInfo not in userContact:
        print("\nSorry, that contact is unavailable. Please try again.\n\n")

def goodbye():
    print("Thank you for using Contract Tracer, please come again!")

def contractTracer():
    hello()

    while True:
        menu = """========================= M E N U =========================
        
        1: Create a contact information
        2: Search the archive for existing contact
        3: Exit
        \n===========================================================
        """
        print(menu)
        time.sleep(0.6)

        userInput = int(input("Please select an option above: "))

        if userInput !=1 and userInput !=2 and userInput !=3:
            print("\nInvalid option. Please try again.")
            time.sleep(0.9)

        if userInput == 1:
            optionOne()
            saveInfo()

        if userInput == 2:
            optionTwo()

        if userInput == 3:
            goodbye()
            break

contractTracer()