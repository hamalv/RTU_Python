temp = input(f"Ievadiet temperaturu\n")
temp = float(temp)
if temp < 35:
    cold = input("Nav par aukstu? (Y/N)\n")
    if cold.upper() == 'Y':
        print("Lietotajam ir auksts")
    elif cold.upper() == 'N':
        print("Lietotajam nav auksts")
elif temp > 35 and temp <= 37:
    print("viss kartiba")
elif temp > 37:
    print("Iespejams drudzis")
else:
    print(f"Ha haa... Sads parametrs {temp} neder")