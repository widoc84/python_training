from sys import maxsize

class User:

    def __init__(self, last_name=None, username=None, nickname=None, title=None, tel=None,mail=None,id=None):
        self.last_name = last_name
        self.username = username
        self.nickname = nickname
        self.title = title
        self.tel = tel
        self.mail = mail
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