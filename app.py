import os
import sys
import json

running = True

# Load notes from JSON file
def load_notes():
    try:
        with open("notes.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save notes to JSON file
def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)

# Initialize notes
notes = load_notes()

print("\033[92m")
print("Notex software")
version = "1.0.0"
print("v." ,version)
print("owner:Fahim Abrar")

print("\033[93m")
print("Sir,please login")

#user login
login = int(input("Enter your passcode: "))

if login == 2580:
    print("Login successful!")
    os.system("cls")
else:
    print("Wrong passcode!")
    print("Please try again.")

#app main
while running:
    print("\033[92m")
    print("Welcome sir!")
    print("#############################")
    print("Sir, what do you want to do?" \
        "\n1. Create a new note" \
        "\n2. View existing notes" \
        "\n3. Delete a note" \
        "\n4. Exit")
    print("#############################")
    print("\033[94m")
    #use choice 
    user = int(input("Enter your choice: "))

    if user == 1:
        print("Create a Note here...")
        note_title = input("Note title: ")
        note_text = input("Note text: ")
        notes[note_title] = {
        "title": note_title,
        "content": note_text
         }

        if note_title in notes:
            print("\033[92m")
            print("note created successfully!")
            save_notes(notes)  # Save notes to JSON file
        else:
            print("try again!")
      
    if user == 2:
         print("Tomar note gulo:")
         for note in notes:
             print(f"title: {notes[note]['title']}")
             print(f"content: {notes[note]['content']}")
             print("--------------------------------------")
    #delete
    if user == 3:
        print("delete a note from here...")
        for note in notes:
            print("\033[93m")
            print(f"title: {notes[note]['title']}")
            print(f"content: {notes[note]['content']}")
            print("--------------------------------------")

        delete = input("Enter the note title to delete: ")

        if delete in notes:
            del notes[delete]
            print("\033[92m")
            print("Note deleted successfully!")
            save_notes(notes)  # Save notes to JSON file
        else:
            print("\033[91m")
            print("Note not found. Please try again.")
             
    if user == 4:
        print("exiting the app....")
        running = False
        print("Thank you for using Notex software!")
        print("Have a nice day!")
        break  # Exit the loop to prevent further iterations
    else:
        if user not in [1, 2, 3, 4]:  # Check for invalid choices
            print("\033[91m")
            print("Invalid choice. Please try again.")