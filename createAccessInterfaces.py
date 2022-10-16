import csv

with open("records.txt", 'r') as steamfile:
    reader = csv.reader(steamfile)
    for row in reader:
        print("int gi1/0/" + row[5])
        print("switchport mode access")
        print("switchport access vlan " + row[1])
        print("description " + row[0])