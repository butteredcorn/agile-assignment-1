"""
@author  - Justin Yee
@version - 1.1

This is an application that creates, stores, exports, imports reminders.
"""

import importlib

reminders = importlib.import_module('reminders')
database = importlib.import_module('database')
engine = importlib.import_module('reminder-engine')     

#initialize application
app = engine.ReminderEngine()
appOn = True

user_options = {
    'show all reminders': '1',
    'search reminders': '2',
    'add reminders': '3',
    'modify reminders': '4',
    'export reminders': '5',
    'import reminders': '6',
    'quit': '7'
}

#run application and handle user input for menu options
while(appOn):
    app.remindersMenu()
    userSelection = input("Select option: ")

    #show all reminders
    if userSelection == user_options['show all reminders']:
        app.getReminderList()

    #search reminders
    elif userSelection == user_options['search reminders']:
        app.querySearchParameter()

    #add reminders
    elif userSelection == user_options['add reminders']:
        app.createReminder()

    #modify reminders
    elif userSelection == user_options['modify reminders']:
        app.modifyReminderByID()

    #export reminders
    elif userSelection == user_options['export reminders']:
        app.exportReminders()
    #import reminders
    elif userSelection == user_options['import reminders']:
        app.importReminders()
    #quit
    elif userSelection == user_options['quit']:
        appOn = False
        print("Have a good day.")

    else:
        print("Please choose one of the seven options provided.")
