import reminders
import pickle


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

    def exportToPickle(self, fileName):
        #to pickle out
        pickle_out = open(f"{fileName}.pickle", "wb") #wb = writable
        pickle.dump(self.__reminders, pickle_out)
        pickle_out.close()

    #need to fix merge conflict with ids
    def importFromPickle(self, fileName):
        pickle_in = open((f"{fileName}.pickle"), "rb") #rb = readable
        importedReminders = pickle.load(pickle_in)

        if self.__reminders == []:
            currentHighestLocalID = 0
        else:
            currentHighestLocalID = int((self.__reminders[-1])._id)

        nextID = currentHighestLocalID + 1

        for importedReminder in importedReminders:
            for localReminder in self.__reminders:
                #id conflict identified
                if importedReminder._id == localReminder._id:
                    if importedReminder._Reminder__text == localReminder._Reminder__text and importedReminder._Reminder__tags == localReminder._Reminder__tags:
                        #exact duplicate identified
                        importedReminders.remove(importedReminder)
                    else:
                        #conflicting ids, but different reminders
                        localReminder._id = nextID
                        nextID = nextID + 1

        #print(importedReminders)
        for reminder in importedReminders:
            self.__reminders.append(reminder)




