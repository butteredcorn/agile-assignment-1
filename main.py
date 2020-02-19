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

    #if all args are None, raise Error
    def searchDatabase(self, tag = None, text = None, both = None):
        store.search(tag, text, both)

#initialize application
app = ReminderEngine()
store = database.Store()

#application start
app.remindersMenu()



reminderText = input('Create a reminder: ')
reminderTag = input('Add some tags?')

reminder1 = reminders.Reminder(reminderText, reminderTag)
store.addReminder(reminder1)
print(store.reminders)

app.searchDatabase(None, None, "a")