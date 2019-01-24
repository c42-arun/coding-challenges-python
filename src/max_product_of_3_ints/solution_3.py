L = [15, 10, 7, 8, 5, 11, 12, 9, 6, -12, -13]

asc_items = L[0:3] 
desc_items = L[0:2] # with two max -ve values we get a +ve

asc_items.sort(reverse=True)
desc_items.sort()

  = asc_items[0] * asc_items[1] * asc_items[2]
max_prod_desc = (desc_items[0] * desc_items[1]) * asc_items[0]

highest = asc_items[0]
second_highest = asc_items[1]

lowest = desc_items[0]
second_lowest = desc_items[1]

print(f"{max_prod_3} - {highest}, {second_highest} - {lowest}, {second_lowest} ")

for i in L[3:]:
    current_max_prod_asc = i * highest * second_highest
    current_max_prod_desc = i * lowest * second_lowest

    if (current_max_prod_asc > max_prod_3):
        max_prod_3 = current_max_prod_asc

        # see if we need to reset max 2 items
        if (i > highest):
            second_highest = highest
            highest = i
        else if (i > second_highest):
            second_highest = i

    if (cur)
    
