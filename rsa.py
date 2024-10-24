import math as m
import random


def gen_prime(bit_len):
    while True:
        try:
            num = random.getrandbits(bit_len)
            if is_prime(num):
                return num
        except ValueError:
            exit(-1)


def is_prime(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def inverse(a, m_proc):
    m0, x0, x1 = m_proc, 0, 1
    while a > 1:
        q_proc = a // m_proc
        m_proc, a = a % m_proc, m_proc
        x0, x1 = x1 - q_proc * x0, x0
    return int(x1 + m0 if x1 < 0 else x1)


def gcd(a, b):
    return int(a if b == 0 else m.gcd(a, a % b))


def generate_keypair(p_proc, q_proc, bit_len):

    p_proc = gen_prime(bit_len)
    q_proc = gen_prime(bit_len)

    n = p_proc * q_proc
    phi = (p_proc - 1) * (q_proc - 1)

    # 1 < e < phi и e взаимно прост с phi
    e = random.randrange(2, phi)
    while m.gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # d * e ≡ 1 (mod phi)
    d = inverse(e, phi)

    return (e, n), (d, n)


def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext


def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)


if __name__ == "__main__":

    while True:
        try:
            bit_length = int(input("Введите количество бит в ключе: "))
            if bit_length < 0:
                print("Некорректный ввод. Введите целое число.")
            break
        except ValueError:
            print("Некорректный ввод. Введите целое число.")

    p = gen_prime(bit_length)
    q = gen_prime(bit_length)

    public, private = generate_keypair(p, q, bit_length)
    print(f'Публичный ключ: [{public}]\nПриватный ключ: [{private}]')

    message = input('Введите текст для шифрования:  ')
    encrypted_message = encrypt(public, message)
    print("Зашифрованное:", encrypted_message)
    decrypted_message = decrypt(private, encrypted_message)
    print("Расшифрованное:", decrypted_message)
