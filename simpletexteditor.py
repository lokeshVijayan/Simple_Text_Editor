import sys
import os

def write():
    
    try:
        print("it will prompt the file name,\
type the file name to create file name,\
then type the text for file,on next time type menu to save the file,\
and to return to the main menu")
        file_name=input("enter your file name: ")
        f1=open(file_name,'a')
        while True:
            
            x=input("enter text then in next step type menu :")
            
            if x.lower()=="menu":
                break
            
            else:
                f1.write(x)
                f1.write("\n")
                
    except Exception as e:
        print(e)
def read():
    try:
        file_name=input("enter your filename: ")
        f1=open(file_name,"r")
        readfile=f1.read()
        print(readfile)
    except Exception as e:
        print(e)

def cwd():
    try:
        print(os.getcwd())
        tochange=input("change Y/N? : ")
        if tochange.startswith("Y"):
            path=input("NEWCWD: ")
            os.chdir(path)
    
        
    except Exception as e:
        print(e)
        
    


while True:
    print('#'* 30)
    print("==================SIMPLE TEXT EDITOR==============")
    print('#'*30)

    print("options: \n write \n read \n cwd \n exit \n delete \n rename")

    do=input("so,how are you going to edit the file: ")
    if do.lower()=="write":
        write()
    if do.lower()=="read":
        read()
    if do.lower()=="cwd":
        cwd()
        

    























        

