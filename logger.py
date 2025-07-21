# logger.py

def log_operation(operation, a, b, result):
    with open("log.txt", "a") as file:
        file.write(f"{a} {operation} {b} = {result}\n")