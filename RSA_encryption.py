import random
import math


def is_prime(p):
    if p==2:
        #print("Prime")
        return True
    elif p%2 and p>2:
        #print("Not Prime")
        return False

    for i in range(3,int(math.sqrt(p)),2):  # as all the even numbers other than 2 are not prime
        if p%i==0:
            #print("Not Prime")
            return False
    #print("Prime")
    return True


def gcd(a,b):  # Using Euclidian Algo
    if a==0:
        return (b,0,1)
    else:
        g,y,x = gcd(b%a,a)
        return (g,x-(b//a)*y,y)


def modular_inverse(a,phi):  # Using extended Euclidian Algo
    g,x,y = gcd(a,phi)

    return x%phi


def rsa_encrypt(plain_text, p,q):
    # Choose p,q <-- Problem

    n=p*q
    phi = (p-1)*(q-1)

    a = random.randint(0,phi-1)
    b=modular_inverse(a,phi)

    cipher_text = (plain_text**a)%n
    return cipher_text


def rsa_decrypt(cipher_text,b,n):

    plain_text = (cipher_text**b)%n
    return plain_text













