import dns.resolver
from ping3 import ping
from geoip2 import database

res = dns.resolver.query("valipl.cp31.ott.cibntv.net")
for ip in res:
    ip = str(ip)
    delay = ping(ip) * 1000
    print(ip, delay)

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

# # 2. check difference
# reader1 = open("data/dns-result-home.txt")
# reader2 = open("data/dns-result-shenzhen.txt")
# dict1 = dict2 = {}
#
# line = reader1.readline()
# while line:
#     dict1[line.split()[0]] = line.split()[1]
#     line = reader1.readline()
#
# line = reader2.readline()
# while line:
#     dict2[line.split()[0]] = line.split()[1]
#     line = reader2.readline()
#
# count = 0
# for k in dict1:
#     print(dict1[k], dict2[k])
#     if dict1[k] != dict2[k]:
#         count += 1
#
# print(count)

# 3. measure CDN quality
# reader = open("data/youku-dns-result-home.txt")
# line = reader.readline()
#
# while line:
#     ip = line.strip()
#     res = ping(ip)
#     print(res * 1000)
#     line = reader.readline()

# # 4. get location of IP address
# reader = database.Reader("C:/Python/GeoLite2-City.mmdb")
# data = open("data/dns-result-home.txt")
# line = data.readline()
#
# bj_list = []
# sz_list = []
# bj = open("beijing.txt", "w")
# sz = open("shenzhen.txt", "w")
#
# while line:
#     ip = line.strip().split()[1]
#     res = reader.city(ip)
#     if res.city.name:
#         # print(res.city.name)
#         if res.city.name == "Beijing":
#             bj.write(ip + "\n")
#             bj_list.append(ip)
#         elif res.city.name == "Shenzhen":
#             sz.write(ip + "\n")
#             sz_list.append(ip)
#     elif res.subdivisions.most_specific.name:
#         # print(res.subdivisions.most_specific.name)
#         if res.subdivisions.most_specific.name == "Beijing":
#             bj_list.append(ip)
#             bj.write(ip + "\n")
#         elif res.subdivisions.most_specific.name == "Shenzhen":
#             sz_list.append(ip)
#             sz.write(ip + "\n")
#     else:
#         # print(res.country.name)
#         pass
#     line = data.readline()
#
# for ip in bj_list:
#     print(ping(ip) * 1000)
#
# print()
#
# for ip in sz_list:
#     print(ping(ip) * 1000)
