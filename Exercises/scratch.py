# PY4E Exercises

# ------------------GRADED
def exercise_hello():
    name1 = input('Enter your name: ')
    print("Hello ",name1) 

# exercise_hello()

# -----------------GRADED
def exercise_2_2():
    """Returns a string greeting the input name from the prompt "enter your name".
    
    Parameters
    ----------
    none: a prompt is given asking for your name

    Returns
    -------
    Hello ___; followed by the name given at the input prompt
    """

    in_name = input("Enter your name: ")
    print("Hello ",name)

# exercise_2_2()

# -----------------GRADED
def exercise_2_3():
    """Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
    Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
    You should use input to read a string and float() to convert the string to a number. 
    Do not worry about error checking or bad user data.
    
    Parameters
    ----------
    none: a prompt is given asking for hours and then for rate
    
    Returns
    -------
    gross pay
    """

    hrs = input("Enter Hours: ")
    rt = input("Enter Rate: ")
    print(float(hrs) * float(rt))

# exercise_2_3()

def exercise_celsius_to_fahrenheit(): 
    # prompt user for celsius temperature
    var1 = float(input("Enter celsius temperature: "))

    # convert celsius to fahrenheit == celsius*(9/5) + 32 
    var2 = var1*(9/5)+32

    # print prompt with fahrenheit
    print("The temperature in Fahrenheit is: ",var2)

# exercise_celsius_to_fahrenheit()

# -----------------GRADED
def exercise_3_1():
    """ Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
    Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
    Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
    You should use input to read a string and float() to convert the string to a number. 
    Do not worry about error checking the user input - assume the user types numbers properly.
    
    Parameters
    ----------
    45, 10.50
    You should use input to read a string and float() to convert the string to a number.

    Returns
    -------
    498.75
    """

    hrs = float(input("Enter Hours: "))  
    rate = float(input("Enter Rate: "))

    if hrs <= 40.0:
        hrs = hrs 
        rate = rate 
    elif hrs > 40.0:
        hrs = hrs
        rate = rate * 1.5
    
    print(hrs*rate)
    
# exercise_3_1()

# -----------------GRADED
def exercise_3_3():
    """Write a program to prompt for a score between 0.0 and 1.0.
    If the score is out of range, print an error. 
    If the score is between 0.0 and 1.0, print a grade using the following table"""

    """>= 0.9     A
       >= 0.8     B
       >= 0.7     C
       >= 0.6     D
       < 0.6      F"""

    # prompt to enter score 
    score = float(input("Enter Score: "))

    # if score isn't between 0.0 and 1.0, print error message and exit.
    if score < 0.0 or score > 1.0:
        print("Error: Please try again.")
        exit()
    # assign grade letters 
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")

# exercise_3_3() 

# -----------------GRADED 
def exercise_4_6():
    def computepay(h, r):

        if h > 40:
            return 1.5 * r * (h - 40) + (40 *r)
        else:
            return h*r
        
    hrs = input("Enter Hours:")
    rate = input("Enter rate per hour:")

    fh = float(h)
    fr = float(r) 
    
    p = computepay(fh*fr)
    print("Pay", p)

exercise_4_6()


    
    

