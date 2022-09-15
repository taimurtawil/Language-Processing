def concat(firstlist, secondlist):
    for i in secondlist:
        firstlist.append(i)
    return firstlist

test_list1 = [1, 2, 3, 4, 5]
test_list2 = [6, 7, 8, 9, 10]

print(concat(test_list1, test_list2))