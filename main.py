import random
import string
import time

class TwoFactorAuthSimulator:
    def __init__(self):
        self.secret_key = self.generate_secret_key()
        self.auth_code = self.generate_auth_code()

    def generate_secret_key(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))

    def generate_auth_code(self):
        return str(random.randint(100000, 999999))

    def get_secret_key(self):
        return self.secret_key

    def get_auth_code(self):
        return self.auth_code

    def update_auth_code(self):
        self.auth_code = self.generate_auth_code()

    def verify_auth_code(self, user_input):
        return self.auth_code == user_input

def main():
    simulator = TwoFactorAuthSimulator()
    print("Secret Key:", simulator.get_secret_key())
    print("Auth Code:", simulator.get_auth_code())

    time.sleep(5)  # 5 second delay

    print("Auth Code updated:")
    simulator.update_auth_code()
    print("New Auth Code:", simulator.get_auth_code())

    user_input = input("Enter your Auth Code: ")
    if simulator.verify_auth_code(user_input):
        print("Auth successful!")
    else:
        print("Auth failed!")

if __name__ == "__main__":
    main()
```

Kodda quyidagilar mavjud:

- `TwoFactorAuthSimulator` klassi yaratildi, u ikki faktorli autentifikatsiya simulyatorini taqdim etadi.
- `generate_secret_key` metodi sekretni keyni generatsiya qiladi.
- `generate_auth_code` metodi autentifikatsiya kodi generatsiya qiladi.
- `get_secret_key` metodi sekretni keyni qaytaradi.
- `get_auth_code` metodi autentifikatsiya kodi qaytaradi.
- `update_auth_code` metodi autentifikatsiya kodi yangilaydi.
- `verify_auth_code` metodi autentifikatsiya kodi saqlangan kodi bilan solishtiradi.
- `main` funksiyasi simulyatorni yaratadi, sekretni key va autentifikatsiya kodi chiqaradi, keyin 5 soniya kutib, autentifikatsiya kodi yangilaydi, so'ng userdan autentifikatsiya kodi kiritishni so'raydi va autentifikatsiya muvaffaqiyatini tekshiradi.
