import csv
dhcpserver = "172.16.254.10"
with open("records.txt", 'r') as steamfile:
    reader = csv.reader(steamfile)
    for row in reader:
        print("int vlan" + row[1])
        print("description " + row[0])
        print("ip addr 172.16." + row[1]+ ".1/24")
        print("no shut")
        print("ip dhcp relay address " + dhcpserver)