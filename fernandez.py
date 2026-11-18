# ================================================
# MY PYTHON Tutorial Program
# ================================================
import time
import sys

finished = []
score = 0
all_q = 14

def slow_print(msg, delay=0.02):
    for letter in msg:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print("")

def loading():
    print("\nPlease wait", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("")

def show_q(q_text):
    print("\n-----------------------------------")
    slow_print("LOADING QUESTION...")
    loading()
    print("QUESTION:")
    slow_print(q_text, 0.03)
    print("-----------------------------------")

def show_choices(list_choices):
    print("Pick one:")
    for item in list_choices:
        time.sleep(0.25)
        slow_print("  " + item, 0.02)

def check_answer(q_text, list_choices, right, why):
    global score
    show_q(q_text)
    show_choices(list_choices)
    print("\nGet ready...")
    for num in [3, 2, 1]:
        print(f"  {num}...")
        time.sleep(0.35)
    ans = input("Your answer (A/B/C/D): ")
    print("\nChecking...", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("")
    if ans.strip().upper() == right:
        print("\nYOU GOT IT!")
        slow_print("Nice! That is correct!", 0.02)
        score += 1
    else:
        print("\nNot quite")
        slow_print(f"Correct answer: {right}", 0.02)
        slow_print("Try to remember it for the exam!", 0.02)
    print("\nWhy?")
    slow_print(why, 0.015)
    input("\nPress Enter to go back...")

def my_menu():
    print("\n===================================")
    print("   MY PYTHON JOURNEY")
    print("   By: Princes Fernandez")
    print("   7 Lessons | Quiz Inside")
    print("===================================")
    topics = [
        "Introduction to Programming",
        "Python Basic Syntax",
        "Arithmetic Operators and Expressions",
        "Basic Input and Output in Python",
        "Conditional Statements in Python",
        "Logical Operator",
        "Introduction to Iteration and Loops"
    ]
    for i, t in enumerate(topics, start=1):
        mark = "DONE -" if i in finished else "TODO -"
        print(f"{mark} {i}. {t}")
    print("")
    done = len(finished)
    print(f"My Progress: {done}/7")
    print(f"My Score (first try): {score} / {all_q}")
    print("===================================")
    print("Type 1-7 to learn, or Q to quit: ", end="")

# =================================================
# LESSON 1 - Introduction to Programming
# =================================================
def start_lesson1():
    print("\n--- LESSON 1: Introduction to Programming ---")
    print("PREPARED BY: Princes Fernandez")
    input("\nPress Enter...")
    print("\nWhat is a programming language?")
    print("It is a special language that computers understand to do tasks.")
    input("\nPress Enter...")
    print("\nLanguages I know:")
    print("Python - Easy and good for beginners")
    print("Java - Good for apps")
    print("C++ - Fast, good for games")
    print("JavaScript - For websites")
    print("PHP - For websites with database")
    print("Ruby - Simple and productive")
    input("\nPress Enter...")
    print("\nWhat is Python?")
    print("Python was created by Guido van Rossum in 1991.")
    print("He is from Netherlands. He made Python simple and readable.")
    print("Python = high-level, interpreted, general-purpose.")
    print("High-level = close to human language.")
    print("Interpreted = runs line by line.")
    print("General-purpose = can do web, AI, games, automation.")
    input("\nPress Enter...")
    print("\nWhy I like Python?")
    print("1. Easy to learn 2. Looks like English 3. Can do many things 4. Many people help online")
    input("\nPress Enter...")
    print("\nWhat do I need?")
    print("Laptop, Python installed, and PyCharm. PyCharm is what we use in school.")
    input("\nPress Enter...")
    print("\nWhat is Algorithm?")
    print("All programs = INPUT -> PROCESS -> OUTPUT")
    input("\nPress Enter...")
    print("Writing the plan in simple English. Not a real language, just a plan.")
    print("Keywords: START, END, DECLARE, INPUT, OUTPUT, IF, ELSE, WHILE, FOR")
    input("\nPress Enter...")
    print("\nExample: Show my name")
    print("START OUTPUT 'Princes Fernandez' END")
    print("In Python: print('Princes Fernandez')")
    try:
        my_age = int(input("\nTry it - Enter your age: "))
        print("Your age is:", my_age)
    except ValueError:
        print("Please type a number like 19.")
    input("\nPress Enter...")
    print("\nData Types: int = 10, float = 12.5, str = 'Hello', bool = True/False")
    input("\nPress Enter...")
    print("\nQuiz Time - Lesson 1")
    check_answer("What is a programming language?", ["A. A special language computers understand", "B. A computer brand", "C. A game", "D. A website"], "A", "Programming language is a special language computers understand to do tasks.")
    check_answer("Who made Python?", ["A. Guido van Rossum in 1991", "B. Bill Gates in 2000", "C. Elon Musk", "D. Mark Zuckerberg"], "A", "Guido van Rossum made Python in 1991.")
    finished.append(1)

# =================================================
# LESSON 2 - Python Basic Syntax
# =================================================
def start_lesson2():
    print("\n--- LESSON 2: Python Basic Syntax ---")
    print("\nSyntax = rules on how to write Python correctly.")
    input("\nPress Enter...")
    print("\n1. print() - To show output")
    print('Example: print("Hello Mabalacat") -> Hello Mabalacat')
    input("\nPress Enter...")
    print("\n2. Indentation - Use spaces to show blocks.")
    print("If you forget spaces, Python will have error. Use 4 spaces.")
    input("\nPress Enter...")
    print("\nPrinting Text needs quotes.")
    print('Correct: print("Hello") | Wrong: print(Hello)')
    print("\nPrinting Numbers no need quotes.")
    print(100)
    print(25.5)
    print("type(100) =", type(100))
    print('type("100") =', type("100"))
    input("\nPress Enter...")
    print("\nComments - Ignored by Python. For explanation only.")
    print("# This is a comment")
    input("\nPress Enter...")
    print("\nMy Profile with print():")
    print("Name: Princes Fernandez | Age: 19 | Favorite: Programming | Dream: IT Professional")
    print('Quote: "Small efforts every day = big success."')
    input("\nPress Enter...")
    print("\nVariables - A named storage. Value can change.")
    my_age = 19
    my_name = "Princes Fernandez"
    print("Age =", my_age, "Name =", my_name)
    my_age = 20
    print("Now Age =", my_age)
    input("\nPress Enter...")
    print("\nNaming Rules:")
    print("Start with letter or _. Cannot start with number.")
    print("Correct: age, _value | Wrong: 1age")
    print("Python is case-sensitive: age and AGE are different.")
    age = 18
    age2 = 20
    print("age =", age, "AGE =", age2)
    input("\nPress Enter...")
    print("\nOutput Variables:")
    print('school = "Clark College Of Science And Technology", print(school)')
    school = "Clark College Of Science And Technology"
    print(school)
    a = "I"; b = "LOVE"; c = "Clark College Of Science And Technology "

    print("With comma:", a, b, c)
    x = "I "; y = "LOVE "; z = "Clark College Of Science And Technology"
    print("With plus:", x + y + z)
    input("\nPress Enter...")
    print("\nQuiz Time - Lesson 2")
    check_answer("What is syntax?", ["A. Rules to write Python correctly", "B. A computer", "C. A game", "D. A password"], "A", "Syntax = rules to write Python correctly.")
    check_answer("What is a variable?", ["A. Named storage to keep data", "B. A computer", "C. A cable", "D. A printer"], "A", "Variable = named storage. Value can change.")
    finished.append(2)

# =================================================
# LESSON 3 - Arithmetic Operators and Expressions
# =================================================
def start_lesson3():
    print("\n--- LESSON 3: Arithmetic Operators and Expressions ---")
    print("\nArithmetic operators = symbols to do math.")
    input("\nPress Enter...")
    print("Operators:")
    print("+ Add 5+3=8 | - Minus 10-4=6 | * Multiply 7*2=14")
    print("/ Divide 15/3=5.0 | // Floor 17//3=5 | % Remainder 10%3=1 | ** Power 2**3=8")
    print("Check:", 5+3, 10-4, 7*2, 15/3, 17//3, 10%3, 2**3)
    input("\nPress Enter...")
    print("\nExpression = values + variables + operators = result")
    print("Example: a=10, b=5, result=a+b -> 15")
    print("Result is:", 10+5)
    input("\nPress Enter...")
    print("\nMy Grades: Math 90, Science 85, English 88")
    print("Average:", round((90+85+88)/3, 2))
    input("\nPress Enter...")
    print("\nMy Rectangle: length 12, width 8")
    print("Area:", 12*8, "Perimeter:", 2*(12+8))
    input("\nPress Enter...")
    print("\nFinal Grade: Prelim 30%, Midterm 30%, Final 40%")
    try:
        p = float(input("Enter Prelim: "))
        m = float(input("Enter Midterm: "))
        f = float(input("Enter Final: "))
        print("Final Grade:", round((p*0.30)+(m*0.30)+(f*0.40), 2))
    except ValueError:
        print("Please type numbers.")
    input("\nPress Enter...")
    print("\nMY BMI Calculator - BMI = Weight / Height^2")
    print("Example: Princes, 55kg, 1.60m")
    try:
        n = input("Enter Name: ")
        w = float(input("Enter Weight (kg): "))
        h = float(input("Enter Height (m): "))
        print("Name:", n, "BMI:", round(w / (h**2), 2))
    except ValueError:
        print("Please type numbers. Height cannot be 0.")
    input("\nPress Enter...")
    print("\nMY Milk Tea Shop Receipt - Total = Price x Qty, VAT 12%")
    print("Example: Princes, Milk Tea, 120, 2, Total 240, VAT 28.80, Pay 268.80")
    try:
        cust = input("Customer Name: ")
        item = input("Item Name: ")
        price = float(input("Price: "))
        qty = int(input("Quantity: "))
        total = price*qty
        vat = total*0.12
        print("Customer:", cust, "Item:", item, "Total:", f"{total:.2f}", "VAT:", f"{vat:.2f}", "Pay:", f"{total+vat:.2f}")
    except ValueError:
        print("Please type numbers.")
    input("\nPress Enter...")
    print("\nMY jollibee Sales - Subtotal, Discount, Due, Change")
    print("Example: Princes, Chickenjoy, 150, 2, 10%, 500 -> Due 270, Change 230")
    try:
        product = input("Product Name: ")
        pr = float(input("Product Price: "))
        q = int(input("Quantity: "))
        disc = float(input("Discount %: "))
        cash = float(input("Cash: "))
        sub = pr*q
        disc_amt = sub*(disc/100)
        due = sub - disc_amt
        print( "Product:", product, "Subtotal:", f"{sub:.2f}", "Discount:", f"{disc_amt:.2f}", "Due:", f"{due:.2f}", "Change:", f"{cash-due:.2f}")
    except ValueError:
        print("Please type numbers.")
    input("\nPress Enter...")
    print("\nQuiz Time - Lesson 3")
    check_answer("What is 5 + 3?", ["A. 8", "B. 15", "C. 2", "D. 53"], "A", "5 + 3 = 8.")
    check_answer("What is 10 % 3?", ["A. 1", "B. 3", "C. 0", "D. 10"], "A", "10 % 3 = 1, remainder.")
    finished.append(3)

# =================================================
# LESSON 4 - Basic Input and Output in Python
# =================================================
def start_lesson4():
    print("\n--- LESSON 4: Basic Input and Output in Python ---")
    print("\nInput makes program interactive.")
    print('Syntax: variable = input("Message: ")')
    print("All input is string by default.")
    my_name = input("Enter your name: ")
    my_age = input("Enter your age: ")
    print("You typed:", my_name, my_age, "Type:", type(my_name))
    input("\nPress Enter...")
    print("\nFormatting Output:")
    n2 = input("Enter your name again: ")
    a2 = input("Enter your age again: ")
    print("Name: ", n2)
    print("Age: ", a2)
    input("\nPress Enter...")
    print("\nConvert to float:")
    try:
        g = float(input("Enter your grade: "))
        print(f"Your grade is {g}")
    except ValueError:
        print("Please type like 89.5")
    input("\nPress Enter...")
    print("\nConvert to int:")
    try:
        ag = int(input("Enter your age: "))
        print(f"Your age is {ag} - Type {type(ag)}")
    except ValueError:
        print("Please type whole number.")
    input("\nPress Enter...")
    print("\nConvert to bool:")
    ans = input("Are you a student? (yes/no): ")
    is_stud = ans.lower() == "yes"
    print("Student?", is_stud)
    input("\nPress Enter...")
    print("\nQuiz Time - Lesson 4")
    check_answer("What is input by default?", ["A. string", "B. int", "C. float", "D. bool"], "A", "All input is string by default. Even 18 becomes '18'.")
    check_answer("How to get float input?", ["A. float(input('Enter grade: '))", "B. input()", "C. str()", "D. bool()"], "A", "Use float() to change input to decimal.")
    finished.append(4)

# =================================================
# LESSON 5 - Conditional Statements in Python
# =================================================
def start_lesson5():
    print("\n--- LESSON 5: Conditional Statements in Python ---")
    print("\nCondition = program makes decision.")
    print("IF age >= 18 THEN 'Adult' ELSE 'Minor'")
    input("\nPress Enter...")
    print("\nIF Statement:")
    try:
        age = int(input("Enter age: "))
        if age >= 18:
            print("Adult")
        print("Done.")
    except ValueError:
        print("Please type number.")
    input("\nPress Enter...")
    print("\nIF-ELSE:")
    try:
        age = int(input("Enter age: "))
        if age >= 18:
            print("Adult")
        else:
            print("Minor")
    except ValueError:
        print("Please type number.")
    input("\nPress Enter...")
    print("\nELIF - For many conditions:")
    try:
        grade = float(input("Enter grade: "))
        if grade >= 90:
            print("A - Excellent!")
        elif grade >= 80:
            print("B - Very Good!")
        elif grade >= 70:
            print("C - Good!")
        elif grade >= 60:
            print("D - Passed!")
        else:
            print("F - Failed!")
    except ValueError:
        print("Please type number.")
    input("\nPress Enter...")
    print("\nNested IF - IF inside IF:")
    try:
        age = int(input("Enter age: "))
        if age >= 18:
            print("Adult")
            if age >= 60:
                print("Senior Citizen")
            else:
                print("Working Age")
        else:
            print("Minor")
    except ValueError:
        print("Please type number.")
    input("\nPress Enter...")
    print("\nQuiz Time - Lesson 5")
    check_answer("What does IF do?", ["A. Makes decision based on condition", "B. Repeats code", "C. Prints only", "D. Deletes files"], "A", "IF makes decision. If True, run code.")
    check_answer("Grade 85 = ?", ["A. B - Very Good!", "B. A", "C. F", "D. C"], "A", "85 is >=80 but <90, so B.")
    finished.append(5)

# =================================================
# LESSON 6 - Logical Operator
# =================================================
def start_lesson6():
    print("\n--- LESSON 6: Logical Operator ---")
    print("\nLogical operators combine conditions.")
    print("and = both True | or = one True | not = reverse")
    input("\nPress Enter...")
    print("\nTruth Table - and:")
    print("True and True =", True and True)
    print("True and False =", True and False)
    print("False and False =", False and False)
    input("\nPress Enter...")
    print("\nTruth Table - or:")
    print("True or False =", True or False)
    print("False or False =", False or False)
    input("\nPress Enter...")
    print("\nTruth Table - not - Reverse the result:")
    print("not True =", not True)
    print("not False =", not False)
    input("\nPress Enter...")
    print("\nExample - and:")
    try:
        age = int(input("Enter age: "))
        ans = input("Student? (yes/no): ")
        is_stud = ans.lower() == "yes"
        if age >= 18 and is_stud:
            print("Adult Student")
        else:
            print("Not Adult Student")
    except ValueError:
        print("Please type number.")
    input("\nPress Enter...")
    print("\nExample - or:")
    try:
        grade = float(input("Enter grade: "))
        if grade >= 90 or grade <= 60:
            print("Special Case")
        else:
            print("Normal Grade")
    except ValueError:
        print("Please type number.")
    input("\nPress Enter...")
    print("\nExample - not:")
    ans = input("Student? (yes/no): ")
    is_stud = ans.lower() == "yes"
    if not is_stud:
        print("Not a student")
    else:
        print("You are a student")
    input("\nPress Enter...")
    print("\nQuiz Time - Lesson 6")
    check_answer("What is not True?", ["A. False", "B. True", "C. Maybe", "D. Error"], "A", "NOT reverses. not True = False.")
    check_answer("What is True and False?", ["A. False", "B. True", "C. Maybe", "D. Error"], "A", "and needs both True. True and False = False.")
    finished.append(6)

# =================================================
# LESSON 7 - Introduction to Iteration and Loops
# =================================================
def start_lesson7():
    print("\n--- LESSON 7: Introduction to Iteration and Loops ---")
    print("\nIteration = do same task many times.")
    print("Without loop: print 4 times | With loop: for in range(4)")
    for i in range(4):
        print("Study Python")
    input("\nPress Enter...")
    print("\nTwo types: for and while")
    print("for = when you know how many times")
    for i in range(3):
        print("Hello! - for loop")
    print("while = while condition is True")
    c = 1
    while c <= 3:
        print("Hello! - while loop")
        c += 1
    input("\nPress Enter...")
    print("\nfor Loop - Print 1 to 5")
    for num in range(1, 6):
        print(num)
    print("range(1,6) = 1,2,3,4,5. Start included, stop excluded.")
    input("\nPress Enter...")
    print("\nCount Down 5 to 1")
    for num in range(5, 0, -1):
        print(num)
    input("\nPress Enter...")
    print("\nOdd Numbers 1 to 9 - range(1, 10, 2)")
    for num in range(1, 10, 2):
        print(num)
    input("\nPress Enter...")
    print("\nwhile Loop - Print 1 to 5")
    c = 1
    while c <= 5:
        print(c)
        c += 1
    print("c += 1 adds 1. When c=6, loop stops.")
    input("\nPress Enter...")
    print("\nQuiz Time - Lesson 7")
    check_answer("What is Iteration?", ["A. Do same task many times", "B. A computer brand", "C. Error", "D. Variable"], "A", "Iteration = do same task many times.")
    check_answer("What is range(1, 6)?", ["A. 1,2,3,4,5", "B. 1,2,3,4,5,6", "C. 0,1,2,3,4,5", "D. 6"], "A", "range(1,6) = 1 to 5. Stop excluded.")
    finished.append(7)

# =================================================
# MAIN
# =================================================
def run():
    while True:
        my_menu()
        pick = input().strip().lower()
        if pick == "1":
            start_lesson1()
        elif pick == "2":
            start_lesson2()
        elif pick == "3":
            start_lesson3()
        elif pick == "4":
            start_lesson4()
        elif pick == "5":
            start_lesson5()
        elif pick == "6":
            start_lesson6()
        elif pick == "7":
            start_lesson7()
        elif pick == "q":
            print("\nThank you for learning, Princes!")
            print(f"Final: Done {len(finished)}/7 | Score {score} / {all_q}")
            print("Good luck on your Final Exam, Princes Fernandez!")
            break
        else:
            print("Please pick 1-7 or Q.")

run()