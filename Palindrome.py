try:
    tc = int(input("Enter the number of test cases you want:- "))
    for i in range(tc):
        n = int(input("Enter the number:- "))
        while True:
            n = n + 1
            t = str(n)
            if t == t[::-1]:
                print(f"The next palindrome for is {t}")
                break
            else:
                continue

except Exception as f:
    print(f"{f} Please try to input numbers not alphabet")
