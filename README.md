# eBay Kleinanzeigen-Chatbot
Since you can communicate with Kleinanzeigen-users via e-mail, I decided to automate some tedious work when selling items. So I wrote a very simple script.

## Prerequisites
In order to run the script, your system must have following prerequesites set:
- Python 3
- win32com
- E-Mail account linked to Outlook application

## Approach 
DISCLAIMER: I use an experimental e-mail account for this kind of purposes, so please do not use your private account. I use my experimental account for eBay Kleinanzeigen, therefore I get the emails on my experimental account.
- Experimental e-mail account needs to be linked with the Outlook application
- chatbot.py needs to be executed in terminal.
- The script checks for the first unread message, gets the content, checks if pattern from json data is in the body message and sends the appropriate answers. 
