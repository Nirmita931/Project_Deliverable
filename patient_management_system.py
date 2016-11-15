# Here system detects whether the user is old or new

print("Welcome to Prudent Healthcare Service!\n")
status = input("Are you a registered user?\n")
if status == "y":
        print("Old User\n")
elif status == "n":
        print("New User\n")
create_Login = input("Create login name\n")
if create_Login == "Old User":
    print("Login name already exists!\n")
elif create_Login == "New User":
    print("User created!")

# Login process.

login = input ("Enter your login name:\n")
print(login)
password = input("Enter your 8-digit password:\n")
print(password)
print("You can take your appointment now.\n")

# This is the process of taking appointment.

disease = input("Please, specify the symptoms or disease:\n")
print(disease)

if disease == "xxx":
    print("Choose the specialist from the list for your checkup.\n")
    print("List of specialist available for the disease you specified.\n")
    print("1. Doctor A")
    print("2. Doctor B")
    print("3. Doctor C")
    print("4. Doctor D")

    choose_doctor = input("Choose one of the specialist\n")
    if choose_doctor == "1":
        print ("Doctor A \n The scheduled time for Doctor A is from 10AM to 11AM\n")

        appointment = input("Confirm the appointment\n")
        if appointment == "fix":
            print("Confirmed\n")
            notify_doctor = input("Notify the doctor about the time of the appointment for checkup\n")
            if notify_doctor == "y":
                print("extract the information of the patient\n")
            else:
                print("Send the information to the doctor\n")
    elif choose_doctor == "2":
        print("Doctor B \n The scheduled time for Doctor B is from 11AM to 12PM\n")

        appointment = input("Confirm the appointment\n")
        if appointment == "fix":
            print("Confirmed\n")
            notify_doctor = input("Notify the doctor about the time of the appointment for checkup\n")
            if notify_doctor == "y":
                print("extract the information of the patient\n")
            else:
                print("Send the information to the doctor\n")
    elif choose_doctor == "3":
        print("Doctor C \n The scheduled time for Doctor C is from 12PM to 01PM\n")

        appointment = input("Confirm the appointment\n")
        if appointment == "fix":
            print("Confirmed\n")
            notify_doctor = input("Notify the doctor about the time of the appointment for checkup\n")
            if notify_doctor == "y":
                print("extract the information of the patient\n")
            else:
                print("Send the information to the doctor\n")

                appointment = input("Confirm the appointment\n")
                if appointment == "fix":
                    print("Confirmed\n")
                    notify_doctor = input("Notify the doctor about the time of the appointment for checkup\n")
                    if notify_doctor == "y":
                        print("extract the information of the patient\n")
                    else:
                        print("Send the information to the doctor\n")
    elif choose_doctor == "4":
        print("Doctor D \n The scheduled time for Doctor D is from 02PM to 03PM\n")

        appointment = input("Confirm the appointment\n")
        if appointment == "fix":
            print("Confirmed\n")
            notify_doctor = input("Notify the doctor about the time of the appointment for checkup\n")
            if notify_doctor == "y":
                print("extract the information of the patient\n")
            else:
                print("Send the information to the doctor\n")

    else:
        print("The doctor is not available\n")

else:
    print("Sorry the doctor is not available.\n")

# This is the billing process after checkup is done.

data_collection = input("Collect the information about the patient by filling up a form.\n")
print(data_collection)

Name = input("Full name of the patient:\n ")
print(Name)
Gender = input("Specify your gender:\n")
print(Gender)
Age = input("Specify your age:\n")
print(Age)
Blood_group = input("Specify your blood group:\n")
print(Blood_group)
Disease = input("Specify your disease:\n")
print(Disease)
Contact = input("Specify your contact information:\n")
print(Contact)

collection_finish = input("Check whether the collection of patient information is finished or not\n")

if collection_finish == "y":
    print("Prepare for  payment\n")
    payment = input("Choose C1 for cash payment and choose C2 for credit payment\n")
    print(payment)
    if payment == "C1":
        print("Payment done by cash\n")
    elif payment == "C2":
        print("Payment done by credit\n")
    else:
        print("Payment not done\n")

else:
    print("error")
logout = input("CLick on logout to shut down")
print(logout)

print("Thank you!!!")














