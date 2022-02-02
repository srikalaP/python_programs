def fact(n):
    if n == 1:
        print("Tha factorial of", n)
    else:
        return n * fact(n - 1)


# num1 = int(input("Enter no"))
num1 = 5
fact1 = fact(num1)
print("fact is", fact1)


def strfunctions():
    str1 = "srikala Sajeesh"
    str2 = "123"
    print(str1.upper())
    print(str1.lower())

    print(str1.title())
    print(str1.swapcase())
    print(str1.capitalize())

    print(str1.startswith("srikala"))
    print(str1.endswith("saj"))

    print(str1.isalnum())
    print(str1.isalpha())
    print(str2.isdigit())


strfunctions()
