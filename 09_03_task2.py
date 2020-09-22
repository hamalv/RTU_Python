num1 = int(input("Ievadiet pirmo skaitli: "))
num2 = int(input("Ievadiet otro skaitli: "))
num_list = []

if num2 < num1:
    print("Paldies, ka piedalījies, bet šāda kombinācija nevar pastāvēt.")
else:
    while num1 <= num2:
        sq = num1**2
        print(f"{num1} kuba ir: {sq}")
        num_list.append(sq)
        num1 += 1
    print(f"Visi kubi {num_list}")