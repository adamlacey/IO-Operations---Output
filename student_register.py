def register_students(num_students):  # Defines student register.
    with open('reg_form.txt', 'w') as file:  # Using 'w' as writing permission \ 
# for text file. User input will be
        for num in range(1, num_students + 1):  # inputted into reg_form.txt. \ 
# Num goes up by 1 each time user inputs.
            while True:
                try:  # User inputs their ID number.
                    student_id = input(f"Please enter you Student {num} ID \
number: ")
                    int(student_id)
                    break
                except ValueError:
                    print("Please enter a valid Student ID.") 
                    
            file.write(f"{student_id}\n")
            print(f"Student {num} registered successfully",'.' * 30)  # * 30 \
# used for dotted line after user inputs student ID.
            file.write('.' * 30 + '\n')
            
if __name__ == "__main__":
    while True:
        try:  # User asked to input how many students attending.
            num_students = int(input("Please state the amount of students for \
exam venue registration: "))  
            if num_students > 0:
                break
            else:  # Error if incorrect student ID is inputted.
                print("Please enter the correct number of students.")
        except ValueError:
            print("Please enter a valid number of students for exam venue \
registration.")
     
register_students(num_students)