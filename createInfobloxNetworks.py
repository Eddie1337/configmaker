import csv
infobloxMaster = "ns.event.nl.gameforce.gg"
cidr = "172.16."
with open("records.txt", 'r') as steamfile:
    reader = csv.reader(steamfile)
    for row in reader:
        network = cidr + row[1] + ".0"
        gateway = cidr + row[1] + ".1"
        print("network;" + network + ";255.255.255.0;;;;;;" + row [0]+ ";;;;" + infobloxMaster + ";False;;;;;;;;;False;False;;;;;;;False;default;;;;95;85;0;10;;"+ gateway +";;;;<empty>")