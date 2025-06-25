from collections import Counter
import CaesarCipher

alphabet = list("abcdefghijklmnopqrstuvwxyz")

def frequency_analysis(text):
    counts = Counter(c.lower() for c in text if c.lower() in alphabet)
    total = sum(counts.values())

    print("Frequency analysis (letters only):")
    for char, count in counts.most_common():
        percentage = (count / total) * 100
        print(f"{char.upper()}: {count} ({percentage:.2f}%)")

    return counts

def guess_caesar_key(ciphertext):
    counts = frequency_analysis(ciphertext)
    if not counts:
        print("No letter found.")
        return None

    # Letter most often appearing in text
    most_common_letter = counts.most_common(1)[0][0]

    # Most common letter in English language -> 'e'
    assumed_plain_letter = 'e'

    # determine key (difference of positions in the alphabet)
    key = (alphabet.index(most_common_letter) - alphabet.index(assumed_plain_letter)) % 26
    print(f"\n🔑 Estimated key (based on '{most_common_letter.upper()}' → 'E'): {key}")
    return key

if __name__ == "__main__":
    key = CaesarCipher.generateKey()
    data = CaesarCipher.readData("./originalData.txt")
    encryptedData = CaesarCipher.encrypt(data, key)
    print(f"{guess_caesar_key(encryptedData)}\nReal Key: {key}")
