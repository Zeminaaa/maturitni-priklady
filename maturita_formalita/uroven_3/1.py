def factorial():
    while True:
        user_input=int(input("Zadej n: "))
        if user_input>=0:
            num=user_input
            break
        else:
            print("Zadejte prosím nezápornou hodnotu!")
    if num==0:
        print(f"{num}! = 1")
    else:
        original_num=num
        result=1
        while num>1:
            result*=num
            num-=1
        print(f"{original_num}! = {result}")
factorial()