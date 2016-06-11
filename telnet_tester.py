import telnetlib

for i in range(1000, 10000):
    try:
        telnetlib.Telnet(host="10.159.162.253", port=str(i), timeout=0.3)
    except:
        pass
    else:
        print 'Port: ', i, ' Open'
