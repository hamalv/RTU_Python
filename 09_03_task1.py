num_list = []
while True:
    num = input(f"Ievadiet skaitli: ")
    if num == 'q' or num == 'Q':
        break
    else:
        num = float(num)
        num_list += [num]
        print(num_list)
        print(f"Top 3 min numbers are: {sorted(num_list)[:3]}")
        print(f"Top 3 max numbers are: {sorted(num_list, reverse=True)[:3]}")
print(num_list)
print(f"Top 3 min numbers are: {sorted(num_list)[:3]}")
print(f"Top 3 max numbers are: {sorted(num_list, reverse=True)[:3]}")
