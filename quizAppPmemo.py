import sys

# Global dictionaries for user data and quizzes
users = {}
quizzes = {
    'cse': [
        {'question': "What is the full form of RAM?", 'options': ['Random Access Memory', 'Read Access Memory', 'Random Allocation Memory', 'Run Access Memory'], 'answer': 'Random Access Memory'},
        {'question': "What is the main component of a computer's motherboard?", 'options': ['Processor', 'Hard Drive', 'Power Supply', 'RAM'], 'answer': 'Processor'},
        {'question': "Which device is used as a primary storage in computers?", 'options': ['Hard Disk', 'RAM', 'SSD', 'Motherboard'], 'answer': 'RAM'},
        {'question': "What is the main function of an operating system?", 'options': ['Word Processing', 'Managing Resources', 'Gaming', 'Graphics'], 'answer': 'Managing Resources'}
    ],
    'python': [
        {'question': "What is the output of print(3 * 3)?", 'options': ['6', '9', '12', '15'], 'answer': '9'},
        {'question': "Which keyword is used to handle exceptions?", 'options': ['catch', 'try', 'except', 'throw'], 'answer': 'except'},
        {'question': "Which function is used to get user input?", 'options': ['input()', 'scan()', 'get()', 'fetch()'], 'answer': 'input()'},
        {'question': "What is a correct file extension for Python files?", 'options': ['.py', '.python', '.pt', '.p'], 'answer': '.py'}
    ],
    'dsa': [
        {'question': "What is the best case time complexity of quicksort?", 'options': ['O(n)', 'O(n^2)', 'O(log n)', 'O(n log n)'], 'answer': 'O(n log n)'},
        {'question': "What data structure uses LIFO principle?", 'options': ['Stack', 'Queue', 'Deque', 'Array'], 'answer': 'Stack'},
        {'question': "What is the height of a binary tree with 7 nodes?", 'options': ['2', '3', '4', '5'], 'answer': '3'},
        {'question': "Which of these is not a linear data structure?", 'options': ['Array', 'Linked List', 'Stack', 'Graph'], 'answer': 'Graph'}
    ]
}

# Function to register a new user
def register():
    print("\nRegister")
    username = input("Enter username: ")
    if username in users:
        print("Username already exists. Please try again.")
    else:
        password = input("Enter password: ")
        users[username] = password
        print("Registration successful! Please login to continue.")

# Function to login
def login():
    print("\nLogin")
    username = input("Enter username: ")
    if username not in users:
        print("Username not found. Please register first.")
        return False
    password = input("Enter password: ")
    if users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Incorrect password.")
        return False

# Function to display the quiz options and handle quiz attempt
def attempt_quiz():
    print("\nSelect a quiz:")
    print("1. CSE")
    print("2. Python")
    print("3. DSA")
    
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        quiz_type = 'cse'
    elif choice == '2':
        quiz_type = 'python'
    elif choice == '3':
        quiz_type = 'dsa'
    else:
        print("Invalid choice. Returning to main menu.")
        return

    # Start the selected quiz
    score = 0
    for question in quizzes[quiz_type]:
        print("\n" + question['question'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        answer = input("Enter the option number for your answer (1-4): ")

        # Validate answer by option number
        try:
            answer_index = int(answer) - 1  # Convert input to zero-based index
            if 0 <= answer_index < len(question['options']) and question['options'][answer_index] == question['answer']:
                score += 1
        except ValueError:
            print("Invalid input. Skipping question.")

    print(f"\nQuiz completed! Your score: {score}/{len(quizzes[quiz_type])}")


while True:
        print("\nMain Menu")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            register()
        elif choice == '2':
            if login():
                while True:
                    print("\nQuiz Menu")
                    print("1. Attempt Quiz")
                    print("2. Logout")
                    
                    sub_choice = input("Enter your choice (1-2): ")
                    
                    if sub_choice == '1':
                        attempt_quiz()
                    elif sub_choice == '2':
                        print("Logged out. Returning to main menu.")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            print("Exiting the quiz app. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
