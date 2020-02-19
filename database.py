import reminders

class Store:
    def __init__(self):
        self.__reminders = []

    #reminder array
    @property
    def reminders(self):
        cache = []
        for reminder in self.__reminders:
            cache.append(reminder.__dict__)
            return cache

    def addReminder(self, reminder):
        self.__reminders.append(reminder)
