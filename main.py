import importlib

reminders = importlib.import_module('reminders')
database = importlib.import_module('database')


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
            #print(searchTerm)
            self.searchDatabase(searchTerm)
        elif searchParameter == "2":
            searchTerm = input("Please enter the exact word or phrase you would like to search: ")
            self.searchDatabase(None, searchTerm)
        elif searchParameter == "3":
            searchTerm = input("Please enter the name of the tag or the exact word or phase you would like to earch: ")
            self.searchDatabase(None, None, searchTerm)

    #if all args are None, raise Error
    def searchDatabase(self, tag = None, text = None, both = None):
        print(store.search(tag, text, both))

    def createReminder(self):
        #ask for user inputted reminder description
        reminderText = input('Create a reminder description: ')

        #ask for user inputted tags for reminder
        reminderTags = input('Add some tags? Separate tags with a comma: ')
        if reminderTags == "":
            reminderTags = None
        formattedTags = [tag.strip() for tag in reminderTags.split(',')]

        #create reminder by calling Reminder in reminders.py
        newReminder = reminders.Reminder(reminderText, formattedTags)

        #store new reminder in Store in database.py
        store.addReminder(newReminder)
        print(f"\nNew reminder with description '{newReminder.text}' added with ID {newReminder.id}!")


    def modifyReminderByID(self):
        selectedID = input('Please enter the reminder ID: ')
        selectedReminder = store.searchByID(selectedID)
        #print(selectedReminder.__dict__)
        print(f"\nCurrently, reminder {selectedReminder.id} is set to '{selectedReminder.text}'.")

        newDescription = input("Please enter the new description: ")
        selectedReminder.text = newDescription
        print(f"\nReminder {selectedReminder.id}'s description has been updated to '{selectedReminder.text}'.")

        newTags = input('Please enter new tags: ')
        if newTags != "":
            selectedReminder.tags = newTags
            print(f"\nReminder {selectedReminder.id}'s tags has been updated to '{selectedReminder.tags}'.")
        else:
            print("Tags were not updated.")
        

#initialize application
app = ReminderEngine()
store = database.Store()
appOn = True

while(appOn):
    app.remindersMenu()
    userSelection = input("Select option: ")

    #show all reminders
    if userSelection == '1':
        app.getReminderList()

    #search reminders
    elif userSelection == '2':
        app.querySearchParameter()

    #add reminders
    elif userSelection == '3':
        app.createReminder()

    #modify reminders
    elif userSelection == '4':
        app.modifyReminderByID()

    #export reminders
    elif userSelection == '5':
        continue
    #import reminders
    elif userSelection == '6':
        continue
    #quit
    elif userSelection == '7':
        appOn = False
        print("Have a good day.")
