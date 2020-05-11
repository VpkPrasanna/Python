#Defining empty list for each csv file 
matrix = []
united_states = []
great_britain = []
france = []
male = []
female = []

#Task1
#Reading the file
with open('example_XLS_file.txt') as source:
    for line in source:
            fields = line.split('\t')
            matrix.append(fields)

#Taking only the rows of based on country names
for i in range(len(matrix)):
    if matrix[i][4] == "United States":
        united_states.append(matrix[i])
    elif matrix[i][4] == "Great Britain":
        great_britain.append(matrix[i])
    elif matrix[i][4] == "France":
        france.append(matrix[i])

#Taking only the male and female rows
for i in range(len(matrix)):
    if matrix[i][3] == "Male":
        male.append(matrix[i])
    elif matrix[i][3] == "Female":
        female.append(matrix[i])

#converting the list of list to csv for united states data
with open('united_states.csv','w') as f:
    for row in united_states:
        for x in row:
            f.write(str(x) + ',')
        f.write('\n')
#converting the list of list to csv for great_britain data
with open('great_britain.csv','w') as f:
    for row in great_britain:
        for x in row:
            f.write(str(x) + ',')
        f.write('\n')
#converting the list of list to csv for France data
with open('france.csv','w') as f:
    for row in france:
        for x in row:
            f.write(str(x) + ',')
        f.write('\n')
#converting the list of list to csv for Male data
with open('male.csv','w') as f:
    for row in male:
        for x in row:
            f.write(str(x) + ',')
        f.write('\n')
#converting the list of list to csv for Female data
with open('female.csv','w') as f:
    for row in female:
        for x in row:
            f.write(str(x) + ',')
        f.write('\n')


#Task2
#These header value have been found from readind the header data of the file (xls file)
#i[3] represents Gender Column
same = matrix
#sorting based on Gender
new = sorted(same,key=lambda i: i[3])
#sorting based on Country
#i[4] represents Country Column
new1 = sorted(new,key=lambda i: i[4])
#sorting based on Age
#i[5] represents Age Column
new2 = sorted(new1,key=lambda i: i[5])


#converting the list of list to csv for Soeted data data
with open('sorted3.csv','w') as f:
    for row in new2:
        for x in row:
            f.write(str(x) + ',')
