import socket
try:
    #creating socket
    s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #dgram__datagram
    print("socket created")
    ip_add="172.16.3.13"
    port=8888
    target_add=(ip_add,port)
    message=input("entrer the message: 😊")
    encoded_msg= message.encode("ascii")
    s.sendto(encoded_msg,target_add)
    print("message sent sucessfully")
    s.close()
except Exception as e:
    print("an error come",e)
