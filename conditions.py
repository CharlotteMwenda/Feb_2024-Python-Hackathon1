# Python Conditional Statements 
def main():
    # Prompt user to enter their age
    age = int(input("Enter your age: "))

    # Check if age is greater than or equal to 18
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."

if __name__ == "__main__":
    main()
