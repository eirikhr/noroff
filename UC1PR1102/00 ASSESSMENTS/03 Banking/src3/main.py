import functionality


def main():
    while True:
        # Printing Main Menu
        functionality.clear_screen()
        print("Welcome.\n")
        print(
            "This program is a digital version of the LLOYDS BANK Application to open a SOLE/JOINT LLOYDS BANK ACCOUNT.")
        print("Please note that you need to read through important details regarding your agreement before entering\n"
              "your information in this program. You can find the agreement in the pdf form on the following link:\n"
              "https://www.lloydsbank.com/assets/media/pdfs/sole_joint_account_form.pdf\n")
        print("This program is solely for simplifying the entering of your personal details.")
        print("Please note that by signing with your INITIALS within the registration process\n"
              "in this program, you agree to all terms and conditions specified on the link above.\n\n")
        print("------ MAIN MENU ------\n")
        print("1: Apply for new Bank Account.")
        print("2: Exit Program")

        # Gets user input.
        main_input = input("Please enter your selection.\n"
                           " ->  ")

        # Decide where to send user.
        if main_input == "1":
            functionality.write_record()
        if main_input == "2":
            print("Goodbye, :)")
            quit()
        else:
            continue


if __name__ == "__main__":
    main()
