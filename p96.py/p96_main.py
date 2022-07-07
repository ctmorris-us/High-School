import os
import copy

os.chdir(.../Users/Christopher/Programming_Projects/Euler Project)



file = open('p96_sudoku.txt', 'r')
import copy
trials = []
NE_Removed = []
Removed = []
turn = 0
sudoku = []
info = []
Rows_v = []
Columns_v = []
Rows_0 = []
Partitions = []
z, n_v, i_v = 0,0,0
Sudoku_play = True
NE_recursed = []
LA_Removed = []

def init_sudoku(file):
    global Removed, NE_Removed, turn, sudoku, info, Rows_v, Columns_v, Rows_0, Partitions,z, Sudoku_play, NE_recursed,LA_Removed
    Sudoku_play = True
    Removed = []
    NE_Removed = []
    NE_recursed = []
    LA_Removed = []
    info = []
    turn = 0
    sudoku = []
    Rows_v = []
    Columns_v = []
    Rows_0 = []
    Partitions = []
    file.readline()
    #initiating the sudoku puzzle in a class
    for n in range(9):
        s = file.readline()
        s = s.strip()
        S = [int(alpha) for alpha in iter(s)]
        sudoku.append(S)
        S = set(S)
        S.remove(0)
        Rows_v.append(S)
    #initializing partitions
    c = 0
    v = 0
    Partitions = []
    parts = []
    t = [(0,3,0,3),(0,3,3,6),(0,3,6,9),(3,6,0,3),(3,6,3,6),(3,6,6,9),(6,9,0,3),(6,9,3,6),(6,9,6,9)]
    for k,l,n,m in t:
        P_temp = [sudoku[rowd][i] for i in range(n,m) for rowd in range(k,l)]
        P_temp = set(P_temp)
        P_temp.remove(0)
        parts.append(P_temp)
        v+=1
        if v == 3:
            Partitions.append(parts)
            parts = []
            v = 0
    #Initiating the rows C of number
    for i in range(9):
        r = []
        for row in sudoku:
            r.append(row[i])
        r = set(r)
        r.remove(0)
        Columns_v.append(r)
    #Finding Row of Zeros Using Indices of the Zeros
    for i in range(9):
        I = []
        for j in range(9):
            if sudoku[i][j] == 0:
                I.append(j)
        Rows_0.append(I)
    #Creating Info list
    info = []
    set_init = {1,2,3,4,5,6,7,8,9}
    q = 0
    h = 0
    z = 0
    sudoku_edit = copy.deepcopy(sudoku)

    for n in range(9):
        if n<= 2:
            q = 0
        elif n<=5:
            q = 1
        else:
            q = 2
        for i in Rows_0[n]:
            if i<=2:
                partition = Partitions[q][0]
                h = 0
            elif i<=5:
                partition = Partitions[q][1]
                h = 1
            else:
                partition = Partitions[q][2]
                h = 2
            row = Rows_v[n]
            column = Columns_v[i]
            pv_temp = set_init - (row|column|partition)
            sudoku_edit[n][i] = pv_temp
            length = len(pv_temp)
            values_p = list(pv_temp)
            values_pi = copy.deepcopy(values_p)
            y = 0
            exec('pv_%s%s = pv_temp' %(n,i))
            info.append([length, values_p, n, i, q, h, y, z, values_pi])
            z += 1


        
        
