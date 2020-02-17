class Career:
    """Career class, to encapsulate the career data"""

    #Initializing the object with name, code, faculty and link
    def __init__(self, name, code, faculty, link):
        self.name = name
        self.code = code
        self.faculty = faculty
        self.link = link
    #To String
    def __str__(self):
        return self.name+","+self.code+","+self.faculty+","+self.link+"\n"

    def compareTo(self, object):
        if self.code == object.code:
            return True
        else:
            return False

