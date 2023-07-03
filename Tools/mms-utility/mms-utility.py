from colorama import init, Fore, Back, Style
from os import system, name
from time import sleep
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

init()

# https://manytools.org/hacker-tools/ascii-banner/
banner = ("""
 █████  █████  █████     ███  ████   ███   █████                     ██████                          █████████                                  █████            
░░███  ░░███  ░░███     ░░░  ░░███  ░░░   ░░███                     ███░░███                        ███░░░░░███                                ░░███             
 ░███   ░███  ███████   ████  ░███  ████  ███████   █████ ████     ░███ ░░░   ██████  ████████     ███     ░░░  ████████  █████ ████ ████████  ███████    ██████ 
 ░███   ░███ ░░░███░   ░░███  ░███ ░░███ ░░░███░   ░░███ ░███     ███████    ███░░███░░███░░███   ░███         ░░███░░███░░███ ░███ ░░███░░███░░░███░    ███░░███
 ░███   ░███   ░███     ░███  ░███  ░███   ░███     ░███ ░███    ░░░███░    ░███ ░███ ░███ ░░░    ░███          ░███ ░░░  ░███ ░███  ░███ ░███  ░███    ░███ ░███
 ░███   ░███   ░███ ███ ░███  ░███  ░███   ░███ ███ ░███ ░███      ░███     ░███ ░███ ░███        ░░███     ███ ░███      ░███ ░███  ░███ ░███  ░███ ███░███ ░███
 ░░████████    ░░█████  █████ █████ █████  ░░█████  ░░███████      █████    ░░██████  █████        ░░█████████  █████     ░░███████  ░███████   ░░█████ ░░██████ 
  ░░░░░░░░      ░░░░░  ░░░░░ ░░░░░ ░░░░░    ░░░░░    ░░░░░███     ░░░░░      ░░░░░░  ░░░░░          ░░░░░░░░░  ░░░░░       ░░░░░███  ░███░░░     ░░░░░   ░░░░░░  
                                                     ███ ░███                                                              ███ ░███  ░███                        
                                                    ░░██████                                                              ░░██████   █████                       
                                                     ░░░░░░                                                                ░░░░░░   ░░░░░                        
""")

print(Fore.RED + Style.BRIGHT + banner)
print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Welcome to the MMS Utility for Cryptography")

