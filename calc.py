def calc():
    try:
        q=int(input("Type Number: "))
        a=input("Type Operator: ")
        z=int(input("Type Number: "))
        if (a=="+"):
            s=q+z
            print(s)
        else:
            print("Error")

        if (a=="/"):
            s=q/z
            print(s)

        if (a=="*"):
            s=q*z
            print(s)

        if (a=="-"):
            s=q-z
            print(s)
    except:
        print("Please Type Number")


print(calc())


