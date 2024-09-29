def create_file():
    """
    Creates a new text file named "my_file.txt" in write mode ('w') and writes three lines of text to it.
    """
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is the first line.\n")
            file.write("The answer is 42.\n")
            file.write("This is the third line with a number: 3.14\n")
    except PermissionError:
        print("Permission denied to create or write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File creation and writing operation completed.")

def read_file():
    """
    Reads the contents of "my_file.txt" and displays them on the console.
    """
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File reading operation completed.")

def append_to_file():
    """
    Opens "my_file.txt" in append mode ('a') and appends three additional lines of text to the existing content.
    """
    try:
        with open("my_file.txt", 'a') as file:
            file.write("This is the fourth line.\n")
            file.write("The answer is still 42.\n")
            file.write("This is the sixth line with a number: 6.28\n")
    except PermissionError:
        print("Permission denied to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File appending operation completed.")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read the file again to display the appended content

if __name__ == "__main__":
    main()