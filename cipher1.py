#for encrypt
#(x+n)mod(num of language letters)

#x is the alphabet order
#n is the key value

#for decrypt
#(x-n)mod(num of language letters) 

def cipher(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Decrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + int(s) - 65) % 26 + 65)
 
        # Decrypt lowercase characters
        else:
            result += chr((ord(char) + int(s) - 97) % 26 + 97)
 
    return result


#check the above function
text = input("input text: ")
s = input("input key: ")

print ("Cipher: " + cipher(text,s))