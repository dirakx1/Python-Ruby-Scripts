#!/usr/local/bin/python

import imaplib
import sys

IMAPSERVER="xxxx.xxxx.com"
EMAIL=sys.argv[1]
PASSWORD=sys.argv[2]

#EMAIL="test@test.com"
#PASSWORD="testesttestesttest"



try:
        mail = imaplib.IMAP4_SSL(IMAPSERVER)
except:
        print "[ERROR] Network error while contacting IMAP server " + IMAPSERVER
        sys.exit()

try:
        mail.login(EMAIL, PASSWORD)
except:
        print "[ERROR] Login failed using " + EMAIL + " / " + PASSWORD + " (bad login/pass)"
        sys.exit()


try:
        mail.select("INBOX", readonly=1)
        retcode, messages = mail.search(None, '(UNSEEN)')
        if len(messages[0]) == 0:
                print "0"
        else:
                print len(messages[0].split(' '))
except:
        print "[ERROR] The INBOX folder does not exist in the mailbox " + EMAIL
        sys.exit()


mail.close()
