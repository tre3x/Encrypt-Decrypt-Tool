from cryptography.fernet import Fernet



def enncrypt(text):
    
    key=Fernet.generate_key()
    
    print("Your Key is:",key.decode('ascii'))
   
    b = bytes(text, 'utf-8')
    
    f=Fernet(key)
    
    print()
    
    token=f.encrypt(b)

    print("Your encrypted text is:",token.decode('ascii'))
   
def deccrypt(key,text):
    k=bytes(key, 'utf-8')
    b = bytes(text, 'utf-8')
    f=Fernet(k)
    
    dec=f.decrypt(b)

    print("Your decrypted text is:",dec.decode('ascii'))
    
    
print("Enter text you want to encrypt or decrypt:")
text=(input())
print()
print("For encryption,press 1.For decryption press 2:")
press=int(input())


if(press==1):
    enncrypt(text)
else:
    print("Enter Key:")
    keyy=input()
    print()
    deccrypt(keyy,text)