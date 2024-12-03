alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def crypt(text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:  # Vérifier si le caractère est dans l'alphabet
            position = alphabet.index(letter) + shift
            position %= len(alphabet)
            cipher_text += alphabet[position]
        else:
            cipher_text += letter  # Conserver les caractères non alphabétiques tels quels
    print(f"Here is the encoded result: {cipher_text}")
    return cipher_text

def decrypt(text, shift):
    plain_text = ""
    for letter in text:
        if letter in alphabet:  # Vérifier si le caractère est dans l'alphabet
            position = alphabet.index(letter) - shift
            position %= len(alphabet)
            plain_text += alphabet[position]
        else:
            plain_text += letter  # Conserver les caractères non alphabétiques tels quels
    print(f"Here is the decoded result: {plain_text}")
    return plain_text

# Demander une entrée utilisateur
original = input("Put your text here (lowercase only): ")

# Tester le chiffrement et le déchiffrement
shift_value = 3
encrypted_text = crypt(text=original, shift=shift_value)
decrypt(text=encrypted_text, shift=shift_value)
