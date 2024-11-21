  # Initialize user variables
u = ""
p = ""

questions_by_topic = {
    "DSA": [
        {
            "question": "Which of the following sorting algorithms can be used to sort a random linked list with minimum time complexity??",
            "options": ["Insertion Sort", "Quick Sort", "Heap Sort", "Merge Sort"],
            "answer": "Merge Sort"
        },
        {
            "question": "In the worst case, the number of comparisons needed to search a singly linked list of length n for a given element is?",
            "options": ["log(2*n)", "n/2", "log(2*n) -1", "n"],
            "answer": "n"
        },
        {
            "question": "Which one of the following is an application of Stack Data Structure?",
            "options": ["Managing function calls", "The stock span problem", "Arithmetic expression evaluation", "All of the above"],
            "answer": "All of the above"
        }
    ],
    "DBMA": [
        {
            "question": "What does SQL stand for?",
            "options": ["Structured Query Language", "Super Quantum Logic", "Stylish Query Lingo", "Server Query Lanuage"],
            "answer": "Structured Query Language"
        },
        {
            "question": "What is the name of the SQL database that comes distributed with Python?",
            "options": ["PySQL", "PostgreSQL", "SQLite", "MySQL"],
            "answer": "SQLite"
        },
        {
            "question": "A view of database that appears to an application program is known as?",
            "options": ["Schema", "Subschema", "Virtual table", "Index Table"],
            "answer": "Subschema"
        },
    ],
    "PYTHON": [
        {
            "question": "What does the 'print' function do in Python?",
            "options": ["It displays text or variables to the console", "It performs mathematical calculations", "It defines a new function", "It creates a loop"],
            "answer": "It displays text or variables to the console"
        },
        {
            "question": "Which Python function is used to get the length of a list?",
            "options": ["len()", "count()", "size()", "length()"],
            "answer": "len()"
        },
        {
            "question": "Which Python data type is mutable?",
            "options": ["List", "Tuple", "Set", "String"],
            "answer": "List"
        },
    ]
}

def start_quiz(topic):
    """Function to start the quiz based on selected topic."""
    # Get the questions for the selected topic
    questions = questions_by_topic.get(topic, [])
    
    if not questions:
        print("No questions available for this topic.")
        return
    
    score = 0  # Initialize score as 0
    total_questions = len(questions)
    
    print(f"\nStarting the {topic.capitalize()} quiz...\n")
    
    # Loop through each question in the selected topic
    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for idx, option in enumerate(q["options"]):
            print(f"{chr(65+idx)}) {option}")
        
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        # Check if answer is correct
        if answer == 'A' and q["options"][0] == q["answer"]:
            print("Correct!\n")
            score += 1
        elif answer == 'B' and q["options"][1] == q["answer"]:
            print("Correct!\n")
            score += 1
        elif answer == 'C' and q["options"][2] == q["answer"]:
            print("Correct!\n")
            score += 1
        elif answer == 'D' and q["options"][3] == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {q['answer']}\n")
    
    # Show final score
    print(f"Quiz finished! You scored {score} out of {total_questions}.\n")

def signup():
    """Signup process to create a new user."""
    global u, p
    u = input("Create username: ").strip()
    p = input("Create password: ").strip()
    print("Signup successful!")
    
def login():
    """Login process to verify credentials."""
    global u, p
    
    if u == "" or p == "":
        print("No user found, please sign up first.")
        return False
    
    ul = input("Enter username: ").strip()
    lp = input("Enter password: ").strip()

    # Check if username matches
    while ul != u:
        print("User not found. Please try again.")
        ul = input("Enter username: ").strip()

    # Check if password matches
    while lp != p:
        print("Incorrect password. Please try again.")
        lp = input("Enter password: ").strip()

    print("Login successful!")
    return True

def main():
    while True:
        print("Select option (l)ogin | (s)ignup | (q)uiz")
        answer = input("").strip().lower()

        if answer == "s":
            # Signup process
            signup()
            print("Now, please log in to continue.")
        
        elif answer == "l":
            # Login process
            if login():
                # After successful login, proceed to quiz
                print("\nSelect a quiz topic:")
                print("1) DSA")
                print("2) DBMS")
                print("3) PYTHON")
                
                topic_choice = input("Enter the number of the topic you want to choose (1/2/3): ").strip()

                # Map the user's choice to a topic
                if topic_choice == "1":
                    selected_topic = "DSA"
                elif topic_choice == "2":
                    selected_topic = "DBMA"
                elif topic_choice == "3":
                    selected_topic = "PYTHON"
                else:
                    print("Invalid choice, please try again.")
                    continue

                # Start quiz for the selected topic
                start_quiz(selected_topic)
                break  # Exit the loop after quiz

        elif answer == "q":
            print("You need to log in first to take the quiz.")
            continue  # If the user tries to access the quiz without logging in, prompt again

        else:
            print("Error: Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
