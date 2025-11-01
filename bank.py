user_id="vicky"
password="tomcr7"
amount=10000

user_input=(input("enter the user name:\n "))

if user_id==user_input:
    user_pass=(input("enter the user name:\n "))

    if password==user_pass:
        print("your login successful")
        withdraw=int(input("enter you withdraw amount:\n "))

        if withdraw <= amount:
            amount-=withdraw
            print("your amount withdraw successfully")
            print("your balance amount: ",amount)
            #some code changes gitbuh
        else:
            print("insufficient balance")
    
    else:
        print("incorrect password")

else:
    print("user not found")
