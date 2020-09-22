age = input(f"Ludzu ievadiet stazu\n")
sal = input(f"Ludzu ievadiet savu menesalgu\n")

age = int(age)
sal = float(sal)

must_have = 2

if age < must_have:
    print("Jums bonuss nepienakas.")
else:
    if sal < 0:
        print("Alga nevar but mazaka par 0")
    else:
        bonus_15 = sal * 0.15
        bonus_total = bonus_15 * (age - must_have)
        print(f"Bonusa 15% ir {bonus_15} un kopejais bonusa apmers is {bonus_total}")
