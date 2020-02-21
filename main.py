"""
@author  - Justin Yee
@version - 1.0

This is an application that creates, stores, exports, imports reminders.
"""

import importlib

reminders = importlib.import_module('reminders')
database = importlib.import_module('database')
engine = importlib.import_module('reminder-engine')     

#initialize application
app = engine.ReminderEngine()
appOn = True

#run application and handle user input for menu options
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
        app.exportReminders()
    #import reminders
    elif userSelection == '6':
        app.importReminders()
    #quit
    elif userSelection == '7':
        appOn = False
        print("Have a good day.")

    else:
        print("Please choose one of the seven options provided.")
