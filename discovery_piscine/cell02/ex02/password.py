password = "Python is awesome"

string = input("Please enter your password : ")

if string != password:
    print("ACCESS DENIED.")

if string == password:
    print("ACCESS GRANTED.")