import importlib

reminders = importlib.import_module('reminders')
database = importlib.import_module('database')

#initialize database
store = database.Store()

class ReminderEngine:
    def __init__(self):
        pass

    def remindersMenu(self):
        print('\n    Reminders menu:\n')
        print('    1. show all reminders')
        print('    2. search reminders')
        print('    3. add reminders')
        print('    4. modify reminders')
        print('    5. export reminders')
        print('    6. import reminders')
        print('    7. quit\n')

    def getReminderList(self):
        if store.reminders == []:
            print("\nYou don't have any reminders! Create some with option 3.")
        else:
            print("")
            for eachReminder in store.reminders:
                print(f"{eachReminder}")

    def querySearchParameter(self):
        searchParameter = input("How would you like to search, by 1: tag, 2: text, or 3: both? ")
        if searchParameter == "1":
            searchTerm = input("Please enter the name of the tag: ")
            self.searchDatabase(searchTerm)
        elif searchParameter == "2":
            searchTerm = input("Please enter the exact word or phrase you would like to search: ")
            self.searchDatabase(None, searchTerm)
        elif searchParameter == "3":
            searchTerm = input("Please enter the name of the tag or the exact word or phase you would like to earch: ")
            self.searchDatabase(None, None, searchTerm)
        else:
            print("Please enter a valid option.")
            self.querySearchParameter()

    #if all args are None, raise Error
    def searchDatabase(self, tag = None, text = None, both = None):
        print(store.search(tag, text, both))

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
            newTags = None
        elif ' ' in newTags and '.' not in newTags:
            return print("Error: Please separate tags with a comma.")

        if newTags != "":
            selectedReminder.tags = newTags
            print(f"\nReminder {selectedReminder.id}'s tags has been updated to '{selectedReminder.tags}'.")
        else:
            print("Tags were not updated.")

    def exportReminders(self):
        fileName = input("Filename to save to? Do not enter any extension: ")
        if '.' in fileName:
            print("Please enter a valid filename.")
        else:
            try:
                store.exportToPickle(fileName)
                print(f"Reminders have been exported to {fileName}.pickle.")
            except:
                print(f"Sorry, but we could not write to '{fileName}'")

    def importReminders(self):
        fileName = input("Filename to open from? Do not enter any extension: ")
        #store.importFromPickle(fileName)
        try:
            store.importFromPickle(fileName)
            print(f"Reminders have been imported from {fileName}.pickle.")
        except:
             print(f"\n The file '{fileName}' does not appear to exist.")