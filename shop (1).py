#with coach tareq<3 .
print("welcome to chocolate" , "\nwhats your name?")
name = input()
if name == "isreal":
    real_name = input("is thats your real name?")
    if real_name == "yes":
        print("get out of my shop")
        exit()              
    elif real_name == "no":
        print("okay, your good to go!")
        your_name =input("so what is your name ?")
        print ("welcome "+ your_name)
        menu = input("heres our menu:\n" + "ps3,ps5,pc,iphone15,samsungs24\n" + "what would you like to order?\n")
        if menu == "ps3" :
            print("this costs you  50$")
            num1 = input("quantity?")
            price = 50 
            total_1 = int(num1) * price
            print("total: " , total_1,"$")
        elif menu == "ps5" :
            print("this costs you  250$")
            num2 = input("quantity?")
            price2 = 250
            total_2 = int(num2) * price2
            print("total: " , total_2,"$")
        elif menu == "pc" :
            print("this costs you 200$")
            num3 = input("quantity?")
            price3 = 200
            total_3 = int(num3) * price3
            print("total:" , total_3,"$")
        elif menu == "iphone15" :
            print("this costs you  500$")
            num4 = input("quantity?")
            price4 = 500
            total_4 = int(num4) * price4
            print("total:" , total_4,"$")
        elif menu == "samsungs24" :
            print("this costs you  300$")
            num5 = input("quantity?")
            price5 = 300
            total_5 = int(num5) * price5
            print("total:" , total_5,"$")
        else :
            print("sorry this item is unavailable.")
            exit()
    else :
        print("please choose between yes,no")
        exit()
else:
    print ("welcome "+ name)
    menu = input("heres our menu:\n" + "ps3,ps5,pc,iphone15,samsungs24\n" + "what would you like to order?\n")
    if menu == "ps3" :
        print("this costs you  50$")
        num1 = input("quantity?")
        price = 50 
        total_1 = int(num1) * price
        print("total:" , total_1,"$")
    elif menu == "ps5" :
        print("this costs you  250$")
        num2 = input("quantity?")
        price2 = 250
        total_2 = int(num2) * price2
        print("total:" , total_2,"$")
    elif menu == "pc" :
        print("this costs you  200$")
        num3 = input("quantity?")
        price3 = 200
        total_3 = int(num3) * price3
        print("total:" , total_3,"$")
    elif menu == "iphone15" :
        print("this costs you  500$")
        num4 = input("quantity?")
        price4 = 500
        total_4 = int(num4) * price4
        print("total:" , total_4,"$")
    elif menu == "samsungs24" :
        print("this costs you  300$")
        num5 = input("quantity?")
        price5 = 300
        total_5 = int(num5) * price5
        print("total:" , total_5,"$")
    else :
        print("sorry this item is unavailable.")
        exit()
comfirm = input("please type yes to confirm your order")
if comfirm == "yes" :
        print("thanks for chossing our shop (chocolate)","your order will be ready soon!")
else :
    exit()






    

