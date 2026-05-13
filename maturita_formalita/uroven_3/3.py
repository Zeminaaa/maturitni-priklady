def fibonacci(n):
    last_nums=[0,1]
    for num in last_nums:
        print(num)
    for i in range(n-2):
        num=sum(last_nums)
        print(num)
        last_nums[0]=last_nums[1]
        last_nums[1]=num
fibonacci(int(input("Zadej n: ")))