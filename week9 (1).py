import os

# Function to get current working directory
def get_current_wd():
    cwd = os.getcwd()
    return cwd

# Function to create folder if not present else set working directory path
def create_directory(path):
    #Check if folder exists
    folder_present = os.path.exists(path)
    # Create folder if folder doesnt exist
    if not folder_present:
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)
    else:
        print('Folder already present. Using existing folder location')

    return None

#Function to wrap string with quotes to handle any comma provided in the user input
def wrap_string(text):
    return '"' + text + '"'

# Function to open the file, read the contents, and display the contents to the user as program output
def show_output(user_folder, filename):
    os.chdir(user_folder)
    f = open(filename, "r")
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line)
    return None

def main():
    # Prompt user for name of directory.
    folder = input('Please specify the folder name: ')

    # Getting the current parent directory path
    parent_dir = get_current_wd()

    # Creating the path for the new directory
    user_folder = os.path.join(parent_dir,folder)

    # Checking and creating the new directory
    create_directory(user_folder)

    # Prompting the user for the name of the file they want to save to the directory in requirement 1
    filename = input('Please specify the file name: ')

    # prompting the user for their name, address, and phone number
    user_name = input('What is your name? ')
    user_addr = input('What is your address? ')
    user_phone = input('What is your phone number? ')

    #Set current directory to new folder
    os.chdir(user_folder)

    # write the user provided data as a line of comma separated values to the file
    f = open(filename, "a")
    output_line = wrap_string(user_name) + ',' + wrap_string(user_addr) + ',' + wrap_string(user_phone) + '\n'
    f.write(output_line)
    f.close()

    # Function to open the file, read the contents, and display the contents to the user as program output
    show_output(user_folder, filename)

    #Set current directory to parent folder
    os.chdir(parent_dir)

if __name__ == '__main__'
    main()
