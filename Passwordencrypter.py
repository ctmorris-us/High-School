





## Make text file and test it##





import os


def closing_off_encrypted_file():
    os.chdir("/Users/Christopher/")
    file = open('file_name', 'w')
    for line in whole:
        for stuff in line:
            file.write(stuff)
            file.write('\n')
    file.close()

def reading_in_encrypted_file():
    global whole
    n = -1
    whole = []
    os.chdir("/Users/Christopher/")
    file = open('file_name' , 'r')

    for line in file:
        line = decrypt(line)
        t = 0
        if line[0] == 'F':
            whole.append([line])
            n += 1
        if line[0] == 'U' or line[0] == 'P':
            t = 1
            whole[n].append(line)
        if line[0] == 'Q':
            t = 3
            whole[n].append(line)
        if line[0] == 'A':
            t = 4
            whole[n].append(line)

        print('\t'*t + line)

    file.close()

def writing_in_encrypted_file():

    man = False

    while True:
        print('Would you like to add, delete, or change anything (y/n)?')
        if y_n():
            man = True
        else:
            print('Okay.')
        break

    while man == True:
        print("would you like to add a new entry (y/n)? ")
        if y_n():
            writing_in_new_info()
        break
                    ##Stops while loop
    while man == True:
        print("Would you like to delete an entry (y/n) ")
        if y_n():
            deleting_info()
        break

    while man == True:
        print("would you like to change an entry (y/n) ")
        if y_n():
            changing_info()
        break

    if man == True:
        print('Would you like to add, delete, or change anything else (y/n)?')
        if y_n():
            writing_in_encrypted_file()
        else:
            print('Okay.')

    return

def writing_in_new_info():

    a = 'name for the information'
    a = 'F: ' + writing_in(a)
    b = 'username'
    b = 'U: ' + writing_in(b)
    c = 'password'
    c = 'P: ' + writing_in(c)

    print('Are there any security questions (y/n)?')
    if y_n():
        print('How many security questions (i.e. 5)')
        z = input()
        z = z.strip()
        z = int(z)
    else:
        z = 0

    Q = []
    A = []
    for value in range(z):
        sn = str(value + 1)
        q = 'security question ' + sn
        q = 'Q' + sn + ': ' + writing_in(q)
        Q.append(q)
        aa = 'security answer ' + sn
        aa = 'A' + sn + ': ' + writing_in(aa)
        A.append(aa)

    print('Here is what you typed overall.')
    print(a)
    print(b)
    print(c)
    for val in range(len(Q)):
        print(Q[val])
        print(A[val])
    print('Does this look right (y/n)?')

    if y_n():
        print('Perfect.')
    else:
        print('Okay we are going to go through the process again.')
        a, b, c, Q, A = writing_in_new_info()

    temp = [a,b,c]
    if len(Q) != 0:
        for val in range(len(Q)):
            temp.append(Q[val])
            temp.append(A[val])
    whole.append(temp)

    print('Would you like to add anything else (y/n)?')
    if y_n():
        writing_in_new_info()
    return

def writing_in(name):

    cont = True
    print('Please type in what you would like the ' + name + ' to be.')
    z = input()
    z = z.strip()

    while cont == True:
        print('You typed ' + z + ' is this correct (y/n)?')
        if y_n():
            break
        else:
            print('Sorry the ' + name + ' did not match, please type in the ' + name + ' again.')
            z = input()
            z = z.strip()
            continue
    return(z)

def deleting_info():
    kep = True
    cont = True

    print ('Please type in the name for the information that you would like to delete.')
    z = input()
    z = z.strip()
    z = z.lower()

    definites = []
    tests = []
    n = 0

    for line in whole:
        if line[0][3:].lower().strip() == z:
            definites = [line, n]
        elif line[0][3:6].lower().strip() == z[0:3]:
            tests.append([line, n])
        n+=1

    if len(definites) != 0:
        print('There is an entry for: ' + str(definites[0][0][3:]) + ' is this what you want to delete (y/n)?')
        if y_n():
            delete_info(definites)
            print('Would you like to delete something else (y/n)?')
            if y_n():
                deleting_info()
            return

    if len(tests) == 0:
        print('There are no possible matches, please look at the list again.')
        print('Would you like to continue to try to delete something (y/n)?')
        if y_n():
            deleting_info()
            return
        else:
            return
    else:
        print('There are ' + str(len(tests)) + ' possible matches. \n'
        'Is what you want to delete any of these (y/n)?')
        for ([entry, n]) in tests:
            print('\t'+ entry[0])
        if y_n():
            print('Which one would you like to delete?')
            while True:
                z = input()
                z = z.strip()
                z = z.lower()
                for ([entry, n]) in tests:
                    if entry[0][3:].lower().strip() == z:
                        del_place = [entry, n]
                        delete_info(del_place)
                        print('Would you like to delete something else (y/n)?')
                        if y_n():
                            deleting_info()
                        return
                print('Sorry the entry ' + z + ' you inputed is not in the list, \n'
                    'please try again.')
                continue
        else:
            print('Okay')
    return

