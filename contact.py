contacts={}
while True:
    print("contact book")
    print("1) add contact")
    print("2) view contact")
    print("3) search contact")
    print("4) delte contact")
    print("5) update contact ")
    print("6) exit")
    choice =input("enter choice:")
    if choice=='1':
        name=input("enter name:")
        phno=input("enter number:")
        email=input("enter email id:")
        address=input("enter address:")
        contacts[name]={"phone ":phno,"email":email,"address":address}
        print("contact added")
    elif choice=='2':
        if not contacts:
            print("no contacts available")
        else:
            for name,phone in contacts.items():
                print(name,":", phone )
    elif choice=='3':
        name=input("enter name:")
        if name in contacts:
            print("phone :",contacts[name])
        else:
            print("contact not found")
    elif choice=='4':
        name=input("enter name:")
        if name in contacts:
            del contacts[name]
            print("contact deletd")
        else:
            print("contact not found")
    elif choice=='5':
        name =input("enter name:")
        if name in contacts:
            new_phno=input("enter new number:")
            new_email=input("enter new email:")
            new_address=input("enter new address:")
            contacts[name]={"phone ":new_phno,"email":new_email,"address":new_address}
            print("contact updated")
        else:
            print("contact not found")
    elif choice=='6':
        print("exiting contact book")
        break
    else:
        print("invalid choice")
                
            
    
          