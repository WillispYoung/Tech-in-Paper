"""
    This document servers as an implementation of Drongo Proposed in
    [Drongo: Speeding Up CDNs with Subnet Assimilation from the Client][CoNEXT'17].

    Author: Willisp Young
    StartDate: 2019-03-15

    For implementation of EDNS(0) ECS option, refer to
    https://github.com/opendns/dnspython-clientsubnetoption.
"""

import dns
import clientsubnetoption
from requests import get


def get_external_ip():
    return get('https://api.ipify.org').text


cso = clientsubnetoption.ClientSubnetOption(get_external_ip(), 24)

message = dns.message.make_query('baidu.com', 'A')
message.use_edns(options=[cso])
r = dns.query.udp(message, '8.8.8.8')

print(r)
print()

for option in r.options:
    if isinstance(option, clientsubnetoption.ClientSubnetOption):
        print(option)


# tracert:
# for youku: results changing over time, cannot access real server.
# for v.qq.com, iqiyi.com: works fine.
