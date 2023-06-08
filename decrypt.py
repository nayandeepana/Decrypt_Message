# Decryption technique using Caesar Cipher

def technique(message):
    l1=[]
    cipher=" "
    for i in range(0,len(message)):
        if message[i] == "$":
            l1.append(' ')
        elif message[i]==" ":
            message[i].strip()
        else:
            x=chr(ord(message[i])-3)
            l1.append(x)
    cipher=cipher.join(l1)
    with open ("dycrypted_message.txt","w") as f:
        f.write(cipher)
    return cipher


message=input("Enter Encrypted message to decrypt : ")
print(technique(message))
