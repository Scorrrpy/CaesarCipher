from collections import Counter
import CaesarCipher

alphabet = list("abcdefghijklmnopqrstuvwxyz")

def frequency_analysis(text):
    counts = Counter(c.lower() for c in text if c.lower() in alphabet)
    total = sum(counts.values())

    print("Häufigkeitsanalyse (nur Buchstaben):")
    for char, count in counts.most_common():
        percentage = (count / total) * 100
        print(f"{char.upper()}: {count} ({percentage:.2f}%)")

    return counts

def guess_caesar_key(ciphertext):
    counts = frequency_analysis(ciphertext)
    if not counts:
        print("Keine Buchstaben gefunden.")
        return None

    # Meistverwendeter Buchstabe im Text
    most_common_letter = counts.most_common(1)[0][0]

    # In der deutschen Sprache ist 'e' der häufigste Buchstabe
    assumed_plain_letter = 'e'

    # Schlüssel schätzen (Unterschied der Positionen im Alphabet)
    key = (alphabet.index(most_common_letter) - alphabet.index(assumed_plain_letter)) % 26
    print(f"\n🔑 Geschätzter Schlüssel (basierend auf '{most_common_letter.upper()}' → 'E'): {key}")
    return key

data = "Wir treffen und um 9 Uhr auf der Weide im südlichen Morrowind oder auch nicht. Ich weiß außerdem dein Geheimstes Geheimnis ;)"
encryptedData = CaesarCipher.encrypt(data, 11)
print(guess_caesar_key(encryptedData))
