from linearSearch import LinearSearch
from Student import Student

data = [24, 18, 12, 9, 16, 66, 32, 4]
res = LinearSearch.search(data,18)
print(res)

data1 = [22, 22.1, 22.3]
res1 = LinearSearch.search(data1, 22.3)
print(res1)

s1 = Student('Alice')
s2 = Student('Bobo')
s3 = Student('Charles')
students = [s1, s2, s3]
Bobo = Student('Bobo')
print(LinearSearch.search(students, Bobo))
