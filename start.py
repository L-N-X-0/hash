# from subprocess import run, PIP
# import time 
import os
os.system('clear')

from bannr import *
from lng import *

deoren = input(G+''' 
1 - DeCode 
2 - EnCode

Please Select :''')

if deoren in ('1','Decode','decode','DeCode'):
    decode = input(R+"Enter Hash :")
    
    def decr_text(text):
        dec_text = ""
        for char in text:
            index=y.index(char)
            dec_text+= x[index]
        return dec_text
    text = decr_text(decode)
    print(R+"\nDecode : " + Y+text)

elif deoren in ('2','encode','encode','EnCode'):
    encode = input(R+"Enter Text :")
    def encr_text(text):
        enc_text = ""
        for char in text:
            index=x.index(char)
            enc_text+= y[index]
        return enc_text
    text = encr_text(encode)
    print(f"\n{R}hash : {Y}{text}")
    
else:
    print(R+"\nPlease Select Try Again")
    