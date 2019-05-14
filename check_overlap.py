reader1 = open("data/v.qq.com-domains-cloud203.txt")
reader2 = open("data/v.qq.com-domains-shenzhen.txt")

list1 = list2 = []
line = reader1.readline()
while line:
    if line != "\n":
        list1.append(line.strip())
    line = reader1.readline()
print(len(list1))

line = reader2.readline()
while line:
    if line != "\n":
        list2.append(line.strip())
    line = reader2.readline()
print(len(list2))

overlap = set(list1).intersection(set(list2))
print(len(overlap))
for url in overlap:
    print(url)
