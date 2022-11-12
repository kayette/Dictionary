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
    global inputName, fullname, age, gender, address, number, vaccine, booster, comorbidity
    print("\nYou have selected: Option 1. Kindly fill up the information below.")
    time.sleep(0.5)
    inputName = input("\nName: ")
    fullname = inputName.upper
    age = input("\nAge: ")
    gender = input("\nGender (F/M/Transman/Transwoman/Rather not disclose): ")
    address = input("\nAddress: ")
    number = input("\nContact Number: ")
    vaccine = input("\nHave you been fully vaccinated againts COVID-19? (Yes/No): ")
    booster = input("\nHave you completed your booster shots against COVID-19? (Yes/No): ")
    comorbidity = input("\nDo you have any existing health conditions? (If yes, please state them. If no, type none.): ")
    loading()
    print("\nYour personal information has been saved. Thank you for your cooperation.\n\n")
    time.sleep(1)

def saveInfo():
    global userContact
    userContact = {
        fullname: {"Name": inputName,
                    "Age" : age,
                    "Gender" : gender,
                    "Address" : address,
                    "Phone" : number,
                    "Vaccine" : vaccine,
                    "Booster" : booster,
                    "Comorbidity" : comorbidity
                    }
    }

def optionTwo():
    global searchInfo
    print("\nYou have selected: Option 2.")
    loading()
    searchInfo = input("\nEnter the full name of the contact you wish to search: ")
    searchInfo = searchInfo.upper
    print()
    loading()
    if searchInfo in userContact:
        show = "\nThis is what we retrived:\n"
        for i in show:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05),
        print()
        for key, value in userContact.items():
            print("Name: ", value["name"], "\nAge: ", value["age"], "\nGender: ", value["gender"], "\nAddress: ", value["address"], "\nContact Number: ", value["number"], "\nFully vaccinated?: ", value["vaccine"], "\nBooster shots complete?: ", value["booster"], "\nComorbidities: ", value["comorbidity"])
        print()
    if searchInfo not in userContact:
        print("\nSorry, than contact is unavailable. Please try again.")

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