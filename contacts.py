# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:58:39 2019

@author: Stob
"""
def menu():
    print('')
    print("1 - Add contacts")
    print("2 - Search contact and print")
    print("3 - Print all contacts")
    print("4 - exit")
    print('\n')
    
    selection = int(input("What to do?:"))
    if selection == 1:
        addcont()
    elif selection == 2:
        search()
    elif selection == 3:
        printall()
    elif selection == 4:
        exiter()
    else:
        print("try again")
        menu()

contacts = {'Steve' : '124514564674',
            'Eisler' : '12345678910'}

def addcont():
    print('\n')
    fh = open("contacts.txt", "a")
    name = str(input("input name:"))
    number = str(input("input number:"))
    contacts[str(name)] = str(number)
    fh.write('|' + name)
    fh.write(' ')
    fh.write(number + '|')
    fh.write(' ')
    fh.close()

    menu()
        
def search():
    print('\n')
    print(list(contacts.keys()))
    search = str(input("Name:"))
    if search in contacts:
        print(contacts[search])
    else:
        print("not found")
    menu()

def printall():
    print('\n')
    for key,value in contacts.items():
        print(key, ':', value)
    
    menu()
    
def exiter():
    print('\n')
    print("Good bye")
    
menu()