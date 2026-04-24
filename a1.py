# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME Bozhang Zhou
# EMAIL bozhangz@uci.edu
# STUDENT ID 93213406

from pathlib import Path
import shlex

def create_file(text):
    if len(text) != 4 or text[2] != "-n":
        print ("ERROR")
        return
    directory=Path(text[1])

    if not directory.exists() and not directory.is_dir():
        print("ERROR")
        return
    else:
        file_path=directory/(text[3]+'.dsu')
        if file_path.exists():
            print("ERROR")
            return
        file_path.touch()
        print(file_path)


def delete_file(text):
    if len(text) != 2:
        print("ERROR")
        return
    
    file_path=Path(text[1])

    if not file_path.exists() or file_path.suffix != '.dsu':
        print("ERROR")
        return
    
    file_path.unlink()
    print(f'{file_path} DELETED')

def read_file(text):

    file_path=Path(text[1])
    if not file_path.exists() or file_path.is_file() or file_path.suffix != ".dsu":
        print("ERROR")
        return
    else:
        content=file_path.read_text()
        
        if content=='':
            print("EMPTY")
        else:
            print(content)


def main():
    while True:
        text=input("C/D/R and file route, type Q to quit:")
        try:
            order_parts=shlex.split(text)
        except ValueError:
            print("Invalid input, please try again")
            continue

        
        if order_parts[0]=="Q":
            break
        elif order_parts[0]=="C":
            create_file(order_parts)
        elif order_parts[0]=="D":
            delete_file(order_parts)
        elif order_parts[0]=="R":
            read_file(order_parts)
        else:
            print("Invalid input, please try again")
            continue

        


        


if __name__=="__main__":
    main()