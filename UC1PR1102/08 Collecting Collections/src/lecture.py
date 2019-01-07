class User:
    def __init__(self):
        """Creates an instance of a new bank User."""
        # Defining dictionaries to store information.
        self.section_one = {}

        
    def get_information(self):
        """Method that gathers required information from user and stores it onto
        its dictionaries."""

        # Section 1 - Personal Detail        
        print("Section 1 - Personal Detail")

        self.section_one["Title"] = input("What is your title? (E.g: Mr, Mrs, Miss, Ms")
        self.section_one["Last Name"] = input("What is your LAST name. (E.g: Doe, Johnson, Hanson")
        self.section_one["First Name"] = input("What is all of your FIRST name(s).")

# And then on to writing the information to a file

number_of_customers = int(input("How many customers to get info from."))
customers = []

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