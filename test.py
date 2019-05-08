from ecs import edns
from ping3 import ping

hops = []
domains = []
content = open("data/traces-cloud203.txt", "r")

count = 0
line = content.readline()
while line:
    domains.append(line.strip())
    line = content.readline()
    hops.append([])
    while len(line) > 10:
        ip = line.split()[-1]
        if ip.startswith('['):
            ip = ip[1:-1]
        hops[count].append(ip)
        line = content.readline()

    line = content.readline()
    count += 1

print(domains)

for i in range(len(hops)):
    for ip in hops[i]:
        print(ip)
        res, _ = edns(domains[i], 24, ip)
        print(res)
    print()

