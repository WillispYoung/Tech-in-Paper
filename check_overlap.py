reader1 = open("data/v.qq.com-domains-cloud203.txt")
reader2 = open("data/v.qq.com-domains-shenzhen.txt")
reader3 = open("data/v.qq.com-domains-home.txt")

list1 = list2 = list3 = []
line = reader1.readline()
while line:
    if line != "\n":
        list1.append(line.strip())
    line = reader1.readline()
# print(len(list1))

line = reader2.readline()
while line:
    if line != "\n":
        list2.append(line.strip())
    line = reader2.readline()
# print(len(list2))

line = reader3.readline()
while line:
    if line != "\n":
        list3.append(line.strip())
    line = reader3.readline()
# print(len(list3))

s1 = set(list1)
s2 = set(list2)
s3 = set(list3)

print(len(s1), len(s2), len(s3))

overlap1 = s1.intersection(s2)
print(len(overlap1))
for url in overlap1:
    print(url)

overlap2 = s2.intersection(s3)
print(len(overlap2))
for u in overlap2:
    print(u)

print(overlap1 == overlap2)

output = open("data/intersection-1.txt", "w")
for url in overlap2:
    output.write(url + "\n")
output.close()

