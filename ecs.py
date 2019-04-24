import dns
import clientsubnetoption

from requests import get
# from tracert import traceroute


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


# traceroute("v.qq.com")

# tracert:
# for youku: results changing over time, cannot access real server.
# for v.qq.com, iqiyi.com: works fine.

