
import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.host.com')
mail.login('mail@mail.com', 'imappasswd')
mail.list()
print mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.
print "OK"
#result, data = mail.search(None, "ALL")
