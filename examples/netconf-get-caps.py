from netconf.client import NetconfSSHSession
host="localhost"
port=830
username="admin"
password="admin"
session = NetconfSSHSession(host, port, username, password)
config = session.get_config()
props=session.capabilities
# ...
for el in props:
    print(el)
   
