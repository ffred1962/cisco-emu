class Emulator():
    def __init__(self):
        self.version="1.0"
        self.isReady=False
        self.users=[
            {
                "name": "user1",
                "passwd": "1234"
            },
            {
                "name": "user2",
                "passwd": "5678"
            }
        ]
    def chkUser(self, user, passwd):
        for u in self.users:
            if (u["name"]==user):
                if (u["passwd"]==passwd):
                    return True
                else:
                    return False        
        return False