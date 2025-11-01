user_id="vickycr7"
password="vickycr77"
amount=10000

user_input=(input("enter the user name: "))

if user_id==user_input:
    user_pass=(input("enter the user name: "))

    if password==user_pass:
        print("your login successful")
        withdraw=int(input("enter you withdraw amount: "))

        if withdraw <= amount:
            amount-=withdraw
            print("your amount withdraw successfully")
            print("your balance amount: ",amount)
        else:
            print("insufficient balance")
    
    else:
        print("incorrect password")

else:
    print("user not found")