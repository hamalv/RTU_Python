
num = int(input(f"ievadiet skaitli\n"))
y = 0
for x in range(2,num):
    if num%x > 0:
        y+=1
if y > 0:
    print("Nav pirmskaitlis")
else:
    print("Pirmskaitlis")
    

