contacts={"Mithran":["0605533313","mithran@gmail.com"]}
name=input("Name: ")
phone=input("Phone No: ")
email=input("Email: ")

contacts[name]=[phone,email]
search=input("verification Name: ")
if search in contacts:
    [phone,email]=contacts[search]
    print(f"{search} : {phone}/{email}")
else:
    print(search,"Not Found")
print(len(contacts),"Contacts")