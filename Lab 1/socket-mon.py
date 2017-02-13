import psutil

numberOfConnections = {}
connectionDetails = []

for connection in psutil.net_connections("tcp"):
        if connection.raddr and connection.laddr:
            raddr =  "%s@%s" % (connection.raddr)
            laddr =  "%s@%s" % (connection.laddr)
            connectionDetails.append({"pid":connection.pid,"laddr":laddr,"raddr":raddr,"status":connection.status})
            numberOfConnections[connection.pid] = numberOfConnections[connection.pid]+1 if connection.pid in numberOfConnections else 1

connectionsSortedByCount = [(value,key) for key,value in numberOfConnections.items()]
connectionsSortedByCount.sort()

print '"pid","laddr","raddr","status"'
for value,key in connectionsSortedByCount:
    for connection in connectionDetails:
        if(key==connection["pid"]):
            print('"%d","%s","%s","%s"' % (key,connection["raddr"],connection["laddr"],connection["status"] ))