# Problem 5
def check_equality():
    print("\nA) Check equality        B) Exit the program")
    choice = input("please enter your choice(A/B) : \n").upper()
    if choice == "A" :
        list1 = []
        list2 = []

        # Get the lists from user and check if it is integer or not
        print("\nplease enter the number you want to add in list 1\nif you want to stop adding numbers input (S) or (Stop)\n")
        while True:
            print("list 1 = ",list1,"\n")
            num = input ("Add: ")
            if num=="S" or num=="s" or num=="stop" or num=="Stop":
                break
            try:
                num = int(num)
                list1.append(num)
            except ValueError:
                print ("Invalid number. Please input a valid number: ")

        print("\nplease enter the number you want to add in list 2\nif you want to stop adding numbers input (S) or (Stop)\n")
        while True:
            print("list 2 = ",list2,"\n")
            num = input ("Add: ")
            if num=="S" or num=="s" or num=="stop" or num=="Stop":
                break
            try:
                num = int(num)
                list2.append(num)
            except ValueError:
                print ("Invalid number. Please input a valid number: ")


        # Check if lists are equal or not
        if len(list1) != len(list2):
            print("\nlist 1:",list1,"\nlist 2:",list2,"\nlists are equal = False")
            check_equality()

        else:
            set1 = set(list1)
            set2 = set(list2)

            for element in list1: 
                x+=ord(str(element))
            for element in list2: 
                y+=ord(str(element))

            if set1 == set2:
                print("\nlist 1:",list1,"\nlist 2:",list2,"\nlists are equal = True")
            else:
                print("\nlist 1:",list1,"\nlist 2:",list2,"\nlists are equal = False")
            print("\n------------------------------------------------")
            # call the check_equality function to know if the user want to start the program again or exit it 
            check_equality()
        check_equality()
    elif choice == "B" :
       print("\nGoodbye\n")  
       exit()
    else :
       print("Invalid choice. Please choose a valid choice\n")
       check_equality()
# print welcome message and start the program
print("\n  -= Welcome to check equality program =-")
result = check_equality()
print(result)
