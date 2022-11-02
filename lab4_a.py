#Write a program that writes to a file the numbers from 1 to 100, and their squares and
#square roots, as a table as shown below. Calculate the width of columns and use the
#appropriate format options when writing the numbers. Write the square root with 3 digits
#after the decimal point.

import math
def main():
    file = open ("square.txt", "w")
    print("Number : Squared : Sq.root:", file=file)
    print("...... : ....... : .......:", file =file)
    for num in range (1, 101):
        column_1 = num
        column_2 = pow(num,2)
        column_3 = round(math.sqrt (num),3)
                                  
        print ( column_1," "*(5-len(str(column_1))),":", column_2," "*(6-len(str(column_2))),":",column_3," "*(6-len(str(column_3))),":", file=file)
   file.close()
   print("I have finished this file")

main()




#Version 2

import math
def numbers():
    print("Starting the Process")
    myfile = open("numbers2.txt", "w")
    myfile.write("Number Squared Sq. Root\n")
    myfile.write("------ ------- --------\n")
    
    for i in range(1,101):
        myfile.write('%6d %7d %7.3f' % (i, i*i, math.sqrt(i)))
        myfile.write ("\n")

    myfile.close()
    print("Finished writing the file")

    
numbers()

