"""
written by B.SasiVatsal on 19th dec,2021
---------------------------------------------------------------------------------------------------------------
Available operations:
1.syph() -----> cypherises the user input text
2.dsyph() -----> decypherises the user input text to plain text
3.ksyph() ------> cypherises the user input text with unique 6 digit security key which can be used to decrypt
4.kdysph() -------> decypherises the 6 digit encrypted user input text to plain text
---------------------------------------------------------------------------------------------------------------
"""
"""
all dictionaries that are used for cyphering and decyphering
"""
cynumdict={"1":"!","2":"@","3":"#","4":"$","5":"%","6":"^","7":"&","8":"*","9":"(","0":")"}
dcynumdict={"!":"1","@":"2","#":"3","$":"4","%":"5","^":"6","&":"7","*":"8","(":"9",")":"0"}
cyphdict={'e': 'C', 'd': 'N', 'c': 'E', 'a': 'L', 'i': 'P', 'j': 'K', 'x': 'X', 's': 'M', 'r': 'D', 'h': 'H', 'k': 'V', 'm': 'W', 'n': 'U', 'u': 'S', 'p': 'R', 'f': 'I', 'g': 'T', 'y': 'J', 'q': 'O', 'z': 'A', 'l': 'Q', 'b': 'G', 'w': 'Z', 'v': 'Y', 'o': 'B', 't': 'F','.':'φ',',':'ζ'}
decyphdict={'C': 'e', 'N': 'd', 'E': 'c', 'L': 'a', 'P': 'i', 'K': 'j', 'X': 'x', 'M': 's', 'D': 'r', 'H': 'h', 'V': 'k', 'W': 'm', 'U': 'n', 'S': 'u', 'R': 'p', 'I': 'f', 'T': 'g', 'J': 'y', 'O': 'q', 'A': 'z', 'Q': 'l', 'G': 'b', 'Z': 'w', 'Y': 'v', 'B': 'o', 'F': 't','?': ' ','φ':'.','ζ':','}
kcyphkey={'1':'‽','2':'⸮','3':'₤','4':'↓','5':'⸘','6':'↑','7':'⅋','8':'‰','9':'⁋','0':'¶'}
kdcyphkey={'‽': '1', '⸮': '2', '₤': '3', '↓': '4', '⸘': '5', '↑': '6', '⅋': '7', '‰': '8', '⁋': '9', '¶': '0'}
#kcyphkey={'1':'ή','2':'ß','3':'Ô','4':'↓','5':'⸘','6':'∂','7':'⅋','8':'ę','9':'ᶂ','0':'ì'}
#kdcyphkey={'ή':'1','ß':'2','Ô':'3','↓':'4','⸘':'5','∂':'6','⅋':'7','ę':'8','ᶂ':'9','ì':'0'}
spclc=['?','.',',','φ','ζ']
import random
"""
driver function for phase-2 decrypting 
takes input as plain text with jumbled words with their respective word positions
using bubble sort algorithm, words are sorted in their respective word positions
after sorting the string is returned to user
"""
def decypherphase2(x2):
    x2+=" "
    def bubbleSort(numls,charls):
        n = len(numls)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if numls[j]>numls[j + 1]:
                    charls[j],charls[j+1]=charls[j+1],charls[j]
                    numls[j],numls[j+1]=numls[j+1],numls[j]
        ans=" "
        x=ans.join(charls)
        X2=intit_check(x,dnumsup)
        return X2
    numls=[]
    charls=[]
    temp=""
    num=0
    for i in x2:
        if i.isspace():
            charls.append(temp)
            numls.append(num)
            num=0
            temp=""
        elif i.isalpha():
            temp+=i
        elif i.isnumeric():
            num=num*10+int(i)
        else:
            temp+=str(i)
    return bubbleSort(numls,charls)
"""
driver fucntion for phase-1 encrypting

takes plain text and assign numbers at the end of each word their respective word positions
then jumbles them randomly
jumbled string of word is sent to phase-2 
"""  
def cypherphase1(x1):  
    x1+=" "
    temp=""
    temp3=""
    word=1
    templs=[]
    for i in x1:
        if i.isspace():
            temp2=str(word)
            templs.append((temp+temp2))
            temp3+=(temp+temp2)
            word+=1
            temp=""
        else:
            temp+=i
        random.shuffle(templs) #used to jumble word randomly
        ans=" "
    x=ans.join(templs)
    return cypher_decypher(x,cyphdict,cynumdict) #jumbled string is sent to phase-2

