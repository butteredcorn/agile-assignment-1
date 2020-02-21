import pickle
import importlib
import itertools
from operator import itemgetter

reminders = importlib.import_module('reminders')

"""
Class for storing, searching, and importing/exporting reminders
Depends on: reminders.py
"""
class Store:

    #reminder objects stored in a list
    def __init__(self):
        self.__reminders = []

    #returns an array of strings describing reminder objects in the Store
    #reminder.__dict__ in the format of {'_id': 0, '_Reminder__text': 'hello world', '_Reminder__tags': 'some tag'}
    @property
    def reminders(self):
        dict_cache = []
        for reminder in self.__reminders:
            dict_cache.append(f"Reminder ID: {reminder.id} | Tags: {reminder.tags}\nDescription: {reminder.text}\n")
        return dict_cache

    #add reminder object to the Store list
    def addReminder(self, reminder):
        self.__reminders.append(reminder)

    #search through Store list and return matching Reminder objects, if found
    def search(self, tag = None, text = None, both = None):
        if tag is None and text is None and both is None:
            raise ValueError("Non-Permissible Search Parameters: Not all three fields can be None.")
        elif (tag):
            searchCache = []
            for reminder in self.__reminders:
                for eachTag in reminder.tags:
                    if eachTag == tag:
                        searchCache.append(reminder)      
            return searchCache #return the whole reminder, engine can parse

        elif (text):
            searchCache = []
            for reminder in self.__reminders:
                if text in reminder.text:
                    searchCache.append(reminder)   
            return searchCache #return __dict__ just for display purposes

        elif (both):
            #note that both is the search term, the option to choose both is handled in the ReminderEngine
            searchCache = []
            for reminder in self.__reminders:
                if reminder.tags == both:
                    searchCache.append(reminder)   
                elif both in reminder.text:
                    searchCache.append(reminder)   
            return searchCache

    #search through Store list by ID and modify that reminder
    def searchByID(self, reminderID):
        if reminderID and isinstance(int(reminderID), int):

            for reminder in self.__reminders:
                if reminder.id == int(reminderID):
                    return reminder
        else:
            return print("Error: Please enter an integer only.")

    #export Store list to root directory as pickle file
    def exportToPickle(self, fileName):
        cacheOut = []
        pickle_out = open(f"{fileName}.pickle", "wb") #wb = writable
        for reminder in self.__reminders:
        #    print(reminder)
            cacheOut.append(reminder)
        pickle.dump(cacheOut, pickle_out)
        pickle_out.close()

    #import pickle file from root directory
    #   - will take care of merge conflicts
    #   - will reset Reminders.resource_cl ID generator
    #   - will sort reminders after merge by ID
    def importFromPickle(self, fileName):
        pickle_in = open((f"{fileName}.pickle"), "rb") #rb = readable
        importedReminders = pickle.load(pickle_in)

        # for reminder in importedReminders:
        #     print(reminder)
        # print(importedReminders)

        if self.__reminders == []:
            currentHighestLocalID = 0
        else:
            currentHighestLocalID = int((self.__reminders[-1]).id)

        nextID = currentHighestLocalID + 1

        setCache = []

        if len(self.__reminders) != 0:
            for localReminder in self.__reminders:
                setCache.append(localReminder)

        
        if len(setCache) != 0:
            for importedReminder in importedReminders:
                for localReminder in setCache:
                    if importedReminder.id == localReminder.id:
                        if importedReminder.text == localReminder.text and importedReminder.tags == localReminder.tags:
                            #exact duplicate identified
                            continue
                        else:
                            #conflicting ids, but different reminders
                            localReminder.id = nextID
                            setCache.append(importedReminder)
                            nextID = nextID + 1
        else:
            for importedReminder in importedReminders:
                #print(importedReminder)
                setCache.append(importedReminder)
                nextID = nextID + 1
            nextID = nextID - 1
        
        #sort order of reminders after merge
        setCache.sort(key=lambda x: x._id)
        #print(setCache)
        self.__reminders = setCache
        
        #sync up the auto-incrementingID generator in reminders
        reminders.resource_cl.setGenerator(nextID)
