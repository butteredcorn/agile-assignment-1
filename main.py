import importlib

reminders = importlib.import_module('reminders')
database = importlib.import_module('database')


class ReminderEngine:
    def __init__(self):
        pass

    def remindersMenu(self):
        print('\nReminders menu:\n')
        print('1. show all reminders')
        print('2. search reminders')
        print('3. add reminders')
        print('4. modify reminders')
        print('5. export reminders')
        print('6. import reminders')
        print('7. quit\n')

    def getReminderList(self):
        print(store.reminders)

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
        reminderText = input('Create a reminder: ')

        #need to allow for delimination of tags
        reminderTag = input('Add some tags?')
        newReminder = reminders.Reminder(reminderText, reminderTag)
        store.addReminder(newReminder)
        print(f"New reminder with description '{newReminder.text}' added with ID {newReminder.id}!")

    def modifyReminderByID(self):
        selectedID = input('Please enter the reminder ID: ')
        selectedReminder = store.searchByID(selectedID)
        #print(selectedReminder.__dict__)
        print(f"Currently, reminder {selectedReminder.id} is set to '{selectedReminder.text}'.")

        newDescription = input("Please enter the new description: ")
        selectedReminder.text = newDescription
        print(f"Reminder {selectedReminder.id} has been updated to '{selectedReminder.text}'.")

        newTags = input('Please enter new tags: ')
        if newTags != "":
            selectedReminder.tags = newTags
            print(f"Reminder {selectedReminder.id} has been updated to '{selectedReminder.text}'.")
        else:
            print("Tags were not updated.")
        

#initialize application
app = ReminderEngine()
store = database.Store()

#application start
app.remindersMenu()



app.createReminder()

app.getReminderList()

#app.querySearchParameter()

app.modifyReminderByID()
