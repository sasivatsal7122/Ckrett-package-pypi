<h1 align="center">ckrett-python-library</h1>
<h2 align="center">version-1.5.0</h2>
This is an useful python library for people who care about privacy, this library is useful to cipher and decipher text using 6 simple functions.

---------------------------------------------------------------------------------------------
Available operations in ckret library:

1.syph() -----> cypherises the user input text\
2.dsyph() -----> decypherises the user input text to plain text\
3.ksyph() ------> cypherises the user input text with unique 6 digit security key\
4.kdsyph() -------> decypherises the text only when 6 digit security key is provided correctly\
5.morse() -----> converts plain english text into morse code\
6.dmorse() -----> converts morse code into plain english text\
7.stot() -------> converts speech to text, can be used in place of input()

---------------------------------------------------------------------------------------------

# Note: 
==> for speech recognition to work that is stot(), <b>pyaudio must be strictly pre-installed</b>, otherwise you'll get an error.\
if pyaudio is already installed you can skip this step and proceed for installation\
or\
install pyaudio by executing the following commands in cmd before or after installing ckrett:
```
step-1 : $ pip install pipwin
step-2 : $ pipwin install pyaudio
```
pipwin is used to install windows binaries and depencies that are required for building and compiling pyaudio setup files
# Installation:
Install from official pypi repo --> https://pypi.org/project/ckrett/ 

or
```
$ pip install ckrett
```

### usecase example:

#### you can either use traditional input() 

```python
import ckrett
x=input()
msg=ckrett.syph(x)
print(msg)
```
### or: 

```python
import ckrett
x=stot()
msg=ckrett.syph(x)
print(msg)
```
#### live demo for stot() : (audio isn't audible since it's a gif)
<img src="ckrett-preview.gif">

### u can change syph(),dsyph(),ksyph(),kdsyph(),morse(),dmorse() respectively depeding on your choice of ciphering

==>changes in 1.5.0:\
$ added morse(),dmorse(),stot()\
$ user can now convert plain english text into morse code and vice versa\
$ using stot() user can dicate a sentence which is recognized using dependecies-pyaudio,pyttxs3,speech_recognition engine that can be stored in var x which can be used for         ciphering directly from speech, instead of typing out the entire sentence using input().

### note-1:
->stot() can only be used to give input in plain english, as special character or encrypted msg's arent recognized accurately\
->use stot() for syph(),ksyph(),morse()

### note-2:
->text ciphered using syph() can only be deciphered strictly by dsyph()\
->text ciphered using ksyph() can only be deciphered strictly by kdsyph()\
->text ciphered using morse() can only be deciphered strictly by dmorse()

### note-3:
->in version 1.0.0,1.5.0 there is no support for characters --> @,#,$,%,^,&,*,(,),! , kindly avoid using them in your sentence.\
->support for these charcaters will be added in next version (2.0.0)

happy ciphering, peace✌.

