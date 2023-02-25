import os
import sys
import socket
from bottle import route, run, template

def getip():
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect(('8.8.8.8', 80))
    ip=sock.getsockname()[0]
    print(f'localip is {ip}')
    return ip

@route('/ping')
def ping():
  return "I am healthy!!"

@route('/hello/<name>')
def echo(name):
  return template('<b>Hello {{name}}</b>', name=name)

print(f'the script name is {sys.argv[0]}')
for i in range(1, len(sys.argv)):
  print(f'parameter {i} is {sys.argv[i]}')

IP_KEY=sys.argv[1]
PORT_KEY=sys.argv[2]

if __name__ == "__main__":
  ip=os.getenv(IP_KEY)
  port=os.getenv(PORT_KEY)
  if ip is None:
    ip=getip()

  if port is None:
    port=8080   

  print(f'ip address: {ip} and port: {port}')
  run(host=ip, port=port)
