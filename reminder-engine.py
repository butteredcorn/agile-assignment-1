import importlib

reminders = importlib.import_module('reminders')
database = importlib.import_module('database')

#initialize database
store = database.Store()

"""
Reminder Engine class used to create functionalities expected of an application that creates, modifies, and stores reminders
    - user inputs are handled in this class
    - errors are handled in this class
Depends on: reminders.py and database.py
"""
class ReminderEngine:

    def __init__(self):
        pass

    #print menu
    def remindersMenu(self):
        print('\n    Reminders menu:\n')
        print('    1. show all reminders')
        print('    2. search reminders')
        print('    3. add reminders')
        print('    4. modify reminders')
        print('    5. export reminders')
        print('    6. import reminders')
        print('    7. quit\n')

    #return list of reminders in Store list
    def getReminderList(self):
        if store.reminders == []:
            print("\nYou don't have any reminders! Create some with option 3.")
        else:
            print("")
            for eachReminder in store.reminders:
                print(f"{eachReminder}")

    #request user input for how to search
    def querySearchParameter(self):
        searchParameter = input("How would you like to search, by 1: tag, 2: text, or 3: both? ")
        if searchParameter == "1":
            searchTerm = input("Please enter the name of the tag: ")
            self.searchDatabase(searchTerm)
        elif searchParameter == "2":
            searchTerm = input("Please enter the exact word or phrase you would like to search: ")
            self.searchDatabase(None, searchTerm)
        elif searchParameter == "3":
            searchTerm = input("Please enter the name of the tag or the exact word or phase you would like to search: ")
            self.searchDatabase(None, None, searchTerm)
        else:
            print("Please enter a valid option.")
            self.querySearchParameter()
   
    #call search function in database after receiving user input for option from querySearchParameter()
    def searchDatabase(self, tag = None, text = None, both = None):
        #note: database will throw error if all fields passed in are None,
        #      however, this is redundant as querySearchParameter() handles the errors.
        result = store.search(tag, text, both)
        if result == [] or result is None:
            print("\nNo matches were found.")
        else:
            print("")
            for eachResult in result:
                print(f"Reminder ID: {eachResult.id} | Tags: {eachResult.tags}\nDescription: {eachResult.text}\n")

    #create a new reminder and store it in Store list
    def createReminder(self):
        #ask for user inputted reminder description
        reminderText = input('Create a reminder description: ')
        if reminderText == "":
            return print("Error: Empty descriptions are not allowed for reminders. Please enter a description.")

        #ask for user inputted tags for reminder
        reminderTags = input('Add some tags? Separate tags with a comma. To join words for a tag, use a hyphen: ')
        if reminderTags == "":
            reminderTags = None
        elif ' ' in reminderTags and '.' not in reminderTags:
            return print("Error: Please separate tags with a comma.")
        
        if reminderTags == None:
            formattedTags = None #pass None if no tags are specified
        else:
            formattedTags = [tag.strip() for tag in reminderTags.split(',')]

        #create reminder by calling Reminder in reminders.py
        newReminder = reminders.Reminder(reminderText, formattedTags)

        #store new reminder in Store in database.py
        store.addReminder(newReminder)
        print(f"\nNew reminder with description '{newReminder.text}' added with ID {newReminder.id}!")

    #modify an existing reminder in Store list
    def modifyReminderByID(self):
        selectedID = input('Please enter the reminder ID: ')
        selectedReminder = store.searchByID(selectedID)
        if selectedReminder is None:
            return print("No such ID exists.")
        #print(selectedReminder.__dict__)
        print(f"\nCurrently, reminder {selectedReminder.id} is set to '{selectedReminder.text}'.")

        newDescription = input("Please enter the new description: ")
        if newDescription == "":
            return print("Error: Empty descriptions are not allowed for reminders. Please enter a description.")

        selectedReminder.text = newDescription
        print(f"\nReminder {selectedReminder.id}'s description has been updated to '{selectedReminder.text}'.")

        newTags = input('Please enter new tags: ')

        if newTags == "":
            print("Tags were not updated.")
        elif ' ' in newTags and '.' not in newTags:
            return print("Error: Please separate tags with a comma.")

        if newTags != "":
            newTags = [tag.strip() for tag in newTags.split(',')]
            selectedReminder.tags = newTags
            print(f"\nReminder {selectedReminder.id}'s tags has been updated to '{selectedReminder.tags}'.")

    #ask for user input for filename and export to pickle file
    def exportReminders(self):
        fileName = input("Filename to save to? Do not enter any extension or spaces: ")
        if '.' in fileName or ' ' in fileName:
            print("\nPlease enter a valid filename.")
        else:
            try:
                store.exportToPickle(fileName)
                print(f"Reminders have been exported to {fileName}.pickle.")
            except:
                print(f"Sorry, but we could not write to '{fileName}'")

    #ask for user input for filename and import from pickle file
    def importReminders(self):
        fileName = input("Filename to open from? Do not enter any extension: ")
        #store.importFromPickle(fileName)
        try:
            store.importFromPickle(fileName)
            print(f"Reminders have been imported from {fileName}.pickle.")
        except:
             print(f"\n The file '{fileName}' does not appear to exist.")