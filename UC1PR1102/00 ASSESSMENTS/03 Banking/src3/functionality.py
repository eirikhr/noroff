from datetime import datetime
import os
import re


class User:
    def __init__(self):
        """Creates an instance of a new bank User."""
        # Defining dictionaries to store information.
        self.section_one = {}
        self.section_two = {}
        self.section_three = {}
        self.section_four = {}
        self.section_five = {}
        self.section_six = {}
        self.section_seven = {}
        self.section_eight = {}
        # Defining variables.
        self.check_joint = None
        self.ever_worked = None
        self.any_savings = None

    def get_input(self, printstring, required=False):
        """Outputs the argument to screen, and returns the user input.
        If required argument is passed as True, the method will force an input from user.

        Args
            printstring (str): Outputs argument to screen before returning input from user
            required (bool): If True, forces user to provide an input.

        Returns:
            value (str): The user input.
        """
        valid = False
        if required:
            while not valid:
                value = input(printstring + "\n ->  ")
                if value:
                    if value.lower() == "quit":
                        print("Goodbye.")
                        quit()
                    return numbersaway(value)
        else:
            value = input(printstring + "\n ->  ")
            if value:
                if value.lower() == "quit":
                    print("Goodbye.")
                    quit()
                return numbersaway(value)

    def is_working(self):
        """Asks for the users work status.

            Returns:
                value (str): The user input. If the user is Unemployed, it formats
                             the input including how many months the user has been
                             unemployed for.
        """
        print("\nAre you:\n")
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
                value = int(input("\nPlease enter your selection by entering 1-9 and pressing enter.\n"
                                  " ->  "))
                if value == 9:
                    value = numbersaway(input("Please explain:\n"
                                              " ->  "))
                    return "9 - " + value
                elif value == 4:
                    while True:
                        try:
                            entry = numbersaway(input("How many months in total have you been unemployed?\n"
                                                      " ->  "))
                            return "Unemployed: {} months".format(entry)
                        # Catches if user doesnt
                        except TypeError:
                            print("Invalid choice. Try again.")
                elif value < 10:
                    value = value
                    return str(value)
                else:
                    print("Invalid choice. Try again.")
            finally:
            #except (ValueError, NameError, TypeError) as e:
                print("Finally Invalid choice. Try again.")

    def yes_no(self, printstring=None):
        """Gets yes or no choice from user.

            Args
                printstring (str): Outputs argument to screen before asking for input from user

            Returns:
                value (str): "Yes" or "No" only.
        """
        print(printstring)
        print("1: Yes")
        print("2: No")
        while True:
            try:
                value = int(input("Please enter your selection by entering 1 or 2 and then pressing enter.\n"
                                  " ->  "))
                if value == 1:
                    return "Yes"
                elif value == 2:
                    return "No"

                # Make sure only 1 or 2 can be selected.
                else:
                    print("That number is not 1 or 2.")
                    continue
            # Catch empty string or string containing non-integrers.
            except (ValueError, TypeError) as e:
                print("I could not register a valid option.")

    def want_debit(self):
        """Gets yes or no choice from user. Returns required information if answer is yes.

            Returns:
                out (str): Shown name for debitcard and Mothers Previous Name.
                           Can also return that user doesnt want to apply.
        """
        while True:
            try:
                value = self.yes_no("Do you want to apply for a debit card?")
                if value == "No":
                    return ["User does not want to apply."]
                elif value == "Yes":
                    in1 = self.get_input("What customer name do you want to appear on the debit card?", True)
                    in2 = self.get_input("Mother's previous name (new debit card customers only)")
                    out = "Yes Customer Name: {} ----- Mothers Previous Name: {}".format(in1, in2)
                    return numbersaway(out)
            finally:
                # Any exceptions are handled by self.yes_no() and self.get_input().
                pass

    def personal_business(self, printstring=None):
        """Gets choice from user.

            Args
                printstring (str): Outputs argument to screen before asking for input from user

            Returns:
                value (str): "Personal." or "Business." only.
        """
        print(printstring)
        print("1: Personal")
        print("2: Business")
        while True:
            try:
                value = int(input("Please enter your selection by entering 1 or 2 and then pressing enter.\n"
                                  " ->  "))
                if value == 1:
                    return "Personal"
                elif value == 2:
                    return "Business"
                # Make sure only 1 or 2 can be selected.
                else:
                    print("That number is not 1 or 2.")
                    continue
            # Catch empty string or string containing non-integrers.
            except (ValueError, TypeError) as e:
                print("I could not register a valid option.")

    def get_information(self):
        """Method that gathers required information from user and stores it onto
        its dictionaries."""

        # Section 1 - Personal Detail
        clear_screen()
        print("Section 1 - Personal Detail")

        self.section_one["Title"] = self.get_input("What is your title? (E.g: Mr, Mrs, Miss, Ms", True)
        self.section_one["Last Name"] = self.get_input("What is your LAST name. (E.g: Doe, Johnson, Hanson", True)
        self.section_one["First Name"] = self.get_input("What is all of your FIRST name(s). "
                                                        + "(E.g: John, Patrick, Eric Roger", True)
        self.section_one["Full Name"] = self.section_one["Title"] + " " + self.section_one["First Name"] + " " + \
                                        self.section_one["Last Name"]
        self.section_one["Date of Birth"] = self.get_input("What is your date of birth? "
                                                           "(E.g: YYYYMMDD / 19901127", True)
        self.section_one["Gender"] = self.get_input("What gender do you identify as? (E.g: Male/Female/Other", True)
        self.section_one["Is Working Code"] = str(numbersaway(self.is_working()))
        self.section_one["Country of Birth"] = self.get_input("Country of Birth:", True)
        self.section_one["Town of Birth"] = self.get_input("Your Town/City of Birth:", True)
        self.section_one["Nationality"] = self.get_input("Nationality:", True)
        self.section_one["Additional Nationalities"] = self.get_input("If applicable, enter all additional nationalit"
                                                                      "ies separated by commas:")
        self.section_one["Country of Residence"] = self.get_input("Country of residence:", True)
        self.section_one["Tax Resident in Country"] = self.get_input("----\n"
                                                                     "If applicable, which countries are you tax "
                                                                     "resident* in? \n*: This is the country where an"
                                                                     " individual is resident under the tax laws of "
                                                                     "such jurisdiction.\n----\n")
        self.section_one["Taxpayer ID Numbers"] = self.get_input("If you have a Taxpayer Identification (TIN) for other"
                                                                 " countries, please provide details below"
                                                                 "----\n"
                                                                 "Guidance: By TIN we mean, Taxpayer Identification "
                                                                 "number, or similar Tax Payer reference \n"
                                                                 "number you hol"
                                                                 "d for your country(ies) you are tax resident in."
                                                                 "\n----\n")
        self.section_one["Mobile Number"] = self.get_input("Your mobile phone number, including area dialing codes")
        self.section_one["Home Number"] = self.get_input("If applicable, your home phone number, "
                                                         "including area dialing codes")
        self.section_one["Work Number"] = self.get_input("If applicable, your work phone number, "
                                                         "including area dialing codes")
        self.section_one["Address"] = self.get_input("Home address (where you live)", True)
        self.section_one["Postal Code"] = self.get_input("Postal code", True)
        self.section_one["Country"] = self.get_input("Country", True)
        self.section_one["Moved in"] = self.get_input("When did you start living at this address?", True)
        self.section_one["Less than three"] = self.yes_no("Did you live elsewhere less than three years ago?")
        if self.section_one["Less than three"] == "Yes":
            self.section_one["Previous Address"] = self.get_input("IMPORTANT: If less than three years at current "
                                                                  "address\n"
                                                                  + "Your previous address:")
            self.section_one["Previous Postal Code"] = self.get_input("Your previous post code:")
            self.section_one["Previous Country"] = self.get_input("Your previous country:")
        self.section_one["Has correspondence address"] = self.yes_no("Is your correspondence address different from "
                                                                     "your home address?")
        if self.section_one["Has correspondence address"] == "Yes":
            self.section_one["Correspondence Address"] = self.get_input("Enter your correspondence address:")
            self.section_one["Correspondence Postal"] = self.get_input("If applicable, enter correspondence post code")
            self.section_one["Correspondence Country"] = self.get_input("If applicable, enter correspondence country")

        # Section 2 - Debit Card Details
        clear_screen()
        print("----- SECTION 2 - DEBIT CARD DETAILS -----")

        self.section_two["Debit Card Information"] = str(self.want_debit())
        self.section_two["Date of Birth"] = self.section_one["Date of Birth"]

        # Section 3 - Marketing Choices
        clear_screen()
        print("----- SECTION 3 - MARKETING CHOICES -----\n\n\n")
        self.section_three["Internet"] = self.yes_no(("We would like to keep you up to date on products and offers that"
                                                      " may be of interest to you. \n"
                                                      "Please select how you would like to hear from us below. \n"
                                                      "\n"
                                                      "These choices won’t affect any necessary information "
                                                      "we need to send you such as statements and, \n"
                                                      "don’t worry, you can change your mind and update "
                                                      "your preferences at any time.\n\n"
                                                      "Internet banking: You’ll see relevant messages when you log on "
                                                      "to Internet Banking and our apps.\n"
                                                      "If you choose 'no', you may still see messages, but they won’t "
                                                      "be tailored to you.\n"))
        self.section_three["Email"] = self.yes_no("May we send you messages through e-mail?")
        self.section_three["Post"] = self.yes_no("May we send you messages through post?")
        self.section_three["Device"] = self.yes_no("May we send you messages as notifications to your mobile device?")
        self.section_three["SMS"] = self.yes_no("May we send you messages through SMS?")
        self.section_three["Phone"] = self.yes_no("May we send you messages through calls?")

        clear_screen()
        print("----- SECTION 4 -  YOUR AGREEMENT-----\n\n\n")

        self.check_joint = self.yes_no("Is your account going to be accessible by any other part?\n"
                                       "In other words: Is this going to be a joint account?\n")
        if self.check_joint == "Yes":
            # The following is only applicable if it is a joint account
            self.section_four["Joint Consent Given"] = self.yes_no("Do you consent to share, with any other party "
                                                                   "to the account, details of any sole partyholdings"
                                                                   " and any holdings\nyou may have in joint name with"
                                                                   " any other party in order that we can determine "
                                                                   "the best rate you are eligible for:")
            self.section_four["Joint Bank Statement"] = self.yes_no("We will send joint account statements to both of "
                                                                    "you unless one of you signs here to say\n"
                                                                    "that you do not want us to send statements to you."
                                                                    "You can cancel this arrangement at any time by\n"
                                                                    "writing to us and we will then send seperate bank"
                                                                    "statements to both of you.\n\n"
                                                                    "Would you like to receive joint bank statements?")
            self.section_four["Joint Consent Initials"] = self.get_input("Please enter your INITIALS "
                                                                         "as a signature to give consent to the joint "
                                                                         "account and bank statement.", True)
        clear_screen()
        print("----")
        print("\nI HEREBY CONFIRM THAT I HAVE RECEIVED THE FOLLOWING DOCUMENTATION:\n")
        print("----")
        self.section_four["Received Terms Cond"] = self.yes_no("Your banking relationship with us (the Personal Banking"
                                                               " terms and conditions)")
        self.section_four["Received Welcome Pack"] = self.yes_no("Welcome Pack")
        self.section_four["Received Rates Advice"] = self.yes_no("Advised and provided with Interest Rates Applicable "
                                                                 "to this account)")
        self.section_four["Received Charges Brochure"] = self.yes_no("Banking Charges Brochure)")
        self.section_four["Received Compensation Info Sheet"] = self.yes_no("Financial Services Compensation Scheme "
                                                                            "Information Sheet)")

        self.section_four["Signature"] = self.get_input("Please provide your INITIALS as a"
                                                        " signature for the information"
                                                        " you have provided in section 4.", True)

        # SECTION FIVE
        clear_screen()
        print("----- SECTION 5 -  EMPLOYMENT DETAILS-----\n\n\n")

        self.section_five["Working"] = self.yes_no("Are you currently working?")

        if self.section_five["Working"] == "Yes":
            self.section_five["Occupation"] = self.get_input("What is your occupation?", True)
            self.section_five["Employer Name"] = self.get_input("What is your employers name?", True)
            self.section_five["Employer Address"] = self.get_input("What is your employer's full address, including "
                                                                   "post code (if known).")
            self.section_five["Employed Current Employed Time"] = self.get_input("How long have you worked "
                                                                                 "for your current employer?")
            self.section_five["Employed Previous Employed Time"] = self.get_input("How long did you work "
                                                                                  "for your previous employer?")
            self.section_five["Employment Pensionable"] = self.yes_no("Is your employment pensionable?")

        if self.section_five["Working"] == "No":
            self.ever_worked = self.yes_no("Have you ever worked?")
            if self.ever_worked == "Yes":
                self.section_five["Previous Employer Employment Time"] = self.get_input("How long did you work "
                                                                                        "for your previous employer?")
        # SECTION SIX
        clear_screen()
        print("----- SECTION 6 - HOUSEHOLD INCOME AND EXPENDITURE DETAILS-----\n\n")
        print("INCOME:\n\n")
        self.section_six["Receives Salary/Wages"] = self.yes_no("Do you receive a Salary/Wages?")

        if self.section_six["Receives Salary/Wages"] == "Yes":
            self.section_six["Salary Frequency"] = self.get_input("At what frequency do you receive this amount? "
                                                                  "E.g: Weekly")
            self.section_six["Salary Into This Account"] = self.yes_no("Will the amount be transferred "
                                                                       "directly into this account?")
            self.section_six["Salary Into Other Account"] = self.yes_no("Are the amount being transferred directly "
                                                                        "to another bank?")
            self.section_six["Salary Received in Cash"] = self.yes_no("Do you receive the amount in Cash?")
            self.section_six["Salary Received by Cheque"] = self.yes_no("Do you receive the amount in Cheque?")

        self.section_six["Receives Benefits"] = self.yes_no("Do you receive any Benefits?")
        if self.section_six["Receives Benefits"] == "Yes":
            self.section_six["Benefit Frequency"] = self.get_input(
                "At what frequency do you receive this amount? E.g: Weekly")
            self.section_six["Benefit Into This Account"] = self.yes_no("Will the amount be transferred "
                                                                        "directly into this account?")
            self.section_six["Benefit Into Other Account"] = self.yes_no("Are the amount being transferred directly "
                                                                         "to another bank?")
            self.section_six["Benefit Received in Cash"] = self.yes_no("Do you receive the amount in Cash?")
            self.section_six["Benefit Received by Cheque"] = self.yes_no("Do you receive the amount in Cheque?")

        self.section_six["Receives Pension"] = self.yes_no("Do you receive any Pension?")
        if self.section_six["Receives Pension"] == "Yes":
            self.section_six["Pension Frequency"] = self.get_input("At what frequency do you receive this amount? "
                                                                   "E.g: Weekly")
            self.section_six["Pension Into This Account"] = self.yes_no("Will the amount be transferred "
                                                                        "directly into this account?")
            self.section_six["Pension Into Other Account"] = self.yes_no("Are the amount being transferred directly "
                                                                         "to another bank?")
            self.section_six["Pension Received in Cash"] = self.yes_no("Do you receive the amount in Cash?")
            self.section_six["Pension Received by Cheque"] = self.yes_no("Do you receive the amount in Cheque?")

        self.section_six["Receives Investment"] = self.yes_no("Do you receive an income from investments?")
        if self.section_six["Receives Investment"] == "Yes":
            self.section_six["Investment Frequency"] = self.get_input("At what frequency do you receive this amount? "
                                                                      "E.g: Weekly")
            self.section_six["Investment Into This Account"] = self.yes_no("Will the amount be transferred "
                                                                           "directly into this account?")
            self.section_six["Investment Into Other Account"] = self.yes_no("Are the amount being transferred directly "
                                                                            "to another bank?")
            self.section_six["Investment Received in Cash"] = self.yes_no("Do you receive the amount in Cash?")
            self.section_six["Investment Received by Cheque"] = self.yes_no("Do you receive the amount in Cheque?")

        self.section_six["Receives Other"] = self.yes_no("Do you receive any other types of income?")
        if self.section_six["Receives Other"] == "Yes":
            self.section_six["Other Frequency"] = self.get_input("At what frequency do you receive this amount? "
                                                                 "E.g: Weekly")
            self.section_six["Other Into This Account"] = self.yes_no("Will the amount be transferred "
                                                                      "directly into this account?")
            self.section_six["Other Into Other Account"] = self.yes_no("Are the amount being transferred directly "
                                                                       "to another bank?")
            self.section_six["Other Received in Cash"] = self.yes_no("Do you receive the amount in Cash?")
            self.section_six["Other Received by Cheque"] = self.yes_no("Do you receive the amount in Cheque?")

        self.section_six["Total Net Monthly Income"] = self.get_input("What is your estimated Total Net Monthly Income"
                                                                      , True)

        clear_screen()
        print("EXPENDITURE:\n\n")
        print("NOTE: Please specify all amounts in British Pounds.\n\n")

        self.section_six["Mortgage or Rent Expenditure"] = self.get_input("Total amount of mortgage/rent expenditure "
                                                                          "on a monthly basis.", True)
        self.section_six["Amount of Lloyd Loans"] = self.get_input("Total amount of loans from Lloyds Bank on "
                                                                   "a monthly basis.", True)
        self.section_six["HP / Other Loans"] = self.get_input("Total amount of HP/Other loans on a monthly basis."
                                                              , True)

        # SECTION SEVEN
        clear_screen()
        print("----- SECTION 7 - SAVINGS-----\n\n")

        self.any_savings = self.yes_no("Do you own any type of savings.")
        if self.any_savings == "No":
            self.section_seven["Owns Savings"] = "Applier does not own savings."
        if self.any_savings == "Yes":
            self.section_seven["Only Lloyds Savings"] = self.yes_no("Do you have Lloyd Bank Savings only?")
            self.section_seven["Non Lloyd Savings"] = self.yes_no("Do you have Non-Lloyd bank savings only?")
            self.section_seven["Lloyd And Other Savings"] = self.yes_no("Do you have Lloyds Bank "
                                                                        "and non-Lloyds Bank Savings?")
            self.section_seven["Total Amount Savings"] = self.get_input("What is the total amount of savings you own?")

        # SECTION EIGHT
        clear_screen()
        print("----- SECTION 8 - BANKING DETAILS-----\n\n")

        self.section_eight["Banking Type"] = self.personal_business("Is your account for Personal use or Business use?")
        self.section_eight["Other Cheque Or DebitCard"] = self.yes_no("Do you hold a cheque or debit "
                                                                      "card at a different bank")
        self.section_eight["Has External Account"] = self.yes_no("Do you own an account at a different bank?")
        if self.section_eight["Has External Account"] == "Yes":
            self.section_eight["External Account Length"] = self.get_input("How long have you banked there?")
            self.section_eight["External Account To Be Closed"] = self.yes_no("Is the account to be closed?")
            if self.section_eight["External Account To Be Closed"] == "No":
                self.section_eight["External Account Not Closing Reason"] = self.get_input("If yes, please explain why")
            else:
                self.section_eight["External Transfer Requested"] = self.yes_no("Would you like us to transfer your "
                                                                                "account?")
        clear_screen()
        print("CREDIT CARD DETAILS")
        self.section_eight["Holds Credit Card"] = self.yes_no("Do you hold any credit card(s)?")
        if self.section_eight["Holds Credit Card"] == "Yes":
            self.section_eight["Amount Credit Card"] = self.get_input("How many Credit Cards do you hold?")
            self.section_eight["Owns Lloyd Credit Card"] = self.yes_no("Are any of them from Lloyds Bank?")
            if self.section_eight["Owns Lloyd Credit Card"] == "Yes":
                self.section_eight["Credit Amount Lloyds"] = self.get_input("What is your credit limit?")
            self.section_eight["Owns Other Credit Card"] = self.yes_no("Do you own credit cards that are not from"
                                                                       "Lloyds Bank?")
            if self.section_eight["Owns Other Credit Card"] == "Yes":
                self.section_eight["Other Credit Card Type"] = self.get_input("What other card type(s) do you "
                                                                              "hold (Please Specify)")
                self.section_eight["Credit Amount Other"] = self.get_input("What is your total credit limit on your "
                                                                           "other credit cards?")

        self.section_eight["Has Mortage"] = self.yes_no("Do you have a mortgage?")
        if self.section_eight["Has Mortage"] == "Yes":
            self.section_eight["Mortgage With Lloyds"] = self.yes_no("Is the mortgage with Lloyds Bank?")
            self.section_eight["Mortgage Outstanding Balance"] = self.get_input(
                "What is the outstanding balance on your mortgage")
            self.section_eight["Estimated House Value"] = self.get_input("What is the estimated value of your house?")


