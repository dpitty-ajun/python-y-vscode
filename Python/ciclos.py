print("BREAK")
for contador in range(1, 10):
    if contador % 2 == 0:
        break
    print(contador)


print("\nCONTINUE")
for contador in range(1, 10):
    if contador % 2 == 0:
        continue
    print(contador)