def find_index():

    global info, turn, Removed, Sudoku_play, NE_Removed, LA_Removed, trials,n_v,i_v
    length_v= 10
    n_v = 0 
    i_v = 0
    z_z = 0 
    removal = 0
    index = []
    removed_from = []

    for values in info:
        if values[0] <= 0 and len(values[1]) == 0:

            Recurse()
            return
        elif 0 < values[0] <= length_v and values[6] < values[0]:

            length_v = values[0]
            n_v = values[2]
            i_v = values[3]
            index = [values[2], values[3], values[4], values[5]]
        else:    
            z_z += 1
    if z_z == z:
        Sudoku_play == False
        return

    if length_v != 10:
        for values in info:
            if values[2] == n_v and values[3] == i_v:
                removal = values[1][values[6]]
                values[1].remove(removal)
                temp_list = values[1]
                values[1] = [removal]
                values[6] += 1
                values[0] = 0
                removed_from.append((values[2], values[3]))
                NE_Removed.append([temp_list, removal, n_v, i_v, values[4], values[5], values[6], turn])
                LA_Removed.append([temp_list, removal, n_v, i_v, values[4], values[5], values[6], turn])
                turn += 1

        for values in info:
            if values[2] == n_v and values[3] != i_v and removal in values[1]:
                values[1].remove(removal)
                values[0] = len(values[1])
                removed_from.append((values[2], values[3]))

            elif values[3] == i_v and values[2] != n_v and removal in values[1]:
                values[1].remove(removal)
                values[0] = len(values[1])
                removed_from.append((values[2], values[3]))

            elif values[4] == index[2] and values[5] == index[3] and values[2] != n_v and values[3] != i_v and removal in values[1]:
                values[1].remove(removal)
                values[0] = len(values[1])
                removed_from.append((values[2], values[3]))
            else:
                continue

        Removed.append([temp_list, removal, n_v, i_v, values[4], values[5], values[6], turn, removed_from])




def Recurse():
    global Removed, info, Row_v, Column_v, Partitions,NE_recursed, LA_Removed
    id_adding = 0
    R_temp = Removed.pop()
    LA_Removed.pop()
    recursed = [R_temp[1], R_temp[2], R_temp[3], R_temp[4], R_temp[5], R_temp[7]]
    NE_recursed.append(recursed)
    m = -1

    for (k, l) in R_temp[8]:
        for values in info:
            if values[2] == k and values[3] == l:
                m +=1
                if m == 0:
                    values[1] = [R_temp[1]] + R_temp[0]
                    values[0] = len(values[1])
                    id_adding = info.index(values)
                else:
                    values[1].insert(0, R_temp[1])

    if len(R_temp[0]) == 0 or (len(R_temp[0]) + 1) < R_temp[6]:
        info[id_adding][6] = 0 
        Recurse()
    

def finalize():
    final_sudoku = copy.deepcopy(sudoku)
    for values in info:
        final_sudoku[values[2]][values[3]] = int((values[1])[0])
    for line in final_sudoku:
        print(line)



tt = 0
while Sudoku_play is True:
    find_index()
    tt += 1
    if tt % 10 == 0:
        print('still going')
print('done')
finalize()


for x in range(25):
    find_index()
LA_Removed
Removed
NE_Removed
NE_recursed

for items in Removed:
    if items[2] == n_r and len(items[0]) == 0:
        recT = False
    if items[3] == i_r and len(items[0]) == 0:
        recT = False
    if items[4] == q_r and items[5] == h_r and len(items[0]) == 0:
        recT = False

if recT == True:

    n_r, i_r = R_temp[2], R_temp[3]
    q_r, h_r = R_temp[4], R_temp[5]
    if values[2] == n_r and values[3] == i_r:
        id_adding = info.index(values)
        recursed_value = [R_temp[1]] + R_temp[0]
        values[1] = recursed_value
        values[0] = len(values[1])

    for values in info:
        if values[2] == n_r and values[3] != i_r and R_temp[1] in values[8]:
            if values[1].count(R_temp[1]) < 1:
                values[1].insert(0, R_temp[1])
                values[0] = len(values[1])

        if values[3] == i_r and values[2] != n_r and R_temp[1] in values[8]:
            if values[1].count(R_temp[1]) < 1:
                values[1].insert(0, R_temp[1])
                values[0] = len(values[1])

        if values[4] == q_r and values[5] == h_r and values[2] != n_r and values[3] != i_r and R_temp[1] in values[8]:
            if values[1].count(R_temp[1]) < 1:
                values[1].insert(0, R_temp[1])
                values[0] = len(values[1])