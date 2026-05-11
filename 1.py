import os 
os.system("cls")

with open ("N205/image.jpeg", "rb") as file :
    baytlar = file.read () 
    print (f"\n{len(baytlar)} ta raqam ")


with open ("rasm.jpeg" , "wb" ) as file : 
    file.write(baytlar) 
    print ("fayl nusxalandie ")   
import opcode
