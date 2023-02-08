list1 = ['Oscar','Johan', 'Johanna','Bill', 'Axel' ]
list2 = list1.copy()
list2.reverse()
print(list2)
element1 = [list2[0]]
print(element1)
list1.insert(3, element1)
print(list1)
print(list1.count(element1))

nummer = [50, 96, 85, 58, 60]
nummer.append