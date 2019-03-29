"""
    This document servers as an implementation of Drongo Proposed in
    [Drongo: Speeding Up CDNs with Subnet Assimilation from the Client][CoNEXT'17].

    Author: Willisp Young
    StartDate: 2019-03-15
"""

import dns.resolver

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8', '8.8.4.4']

answers = resolver.query("google.com", "A")
for data in answers:
    print data

# baidu.com [with/without nameserver; China/Singapore]
# 220.181.57.216 (Beijing, Haidian District)
# 123.125.115.110 (Beijing, Xicheng District)

# google.com
# Singapore [without nameserver]
# 172.217.194.100 (Virginia)
# 172.217.194.138 (Singapore)
# 172.217.194.113
# 172.217.194.101
# 172.217.194.102
# 172.217.194.139
# China [without nameserver]
# 6.6.6.6 (fake)
# China [with nameserver]
# 172.217.161.174 (HK)