def rot_encrypt(inputstring, shift=8):
    """Main function for encrypting data."""

    cipher = ""
    for char in inputstring:
        if char == " ":
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher


def numbersaway(text):
    """Replaces numbers in a string with text in dictionary.

    Args
        text (str): Input string to strip and replace numbers from

    Returns
        text (str): The input string, but with numbers replaced by text."""
    l = {
        "1": "ONE",
        "2": "TWO",
        "3": "THREE",
        "4": "FOUR",
        "5": "FIVE",
        "6": "SIX",
        "7": "SEVEN",
        "8": "EIGHT",
        "9": "NINE",
        "0": "ZERO"
    }
    for k, v in l.items():
        t = re.compile(re.escape(k), re.IGNORECASE)
        text = t.sub(v, text)
    return text


def clear_screen():
    """Clears screen for readability."""
    # If client runs Windows (NT), uses "cls", else uses "clear".
    os.system("cls" if os.name == "nt" else "clear")


def write_record():
    """Function that creates an instance of the class User().
    From there it calles the User().get_information() method, and stores the instances variables into
    a list.

    After that, the function writes an encrypted version of the information to a .txt file.
    """
    clear_screen()
    print("---- SINGLE/JOINT ACCOUNT ----")
    print("1 - Create an account for a single customer\n"
          "2 - Create a joint account for two customers\n"
          "      - If two customers are selected, information about the second user of the account\n"
          "      - will be entered sequentially after the First Customer has entered his/hers information.\n\n")

    try:
        customers = []
        number_of_customers = int(input("Please enter your selection by entering 1 or 2 and then pressing enter.\n"
                                        " ->  "))
        if number_of_customers == 1 or number_of_customers == 2:    # Can only be 1 or 2.

            # Run one time per customer in joint account.
            # Creates an instance of User()
            # Gets information to add to the instance.
            # Adds the information to the list.
            for i in range(number_of_customers):
                user = User()
                user.get_information()
                customers.append(user)

            # Sets up filename and opens a new file with timestamp as identifyer.
            filename = str(datetime.now().timestamp()) + ".txt"
            file = open(filename, 'w')

            file.write("------------ SECTION 1 DATA -----------\n\n")
            for key in customers[0].section_one.keys():
                for j in range(len(customers)):
                    file.write("[" + key + "]:")
                    file.write("\n")
                    file.write(rot_encrypt(customers[j].section_one[key]) if customers[j].section_one[key] else "")
                    file.write("\n")

            file.write("\n------------ SECTION 2 DATA -----------\n\n")
            for key in customers[0].section_two.keys():
                for j in range(len(customers)):
                    file.write("[" + key + "]:")
                    file.write("\n")
                    file.write(rot_encrypt(customers[j].section_two[key]) if customers[j].section_two[key] else "")
                    file.write("\n")

            file.write("\n------------ SECTION 3 DATA -----------\n\n")
            for key in customers[0].section_three.keys():
                for j in range(len(customers)):
                    file.write("[" + key + "]:")
                    file.write("\n")
                    file.write(
                        rot_encrypt(customers[j].section_three[key]) if customers[j].section_three[key] else "")
                    file.write("\n")

            file.write("\n------------ SECTION 4 DATA -----------\n\n")
            for key in customers[0].section_four.keys():
                for j in range(len(customers)):
                    file.write("[" + key + "]:")
                    file.write("\n")
                    file.write(
                        rot_encrypt(customers[j].section_four[key]) if customers[j].section_four[key] else "")
                    file.write("\n")

            file.write("\n------------ SECTION 5 DATA -----------\n\n")
            for key in customers[0].section_five.keys():
                for j in range(len(customers)):
                    file.write("[" + key + "]:")
                    file.write("\n")
                    file.write(
                        rot_encrypt(customers[j].section_five[key]) if customers[j].section_five[key] else "")
                    file.write("\n")

            file.write("\n------------ SECTION 6 DATA -----------\n\n")
            for key in customers[0].section_six.keys():
                for j in range(len(customers)):
                    file.write("[" + key + "]:")
                    file.write("\n")
                    file.write(rot_encrypt(customers[j].section_six[key]) if customers[j].section_six[key] else "")
                    file.write("\n")

            file.write("\n------------ SECTION 7 DATA -----------\n\n")
            for key in customers[0].section_seven.keys():
                for j in range(len(customers)):
                    file.write("[" + key + "]:")
                    file.write("\n")
                    file.write(rot_encrypt(customers[j].section_seven[key]) if customers[j].section_seven[key] else "")
                    file.write("\n")

            file.write("\n------------ SECTION 8 DATA -----------\n\n")
            for key in customers[0].section_eight.keys():
                for j in range(len(customers)):
                    file.write("[" + key + "]:")
                    file.write("\n")
                    file.write(rot_encrypt(customers[j].section_eight[key]) if customers[j].section_eight[key] else "")
                    file.write("\n")

        # Make sure only 1 or 2 can be selected.
        else:
            print("That number is not 1 or 2.")
    except (ValueError, NameError, TypeError) as e:
        print("Thats not a valid option.")

user1 = User()
print(numbersaway(user1.is_working()))