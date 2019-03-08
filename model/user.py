from sys import maxsize

class User:

    def __init__(self, last_name=None, username=None, nickname=None, title=None, address=None, homephone=None, mobilephone=None,
                 workphone=None, secondaryphone=None, email=None, email2=None, email3=None, all_phone=None, all_email=None, id=None):
        self.last_name = last_name
        self.username = username
        self.nickname = nickname
        self.title = title
        self.address = address
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.all_phone = all_phone
        self.all_email = all_email
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id,self.username,self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.username == other.username \
               and self.last_name == other.last_name

    def id_or_nmx(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize