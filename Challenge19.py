#list of alphabets
g.lobal alpha
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#encrypting function that takes two params : text  and key , text being a string and key being a list 
def encrypt(text,key):
    for i in text:
        #using enumerate to get the position of the alphabet in terms of x and j being used to compare letter i if equal
        for x,j in enumerate(alpha):
            if(i == j): 
                key.append(alpha[x+2]) #if equal then add the x by 2 positions and then append that to the key 
    return key 
#decrypting function reverse the encrypting however both parameters have to be a list value
def decrypt(key,text):
    for i in key:
        for x,j in enumerate(alpha):
            if(i == j):
                text.append(alpha[x-2])
    return text
print(encrypt("CARLOS",[]))
print(decrypt(['E','C','T','N','Q','U'],[]))
