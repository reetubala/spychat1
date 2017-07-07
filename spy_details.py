import datetime

def get_now():
    return datetime.datetime.now()


#Creating a class for spy detail
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

class ChatMessage:
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = get_now()
        self.sent_by_me = sent_by_me

spy = Spy('Raman','Ms.',18,4.5)

Ekta = Spy('Ekta','Ms.',19,4.5)
Sonia  = ('Sonia','Ms.',20,4.5)
Kajal = ('Kajal','Ms.',21,4.5)
Sudha = ('Sudha','Ms.',22,4.5)


friends = ['Ekta','Sonia','Kajal','Sudha']

