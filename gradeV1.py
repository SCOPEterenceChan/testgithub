from Student import Student
from Student121V0 import Student121
import matplotlib.pyplot as plt

studentList = []

fileIn = open('markdata.dat', 'r')
line = fileIn.readline()
lineNum=0
while line != '':
    studentList.append(Student121(line))
    line = fileIn.readline()
    
for e in studentList:
    print(Student.__str__(e))

fig = plt.figure(figsize=(10,8))    # width x height in inches
ax1 = fig.add_subplot(111)
         
gradeFeq = {'A':0,'B':0,'C':0,'D':0,'F':0}
                        
ax1.bar(['A','B','C','D','F'],[4,2,2,0,3])
                
ax1.set_xlabel('Grade')
ax1.set_ylabel('Student Numbers')
ax1.set_title('Grade Distribution')

plt.show()

fileIn.close()  