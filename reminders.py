import database

import itertools

#generate unique id
class resource_cl():
    id_generator = itertools.count()

    def __init__(self):
        self._id = next(self.id_generator)



#reminders have id, text, tags

class Reminder(resource_cl):

    #generate unique id
    #newid = next(itertools.count())

    def __init__(self, text, tags = ""):
        super().__init__()
        #self.id = resource_cl.newid()
        self.__text = text
        self.__tags = tags

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    @property
    def id(self):
        return self._id

reminder1 = Reminder("hello world")

print(reminder1.__dict__)
print(reminder1.id)