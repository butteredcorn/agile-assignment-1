import importlib

reminders = importlib.import_module('reminders')
database = importlib.import_module('database')

reminderText = input('Create a reminder: ')
reminderTag = input('Add some tags?')

reminder1 = reminders.Reminder(reminderText, reminderTag)
store1 = database.Store()
store1.addReminder(reminder1)
print(store1.reminders)