def changing_info():
    cont = True
    kep = True

    print ('Please type in the name for the information that you would like to change (Not Case Sensitive).')
    z = input()
    z = z.strip()
    z = z.lower()

    tests = []
    positives = []
    n = 0
    for line in whole:
        if line[0][3:].lower().strip() == z:
            positives = [line, n]
        elif line[0][3:6].lower().strip() == z[0:3]:
            tests.append([line, n])
        n+=1

    if len(positives) != 0:
        print('There is an entry for ' + str(positives[0][0][0][3:]) + ' is this what you want to change (y/n)?')
        if y_n():
            line, n = change_info(positives)
            whole[n] = line
        else:
            pass

        print('Is there any other information that you would like to change (y/n)?')
        if y_n():
            changing_info()
            return


    print('There are ' + str(len(tests)) + ' possible matches. \n'
    'Is what you want to change any of these (y/n)?')
    for ([entry, n]) in tests:
        print('\t'+ entry[0])
    if y_n():
        print('Which one would you like to change?')
        while True:
            z = input()
            z = z.strip()
            z = z.lower()
            for ([entry, n]) in tests:
                if entry[0][3:].lower().strip() == z:
                    change_place = [entry, n]
                    line, n = change_info(change_place)
                    whole[n] = line
                    print('Is there any other information that you would like to change (y/n)?')
                    if y_n():
                        changing_info()
                        return
            print('Sorry the entry (' + z + ') you inputed is not in the list, \n'
            'please try again.')
            continue

    else:
        print('Okay')
    print('Is there any other information that you would like to change (y/n)?')
    if y_n():
        changing_info()
    return

def change_info(change_place):

    cont = True

    temp_change = change_place[0]
    temp_place = change_place[1]

    print('Here is the info for ' + str(temp_change[0]) + '.')
    for line in temp_change:
        print(line)

    print('Please select what you would like to change by typing \n'
    '"F", "U", "P", (and if there are questions) Q#, or A#.')

    while True:

        z = input()
        z = z.strip()
        z = z.lower()

        if z[0] not in ['f','u','p','q','a']:
            print('You did not select a valid response, please try again.')
            continue
        elif (len(z) == 2) and (z[0] in ['p','q']) and (z[1] not in ['1', '2', '3', '4', '5', '6', '7','8','9']):
            print('Please Follow the form for questions and answers as Q# or A# with # being the number.')
            continue
        else:
            if z[0] == 'f':
                thing_to_change = 0
            elif z[0] == 'u':
                thing_to_change = 1
            elif z[0] == 'p':
                thing_to_change = 2
            elif z[0] == 'q':
                thing_to_change = 3 + 2 * (int(z[1]) - 1)
            elif z[0] == 'a':
                thing_to_change = 4 + 2 * (int(z[1]) - 1)
            else:
                pass

            if len(temp_change) < thing_to_change:
                print('What you selected is not in the scope of what is available to change.')
                print('Please try again.')
                continue
            break
    if len(temp_change) >= (thing_to_change + 1):

        print('Please type what you would like the new information to be (This is case sensitive).')
        while True:
            z = input()
            z = z.strip()

            print('You typed: ' + z)
            print('Is this correct (y/n)?')
            if y_n():
                temp_change[thing_to_change] = z
                print('The information has been changed.')
                break
            else:
                print('Please retype what you would like the information to be (case sensitive).')
                continue


    print('Would you like to change anything else within this section? (y/n)?')
    if y_n():
        avail = [temp_change, temp_place]
        temp_change, temp_place =  change_info(avail)
    else:
        print('Okay')

    print('All information has been changed ')
    return(temp_change, temp_place)

def delete_info(place):
    del whole[place[1]]
    print("\nThe information for " + place[0][0][3:] + 'was deleted.')
    return

def encrypt(line):
    return(line)
    x = list(map(ord, line))
    new = [x[0]]
    for value in range(len(x)-1):
        y = abs(x[value + 1] - x[value])
        new.append(y)
        new.append(x[value+1])

def decrypt(line):
    return(line)
    ###encryption function
def y_n():
    yes = {'yes','y', 'ye', ''}
    no = {'no','n'}

    while True:
        x = input()
        x = x.lower()
        if x in yes:
            return True
        elif x in no:
            return False
        else:
            print('Not a valid response try again. Type either "y" or "n"')
            continue



if __name__ == "__main__":

    reading_in_encrypted_file()
    writing_in_encrypted_file()
    closing_off_encrypted_file()
