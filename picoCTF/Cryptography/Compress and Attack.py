from pwn import *
import string

def get_min_args(zlib_oracle):
    srtd_oracle = sorted(zlib_oracle, key=lambda i: zlib_oracle[i])
    min_value = zlib_oracle[srtd_oracle[0]]
    min_args = []
    for arg in srtd_oracle:
        if zlib_oracle[arg] == min_value:
            min_args.append(arg)
        else:
            break
    return min_args

if __name__ == "__main__":
    # r = process(argv=["python", "compress_and_attack.py"])
    r = remote("mercury.picoctf.net", 29858)
    alphabet = string.ascii_letters + string.digits + "_}"
    base = ["picoCTF{"]
    found = False    
    while not found:
        zlib_oracle = {}
        for partial in base:
            for char in alphabet:
                try:
                    print(r.recvuntil("encrypted: ").decode(), end="")
                    payload = partial + char
                    r.sendline(payload)
                    print(payload)
                    r.recvline()
                    r.recvline()
                    val = int(r.recvline().decode()[:-1])
                    zlib_oracle[payload] = val
                except:
                    # server closes the connection after some time
                    r = remote("mercury.picoctf.net", 50899)
        base = get_min_args(zlib_oracle)
        if len(base) == 1 and base[0][-1] == '}':
            found = True
            r.close()
    print("Flag found: {}".format(base[0]))