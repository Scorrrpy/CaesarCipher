alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(data, key):
    if key > 25 or key < 1:
        return ("key ist nicht im gültigen Bereich (0 - 26)!")
    encryptedData = ""
    charCount = len(alphabet)
    for c in data:
        cl = c.lower()
        if cl in alphabet:
            if str(c).isupper():
                c = alphabet[alphabet.index(cl) + key if alphabet.index(cl) + key < charCount else alphabet.index(cl) + key - charCount].upper()
            else:
                c = alphabet[alphabet.index(cl) + key if alphabet.index(cl) + key < charCount else alphabet.index(cl) + key - charCount]
        encryptedData = f"{encryptedData}{c}"
    return encryptedData

def decrypt(data, key):
    if key > 25 or key < 1:
        return ("key ist nicht im gültigen Bereich (0 - 26)!")
    decryptedData = ""
    charCount = len(alphabet)
    for c in data:
        cl = c.lower()
        if cl in alphabet:
            if str(c).isupper():
                c = alphabet[alphabet.index(cl) - key if alphabet.index(cl) - key >= 0 else alphabet.index(cl) - key + charCount].upper()
            else:
                c = alphabet[alphabet.index(cl) - key if alphabet.index(cl) - key >= 0 else alphabet.index(cl) - key + charCount]
        decryptedData = f"{decryptedData}{c}"
    return decryptedData

data =  """
       Treffen wir uns morgen um 14 Uhr am alten Baum!
        """
key = 1
encryptedData = encrypt(data, key)
decryptedData = decrypt(encryptedData, key)

print(f"Encrypted: {encryptedData}\nDecrypted: {decryptedData}")