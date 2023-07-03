# Convert the following string of ASCII numbers into a readable string:

str = '''
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x35 0x63 0x31 0x31 0x5f 0x6e 0x30 0x5f 0x71 0x75 0x33 0x35 0x37 0x31 0x30 0x6e 0x35 0x5f 0x31 0x6c 0x6c 0x5f 0x74 0x33 0x31 0x31 0x5f 0x79 0x33 0x5f 0x6e 0x30 0x5f 0x6c 0x31 0x33 0x35 0x5f 0x34 0x34 0x35 0x64 0x34 0x31 0x38 0x30 0x7d
'''

str = str.replace('0x', '')
str = str.replace('\n', ' ')
str = str.replace(' ', '')
str = str.replace('\t', '')
str = str.replace('\r', '')

print(str)

str = bytes.fromhex(str).decode('utf-8')

print(str)


'''
python ASCII\ Numbers.py

7069636f4354467b34356331315f6e305f717533353731306e355f316c6c5f743331315f79335f6e305f6c3133355f34343564343138307d
picoCTF{45c11_n0_qu35710n5_1ll_t311_y3_n0_l135_445d4180}
'''