import math

def gcdExtended_rec(a, b):
    if a == 0 : 
        return b,0,1
             
    gcd,x1,y1 = gcdExtended_rec(b%a, a) 
     
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y 

def gdcExtended(e, phi):
    (gcd, x, y) = gcdExtended_rec(e, phi)
    if gcd != 1:
        return None
    return x % phi

def primeFactors(n):
    limit = math.floor(math.sqrt(n))
    if n % 2 == 0:
        return (2, n // 2)

    for i in range(3, limit+1, 2):
        if n % i == 0:
            return (i, n // i)

def phi(n):
    (p, q) = primeFactors(n)
    print("p:", p, "q:", q)
    return (p - 1) * (q - 1)

def rsa_encrypt_decrypt(input_file, output_file, key, n):
    with open(input_file, 'rb') as f:
        data = f.read()

    processed_data = [(pow(byte, key, n)) for byte in data]

    with open(output_file, 'wb') as f:
        f.write(bytearray(processed_data))

n = int(input("Enter a number N: "))
e = int(input("Enter a number e: "))

n_phi = phi(int(n))
print("Phi of", n, "is", n_phi)

d = gdcExtended(int(e), n_phi)

print("d is", d)

# texto_claro = input("Enter the input file: ")
# claro = open(texto_claro, "rb")
# cifrado = open("encriptado", "wb+")
# decifrado = open("decriptado", "wb+")
# 
# while True:
#     
#     byte = int.from_bytes(claro.read(1), byteorder='big', signed=False)
#     if not byte:
#         break
# 
#     c_byte = pow(byte, int(e), int(n))
#     cifrado.write(c_byte.to_bytes(1, byteorder='big', signed=False))
#     
#     d_byte = pow(c_byte, int(d), int(n))
#     decifrado.write(d_byte.to_bytes(1, byteorder='big', signed=False))

