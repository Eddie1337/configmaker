import csv
cidr = "172.16."
infobloxMaster = "ns.event.nl.gameforce.gg""

with open("records.txt", 'r') as steamfile:
    reader = csv.reader(steamfile)
    for row in reader:
        description = row[0]
        network = cidr + row[1] + ".0"
        gateway = cidr + row[1] + ".1"
        start = cidr + row[1] + ".10"
        end = cidr + row[1] + ".250"
        print("dhcprange;" + end + ";;" + start + ";;False;;;;;;False;;False;;;;;False;False;;;;;;;;;;;" + infobloxMaster + ";;;;" + description + ";default;;;;;95;85;0;10;;;;MEMBER;;;")