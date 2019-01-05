import os
import datetime



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


def clear_screen():
    """Clears screen for readability."""
    # If client runs Windows (NT), uses "cls", else uses "clear".
    os.system("cls" if os.name == "nt" else "clear")


def new_account_record():

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
                        print("TEST: PRINTING RETURN ON UNEMPLOYED")
                        print(output)
                        return output
                    except ValueError:
                        print("Please enter amount of months in numbers.")
                elif value < 8:
                    return str(value)
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid choice. Try again.")

    def write_record():
        """
        The function that is responsible for the write-to-file
        functionality.
        """
        try:
            now = datetime.datetime.now()
            file_name = now.strftime("%Y-%m-%d %H.%M.%S - ") + text_box1.get() + ".txt"
            file_intro = "\n\n______________________________________________\n" \
                         "               Bank Account Record" \
                         "\n______________________________________________\n\n"
            with open(file_name, "w") as file:  # The text formatting and writing to file implementation.
                file.write(file_intro +
                           "\n\nSECTION 1: "
                           "\n\tCase Reference Number: " + text_box2.get() +
                           "\n\tItem Reference Number: " + text_box3.get() +
                           "\n\nINVESTIGATION: "
                           "\n\tStart Date: " + text_box4.get() +
                           "\n\tStart Time: " + text_box5.get() + "\n"
                                                                  "\nCOMMENTS: " + "\n\t" + usage_entry.get("1.0",
                                                                                                            tk.END) +
                           "_________________________________________"
                           "\nFinish Date: " + text_box6.get() +
                           "\nFinish Time: " + text_box7.get() +
                           "\nInvestigator Name: " + text_box8.get() + "\n"
                                                                       "\nSignature: "
                                                                       "\n\n_________________________________________\n\n")
        finally:
            box.showinfo("Report Created", "Your Forensics Report Has Been Made")  # Informing users of file created

    def want_debit():
        print("Do you want to apply for a debit card?:\n")
        print("1: Yes")
        print("2: No")
        while True:
            try:
                value = int(get_input("\nPlease enter your selection by entering 1-2 and pressing enter."))
                if value == 2:
                    return ["User does not want to apply."]
                else:
                    out = []
                    out.append(get_input("Customer name to appear on card"))
                    out.append(get_input("Mother's previous name (new debit card customers only"))
                    return out
            except ValueError:
                print("Please enter a valid option in numbers.")


    first_title = get_input("What is your title? (E.g: Mr, Mrs, Miss, Ms")
    first_last_name = get_input("What is your LAST name. (E.g: Doe, Johnson, Hanson")
    first_first_name = get_input("What is all of your FIRST name(s). (E.g: John, Patrick, Eric Roger")
    first_dob = get_input("What is your date of birth? (E.g: YYYY-MM-DD / 2019-01-01")
    first_gender = get_input("What gender do you identify as? (E.g: Male/Female/None")
    first_working = is_working()
    first_cob = get_input("Country of Birth:")
    first_tob = get_input("Your Town/City of Birth:")
    first_nationality = get_input("Nationality:")
    first_nationality_extra = get_input("If applicable, enter all additional nationalities seperated by commas:")
    first_cor = get_input("Country of residence:")
    first_tax_resident = get_input("----\n"
                                   "Please note: *This is the country where an individual is "
                                   "resident under the tax laws of such jurisdiction.\n"
                                   "----\n"
                                   "If applicable, which countries are you tax resident* in?")
    first_foreing_tin = get_input("----\n"
                                  "Guidance: By TIN we mean, Taxpayer Identification number, "
                                  "or similar Tax Payer reference number you hold for your contry(ies)"
                                  " you are tax resident in.\n"
                                  "----\n"
                                  "If you have a Taxpayer Identification (TIN) for other countries, "
                                  "please provide details below")
    first_phone_mobile = get_input("Your mobile phone number, including area dialing codes")
    first_phone_home = get_input("If applicable, your home phone number, including area dialing codes")
    first_phone_work = get_input("If applicable, your work phone number, including area dialing codes")
    first_address = get_input("Home address (where you live)")
    first_postcode = get_input("Post code")
    first_country = get_input("Country")
    first_movedin = get_input("When did you start living at this address?")
    first_previous_address = get_input("IMPORTANT: If less than three years at current address\n"
                              "Your previous address:")
    first_previous_postcode = get_input("If applicable, previous post code:")
    first_previous_country = get_input("If applicable, previous country:")
    first_corr_address = get_input("IMPORTANT: Only applicable if different from your home address\n"
                                   "Enter your correspondence address:")
    first_corr_postcode = get_input("If applicable, enter correspondence post code")
    first_corr_country = get_input("If applicable, enter correspondence country")
    first_apply_debit = want_debit()
    first_debit_name = first_apply_debit[0]
    first_debit_mpn = first_apply_debit[1]










    # SECTION TWO










def menu():
    """Main loop of this program.
    Asks user for the input, and calls the appropriate function.
    """
    while True:

        # Printing Main Menu
        print("------ MAIN MENU ------\n")
        print("1: New Bank Account Record")
        print("2: Exit the program.\n")


        # Gets user input.
        main_input = get_input("Please enter your selection.")

        # Decide where to send user.
        if main_input == "1":
            new_account_record()
            continue
        elif main_input == "2":
            quit()
        else:
            clear_screen()
            continue


if __name__ == "__main__":
    menu()