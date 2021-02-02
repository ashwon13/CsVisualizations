#Ashwin Pulla
#2/2/2021
#I DID IN PYTHON 3
def decrypt(data):
    
    letters=[]
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    final=[]
    data=data
    print("Decrypting... ")
    letters=[char for char in data] 
    length=len(letters)
    positions=[]
    for element in letters:
        try:
            position=alphabet.index(element)
        
            positions.append(position)
        except:
            positions.append(element)
    finalPositions=[]
    
    for element in positions:
        try:
            element=element-13
            finalPositions.append(element)
        except:
            finalPositions.append(element)
       
    
    final=[]
    for element in finalPositions:
        try:
            final.append(alphabet[element])   
        except:
            final.append(element)  
    finalString = ''.join(final)
    print(finalString)
        
def encrypt(data):
    data=data
    letters=[]
    letters=[char for char in data] 
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    positions=[]
    

    for element in letters:
        try:
            position=alphabet.index(element)
        
            positions.append(position)
        except:
            positions.append(element)
    finalPositions=[]
    
    for element in positions:
        try:
            
            element=element+13
            if element>=26:
                element=element-26
                1
            finalPositions.append(element)
            
        except:
            finalPositions.append(element)
    final=[]   
    
    for element in finalPositions:
        try:
            final.append(alphabet[element])   
        except:
            final.append(element)  
    
    finalString = ''.join(final)
    print(finalString)  

    


    
        
choice=input("type 1 to encrypt or type 2 to decrypt")

if choice=="1" or choice==1:
    data=str(input("What would you like to encrypt"))
    encrypt(data)
elif choice=="2" or choice==2:
    data=str(input("what do you want to decrypt"))
    decrypt(data)

