"""
problem statement:
1. create a program capable of displaying questions to user like KBC(kaun Baneda Crorepati)
2. use list data type to store the questions and their correct answers
3. Display the final amount the person is taking home after playing the game

"""

questions = [
    {
        "question": "What is the Captial of Pakistan?",
        "options": ["Islamabad", "Kharachi", "Lahore"],
        "correct": "Islamabad"
    },
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai"],
        "correct": "Delhi"
    }

]
    
for q in questions:

    print("\n" + q["question"])

    for idx, option in enumerate(q["options"], start=1):
        print(f"{idx}. {option}")
   
    user_choice = input("Enter the option number: ")
   
    if user_choice.isdigit():
        user_choice = int(user_choice)
        
        #to validate user input
        if 1 <= user_choice <= len(q['options']):
            selected_option = q["options"][user_choice - 1]

            #check if the answer is correct or not
            if selected_option == q["correct"]:
                print("Correct! you got 10 points")
            else:
                print(f"wrong! The correct answer is {q["correct"]}. \n")
        else:
            print("invalid Choose! Please enter a valid option number. \n")

    else:
        print("invalid Input, Please enter a number.\n")




