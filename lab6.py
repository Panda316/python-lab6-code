#All the files are pushed in github repository 
#This statement import all the functions of file Library.py 
#We can also import functions as needed by replacing * with function names

from Library import *;

def main():
    print("Parth Prajapati \n 90541124369\n")

if __name__=="__main__":

    #In all the programs below, functions that are written in Library.py file return some values of output and it's printed via calling the function in print function 

    #Program 1 
    print("Milege per Gallon is",calculateMpg(200,10))
    #Program 2 
    print("The are of circle is",calculateAreaOfCircle(50))
    #Program 3
    print("The ditance between two points is ",calculateDistanceBetweenPoints(12,15,25,50))
    #Program 4
    print("Farenhit : ",toFarenhit(40))