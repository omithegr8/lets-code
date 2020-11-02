feet = float(input(' enter your height in foot : '))
type = input(" enter a number in meter/cm/mmww   : ")

if type == 'meter':
    print(feet * 0.3048)

elif type == "cm":
    print(feet * 30.48)

elif type == "mm":
    print(feet * 304.8)

else :
    print("u have enter wrong input!!")
