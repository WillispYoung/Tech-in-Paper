import subprocess


def tracert(domain):
    p = subprocess.Popen("tracert " + domain, stdout=subprocess.PIPE, bufsize=1)
    count = 0
    res = []
    while True:
        line = p.stdout.readline()
        if not line:
            break
        # print(line)
        if count > 3:
            items = line.split()
            if len(items) < 3:  # last line is empty line
                break
            ip = items[-1]
            ip = ip.decode("UTF-8")
            if ip[0] == '[':    # in case domain name is represented
                ip = ip[1:-1]
            # print(ip)
            res.append(ip)
        count += 1
    return res


if __name__ == "__main__":
    tracert("apd-4ca339c635848992779008d33f0ee5a5.v.smtcdns.com")
