import dns.resolver

# # 1. dns
# reader = open("data/intersection-1.txt", "r")
# writer = open("data/dns-result.txt", "w")
#
# line = reader.readline()
# while line:
#     line = line.strip()
#     result = dns.resolver.query(line, 'A')
#     writer.write(line + " ")
#     for item in result:
#         writer.write(str(item) + " ")
#     writer.write("\n")
#     line = reader.readline()
#
# writer.close()

# 2. check difference
reader1 = open("data/dns-result-home.txt")
reader2 = open("data/dns-result-shenzhen.txt")
dict1 = dict2 = {}

line = reader1.readline()
while line:
    dict1[line.split()[0]] = line.split()[1]
    line = reader1.readline()

line = reader2.readline()
while line:
    dict2[line.split()[0]] = line.split()[1]
    line = reader2.readline()

count = 0
for k in dict1:
    print(dict1[k], dict2[k])
    if dict1[k] != dict2[k]:
        count += 1

print(count)

