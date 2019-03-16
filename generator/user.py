from model.user import User
from fixture.additional import MH
import os.path
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of user", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/users.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

testdata = [
    User(last_name=MH.random_string("last_name", 10),
         username=MH.random_string("username", 10),
         nickname=MH.random_string("nickname", 10),
         title=MH.random_string("title", 8),
         address=MH.random_string("address", 40),
         homephone=MH.random_number(7),
         workphone=MH.random_number(7),
         mobilephone=MH.random_number(7),
         secondaryphone=MH.random_number(7),
         email=MH.random_email(7),
         email2=MH.random_email(7),
         email3=MH.random_email(7))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))