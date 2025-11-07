#contact book 
#lets create a contact book for each member and maybe give them the option to add favorites 

#create each dictionary holds data outside of loop so it wont get discarded after iterating through each member
contacts = {}
#family = {}
favorite = {}

#intro maybe setting up phone service 
print("Thank you for choosing AT&T!")

#amount of family memebers
n = int(input("How many people are on the phone plan?: "))

#create loop for n amount of people 
for i in range(n):


  #input 
  family = input("Whose phone is this?: ")
  family = family.strip().title()

  #selection menu
  while True: 
    print("\nContact Menu: ")
    print("1. Add Contact\n2. Find Contact\n3. List All Contacts\n4. Favorite Contact\n5. Delete Contact\n6. Exit Menu")

    choice = int(input(f"What would you like to do {family}?: "))

    if choice == 1: 
      while True:
        # add name and phone of contact 
        name = input("What is the name of the contact?: ")
        name = name.strip().title()


        #while loop for user error 
        while True:
          phone = input(f"What is {name}'s number?: ")
          if not phone.isdigit(): 
            print(f"Sorry {phone} is not a valid number please try again.")
            continue
          else: 
            #initialize dictionary assigning each family member and its contacts and numbers
            #use setdefault to ensure the inner dictionary exists for that family name
            contacts.setdefault(family, {})[name] = phone
            print(f"{phone} for {name} has been added!")
            break
        another = input("Would you like to enter another contact?(y/n): ")
        if another == 'y': continue
        else: break
         
    elif choice == 2:
      #find contact
      name = input("Who are you trying to find?: ")
      name = name.strip().title()

      #if name is found
      if name in contacts[family]:
        #set the number equal to the dictionary value
        findphone = contacts[family][name]
        print(f"This is {name}'s number: {findphone}")
      else:
        print(f"{name} is not in your contact book. Please try again.")

          
    elif choice == 3:
      #show contacts
      #if family member exists in contacts dictionary and they have at least one contact
      if family in contacts and contacts[family]:
        print(f"\n{family}'s Contacts:")

        #for each contact, and phone number in list print 
        for name, phone in contacts[family].items():
            print(f"  {name}: {phone}")
      else:
        print(f"{family} has no contacts yet!")

      #show favorites
      #if family member has favorites and favorite list is not empty
      if family in favorite and favorite[family]:
        print(f"{family}'s Favorites ({len(favorite[family])}):")
        #same as regualr contatc list
        for name, phone in favorite[family].items():
            print(f"  {name}: {phone}")

    elif choice == 4:
      #adding favorite
      while True: 
        name = input("What contact would you like to add to your favorites?: ")
        name = name.strip().title()

        if name in contacts[family]:
          #use same variable for name because phone is already assigned to the name
          #saves favorited contact and phone
          favnamephone = contacts[family][name]
          favorite.setdefault(family, {})[name] = favnamephone
          print(f"{name}'s contact has been saved in favorites tab!")
        else:
          print(f"{name} is not found in contact book.")
        
        another = input("Would you like to favorite another contact?(y/n): ")
        if another == 'y': continue
        else: break

    elif choice == 5:
      #deletion
      while True: 
        name = input("What contact would you like to delete?: ")
        name = name.strip().title() 

        #check with first total dictionary 
        if name in contacts[family]:
          del contacts[family][name]
          if name in favorite[family]:
            del favorite[family][name]
          print(f"{name} deleted from contacts.")
        else:
          print(f"{name} is not in contact book.")
        another = input("Would you like to delete another contact?(y/n): ")
        if another == 'y': continue
        else: break
    
    elif choice == 6:
      print(f"{family} has finished adding contacts.")
      break 

    else: 
      print(f"{choice} is invalid please try again") 
      continue 

print("\nALL CONTACTS:")
#use new variable family_name instead of family since it doesn't exist outside of the loop, makes code more clearer
for family_name in contacts.keys():
    print(f"\n{family_name}:")
    if contacts[family_name]:
        for name, phone in contacts[family_name].items():
            #if contact is a favorite assign a star next to the contact
            is_fav = "⭐" if family_name in favorite and name in favorite[family_name] else ""
            print(f"  {name}: {phone} {is_fav}")
    else:
        print("  No contacts")

print("\nALL FAVORITES:")
for family_name in favorite.keys():
    print(f"\n{family_name}:")
    if favorite[family_name]:
        for name, phone in favorite[family_name].items():
            print(f"  {name}: {phone}")
    else:
        print("  No favorites")
        




    




  




