list2 = [1,2,3,4,5,3,8]
max_list2 = list2[0]
for i in list2:
    if i > max_list2:
        max_list2 = i
print(max_list2)


def max_num(list1):
    max_list1 = list1[0]
    for i in list1:
        if i > max_list1:
            max_list1 = i
    return max_list1

print(max_num([1,2,-1,4,5]))

class Max:
    def max_num(self, list1):
        max_list1 = list1[0]
        for i in list1:
            if i > max_list1:
                max_list1 = i
        return max_list1


max_numbers = Max()

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(max_numbers.max_num(numbers))


