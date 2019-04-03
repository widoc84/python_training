import mysql.connector
from model.group import Group
from model.user import User


class DbFixture:
    def __init__(self,host,name,user,password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection= mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_user_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home,work,mobile,phone2,email,email2,email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname,address,home,work,mobile,phone2,email,email2,email3) = row
                list.append(User(id=str(id),
                                 username=firstname,
                                 last_name=lastname,
                                 address=address,
                                 homephone=home,
                                 workphone=work,
                                 mobilephone=mobile,
                                 secondaryphone=phone2,
                                 email=email,
                                 email2=email2,
                                 email3=email3,))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()