"""
driver fucntion for phase-2 encrypting and decrpting

encrypting and decrypting can be done in same function by changing the dictionary attributes
takes 3 arguments, x i.e string is constant
adictionary and ndictionary changes depending on the operation i.e cyphering/decyphering required to perform 
"""
def cypher_decypher(x,adictionary,ndictionary):
    strr=""
    def num(i):
        return ndictionary.get(i)
    def char(i):
        return adictionary.get(i)
    for i in x:
        if(i.isspace()):
            strr+="?"
        elif i.isnumeric():
            strr+=str(num(i))
        elif i.isalpha() or (i in spclc):
            strr+=str(char(i))
        elif (i in cnumsup.keys()) or (i in dnumsup.keys()):
            strr+=i
        else:
            strr+=str(num(i)) 
    return strr        

"""
driver code for functions in ckret module
"""

"""
driver code for cypherring and decyphering without key
"""
"""
support for numbers in user given sentence
"""
cnumsup={"1":"√","2":"⋎","3":"§","4":"∁","5":">","6":"/","7":"₡","8":":","9":"∀","0":"<"}
dnumsup={"√": '1', '⋎': '2', '§': '3', '∁': '4', '>': '5', '/': '6', '₡': '7', ':': '8', '∀': '9', '<': '0'}
def intit_check(X,xdict):
    x1=""
    def num(i):
        return xdict.get(i)
    for i in X:
        if X.isnumeric() or (i in xdict.keys()):
            x1+=num(i)
        else:
            x1+=i    
    return x1

def syph(x):
    y=x.lower()
    x2=intit_check(y,cnumsup)
    return cypherphase1(x2)
def dsyph(x):
    if x[-1] in kdcyphkey.keys(): #checking if the text entered is encrypted or not
        return ("message encrypted with key....try kdsyph()")
    else:
        X=cypher_decypher(x,decyphdict,dcynumdict) #phase-1 decyphering
        return decypherphase2(X)  #phase-2 decyphering and returning plain text
"""
driver code for cyphering with key and decyphering with key
"""
def return_cypher_text(withoutkey,ckey_list,res_num):
    withoutkey_list=list(withoutkey)
    res_num.sort()
    res_num.pop()
    n=0
    for i in res_num:
        withoutkey_list.insert(i,ckey_list[n])
        n+=1
    t=""                                                    
    kysph_text=str(t.join(withoutkey_list))
    return kysph_text
def ksyph(x):
    y=x.lower()
    x2=intit_check(y,cnumsup)
    withoutkey=cypherphase1(x2)
    l=len(withoutkey)
    res=((random.sample(range(0,10),6)))
    res_numls=[]
    for i in res:
         res_numls.append(str(i)) 
    t=""                                                    
    key=str(t.join(res_numls))
    res_numls.sort()
    keysorted=str(t.join(res_numls))
    ckey=cypher_decypher(keysorted,cyphdict,kcyphkey) #cyphering the numeric key
    ckey_list=list(ckey)
    print("your secret key is:",key)    #printing the generated 'numeric' security key to the user
    return (return_cypher_text(withoutkey,ckey_list[:5],res)+ckey_list[5])
def kdsyph(x):
    leng=len(x)
    if x[-1] not in kdcyphkey.keys(): #condition to check msg is encrypted or not
        return ("message not encrypted with key....try dsyph()") 
    else:
        cckey=""
        t=""
        user_given_ls=list(x)
        user_key=input("enter secret key: ") #asking user to enter their unique security key
        user_key_ls=list(user_key)
        user_key_ls.sort()
        check_key=str(t.join(user_key_ls))
        for i in user_key_ls:
            cckey+=str(user_given_ls[int(i)])
        ckey=cckey.rstrip(cckey[-1])
        dkey=cypher_decypher(ckey,decyphdict,kdcyphkey)  #decrypting the 6 digit security key and checking authencity
        list(ckey)
        if dkey==check_key.rstrip(check_key[-1]):
            for i in ckey:
                user_given_ls.remove(str(i))
            user_given_ls.pop()    
            return dsyph(user_given_ls)  #returning decyphered text if security key entered by user is authentic
        else:
            return ("you entered wrong key cannot decrypt...teriminating.......") #returning false if key is not authentic

