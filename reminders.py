import itertools

#generate unique id
class resource_cl():
    id_generator = itertools.count()

    @classmethod
    def setGenerator(cls, newCount):
        resource_cl.id_generator = itertools.count(newCount)

    def __init__(self):
        self._id = next(self.id_generator)


#reminders have id, text, tags
class Reminder(resource_cl):

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

