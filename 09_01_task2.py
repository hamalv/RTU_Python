import os
vards = input(f"Ievadiet vardu\n")
clear = lambda: os.system('clear')
clear()
print(vards.replace(len(vards),'*'))