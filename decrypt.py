def decrypt(data):
    
    letters=[]
    final=[]
    data=data
    print("Decrypting... ")
    letters=[char for char in data] 
    length=len(letters)
    
    if (length % 2) == 0:
        B = letters[:(length//2)]
        C = letters[(length//2):]
        for element in range(len(B)):
            k=B[element]
            l=C[element]
            final.append(k)
            final.append(l)
    
    
    else:
        C = letters[:(length//2)+1]
        B = letters[(length//2)+1:]
        B.append(".")
        for element in range(len(B)):
            k=C[element]
            l=B[element]
            final.append(k)
            final.append(l)
            
        final.pop()
    finalString = ''.join(final)
    print(finalString)
        
def encrypt(data):
    data=data
    letters=[]
    letters=[char for char in data] 
    evens = [letters[i] for i in range(len(letters)) if i % 2 == 0]
    odds = [letters[i] for i in range(len(letters)) if i % 2 != 0]
    print("Encrypting...")
    for i in odds:
   # appending the elements of list2 into list1
        evens.append(i)
        

    stringEncrypt = ''.join(evens)
    print(stringEncrypt)


    
        
choice=input("type 1 to encrypt or type 2 to decrypt")

if choice=="1" or choice==1:
    data=str(input("What would you like to encrypt"))
    encrypt(data)
elif choice=="2" or choice==2:
    data=str(input("what do you want to decrypt"))
    decrypt(data)

