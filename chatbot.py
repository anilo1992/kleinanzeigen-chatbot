import win32com.client
import json
import random
import time

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)

f = open(r'C:\Users\Anil\Documents\Anilo\Projekte\Python\eBay-Kleinanzeigen\chatdata.json')
data = json.load(f)

messages = inbox.Items
for message in messages:
    if message.UnRead == True: 
        message.Unread = False
        for data in data["chatdata"]:
            for eingabe in data["eingabe"]:
                if eingabe in str(message.Body).lower():
                    reply = message.Reply() 
                    reply.Body = str(random.choice(data["antwort"]))
                    reply.Send()
                    print('Antwort ist erfolgt.')
                    time.sleep(1)
