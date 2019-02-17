with open("C:/Beslenme/Template.xlsx","rb") as f:
    a = f.read()
    print(a.decode("utf-8","replace"))