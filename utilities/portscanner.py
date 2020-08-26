#https://docs.python.org/3/howto/sockets.html

#!/usr/bin/python3
import socket
import sys
import subprocess
#Starts a TCP scan on a given IP address /24 range

def scanRange(network, startPort, endPort):
  open_ip_ports_map={}
  for j in range(256):
    ip=network+str(j)
    open_ports_list=tcp_scan(ip,1,30000)
    open_ip_ports_map[ip]=open_ports_list
  return open_ip_ports_map



#Creates a TCP socket and attempts to connect via supplied port
def tcp_scan(ip, startPort, endPort):
  print('scanning ip:',ip)
  # check if ip is reachable
  res = subprocess.call(['ping', '-c', '1', ip])
  if res == 0:
      print( "ping to", ip, "OK")
  elif res == 2:
      print("no response from", ip)
      return None
  else:
      print("ping to", ip, "failed!")
      return None
#scan for ports now
  open_ports_list=[]
  for port in range(startPort,endPort+1):
    print('scanning :', port)
    #asocket=socket(socket.AF_INET,socket.SOCK)
    asocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result=asocket.connect_ex((ip,port))
    if result == 0:
      open_ports_list.append(port)
  return open_ports_list


if __name__ == '__main__':
    # Timeout in seconds
    #socket.setdefaulttimeout(0.01)
    #scan
    #print(tcp_scan('192.168.1.71',0,2000))

    open_ip_ports_map=scanRange('192.168.1.',0,2000)
    f=open('ports.txt','w')
    for k,v in open_ip_ports_map:
      print('ip:', k, 'ports:', v)
      f.writelines(('ip:', str(k), '  ports:', str(v)))
    f.close()

