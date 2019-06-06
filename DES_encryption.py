import math
import numpy as np

# 64bit initial permutation
IPtable = (58,50,42,34,26,18,10,2,
           60,52,44,36,28,20,12,4,
           62,54,46,38,30,22,14,6,
           64,56,48,40,32,24,16,8,
           57,49,41,33,25,17,9,1,
           59,51,43,35,27,19,11,3,
           61,53,45,37,29,21,13,5,
           63,55, 47,39,31,23,15,7)

# 64bit inverse initial permutation
IIPtable = (40,8,48,16,56,24,64,32,
            39,7,47,15,55,23,63,31,
            38,6,46,14,54,22,62,30,
            37,5,45,13,53,21,61,29,
            36,4,44,12,52,20,60,28,
            35,3,43,11,51,19,59,27,
            34,2,42,10,50,18,58,26,
            33,1,41,9,49,17,57,25)

# 48bit key permutation
P1table = (32,1,2,3,4,5,
           4,5,6,7,8,9,
           8,9,10,11,12,13,
           12,13,14,15,16,17,
           16,17,18,19,20,21,
           20,21,22,23,24,25,
           24,25,26,27,28,29,
           28,29,30,31,32,1)

# 32bit SBOX output permutation
P2table = (16,7,20,21,29,12,28,17,
           1,15,23,26,5,18,31,10,
           2,8,24,14,32,27,3,9,
           19,13,30,6,22,11,4,25)

# 48bit key final_permutation
Ftable = (14,17,11,24,1,5,3,28,
          15,6,21,10,23,19,12,4,
          26,8,16,7,27,20,13,2,
          41,52,31,37,47,55,30,40,
          51,45,33,48,44,49,39,56,
          34,53,46,42,50,36,29,32)

# Left Shift
Fshift = (1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1)

# Initialization Vector
IVec = '0000000000000000000000000000000000000000000000000000000000000000'

# SBOX
sbox = 8 * [64 * [0]]

sbox[0] = (14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
           0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
           4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
           15,12,8,2,4,9,1,7,5,11,13,14,10,0,6,3)

sbox[1] = (15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
           3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
           0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
           13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9)

sbox[2] = (10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
           13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
           13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
           1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12)

sbox[3] = (7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
           13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
           10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
           3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14)

sbox[4] = (2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
           14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
           4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
           11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3)

sbox[5] = (12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
           10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
           9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
           4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13)

sbox[6] = (4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
           13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
           1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
           6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12)

sbox[7] = (13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
           1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
           7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
           2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11)


def initial_permutation(input_text):
    ip = IPtable
    permuted_text = [0]*64

    for i in range(64):
        permuted_text[i] = input_text[ip[i]-1]
    print(permuted_text)

    return permuted_text


def inverse_initial_permutation(input_text):
    iip = IIPtable
    permuted_text = [0] * 64

    for i in range(64):
        permuted_text[i] = input_text[iip[i]-1]

    return permuted_text


def s_box(input_text):
    permuted_text = ""

    for i in range(8):
        tmp = input_text[i*6:i*6+6]
        tmp = ''.join(tmp)
        value = sbox[i][int(tmp, 2)]
        val1 = "{0:{fill}4b}".format(value, fill='0')
        permuted_text += val1

    return permuted_text


def f1_permutation1(input_text):
    f1_p1 = P1table
    permuted_text = [0] * 48

    for i in range(48):
        permuted_text[i] = input_text[f1_p1[i]-1]

    return permuted_text


def f1_permutaion2(input_text):
    f1_p2 = P2table
    permuted_text = [0] * 32

    for i in range(32):
        permuted_text[i] = input_text[f1_p2[i]-1]

    return permuted_text


def f2_shift(key, iteration):
    key_l = key[:28]
    key_r = key[28:]
    after_f2_r = [0] * 28
    after_f2_l = [0] * 28
    f2 = Fshift

    for i in range(1, 28):
        after_f2_r[i] = key_l[i - f2[iteration]]
        after_f2_l[i] = key_r[i - f2[iteration]]

    after_f2_l[0] = key_l[27-f2[iteration]]
    after_f2_r[0] = key_r[27-f2[iteration]]

    key1 = after_f2_l + after_f2_r

    return key1


def f3(input_text):

    permuted_text = [0] * 48

    for i in range(48):
        permuted_text[i] = input_text[Ftable[i]-1]
    return permuted_text


