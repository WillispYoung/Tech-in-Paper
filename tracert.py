import sys
import socket
import struct
import time
import random

# constants for use in making and receiving ICMP messages
ICMP_REQUEST_TYPE = 8
ICMP_REPLY_TYPE = 0
ICMP_CODE = 0


def to_digit(value):
    """ Converts a value to be numeric
    :param value: the value to be converted to a number
    :return: the value itself it is already a number, else the
            numeric form of the value
    """
    if isinstance(value, int):
        return value

    return ord(value)


def checksum(source):
    """ Calculates a checksum for source to be used in network communications
    :param source: the input to calculate the checksum for
    :return: the calculated checksum
    """
    checksum_return = 0
    length = len(source)

    for char in range(0, length, 2):
        if char + 1 == length:
            checksum_return += to_digit(source[char])
            break
        checksum_return += (to_digit(source[char + 1]) << 8) + to_digit(source[char])

    checksum_return = (checksum_return >> 16) + (checksum_return & 0xffff)
    checksum_return += (checksum_return >> 16)
    checksum_return = ~checksum_return

    return checksum_return & 0xffff


def create_sender(ttl):
    s = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_DGRAM,
        proto=socket.IPPROTO_UDP
    )

    s.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

    return s


def create_receiver(port):
    rx = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    rx.settimeout(5)
    rx.bind(('', port))
    return rx


def traceroute(destination, max_hops=30):
    ttl = 1
    hops = []
    target_ip = socket.gethostbyname(destination)

    while ttl < max_hops:
        # sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
        # sock.settimeout(timeout)
        # sock.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        port = random.randint(33333, 55555)
        # sock.bind(("", port))
        receiver = create_receiver(port)
        sender = create_sender(ttl)
        sender.sendto(b'', (target_ip, port))

        address = None
        try:
            _, address = receiver.recvfrom(1024)
        except socket.error as e:
            print(e)
        finally:
            # sock.close()
            receiver.close()
            sender.close()

        if address:
            print(address[0])
            hops.append(address[0])
            if address[0] == target_ip:
                break

        ttl += 1

    return hops


if __name__ == "__main__":
    hops = traceroute("baidu.com")
