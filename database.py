import pickle
import importlib
import itertools
from operator import itemgetter

reminders = importlib.import_module('reminders')



class Store:

    def __init__(self):
        self.__reminders = []

    #reminder array
    @property
    def reminders(self):
        dict_cache = []
        for reminder in self.__reminders:
            dict_cache.append(reminder.__dict__)
        #return __dict__ just for display purposes
        return dict_cache #in the format of: [{'_id': 0, '_Reminder__text': 'hello world', '_Reminder__tags': 'some tag'}]

    def addReminder(self, reminder):
        self.__reminders.append(reminder)


    #[{'_id': 0, '_Reminder__text': 'hello world', '_Reminder__tags': 'some tag'}]
    def search(self, tag = None, text = None, both = None):
        if tag is None and text is None and both is None:
            raise ValueError("Non-Permissible Search Parameters: Not all three fields can be None.")
        elif (tag):
            searchCache = []
            for reminder in self.__reminders:
                for eachTag in reminder._Reminder__tags:
                    if eachTag == tag:
                        searchCache.append(reminder.__dict__)    
            return searchCache #return __dict__ just for display purposes

        elif (text):
            searchCache = []
            for reminder in self.__reminders:
                if text in reminder._Reminder__text:
                    searchCache.append(reminder.__dict__)
            return searchCache #return __dict__ just for display purposes

        elif (both):
            #note that both is the search term, the option to choose both is handled in the ReminderEngine
            searchCache = []
            for reminder in self.__reminders:
                if reminder._Reminder__tags == both:
                    searchCache.append(reminder.__dict__)
                elif both in reminder._Reminder__text:
                    searchCache.append(reminder.__dict__)
            return searchCache

    def searchByID(self, reminderID):
        if reminderID and isinstance(int(reminderID), int):

            for reminder in self.__reminders:
                if reminder._id == int(reminderID):
                    return reminder
        else:
            return print("Error: Please enter an integer only.")

    def exportToPickle(self, fileName):
        cacheOut = []
        pickle_out = open(f"{fileName}.pickle", "wb") #wb = writable
        for reminder in self.__reminders:
        #    print(reminder)
            cacheOut.append(reminder)
        pickle.dump(cacheOut, pickle_out)
        pickle_out.close()

    def importFromPickle(self, fileName):
        pickle_in = open((f"{fileName}.pickle"), "rb") #rb = readable
        importedReminders = pickle.load(pickle_in)

        # for reminder in importedReminders:
        #     print(reminder)
        # print(importedReminders)

        if self.__reminders == []:
            currentHighestLocalID = 0
        else:
            currentHighestLocalID = int((self.__reminders[-1])._id)

        nextID = currentHighestLocalID + 1

        setCache = []

        if len(self.__reminders) != 0:
            for localReminder in self.__reminders:
                setCache.append(localReminder)

        
        if len(setCache) != 0:
            for importedReminder in importedReminders:
                for localReminder in setCache:
                    if importedReminder._id == localReminder._id:
                        if importedReminder._Reminder__text == localReminder._Reminder__text and importedReminder._Reminder__tags == localReminder._Reminder__tags:
                            #exact duplicate identified
                            continue
                        else:
                            #conflicting ids, but different reminders
                            localReminder._id = nextID
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