while True:
    print("Welcome to the MMS Utility for Cryptography")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Choose the method of encryption")
        print("1. Text to Morse Code")
        print("2. Text to Binary")
        print("3. Text to Octal")
        print("4. Text to Hexadecimal")
        print("5. Text to Base32")
        print("6. Text to Base64")
        print("7. Text to Caesar Cipher")
        print("8. Text to Affine Cipher")
        print("9. Text to ROT13 Cipher")
        print("10. Text to A1Z26 Cipher")
        print("11. Text to Vigenere Cipher")
        print("12. Text to Baconian Cipher")
        print("13. Text to Alphabetical Substitution Cipher")
        print("14. Text to Rail Fence Cipher")
        print("15. Text to Polybius Square Cipher")
        print("16. Text to ADFGVX Cipher")
        print("17. Text to Bifid Cipher")
        print("18. Text to Nihilist Cipher")
        print("19. Text to Tap Code")
        print("20. Text to Trifid Cipher")
        print("21. Text to HMAC")
        print("22. Text to SHA-1")
        print("23. Text to SHA-224")
        print("24. Text to SHA-256")
        print("25. Text to SHA-384")
        print("26. Text to SHA-512")
        print("27. Text to MD5")
        print("28. Text to MD4")
        print("29. Text to MD2")
        print("30. Text to RIPEMD-160")
        print("31. Text to RIPEMD-320")
        print("32. Text to Whirlpool")
        print("33. Text to GOST")
        print("34. Text to Keccak")
        print("35. Text to FNV")
        print("36. Text to Systematic Convolutional Code")
        print("37. Text to Hamming Code")
        print("38. Text to Reed-Solomon Code")
        print("39. Text to Huffman Code")
        print("40. Text to Arithmetic Code")
        print("41. Text to LZW")
        print("42. Text to Run Length Encoding")
        print("43. Text to Burrows-Wheeler Transform")
        print("44. Text to Atbash Cipher")

        choice = input("Enter your choice: ")

        if choice == '1':
            clear()
            print("Text to Morse Code")
            text = input("Enter the text: ")
            text = text.upper()
            morse_code = {'A':'.-', 'B':'-...', 
                'C':'-.-.', 'D':'-..', 'E':'.', 
                'F':'..-.', 'G':'--.', 'H':'....', 
                'I':'..', 'J':'.---', 'K':'-.-', 
                'L':'.-..', 'M':'--', 'N':'-.', 
                'O':'---', 'P':'.--.', 'Q':'--.-', 
                'R':'.-.', 'S':'...', 'T':'-', 
                'U':'..-', 'V':'...-', 'W':'.--', 
                'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                '1':'.----', '2':'..---', '3':'...--', 
                '4':'....-', '5':'.....', '6':'-....', 
                '7':'--...', '8':'---..', '9':'----.', 
                '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                '?':'..--..', '/':'-..-.', '-':'-....-', 
                '(':'-.--.', ')':'-.--.-', '!':'-.-.--', 
                '&':'.-...', ':': '---...', ';': '-.-.-.', 
                '=': '-...-', '+': '.-.-.', '_': '..--.-', 
                '"': '.-..-.', '$': '...-..-', '@': '.--.-.', 
                ' ':'/'}
            morse_code_text = ""

            for i in text:
                morse_code_text += morse_code[i] + " "

            print("The Morse Code is: " + morse_code_text)

        elif choice == '2':
            clear()
            print("Text to Binary")
            text = input("Enter the text: ")

            binary_text = ""

            for i in text:
                binary_text += bin(ord(i))[2:] + " "

            print("The Binary Code is: " + binary_text)

        elif choice == '3':
            clear()
            print("Text to Octal")
            text = input("Enter the text: ")

            octal_text = ""

            for i in text:
                octal_text += oct(ord(i))[2:] + " "

            print("The Octal Code is: " + octal_text)
        
        elif choice == '4':
            clear()
            print("Text to Hexadecimal")
            text = input("Enter the text: ")

            hexadecimal_text = ""

            for i in text:
                hexadecimal_text += hex(ord(i))[2:] + " "

            print("The Hexadecimal Code is: " + hexadecimal_text)

        elif choice == '5':
            clear()
            print("Text to Base32")
            text = input("Enter the text: ")

            base32_text = base64.b32encode(text.encode('ascii'))

            print("The Base32 Code is: " + base32_text.decode('ascii'))

        elif choice == '6':
            clear()
            print("Text to Base64")
            text = input("Enter the text: ")

            base64_text = base64.b64encode(text.encode('ascii'))

            print("The Base64 Code is: " + base64_text.decode('ascii'))

        elif choice == '7':
            clear()
            print("Text to Caesar Cipher")
            text = input("Enter the text: ")
            key = int(input("Enter the key: "))
            key = key % 26

            caesar_cipher_text = ""

            for i in text:
                if i.isupper():
                    caesar_cipher_text += chr((ord(i) + key - 65) % 26 + 65)
                elif i.islower():
                    caesar_cipher_text += chr((ord(i) + key - 97) % 26 + 97)
                else:
                    caesar_cipher_text += i

            print("The Caesar Cipher is: " + caesar_cipher_text)

        elif choice == '8':
            clear()
            print("Text to Affine Cipher")
            text = input("Enter the text: ")
            key1 = int(input("Enter the key1: "))
            key2 = int(input("Enter the key2: "))
            key1 = key1 % 26
            key2 = key2 % 26

            affine_cipher_text = ""

            for i in text:
                if i.isupper():
                    affine_cipher_text += chr(((ord(i) * key1) + key2 - 65) % 26 + 65)
                elif i.islower():
                    affine_cipher_text += chr(((ord(i) * key1) + key2 - 97) % 26 + 97)
                else:
                    affine_cipher_text += i

            print("The Affine Cipher is: " + affine_cipher_text)

        elif choice == '9':
            clear()
            print("Text to ROT13 Cipher")
            text = input("Enter the text: ")

            rot13_cipher_text = ""

            for i in text:
                if i.isupper():
                    rot13_cipher_text += chr((ord(i) + 13 - 65) % 26 + 65)
                elif i.islower():
                    rot13_cipher_text += chr((ord(i) + 13 - 97) % 26 + 97)
                else:
                    rot13_cipher_text += i

            print("The ROT13 Cipher is: " + rot13_cipher_text)

        elif choice == '10':
            clear()
            print("Text to A1Z26 Cipher")
            text = input("Enter the text: ")

            a1z26_cipher_text = ""

            for i in text:
                if i.isupper():
                    a1z26_cipher_text += str(ord(i) - 64) + "-"
                elif i.islower():
                    a1z26_cipher_text += str(ord(i) - 96) + "-"
                else:
                    a1z26_cipher_text += i

            print("The A1Z26 Cipher is: " + a1z26_cipher_text)

        elif choice == '11':
            clear()
            print("Text to Vigenere Cipher")
            text = input("Enter the text: ")

            vigenere_cipher_text = ""

            for i in text:
                if i.isupper():
                    vigenere_cipher_text += chr((ord(i) + 13 - 65) % 26 + 65)
                elif i.islower():
                    vigenere_cipher_text += chr((ord(i) + 13 - 97) % 26 + 97)
                else:
                    vigenere_cipher_text += i

            print("The Vigenere Cipher is: " + vigenere_cipher_text)

        elif choice == '12':
            clear()
            print("Text to Baconian Cipher")
            text = input("Enter the text: ")

            baconian_cipher_text = ""

            for i in text:
                if i.isupper():
                    baconian_cipher_text += baconian_cipher[i] + " "
                elif i.islower():
                    baconian_cipher_text += baconian_cipher[i.upper()] + " "
                else:
                    baconian_cipher_text += i

            print("The Baconian Cipher is: " + baconian_cipher_text)

        elif choice == '13':
            clear()
            print("Text to Alphabetical Substitution Cipher")
            text = input("Enter the text: ")

            alphabetical_substitution_cipher_text = ""
            
            for i in text:
                if i.isupper():
                    alphabetical_substitution_cipher_text += alphabetical_substitution_cipher[i] + " "
                elif i.islower():
                    alphabetical_substitution_cipher_text += alphabetical_substitution_cipher[i.upper()] + " "
                else:
                    alphabetical_substitution_cipher_text += i

            print("The Alphabetical Substitution Cipher is: " + alphabetical_substitution_cipher_text)

        elif choice == '14':
            clear()
            print("Text to Rail Fence Cipher")
            text = input("Enter the text: ")

            rail_fence_cipher_text = ""

            for i in range(2):
                for j in range(i, len(text), 2):
                    rail_fence_cipher_text += text[j]

            print("The Rail Fence Cipher is: " + rail_fence_cipher_text)

        elif choice == '15':
            clear()
            print("Text to Polybius Square Cipher")
            text = input("Enter the text: ")

            polybius_square_cipher_text = ""

            for i in text:
                if i.isupper():
                    polybius_square_cipher_text += polybius_square_cipher[i] + " "
                elif i.islower():
                    polybius_square_cipher_text += polybius_square_cipher[i.upper()] + " "
                else:
                    polybius_square_cipher_text += i

            print("The Polybius Square Cipher is: " + polybius_square_cipher_text)

        elif choice == '16':
            clear()
            print("Text to ADFGVX Cipher")
            text = input("Enter the text: ")

            adfgvx_cipher_text = ""

            for i in text:
                if i.isupper():
                    adfgvx_cipher_text += adfgvx_cipher[i] + " "
                elif i.islower():
                    adfgvx_cipher_text += adfgvx_cipher[i.upper()] + " "
                else:
                    adfgvx_cipher_text += i

            print("The ADFGVX Cipher is: " + adfgvx_cipher_text)

        elif choice == '17':
            clear()
            print("Text to Bifid Cipher")
            text = input("Enter the text: ")

            bifid_cipher_text = ""

            for i in text:
                if i.isupper():
                    bifid_cipher_text += bifid_cipher[i] + " "
                elif i.islower():
                    bifid_cipher_text += bifid_cipher[i.upper()] + " "
                else:
                    bifid_cipher_text += i

            print("The Bifid Cipher is: " + bifid_cipher_text)

        elif choice == '18':
            clear()
            print("Text to Nihilist Cipher")
            text = input("Enter the text: ")

            nihilist_cipher_text = ""

            for i in text:
                if i.isupper():
                    nihilist_cipher_text += nihilist_cipher[i] + " "
                elif i.islower():
                    nihilist_cipher_text += nihilist_cipher[i.upper()] + " "
                else:
                    nihilist_cipher_text += i

            print("The Nihilist Cipher is: " + nihilist_cipher_text)

        elif choice == '19':
            clear()
            print("Text to Tap Code")
            text = input("Enter the text: ")

            tap_code_text = ""

            for i in text:
                if i.isupper():
                    tap_code_text += tap_code[i] + " "
                elif i.islower():
                    tap_code_text += tap_code[i.upper()] + " "
                else:
                    tap_code_text += i

            print("The Tap Code is: " + tap_code_text)

        elif choice == '20':
            clear()
            print("Text to Trifid Cipher")
            text = input("Enter the text: ")

            trifid_cipher_text = ""

            for i in text:
                if i.isupper():
                    trifid_cipher_text += trifid_cipher[i] + " "
                elif i.islower():
                    trifid_cipher_text += trifid_cipher[i.upper()] + " "
                else:
                    trifid_cipher_text += i

            print("The Trifid Cipher is: " + trifid_cipher_text)

        elif choice == '21':
            clear()
            print("Text to HMAC")
            text = input("Enter the text: ")

            hmac_text = ""

            for i in text:
                if i.isupper():
                    hmac_text += hmac[i] + " "
                elif i.islower():
                    hmac_text += hmac[i.upper()] + " "
                else:
                    hmac_text += i

            print("The HMAC is: " + hmac_text)

        elif choice == '22':
            clear()
            print("Text to SHA-1")
            text = input("Enter the text: ")

            sha1_text = ""

            for i in text:
                if i.isupper():
                    sha1_text += sha1[i] + " "
                elif i.islower():
                    sha1_text += sha1[i.upper()] + " "
                else:
                    sha1_text += i

            print("The SHA-1 is: " + sha1_text)

        elif choice == '23':
            clear()
            print("Text to SHA-224")
            text = input("Enter the text: ")

            sha224_text = ""

            for i in text:
                if i.isupper():
                    sha224_text += sha224[i] + " "
                elif i.islower():
                    sha224_text += sha224[i.upper()] + " "
                else:
                    sha224_text += i

            print("The SHA-224 is: " + sha224_text)

        elif choice == '24':
            clear()
            print("Text to SHA-256")
            text = input("Enter the text: ")

            sha256_text = ""

            for i in text:
                if i.isupper():
                    sha256_text += sha256[i] + " "
                elif i.islower():
                    sha256_text += sha256[i.upper()] + " "
                else:
                    sha256_text += i

            print("The SHA-256 is: " + sha256_text)

        elif choice == '25':
            clear()
            print("Text to SHA-384")
            text = input("Enter the text: ")

            sha384_text = ""

            for i in text:
                if i.isupper():
                    sha384_text += sha384[i] + " "
                elif i.islower():
                    sha384_text += sha384[i.upper()] + " "
                else:
                    sha384_text += i

            print("The SHA-384 is: " + sha384_text)

        elif choice == '26':
            clear()
            print("Text to SHA-512")
            text = input("Enter the text: ")

            sha512_text = ""

            for i in text:
                if i.isupper():
                    sha512_text += sha512[i] + " "
                elif i.islower():
                    sha512_text += sha512[i.upper()] + " "
                else:
                    sha512_text += i

            print("The SHA-512 is: " + sha512_text)

        elif choice == '27':
            clear()
            print("Text to MD5")
            text = input("Enter the text: ")

            md5_text = ""

            for i in text:
                if i.isupper():
                    md5_text += md5[i] + " "
                elif i.islower():
                    md5_text += md5[i.upper()] + " "
                else:
                    md5_text += i

            print("The MD5 is: " + md5_text)

        elif choice == '28':
            clear()
            print("Text to MD4")
            text = input("Enter the text: ")

            md4_text = ""

            for i in text:
                if i.isupper():
                    md4_text += md4[i] + " "
                elif i.islower():
                    md4_text += md4[i.upper()] + " "
                else:
                    md4_text += i

            print("The MD4 is: " + md4_text)

        elif choice == '29':
            clear()
            print("Text to MD2")
            text = input("Enter the text: ")

            md2_text = ""

            for i in text:
                if i.isupper():
                    md2_text += md2[i] + " "
                elif i.islower():
                    md2_text += md2[i.upper()] + " "
                else:
                    md2_text += i

            print("The MD2 is: " + md2_text)

        elif choice == '30':
            clear()
            print("Text to RIPMD-160")
            text = input("Enter the text: ")

            ripmd160_text = ""

            for i in text:
                if i.isupper():
                    ripmd160_text += ripmd160[i] + " "
                elif i.islower():
                    ripmd160_text += ripmd160[i.upper()] + " "
                else:
                    ripmd160_text += i

            print("The RIPMD-160 is: " + ripmd160_text)

        elif choice == '31':
            clear()
            print("Text to RIPMD-320")
            text = input("Enter the text: ")

            ripmd320_text = ""

            for i in text:
                if i.isupper():
                    ripmd320_text += ripmd320[i] + " "
                elif i.islower():
                    ripmd320_text += ripmd320[i.upper()] + " "
                else:
                    ripmd320_text += i

            print("The RIPMD-320 is: " + ripmd320_text)

        elif choice == '32':
            clear()
            print("Text to Whirlpool")
            text = input("Enter the text: ")

            whirlpool_text = ""

            for i in text:
                if i.isupper():
                    whirlpool_text += whirlpool[i] + " "
                elif i.islower():
                    whirlpool_text += whirlpool[i.upper()] + " "
                else:
                    whirlpool_text += i

            print("The Whirlpool is: " + whirlpool_text)

        elif choice == '33':
            clear()
            print("Text to GOST")
            text = input("Enter the text: ")

            gost_text = ""

            for i in text:
                if i.isupper():
                    gost_text += gost[i] + " "
                elif i.islower():
                    gost_text += gost[i.upper()] + " "
                else:
                    gost_text += i

            print("The GOST is: " + gost_text)

        elif choice == '34':
            clear()
            print("Text to Keccak")
            text = input("Enter the text: ")

            keccak_text = ""

            for i in text:
                if i.isupper():
                    keccak_text += keccak[i] + " "
                elif i.islower():
                    keccak_text += keccak[i.upper()] + " "
                else:
                    keccak_text += i

            print("The Keccak is: " + keccak_text)

        elif choice == '35':
            clear()
            print("Text to FNV")
            text = input("Enter the text: ")

            fnv_text = ""

            for i in text:
                if i.isupper():
                    fnv_text += fnv[i] + " "
                elif i.islower():
                    fnv_text += fnv[i.upper()] + " "
                else:
                    fnv_text += i

            print("The FNV is: " + fnv_text)

        elif choice == '36':
            clear()
            print("Text to Systematic Convolutional Code")
            text = input("Enter the text: ")

            scc_text = ""

            for i in text:
                if i.isupper():
                    scc_text += scc[i] + " "
                elif i.islower():
                    scc_text += scc[i.upper()] + " "
                else:
                    scc_text += i

            print("The Systematic Convolutional Code is: " + scc_text)

        elif choice == '37':
            clear()
            print("Text to Hamming Code")
            text = input("Enter the text: ")

            hamming_text = ""

            for i in text:
                if i.isupper():
                    hamming_text += hamming[i] + " "
                elif i.islower():
                    hamming_text += hamming[i.upper()] + " "
                else:
                    hamming_text += i

            print("The Hamming Code is: " + hamming_text)

        elif choice == '38':
            clear()
            print("Text to Reed-Solomon Code")
            text = input("Enter the text: ")

            rs_text = ""

            for i in text:
                if i.isupper():
                    rs_text += rs[i] + " "
                elif i.islower():
                    rs_text += rs[i.upper()] + " "
                else:
                    rs_text += i

            print("The Reed-Solomon Code is: " + rs_text)

        elif choice == '39':
            clear()
            print("Text to Huffman Code")
            text = input("Enter the text: ")

            huffman_text = ""

            for i in text:
                if i.isupper():
                    huffman_text += huffman[i] + " "
                elif i.islower():
                    huffman_text += huffman[i.upper()] + " "
                else:
                    huffman_text += i

            print("The Huffman Code is: " + huffman_text)

        elif choice == '40':
            clear()
            print("Text to Arithmetic Coding")
            text = input("Enter the text: ")

            ac_text = ""

            for i in text:
                if i.isupper():
                    ac_text += ac[i] + " "
                elif i.islower():
                    ac_text += ac[i.upper()] + " "
                else:
                    ac_text += i

            print("The Arithmetic Coding is: " + ac_text)

        elif choice == '41':
            clear()
            print("Text to Lempel-Ziv-Welch")
            text = input("Enter the text: ")

            lzw_text = ""

            for i in text:
                if i.isupper():
                    lzw_text += lzw[i] + " "
                elif i.islower():
                    lzw_text += lzw[i.upper()] + " "
                else:
                    lzw_text += i

            print("The Lempel-Ziv-Welch is: " + lzw_text)

        elif choice == '42':
            clear()
            print("Text to Run-Length Encoding")
            text = input("Enter the text: ")

            rle_text = ""

            for i in text:
                if i.isupper():
                    rle_text += rle[i] + " "
                elif i.islower():
                    rle_text += rle[i.upper()] + " "
                else:
                    rle_text += i

            print("The Run-Length Encoding is: " + rle_text)

        elif choice == '43':
            clear()
            print("Text to Burrows-Wheeler Transform")
            text = input("Enter the text: ")

            bwt_text = ""

            for i in text:
                if i.isupper():
                    bwt_text += bwt[i] + " "
                elif i.islower():
                    bwt_text += bwt[i.upper()] + " "
                else:
                    bwt_text += i

            print("The Burrows-Wheeler Transform is: " + bwt_text)

        elif choice == '44':
            clear()
            print("Text to Atbash Cipher")
            text = input("Enter the text: ")

            atbash_text = ""

            for i in text:
                if i.isupper():
                    atbash_text += atbash[i] + " "
                elif i.islower():
                    atbash_text += atbash[i.upper()] + " "
                else:
                    atbash_text += i

            print("The Atbash Cipher is: " + atbash_text)

    elif choice == '2':
        print("Choose the method of decryption")
        print("1. Morse Code to Text")
        print("2. Binary to Text")
        print("3. Octal to Text")
        print("4. Hexadecimal to Text")
        print("5. Base32 to Text")
        print("6. Base64 to Text")
        print("7. Caesar Cipher to Text")
        print("8. Affine Cipher to Text")
        print("9. ROT13 Cipher to Text")
        print("10. A1Z26 Cipher to Text")
        print("11. Vigenere Cipher to Text")
        print("12. Baconian Cipher to Text")
        print("13. Alphabetical Substitution Cipher to Text")
        print("14. Rail Fence Cipher to Text")
        print("15. Polybius Square Cipher to Text")
        print("16. ADFGVX Cipher to Text")
        print("17. Bifid Cipher to Text")
        print("18. Nihilist Cipher to Text")
        print("19. Tap Code to Text")
        print("20. Trifid Cipher to Text")
        print("21. HMAC to Text")
        print("22. SHA-1 to Text")
        print("23. SHA-224 to Text")
        print("24. SHA-256 to Text")
        print("25. SHA-384 to Text")
        print("26. SHA-512 to Text")
        print("27. MD5 to Text")
        print("28. MD4 to Text")
        print("29. MD2 to Text")
        print("30. RIPEMD-160 to Text")
        print("31. RIPEMD-320 to Text")
        print("32. Whirlpool to Text")
        print("33. GOST to Text")
        print("34. Keccak to Text")
        print("35. FNV to Text")
        print("36. Systematic Convolutional Code to Text")
        print("37. Hamming Code to Text")
        print("38. Reed-Solomon Code to Text")
        print("39. Huffman Code to Text")
        print("40. Arithmetic Code to Text")
        print("41. LZW to Text")
        print("42. Run Length Encoding to Text")
        print("43. Burrows-Wheeler Transform to Text")

        choice = input("Enter your choice: ")

        if choice == '1':
            clear()
            print("Morse Code to Text")
            text = input("Enter the Morse Code: ")
            text = text.upper()
            morse_code = {'.-':'A', '-...':'B', 
                '-.-.':'C', '-..':'D', '.':'E', 
                '..-.':'F', '--.':'G', '....':'H', 
                '..':'I', '.---':'J', '-.-':'K', 
                '.-..':'L', '--':'M', '-.':'N', 
                '---':'O', '.--.':'P', '--.-':'Q', 
                '.-.':'R', '...':'S', '-':'T', 
                '..-':'U', '...-':'V', '.--':'W', 
                '-..-':'X', '-.--':'Y', '--..':'Z', 
                '.----':'1', '..---':'2', '...--':'3', 
                '....-':'4', '.....':'5', '-....':'6', 
                '--...':'7', '---..':'8', '----.':'9', 
                '-----':'0', '--..--':', ', '.-.-.-':'.', 
                '..--..':'?', '-..-.':'/', '-....-':'-', 
                '-.--.':'(', '-.--.-':')', '-.-.--':'!', 
                '.-...':'&', '---...':':', '-.-.-.':';', 
                '-...-':'=', '.-.-.':'+', '.-..-.':'"', 
                '...-..-':'$', '.--.-.':'@', '/':' '}

            morse_code_text = ""
            morse_code_word = text.split(" / ")

            for i in morse_code_word:
                morse_code_letter = i.split(" ")
                for j in morse_code_letter:
                    morse_code_text += morse_code[j]
                morse_code_text += " "

            print("The Text is: " + morse_code_text)

        elif choice == '2':
            clear()
            print("Binary to Text")
            text = input("Enter the Binary Code: ")

            binary_text = ""
            binary_word = text.split(" ")

            for i in binary_word:
                binary_text += chr(int(i, 2))

            print("The Text is: " + binary_text)

        elif choice == '3':
            clear()
            print("Octal to Text")
            text = input("Enter the Octal Code: ")

            octal_text = ""
            octal_word = text.split(" ")

            for i in octal_word:
                octal_text += chr(int(i, 8))

            print("The Text is: " + octal_text)

        elif choice == '4':
            clear()
            print("Hexadecimal to Text")
            text = input("Enter the Hexadecimal Code: ")

            hexadecimal_text = ""
            hexadecimal_text = bytearray.fromhex(text).decode()

            print("The Text is: " + hexadecimal_text)

        elif choice == '5':
            clear()
            print("Base32 to Text")
            text = input("Enter the Base32 Code: ")

            base32_text = ""
            base32_text = base64.b32decode(text).decode()

            print("The Text is: " + base32_text)

        elif choice == '6':
            clear()
            print("Base64 to Text")
            text = input("Enter the Base64 Code: ")

            base64_text = ""
            base64_text = base64.b64decode(text).decode()

            print("The Text is: " + base64_text)

        elif choice == '7':
            clear()
            print("Caesar Cipher to Text")
            text = input("Enter the Caesar Cipher: ")

            caesar_text = ""
            caesar_word = text.split(" ")

            for i in caesar_word:
                caesar_text += chr(int(i) + 97)

            print("The Text is: " + caesar_text)

        elif choice == '8':
            clear()
            print("Affine Cipher to Text")
            text = input("Enter the Affine Cipher: ")

            affine_text = ""

            for i in text:
                if i == ' ':
                    affine_text += ' '
                else:
                    affine_text += chr((int(i) - 1) % 26 + 97)

            print("The Text is: " + affine_text)

        elif choice == '9':
            clear()
            print("ROT13 Cipher to Text")
            text = input("Enter the ROT13 Cipher: ")

            rot13_text = ""

            for i in text:
                if i == ' ':
                    rot13_text += ' '
                else:
                    rot13_text += chr((int(i) - 1) % 26 + 97)

            print("The Text is: " + rot13_text)

        elif choice == '10':
            clear()
            print("A1Z26 Cipher to Text")
            text = input("Enter the A1Z26 Cipher: ")

            a1z26_text = ""
            a1z26_word = text.split(" ")

            for i in a1z26_word:
                a1z26_text += chr(int(i) + 96)

            print("The Text is: " + a1z26_text)

        elif choice == '11':
            clear()
            print("Vigenere Cipher to Text")
            text = input("Enter the Vigenere Cipher: ")

            vigenere_text = ""
            vigenere_word = text.split(" ")

            for i in vigenere_word:
                vigenere_text += chr(int(i) + 96)

            print("The Text is: " + vigenere_text)

        elif choice == '12':
            clear()
            print("Baconian Cipher to Text")
            text = input("Enter the Baconian Cipher: ")

            baconian_text = ""
            baconian_word = text.split(" ")

            for i in baconian_word:
                baconian_text += chr(int(i) + 96)

            print("The Text is: " + baconian_text)

        elif choice == '13':
            clear()
            print("Alphabetical Substitution Cipher to Text")
            text = input("Enter the Alphabetical Substitution Cipher: ")

            alphabetical_substitution_text = ""

            for i in text:
                if i == ' ':
                    alphabetical_substitution_text += ' '
                else:
                    alphabetical_substitution_text += chr((int(i) - 1) % 26 + 97)

            print("The Text is: " + alphabetical_substitution_text)

        elif choice == '14':
            clear()
            print("Rail Fence Cipher to Text")
            text = input("Enter the Rail Fence Cipher: ")

            rail_fence_text = ""

            for i in text:
                if i == ' ':
                    rail_fence_text += ' '
                else:
                    rail_fence_text += chr((int(i) - 1) % 26 + 97)

            print("The Text is: " + rail_fence_text)

        elif choice == '15':
            clear()
            print("Polybius Square Cipher to Text")
            text = input("Enter the Polybius Square Cipher: ")

            polybius_square_text = ""

            for i in text:
                if i == ' ':
                    polybius_square_text += ' '
                else:
                    polybius_square_text += chr((int(i) - 1) % 26 + 97)

            print("The Text is: " + polybius_square_text)

        elif choice == '16':
            clear()
            print("ADFGVX Cipher to Text")
            text = input("Enter the ADFGVX Cipher: ")

            adfgvx_text = ""

            for i in text:
                if i == ' ':
                    adfgvx_text += ' '
                else:
                    adfgvx_text += chr((int(i) - 1) % 26 + 97)

            print("The Text is: " + adfgvx_text)

        elif choice == '17':
            clear()
            print("Bifid Cipher to Text")
            text = input("Enter the Bifid Cipher: ")

            bifid_text = ""

            for i in text:
                if i == ' ':
                    bifid_text += ' '
                else:
                    bifid_text += chr((int(i) - 1) % 26 + 97)

            print("The Text is: " + bifid_text)

        elif choice == '18':
            clear()
    else:
        clear()
        exit("Thank you for using MMS Utility for Cryptography")