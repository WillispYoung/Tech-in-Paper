import socket
import random
import struct
import time


def create_sender(ttl):
    s = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_DGRAM,
        proto=socket.IPPROTO_UDP
    )

    s.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
    return s


def create_receiver(port):
    s = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_RAW,
        proto=socket.IPPROTO_ICMP
    )

    timeout = struct.pack("ll", 5, 0)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)

    try:
        s.bind(('', port))
    except socket.error as e:
        print(e)
        raise IOError('Unable to bind receiver socket: {}'.format(e))

    return s


def traceroute(domain, hops=30):
    try:
        ip_addr = socket.gethostbyname(domain)
    except socket.error as e:
        raise IOError('Unable to resolve {}: {}', domain, e)

    text = 'traceroute to {} ({}), {} hops max'.format(domain, ip_addr, hops)
    print(text)

    ttl = 1
    lport = random.randint(33434, 33534)

    while True:
        start = time.time()
        receiver = create_receiver(lport)
        sender = create_sender(ttl)
        sender.sendto(b'', (ip_addr, lport))

        # data, addr = receiver.recvfrom(1024)
        addr = None
        try:
            data, addr = receiver.recvfrom(1024)
        except socket.error as e:
            print(e)
            pass
        finally:
            receiver.close()
            sender.close()

        end = time.time()
        if addr:
            time_cost = round((end - start) * 1000, 2)
            print('{:<4} {} {} ms'.format(ttl, addr[0], time_cost))
            if addr[0] == ip_addr:
                break
        else:
            print('{:<4} *'.format(ttl))

        ttl += 1

        if ttl > hops:
            break


if __name__ == "__main__":
    traceroute("v.qq.com")
