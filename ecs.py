import dns
import clientsubnetoption

from requests import get


def get_external_ip():
    return get('https://api.ipify.org').text


def edns(domain, scope, subnet=None):
    if subnet:
        cso = clientsubnetoption.ClientSubnetOption(subnet, scope)
    else:
        cso = clientsubnetoption.ClientSubnetOption(get_external_ip(), scope)

    message = dns.message.make_query(domain, 'A')
    message.use_edns(options=[cso])
    response = dns.query.udp(message, "192.168.1.1")

    res = []
    # print(type(response.answer), len(response.answer))
    for entry in response.answer:
        items = entry.to_text().split("\n")
        for item in items:
            item = item.split()[-1]
            res.append(item)
        # print(item.to_text(), type(item.to_text()))

    support = None
    for option in response.options:
        if isinstance(option, clientsubnetoption.ClientSubnetOption):
            support = option.__repr__().split("(")[-1][:-1].split(",")

    return res, support


if __name__ == "__main__":
    a, b = edns("apd-82cb731adc411313ffef07c4a1729a0f.v.smtcdns.com", 24)
    print(a)
    print(b)
