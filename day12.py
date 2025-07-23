




def welcome_message():
    
    print("=" * 30)
    
    print("Welcome to the grade calculator.")

    print("=" * 30)








def get_test_scores():

    first = float(input("Put the first score here: "))
    second = float(input("Put the second score here: "))
    third = float(input("Put the third score here: "))

    return first,second,third
first,second,third= get_test_scores()



def calculate_average(first, second, third):
    total = first + second + third
    average = total/3

    print(f"\nYour average is: {average}")

    return average

Final_average = calculate_average(first, second, third)

def get_letter_grade(average):
    if average >= 90:
        return "Your final grade is A. :)"
    elif average >= 80:
        return "Your final grade is B"
    elif average >= 70:
        return "Your final grade is C"
    elif average >= 60:
        return "Your final grade is D"
    else:
        return "Your final grade is F. :("


def display_result(first, second, third, Final_average, letter_grade):
    print("\nYour Results:")
    print(f"Test 1: {first}")
    print(f"Test 2: {second}")
    print(f"Test 3: {third}")
    print(f"Average: {Final_average}")
    print(f"Grade: {letter_grade}")

def main():
    welcome_message()

    first, second, third = get_test_scores()

    avg = calculate_average(first, second, third)

    letter_grade = get_letter_grade(avg)

    display_result(first, second, third, Final_average, letter_grade)
    print("\nThank you!")

if __name__ == "__main__":
    main()