class dataExport:

    def mrgFunction():
        gender = input("enter the gender :")
        age = int(input("enter the age :"))

        if gender == "Male" and age >= 21:
            print("Your Gender:", gender)
            print("Your Age:", age)
            print("ELIGIBLE")
        elif gender == "Female" and age >= 18:
            print("Your Gender:", gender)
            print("Your Age:", age)
            print("ELIGIBLE")
        else:
            print("Your Gender:", gender)
            print("Your Age:", age)
            print("NOT ELIGIBLE")

    def fieldList():
        listItem = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing",
        ]

        print("Sub-fields in AI are:")
        for items in listItem:
            print(items)

    def triangle():
        Height = 32
        Breadth = 34
        print("Height:", Height)
        print("Breadth:", Breadth)
        print("Area formula: (Height*Breadth)/2")
        areaformula = (Height * Breadth) / 2
        print("Area of Triangle:", areaformula)

        Height1 = 2
        Height2 = 4
        Breadth1 = 4
        print("Height1:", Height1)
        print("Height2:", Height2)
        print("Breadth:", Breadth1)
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter = Height1 + Height2 + Breadth1
        print("Perimeter of Triangle:", perimeter)

    def OddEven():
        data = int(input("Enter a number: "))
        if (data % 2) == 0:
            print(data, "is Even number")
        else:
            print(data, "is Odd number")
        return data

    def percentage():
        Subject1 = 98
        Subject2 = 87
        Subject3 = 95
        Subject4 = 95
        Subject5 = 93

        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        print("Total :", Total)

        Percentage = (Total / 500) * 100
        print("Percentage :", Percentage)