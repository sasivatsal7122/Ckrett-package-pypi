<h1 align="center">ckret-python-library</h1>
This is an useful python library for people who care about privacy, this library is useful to cipher and decipher text using 4 simple functions.

---------------------------------------------------------------------------------------------
Available operations in ckret library:

1.syph() -----> cypherises the user input text\
2.dsyph() -----> decypherises the user input text to plain text\
3.ksyph() ------> cypherises the user input text with unique 6 digit security key\
4.kdysph() -------> decypherises the text only when 6 digit security key is provided correctly\

---------------------------------------------------------------------------------------------

usecase example:
```python
import ckret
x=input()
msg=ckret.syph(x)
print(msg)
```
u can change syph(),dsyph(),ksyph(),kdsyph() respectively depeding on your operation

note:\
text ciphered using syph() can only be deciphered strictly by dsyph()\
text ciphered using ksyph() can only be deciphered strictly by kdsyph()

happy ciphering, peace✌.

