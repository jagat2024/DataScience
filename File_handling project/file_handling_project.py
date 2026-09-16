from pathlib import Path
import os
def read_FileandFolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def Create_file():
    
    try:
        read_FileandFolder();
        name=input("Enter your file name")
        p=Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data= input("what do you want to write in the file:-> ")
                fs.write(data)
            print("=========================FIle created succesfully=======================")
        else:
            print("===========================The file already exists======================")
            
    except Exception as err:
        print(f"unable to open the file as {err}")
    

def Read_file():
    try:
        read_FileandFolder()
        name=input("enter the name of the file")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fp:
                data= fp.read()
                print(data)
            print("========================FILE READED SUCCESSFULLY========================")
        else:
            print("========================THE FILE DOESNT EXISTS===========================")
    except Exception as err:
        print(f"ERROR occureed as {err}")


def Update_file():
    try:
        read_FileandFolder()
        name=input("enter the name of the file you want to update")
        p=Path(name)
        if p.exists() and p.is_file():
            print("Press 1 to rename a file")
            print("press 2 to update the content of the file")
            print("Press 3 to append the content in the file")
            res=int(input("enter your choice"))
            if(res==1):
                name2=input("enter the new  name of the file")
                p2=Path(name2)
                p.rename(p2)
                print("--------------------------------THE FILE IS SUCCESSFULLY RENAMED-----------------------------")
            
            elif( res==2):
                data=input("enter the data you want to override the file: ")
                with open(p,'r') as fs:
                    fs.write(data)
                print("-----------------------------------FILE SUCCESSFULLY OVERWRITTEN----------------------------")
            elif(res==3):
                sen=input("enter the data you want to append in the file:-> ")
                with open(p,'a+') as fp:
                    fp.write("\n "+sen)
                print("---------------------------FILE SUCCESSFULLY APPENDED BY NEW DATA------------------------------")
            else:
                print("Enter a valid choice")
    except Exception as err:
        print(f"exception occur as {err}")

def Delete_file():
    try:
        read_FileandFolder()
        name=input("enter the file name you want to delete")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("===========FILE REMOVED SUCCESSFULLY==============")
        else:
            print("=================NO SUCH FILE EXISTS==================")
    except Exception as err:
        print(f"ERROR OCCURRED AS {err}")
print("Some operations to be performed are:")
print("Press 1 to Create a file")
print("Press 2 to Read a file")
print("Press 3 to Update a file")
print("Press 4 to Delete a file")
check=int(input("Enter your desired choice: "))
read_FileandFolder()
if(check==1):
    Create_file()
elif check==2:
    Read_file()
elif check==3:
    Update_file()
elif check==4:
    Delete_file()
else:
    print("ENTER A VALID CHOICE")
