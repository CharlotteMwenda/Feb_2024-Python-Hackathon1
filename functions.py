# Functions & Fibonacci Sequence
# Question
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
#We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.
def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = []  # Initialize an empty list to store the Fibonacci sequence
    if n <= 0:
        return fibonacci_sequence  # Return an empty list for n <= 0
    elif n == 1:
        fibonacci_sequence.append(0)  # If n == 1, return [0]
        return fibonacci_sequence
    else:
        a, b = 0, 1  # Initialize variables for the first two terms of the Fibonacci sequence
        fibonacci_sequence.extend([a, b])  # Add the first two terms to the sequence
        for _ in range(2, n):
            c = a + b
            fibonacci_sequence.append(c)  # Append the next term to the sequence
            # Update variables for the next iteration
            a, b = b, c
        return fibonacci_sequence  # Return the generated Fibonacci sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print(fibonacci_sequence)
