# Global variable
counter = 0

def increment():
    global counter 
    counter += 1
    print(f"Counter value: {counter}")

increment()  # Counter value: 1
increment()  # Counter value: 2
increment()  # Counter value: 3

