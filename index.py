#password generator 

import random

#alphabet = "abcdefghijklmonpqrstuvwxyz"
#set2 = "abcdefghijklmonpqrstuvwxyzABCDEFGHIJLKMNOPQRSTUVWXYZ"
#set3 = "abcdefghijklmonpqrstuvwxyzABCDEFGHIJLKMNOPQRSTUVWXYZ0123456789!@#$%^&*()"


#list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#list2 = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#list3 = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#list4 = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']



list5 = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 
         [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
         [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']]


def main():
    size = int(input("size of password "))
    password = ""
    for x in range(size):
        index1 = random.randint(0,3)
        i = len(list5[index1]) - 1
        index2 = random.randint(0,i)
        print('index1: ', index1, " i: ", i, " index2: ", index2 )
        password += list5[index1][index2]

    print(password)


main()
    