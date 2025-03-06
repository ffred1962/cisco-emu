# python's ssh server
# idea and some code form https://habr.com/ru/articles/791620/ 
import socket
import paramiko
import threading
from paramiko import Transport, RSAKey

# ssh-keygen
good_pub_key = RSAKey(filename="test.rsa")


class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()
        self.user = 'root'
        self.password = 'root'

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        print("user: ", username)
        print("pass: ", password)
        if (username == self.user) and (password == self.password):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def check_auth_publickey(self, username, key):
        if (username == self.user) and (key == good_pub_key):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def enable_auth_gssapi(self):
        return False

    def get_allowed_auths(self, username):
        return "password,publickey"

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True

    def check_channel_pty_request(
        self, channel, term, width, height, pixelwidth, pixelheight, modes
    ):
        return True


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', 22))
    server.listen(5)

    while True:
        try:
            client, addr = server.accept()

            t = Transport(client)
            t.load_server_moduli()
            t.add_server_key(good_pub_key)
            t.start_server(server=Server())
            print("ssh server started!")
            chan = t.accept(20)

            if not chan:
                continue

            chan.send(
                "Welcome to my test server!\n \r"
            )

            chan.send("\n \n \r")

            chan.close()
        except Exception as e:
            print(e)