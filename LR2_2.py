#Programming Problem 2
def file_navigator():
    import os
    print("Current working directory:", os.getcwd())
    filename = input("Enter the filename: ")
    print(f"Trying to open file: {filename}")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Please input a valid filename")
        return
    print(f"The file contains {len(lines)} lines")
    while True:
        try:
            line_number = int(input("Enter the line number (input 0 to quit): "))
        except ValueError:
            print("Please input a valid number")
            continue
        if line_number == 0:
            print(f"Exiting the program. Thank you!")
            break
        elif 1 <= line_number <= len(lines):
            print(f"Line {line_number}: {lines[line_number-1].strip()}")
        else:
            print(f"Invalid line number. Input a number between 1 and {len(lines)}")

# Running the program
if __name__=="__main__":
    file_navigator()
