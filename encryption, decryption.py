def caesar_cipher(text, shift, mode):
  

  result = ""
  for char in text:
    if char.isalpha():
      
      start = ord('A') if char.isupper() else ord('a')
      
      shifted_char = (ord(char) - start + shift) % 26 + start
      result += chr(shifted_char)
    else:
      result += char
  return result


message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter mode (encrypt/decrypt): ")


if mode.lower() == "encrypt":
  encrypted_message = caesar_cipher(message, shift, mode)
  print("Encrypted message:", encrypted_message)
elif mode.lower() == "decrypt":
  decrypted_message = caesar_cipher(message, -shift, mode)  
  print("Decrypted message:", decrypted_message)
else:
  print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")