# def initial_key_permutation(input_text):
#     initial_key_p = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
#
#     permuted_text = [0] * 56
#
#     for i in range(56):
#         permuted_text[i] = input_text[initial_key_p[i]-1]
#     return permuted_text


def block_cipher_encryption(input_text, key,iteration):

    input_text_l = input_text[:32]
    input_text_r = input_text[32:]

    cipher_text_l = input_text_r
    text1 = f1_permutation1(input_text_r)

    # key1 comes from f2
    key2 = f3(key)
    skey2 = ''.join(key2)

    stext1 = ''.join(text1)
    text2 = '{1:0{0}b}'.format(len(skey2), int(skey2, 2) ^ int(stext1, 2))
    text2 = list(text2)
    text3 = s_box(text2)  # from s box
    text4 = f1_permutaion2(text3)

    input_text_l=''.join(input_text_l)
    text4 = ''.join(text4)

    cipher_text_r = '{1:0{0}b}'.format(len(input_text_l), int(input_text_l, 2) ^ int(text4, 2))
    cipher_text = cipher_text_l + cipher_text_r

    return cipher_text


def block_cipher_decryption(input_text, key,iteration):

    input_text_l = input_text[:32]
    input_text_r = input_text[32:]

    plain_text_r = input_text_l

    text1 = f1_permutation1(input_text_l)

    # key1 comes from f2
    key2 = f3(key)
    skey2 = ''.join(key2)

    stext1 = ''.join(text1)
    text2 = '{1:0{0}b}'.format(len(skey2), int(skey2, 2) ^ int(stext1, 2))
    text2 = list(text2)
    text3 = s_box(text2)  # from s box
    text4 = f1_permutaion2(text3)

    input_text_l=''.join(input_text_l)
    text4 = ''.join(text4)

    plain_text_l = '{1:0{0}b}'.format(len(input_text_r), int(input_text_r, 2) ^ int(text4, 2))
    plain_text = plain_text_l + plain_text_r

    return plain_text

l = '1010101010101010101010101010101010101010101010101010101010101010'
k = '1111111111111111111111111111111111111111111111111111110'


#block_cipher_decryption(block_cipher_encryption(l,k,1),k,1)


def des_16rounds_encryption(input_text,key):

    for i in range(16):
        key = f2_shift(key, i)

        input_text = block_cipher_encryption(input_text,key,i)

    return input_text


def des_16rounds_decryption(input_text,key):
    key_list = []
    k1 = key

    for i in range(16):

        k1=f2_shift(k1, i)
        key_list.append(k1)

    for i in range(16):
        input_text = block_cipher_decryption(input_text,key_list[15-i],i)

    return input_text


padding = 0
def cbc_encryption(input_text,key):
    msg = ""
    alternate = IVec

    split_list = [input_text[i:i + 64] for i in range(0, len(input_text), 64)]

    for i in range(len(split_list)):
        global padding
        inp = split_list[i]

        if i == len(split_list)-1:
            inp = list(split_list[i])
            z = len(inp) % 64
            padding = 64-z
            if z!=0:
                inp = ''.join(inp)
                for i in range(64-z):
                    inp+='0'

        inp = ''.join(inp)
        inp = '{1:0{0}b}'.format(len(inp), int(inp, 2) ^ int(alternate, 2))

        v=des_16rounds_encryption(inp,key)
        msg+=v
        alternate = v

    return msg


def cbc_decryption(input_text,key):
    global padding

    msg = ""
    alternate = IVec

    split_list = [input_text[i:i + 64] for i in range(0, len(input_text), 64)]

    for i in range(len(split_list)):
        inp = split_list[i]

        v=des_16rounds_decryption(inp,key)
        v = '{1:0{0}b}'.format(len(v), int(v, 2) ^ int(alternate, 2))

        alternate = split_list[i]
        msg+=v

    lm = len(msg)
    msg = msg[:lm-padding]

    return msg

# Read the message from a text file and encrypt it using DES Algorithm and write it to a text file

file = open("input.txt","r")
m=file.readline()

# Use any 64-bit key
# k = '0000110000110010001011100101001100111101011110000110101011100011'

y=cbc_encryption(m,k)
print("Encrypted message: "+y)
z = cbc_decryption(y,k)
print("Decrypted message: "+z)

file = open("output.txt","w")
file.write(y)








