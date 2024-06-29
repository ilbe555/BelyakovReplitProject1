def caesar_cipher(text, key):
  en_alphabet = "abcdefghijklmnopqrstuvwxyz"
  result = ""
  for char in text.lower():
      if char in en_alphabet:
          shift = key % 26
          index = (en_alphabet.index(char) + shift) % 26
          result += en_alphabet[index]
      else:
          result += char
  return result