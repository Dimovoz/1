grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_ = list(students)
list_.sort()

sA = list_[0]
sB = list_[1]
sJ = list_[2]
sK = list_[3]
sS = list_[4]

nA = sum(grades[0]) / len(grades[0])
nB = sum(grades[1]) / len(grades[1])
nJ = sum(grades[2]) / len(grades[2])
nK = sum(grades[3]) / len(grades[3])
nS = sum(grades[4]) / len(grades[4])

dict_ = {sA : nA, sB : nB, sJ : nJ, sK : nK, sS : nS }
print(dict_)