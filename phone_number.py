#For command Line Arguments
import sys

#Getting the input passed from the command line arguments

number = sys.argv[1] 

#Function for finding the Consecutive Repeating numbers
#Function will accept phone number as string
def printRLE(s): 
    list1=[]  
    i = 0
    count1=0
    #checking the initial condition to procees
    if len(s)<2:
        print("Not enough numbers")
    while( i < len(s)-1) : 
        # Counting occurrences of s[i] 
        count = 1
        while s[i] == s[i + 1] : 
            i += 1
            count += 1
            if i + 1 == len(s): 
                break
        list1.append(str(count))
        
        if count!=1:
            print(str(s[i])+"--> "+str(count)+" Times",end = "")
            print ('\n')
        i += 1
    for i in range(0,len(list1)):
        if (list1[i]=='1'):
            count1=count1+1;
    if count1==len(list1):
        print("No consecutive repeated characters in the Phone number")  
  
# Driver Code 
if __name__ == "__main__":  
    # function calling  
    printRLE(number) 
