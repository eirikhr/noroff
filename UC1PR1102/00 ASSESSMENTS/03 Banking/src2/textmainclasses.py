from datetime import datetime


def rot_encrypt(raw_string="Hello, World", n=1):
    enc_string = ""
    raw_string = str(raw_string)
    for letter in raw_string:
        enc_letter = chr(ord(letter) + n)
        enc_string = enc_string + enc_letter

    return enc_string


def rot_decrypt(enc_string, n=1):
    raw_string = ""
    for letter in enc_string:
        raw_letter = chr(ord(letter) - n)
        raw_string = raw_string + raw_letter

    return raw_string


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
                       "\n\nFIRST PERSON: "
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


    def __init__(self):
        self.section_one = {}
        self.section_two = {}


    def get_input(self, printstring, required=False):
        """Outputs the argument to screen, and returns the user input.

        Args
            printstring (str): Outputs printstring to screen before returning input from user

        Returns:
            The user input.
        """
        valid = False
        if required:
            while not valid:
                value = input(printstring + " ->  ")
                if value:
                    if value.lower() == "quit":
                        print("Goodbye.")
                        quit()
                    return value
        else:
            value = input("-> " + printstring)
            if value:
                if value.lower() == "quit":
                    print("Goodbye.")
                    quit()
                return value

    def is_working(self):
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
                value = int(self.get_input("\nPlease enter your selection by entering 1-9 and pressing enter."))
                if value == 9:
                    value = self.get_input("Please explain:")
                    return value
                elif value == 4:
                    while True:
                        try:
                            entry = int(self.get_input("How many months in total have you been unemployed?"))
                            return "Unemployed: {} months".format(entry)
                        except Exception:
                            print("Please enter amount of months in numbers.")
                elif value < 8:
                    return value
                else:
                    print("Invalid choice. Try again.")
            except Exception:
                print("Invalid choice. Try again.")

    def get_information(self):
        print("Section 1, Personal Detail")
        self.section_one["title"] = self.get_input("What is your title? (E.g: Mr, Mrs, Miss, Ms", True)
        self.section_one["last"] = self.get_input("What is your LAST name. (E.g: Doe, Johnson, Hanson")
        self.section_one["first"] = self.get_input("What is all of your FIRST name(s). (E.g: John, Patrick, Eric Roger")
        self.section_one["dob"] = self.get_input("What is your date of birth? (E.g: YYYY-MM-DD / 2019-01-01")
        self.section_one["gender"] = self.get_input("What gender do you identify as? (E.g: Male/Female/None")
        self.section_one["working"] = self.is_working()
        self.section_one["cob"] = self.get_input("Country of Birth:")
        self.section_one["tob"] = self.get_input("Your Town/City of Birth:")
        self.section_one["nat"] = self.get_input("Nationality:")
        self.section_one["nat_ext"] = self.get_input("If applicable, enter all additional nationalities seperated by commas:")
        self.section_one["cor"] = self.get_input("Country of residence:")
        self.section_one["residency"]  = self.get_input("----\n"
                                                        + "Please note: *This is the country where an individual is "
                                                        + "resident under the tax laws of such jurisdiction.\n"
                                                        + "----\n"
                                                        + "If applicable, which countries are you tax resident* in?")
        self.section_one["tin"] = self.get_input("----\n"
                                                 + "Guidance: By TIN we mean, Taxpayer Identification number, "
                                                 + "or similar Tax Payer reference number you hold for your contry(ies)"
                                                 + " you are tax resident in.\n"
                                                 + "----\n"
                                                 + "If you have a Taxpayer Identification (TIN) for other countries, "
                                                 + "please provide details below")
        self.section_one["tel_mob"] = self.get_input("Your mobile phone number, including area dialing codes")
        self.section_one["tel_home"] = self.get_input("If applicable, your home phone number, including area dialing codes")
        self.section_one["tel_work"] = self.get_input("If applicable, your work phone number, including area dialing codes")
        self.section_one["addr"] = self.get_input("Home address (where you live)")
        self.section_one["postal"] = self.get_input("Post code")
        self.section_one["country"] = self.get_input("Country")
        self.section_one["living"] = self.get_input("When did you start living at this address?")
        self.section_one["prev_addr"] = self.get_input("IMPORTANT: If less than three years at current address\n"
                                                       + "Your previous address:")
        self.section_one["prev_postal"] = self.get_input("If applicable, previous post code:")
        self.section_one["prev_country"] = self.get_input("If applicable, previous country:")
        self.section_one["cor_addr"] = self.get_input("IMPORTANT: Only applicable if different from your home address\n"
                                                      + "Enter your correspondence address:")
        self.section_one["cor_postal"] = self.get_input("If applicable, enter correspondence post code")
        self.section_one["cor_country"] = self.get_input("If applicable, enter correspondence country")


customers = []
number_of_customers = int(input("How many customers will be on this account? (1 or 2)"))

for i in range(number_of_customers):
    user = User()
    user.get_information()
    customers.append(user)

filename =str(datetime.now().timestamp()) + customers[0].section_one["first"]

file = open(filename, 'w')

for key in customers[0].section_one.keys():
    for j in range(len(customers)):
        file.write("***"+key+"***")
        file.write("\n")
        file.write(rot_encrypt(customers[j].section_one[key]) if customers[j].section_one[key] else "")
        file.write("\n")











