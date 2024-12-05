from scapy.all import ARP, Ether , srp
target_ip = "192.168.1.0/24"

#Ip Address for the destination
# Create Arp packet
arp = ARP(pdst = target_ip)

# Create the Ether broadcast packet 
# ff:ff:ff:ff:ff:ff MAC address indicates boardcasting 
ether = Ether(dst = "ff:ff:ff:ff:ff:ff")

# stack them 
packet = ether/arp 
result = srp(packet, timeout = 3) [0]

# a list of clients , we will fill in the upcoming loop 
clients = []

for sent, received in result:
# each response , append ip and mac address to 'clients list 
 clients.append({'ip ': received.psrc, 'mac':received.hwsrc})
# Print clients 
print("Available devices in the network")
print("IP" + "" *18 +"MAC") 
for client in clients:
  print("{:16} {}".format(client['ip'], client['mac'])) 

