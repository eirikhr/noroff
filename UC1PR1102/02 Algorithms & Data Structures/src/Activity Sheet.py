"""
Pseudocode:

Ask for the first persons name.

Ask for the first persons favorite programming language.

Print the first name and his/hers favorite programming language.

Ask for the second persons name.

Ask for the second persons favorite programming language.

"""

name = input("What is your name? ")
lang = input("What is your favorite programming language? ")

print("Your name is {} and your favorite programming language is {}\n".format(name.capitalize(), lang.lower()))
print("But isn't there two of you?")

second = input("And whats your name? ")
langsec = input("What is your favorite programming language? ")

print("So here we have {} and {}. Their favorite programming languages are {} and {}"
       .format(name.capitalize(), second.capitalize(), lang.lower(), langsec.lower()))

"""

4. SPOT THE ERRORS! Find and correct the error(s) in each of the following code
samples. Try running the corrected code in Python!
a. print 'hello'

b. food = input(What is your favourite food?)

c. home = input("Where do you live?')

d. print = 'Hello World!'

e. input('What is your name? ')
print(name)

f. sum = 1 + 2
print('sum')

g. print("Hello World"\n)

h. message = 'Spam'
print('I love' message)
print(Message*5)

i. greeting = Welcome to the course
Print(Greeting)

j. print('Welcome' + 'to' + 'the' + 'course')

--------ANSWERS----------

a.  The argument of the print function needs to be placed inside brackets.
    Corrected:
        print('hello')

b.  The argument of the input() function needs to have quote signs in order to display text.
    Corrected:
        food = input("What is your favourite food?")

c.  The quotes inside a function() cannot be both single and double.
    It needs to be either double quotes print("Like this"), or single quotes -> print('Like this')
    Corrected:
        home = input("Where do you live?")

d.  This sample is not immediately wrong. However, if the purpose is to print "Hello World", it is not correct.
    The sample stores "Hello World" into a variable called print.
    If the purpose is to actually print it to screen you have two options:
        Option 1: print("Hello World")
        Option 2: print(print)
    The second option only works if print is defined like in the sample code.

e.  We have not stored the input anywhere.
    Corrected:
        name = input('What is your name? ')
        print(name)

f.  The print part is printing the string 'sum' and not the variable sum. Therefore, it will print the text sum, not
    the value stored in the variable sum.
    Corrected:
        sum = 1 + 2
        print(sum)

g.  \n defines a new line inside the print function. However, \n needs to be added inside the brackets.
    Corrected:
        print("Hello World!\n")

h.  In the first print, we need to add a , or a + in order to display it inside the same print().
    In the second print,  we are trying to print Message, not message. Variables are case sensitive.
    Corrected:
        message = 'Spam'
        print('I love', message)
        print(message*5)

i.  A string needs quotes in order to be stored.
    Also, variables are still case sensitive, so we still need to type greeting in lowercase.
    Corrected:
        greeting = "Welcome to the course"
        Print(greeting)

j.  The + operator simply adds the strings. Because there are no spaces within the "Words" "Inside" "Quotes" it will
    simply add them together with no spaces. I like to use , instead because it automatically adds a space.
    Corrected:
        print('Welcome', 'to', 'the', 'course')

"""
