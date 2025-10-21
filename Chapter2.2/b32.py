def caesar_cipher(text: str, shift: int = 3) -> str:
    result: str = ""  
    shift = shift*-1
    for char in text:
        if char.isalpha():
            base: int = ord('A') if char.isupper() else ord('a')
            
            shifted: int = (int(ord(char)) - base + shift) % 26 + base
            result += chr(shifted) 
        else:
            result += char  
    return result


message: str = input("Enter a message: ")
encrypted: str = caesar_cipher(message, 3)
print("Decrypted message:", encrypted)