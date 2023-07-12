dwarf_array = []

for i in range(7):
    dwarf_array.append(int(input()))
    if dwarf_array[i] >= 100:
        del dwarf_array[i]
        break

dwarf_array.sort(reverse=True)
print(dwarf_array[0])
print(dwarf_array[1])