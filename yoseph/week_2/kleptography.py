prefix_length, _ = map(int, input().split())

plaintext = input()[::-1]
ciphertext = input()[::-1]

alphabets = "abcdefghijklmnopqrstuvwxyz"

for x, char in enumerate(ciphertext[:len(ciphertext) - prefix_length]):
    decrypted_char = alphabets[(ord(char) - ord(plaintext[x])) % 26]
    plaintext += decrypted_char

print(plaintext[::-1])
