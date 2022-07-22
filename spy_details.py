# spy_name='BOND'
# spy_salutation='Mr'
# spy_rating=5.0
# spy_age=30

class Spy:
    def __init__(self,spy_name,spy_salutation,spy_age,spy_rating):
        self.spy_name = spy_name
        self.spy_salutation = spy_salutation
        self.spy_age = spy_age
        self.spy_rating = spy_rating
        self.is_online = True
        self.chats = []
        self.current_status_message = 'Hey! I am on Spychat & Available'

class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


