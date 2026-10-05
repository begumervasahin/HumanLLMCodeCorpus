class_list = []
att_list = []
data = []
rows = 0
cols = 0
prob_0 = []
prob_1 = []
tmp_list = []
train = input('\nPlease input name of training dataset (with file extension): ')
test = input('\nPlease input name of test dataset (with file extension): ')
with open(train, 'r') as file:
    attributes = file.readline()
    for i in attributes.split()[:-1]:
        att_list.append(i)
    cols = len(att_list)
    for l in file:
        rows+=1
        class_list.append(l.split()[cols])
        data.append(l.split())
c0 = (class_list.count('0'))/len(class_list)
c1 = (class_list.count('1'))/len(class_list)
for i in range (0, cols):
    tmp_list = [row[i] for row in data]
    c_0_t_0_count = 0
    c_0_t_1_count = 0
    c_1_t_0_count = 0
    c_1_t_1_count = 0
    t_0_count = 0
    t_1_count = 0
    for j in range(0, rows):
        if(tmp_list[j] == '0'):
            t_0_count = t_0_count+1
            if(class_list[j] == '0'):
                c_0_t_0_count = c_0_t_0_count + 1
            else:
                c_0_t_1_count = c_0_t_1_count + 1
        if(tmp_list[j] == '1'):
            t_1_count = t_1_count + 1
            if(class_list[j] == '1'):
                c_1_t_1_count = c_1_t_1_count + 1
            else:
                c_1_t_0_count = c_1_t_0_count + 1
    prob_0.append((c_0_t_0_count/t_0_count))
    prob_0.append((c_0_t_1_count/t_0_count))
    prob_1.append((c_1_t_0_count/t_1_count))
    prob_1.append((c_1_t_1_count/t_1_count))
j = 0
print('P(C = 0): ' + str(c0))
for i in range (0, cols):
    print('P('+ att_list[i] + ' = 0|c = 0): '+ str("%.2f" % prob_0[j]) + ' P(' + att_list[i] + ' = 1|c = 0): '+ str("%.2f" % prob_0[j+1]), end = ' ')
    j = j + 2
print('\n\n')
j = 0
print('P(C = 1): ' + str(c1))
for i in range (0, cols):
    print('P('+ att_list[i] + ' = 0|c = 1): '+ str("%.2f" % prob_1[j]) + ' P(' + att_list[i] + ' = 1|c = 1): '+ str("%.2f" % prob_1[j+1]), end = ' ')
    j = j + 2
def getClass(row, prob_0, prob_1, c0, c1):
    row = list(map(int, row))
    p0 = c0
    p1 = c1
    for i in range (0, len(row)-1):
        j = i*2
        if(row[i] == 0):
            p0 = p0*prob_0[j]
            p1 = p1*prob_1[j]
        else:
            p0 = p0*prob_0[j+1]
            p1 = p1*prob_1[j+1]
    if(p1 > p0):
        return('1')
    else:
        return('0')
a_count = 0
for i in range(0, rows):
    c = getClass(data[i], prob_0, prob_1, c0, c1)
    if(c == class_list[i]):
        a_count = a_count+1
print('\n\nAccuracy on training set (' + str(rows) + ' instances) is: ' + str("%.2f" % ((a_count/rows)*100)))
class_list = []
att_list = []
data = []
rows = 0
cols = 0
with open(test, 'r') as file:
    attributes = file.readline()
    for i in attributes.split()[:-1]:
        att_list.append(i)
    cols = len(att_list)
    for l in file:
        rows+=1
        class_list.append(l.split()[cols])
        data.append(l.split())
a_count = 0
for i in range(0, rows):
    c = getClass(data[i], prob_0, prob_1, c0, c1)
    if(c == class_list[i]):
        a_count = a_count+1
print('\n\nAccuracy on test set (' + str(rows) + ' instances) is: ' + str("%.2f" % ((a_count/rows)*100)))