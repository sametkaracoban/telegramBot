# -*- coding: utf-8 -*-
import telepot
from mailGit import MailOperation

def handle(msg):
    if sender_id== msg['chat']['id']:
        command =  msg['text']
        command.encode("utf-8")

        print ('Got command: %s' % command)

        if command.lower() == u'command #1':
           bot.sendMessage(sender_id, 'answer #1')
           #processes
           #
           #
        elif command.lower() == u'command #2':
           bot.sendMessage(sender_id, 'answer #2')
           #processes
           #
           #
        elif command.lower() == u'command #3':

           bot.sendMessage(sender_id, 'answer #3')
           #processes
           #
           #
        elif command.lower() == u'send e-mail':
            
            goMail = MailOperation()
            goMail.sendMail('subject','from','to','e-mail body')
            bot.sendMessage(sender_id, 'e-mail sent')

sender_id = 283018549;
bot = telepot.Bot('your authentication token')
bot.message_loop(handle)
bot.sendMessage(sender_id, "send a message to telegram user")


print ('print something to console .')
while True:
    pass
