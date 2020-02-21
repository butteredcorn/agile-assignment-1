import itertools

"""
Itertools class used to generate an auto-incrementing ID
Depends on: itertools module
"""
class resource_cl():
    #generate unique id
    id_generator = itertools.count()

    @classmethod
    def setGenerator(cls, newCount):
        resource_cl.id_generator = itertools.count(newCount)

    def __init__(self):
        self._id = next(self.id_generator)


"""
Reminders class used to create Reminder objects
Parent class: resource_cl()
"""
class Reminder(resource_cl):

    #reminders have id, text, tags
    #reminder.__dict__ in the format of: [{'_id': 0, '_Reminder__text': 'hello world', '_Reminder__tags': 'some tag'}]
    def __init__(self, text, tags = ""):
        super().__init__()
        self.__text = text
        self.__tags = tags


    #text attribute
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value


    #tags attribute
    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def tags(self, value):
        self.__tags = value


    #auto-incrementing id attribute
    @property
    def id(self):
        return self._id

    #for import merge conflict on ids
    @id.setter
    def id(self, value):
        self._id = value

