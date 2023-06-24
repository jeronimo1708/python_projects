#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
STARTING_FILE = "./Input/Letters/starting_letter.txt"
DESTINATION_DIRECTORY = "/home/jeronimo/dev/python_projects/mail_merge/Output/ReadyToSend/"
NAMES_FILE = "/home/jeronimo/dev/python_projects/mail_merge/Input/Names/invited_names.txt"
STRING_TO_REPLACE = "[name]"

# Read the names that are to be added to the invite.
# Saved the names in an array.
with open(NAMES_FILE) as file:
    NAMES = [line.rstrip('\n') for line in file]

# Read contents from the starting files and save them in an array
with open(STARTING_FILE) as file:
    FILE_CONTENTS = [line for line in file]

# Iterate over the NAMES array and replace the "[name]" with actual names in the first step.
# Then write the contents to the new files in the DESTINATION Directory
for name in NAMES:
    FILE_CONTENTS[0] = FILE_CONTENTS[0].replace(STRING_TO_REPLACE, name)
    STRING_TO_REPLACE = name
    with open(f"{DESTINATION_DIRECTORY}letter_for_{name}.txt", "w+") as file:
        for line in FILE_CONTENTS:
            file.write(line)
        print(f"{name} file written")





# with open()


        