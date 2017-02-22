import socket
import sys

IS_SECOND_CONSOLE = False
if len(sys.argv) > 0:
    if "-SecondConsole" in sys.argv:
        IS_SECOND_CONSOLE = True

def InitializeHost(port=50007):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    return s.accept()[0]

def InitializeClient(ipAddress='127.0.0.1',port=50007):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ipAddress, port))
    return s

def Wait(connection, message=' '):
    while 1:
        data = connection.recv(1024)
        if not data: break
        connection.sendall(data)

def Send(connection, message):
    connection.sendall(message)
    data = connection.recv(1024)
    return str(data)

def Step1():
    print "Hello Step 1!"

def Step2(s):
    lbCheckResult = True
    print "This is step 2."
    Send(s, str(lbCheckResult))

def Step3():
    print "This is the third step."

def Step4():
    print "This is the last step"

if IS_SECOND_CONSOLE:
    s = InitializeHost()
    Wait(s)
    Step2(s)
    #Wait(s)
    Step4()
    s.close()
else:
    s = InitializeClient()
    Step1()
    Send(s,'2')
    Step3()
    Wait(s,'4')
    s.close()
