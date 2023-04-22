import requests


# create basic UI
# (1) the program must fetch user information
# (2) dedicated window to paste content
# (3) dedicated window to fetch content
# the program must store api keys (encrypted)
# and the user keys. It must also store fetched data in secure
# files
# (4) send the fetched data via e-mail

# API user log-in data

class User():
    def __init__(self):
        self.api_dev_key = str()
        self.api_user_name = str()
        self.api_user_password = str()
        self.api_user_key = str()
        self.paste_url = r"https://pastebin.com/api/api_post.php"
        self.login_url = r"https://pastebin.com/api/api_login.php"
        self.d = {"api_dev_key": self.api_dev_key, "api_user_name": self.api_user_name,
                  "api_user_password": self.api_user_password}

    # This method gets the user key from the API
    def get_user_key(self, dev_key, user_name, user_pw):
        self.api_dev_key = dev_key
        self.api_user_name = user_name
        self.api_user_password = user_pw
        try:
            d = {'api_dev_key': f"{dev_key}", 'api_user_name': f"{user_name}", 'api_user_password': f"{user_pw}"}
            request = requests.post(f"{self.login_url}", d)
            self.api_user_key = request.text
            print(f"[i] {request.status_code} \t {request.text}")
            return request.text
        except Exception as E:
            print(f"[X] {E}\t Try again")

    # This method retrieves user information based on the api_option given by the user
    # TODO check if the api_option is valid
    def get_user_details(self, api_option):
        userinfo = {"api_option": f"{api_option}", "api_user_key": f"{self.api_user_key}",
                    "api_dev_key": f"{self.api_dev_key}"}
        with open("list.xml", "w") as f:
            f.write(requests.post(self.paste_url, userinfo).text)
        return requests.post(self.paste_url, userinfo).text


u = User()
u.get_user_key(r"", r"", r"")
print(u.get_user_details("list"))