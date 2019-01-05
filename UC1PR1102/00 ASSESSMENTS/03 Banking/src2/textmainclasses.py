from datetime import datetime


def get_input(printstring=""):
    """Outputs the argument to screen, and returns the user input.

    Args
        printstring (str): Outputs printstring to screen before returning input from user

    Returns:
        The user input.
    """
    printstring = str(printstring)
    if len(printstring) > 0:
        print(printstring)
    value = input("-> ")
    if value.lower() == "quit":
        print("Goodbye.")
        quit()
    return value


def is_working():
    print("Are you:\n")
    print("1: Employed")
    print("2: Self employed")
    print("3: Part time")
    print("4: Unemployed")
    print("5: Not working")
    print("6: Seeking work")
    print("7: Retired")
    print("8: Studying")
    print("9: Other")
    while True:
        try:
            value = int(get_input("\nPlease enter your selection by entering 1-9 and pressing enter."))
            if value == 9:
                value = get_input("Please explain:")
                return value
            elif value == 4:
                try:
                    entry = int(get_input("How many months in total have you been unemployed?"))
                    output = "Unemployed: {} months".format(entry)
                    return output
                except ValueError:
                    print("Please enter amount of months in numbers.")
            elif value < 8:
                return str(value)
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid choice. Try again.")


def want_debit():
    print("Do you want to apply for a debit card?:\n")
    print("1: Yes")
    print("2: No")
    while True:
        try:
            value = int(get_input("\nPlease enter your selection by entering 1-2 and pressing enter."))
            if value == 2:
                return ["User does not want to apply.", "User does not want to apply."]
            else:
                out = []
                out.append(get_input("Customer name to appear on card"))
                out.append(get_input("Mother's previous name (new debit card customers only"))
                return out
        except ValueError:
            print("Please enter a valid option in numbers.")


def write_record(file_name):
    """
    The function that is responsible for the write-to-file
    functionality.
    """
    try:
        file_intro = "\n\n______________________________________________\n" \
                     "               Bank Account Record" \
                     "\n______________________________________________\n\n"
        with open(file_name, "w") as file:  # The text formatting and writing to file implementation.
            file.write(file_intro +
                       "\n\nSECTION 1: "
                       "\n\tTitle: " + placeholder +
                       "\n\tLast Name: " + placeholder +
                       "\n\tSELECTME: " + placeholder +
                       "\n\tSELECTME: " + placeholder +
                       "\n\tSELECTME: " + placeholder +
                       "\n\tSELECTME: " + placeholder +
                       "\n\tSELECTME: " + placeholder +
                       "\n\tSELECTME: " + placeholder +
                       "\n\tSELECTME: " + placeholder +
                       "\n\tSELECTME: " + placeholder +
                       "_________________________________________"
                       "\n\tSELECTME: " + placeholder +
                       "\n\tSELECTME: " + placeholder)
    finally:
        print("Report Created", "Your Forensics Report Has Been Made")  # Informing users of file created


class User:
    num_of_entries = 0

    def __init__(self, title, last, first, dob, gender, working, cob, tob, nationality, add_nationality, cor
                 , tax_residency, foreing_tin, mobile, tel_home, tel_work, address, postcode, country, moved_in_date,
                 previous_addr, previous_postal, previous_country, corr_addr, corr_postal, corr_country,
                 debit_name, debit_mpn):

        self.title = title
        self.last = last
        self.first = first
        self.dob = dob
        self.gender = gender
        self.working = working
        self.cob = cob
        self.tob = tob
        self.nationality = nationality
        self.add_nationality = add_nationality
        self.cor = cor
        self.tax_residency = tax_residency
        self.foreing_tin = foreing_tin
        self.mobile = mobile
        self.tel_home = tel_home
        self.tel_work = tel_work
        self.address = address
        self.postcode = postcode
        self.country = country
        self.moved_in_date = moved_in_date
        self.previous_addr = previous_addr
        self.previous_postal = previous_postal
        self.previous_country = previous_country
        self.corr_addr = corr_addr
        self.corr_postal = corr_postal
        self.corr_country = corr_country
        self.debit_name = debit_name
        self.debit_mpn = debit_mpn


        self.filename =  datetime.now().strftime("%Y-%m-%d %H.%M.%S ") + self.last + ".txt"
        #num_of_entries += 1


def get_information():
    THE_LIST = []
    THE_LIST.append(get_input("What is your title? (E.g: Mr, Mrs, Miss, Ms"))
    THE_LIST.append(get_input("What is your LAST name. (E.g: Doe, Johnson, Hanson"))
    THE_LIST.append(get_input("What is all of your FIRST name(s). (E.g: John, Patrick, Eric Roger"))
    THE_LIST.append(get_input("What is your date of birth? (E.g: YYYY-MM-DD / 2019-01-01"))
    THE_LIST.append(get_input("What gender do you identify as? (E.g: Male/Female/None"))
    THE_LIST.append(get_input(is_working()))
    THE_LIST.append(get_input("Country of Birth:"))
    THE_LIST.append(get_input("Your Town/City of Birth:"))
    THE_LIST.append(get_input("Nationality:"))
    THE_LIST.append(get_input("If applicable, enter all additional nationalities seperated by commas:"))
    THE_LIST.append(get_input("Country of residence:"))
    THE_LIST.append(get_input("----\n"
                              "Please note: *This is the country where an individual is "
                              "resident under the tax laws of such jurisdiction.\n"
                              "----\n"
                              "If applicable, which countries are you tax resident* in?"))
    THE_LIST.append(get_input("----\n"
                              "Guidance: By TIN we mean, Taxpayer Identification number, "
                              "or similar Tax Payer reference number you hold for your contry(ies)"
                              " you are tax resident in.\n"
                              "----\n"
                              "If you have a Taxpayer Identification (TIN) for other countries, "
                              "please provide details below"))
    THE_LIST.append(get_input("Your mobile phone number, including area dialing codes"))
    THE_LIST.append(get_input("If applicable, your home phone number, including area dialing codes"))
    THE_LIST.append(get_input("If applicable, your work phone number, including area dialing codes"))
    THE_LIST.append(get_input("Home address (where you live)"))
    THE_LIST.append(get_input("Post code"))
    THE_LIST.append(get_input("Country"))
    THE_LIST.append(get_input("When did you start living at this address?"))
    THE_LIST.append(get_input("IMPORTANT: If less than three years at current address\n"
                              "Your previous address:"))
    THE_LIST.append(get_input("If applicable, previous post code:"))
    THE_LIST.append(get_input("If applicable, previous country:"))
    THE_LIST.append(get_input("IMPORTANT: Only applicable if different from your home address\n"
                              "Enter your correspondence address:"))
    THE_LIST.append(get_input("If applicable, enter correspondence post code"))
    THE_LIST.append(get_input("If applicable, enter correspondence country"))
    apply_debit = want_debit()

    THE_LIST.append(apply_debit[0])
    THE_LIST.append(apply_debit[1])

    return THE_LIST



def add_record():
    User(*add_record())


#print(THE_LIST)
"""
THE_LIST = ['Mr', 'Rynning', 'Eirik Hansen', '1989-03-06', 'Male', '', 'Norge', '', '', '', '', '', '', '+4790050985',
            '', '', '', '', '', '', '', '', '', '', '', '', 'Eirik Rynning', 'Bjørg Hansen']
"""

test = User(*add_record())
print(test.debit_mpn)
print(test.debit_name)
print(test.filename)
#file = User(test[2] + test[1])

#print(file.filename)

#print(test.first)
#print(test.last)
#print(test.filename)












