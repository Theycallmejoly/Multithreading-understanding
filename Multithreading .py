import threading
import time
import math

# Function to calculate factorial
def factorial(n):
    time.sleep(1)  # Simulate some time-consuming task
    return math.factorial(n)

def main():
    # Define numbers for which factorial will be calculated
    numbers = [5, 4, 3, 2, 1]

    # Create threads to calculate factorial for each number
    threads = []
    for num in numbers:
        thread = threading.Thread(target=lambda: print(f"Factorial of {num}: {factorial(num)}"))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
