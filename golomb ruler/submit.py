#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L
import sys


maxConflictedVar=[]

def BT(L, M):
    marks=[]
    flag=True
    counter=0
    domainVals=[i for i in range(0,length+1)]
    result,counter=RecBT(L, M,marks,domainVals,flag,counter)
    
    return result,counter

#Your backtracking function implementation
def RecBT(L, M,marks,domainVals,flag,counter):
    "*** YOUR CODE HERE ***"
    #if assignment is complete then return assignment
    if len(marks)==M:
        
        result=marks       
        return result,counter
    else:
        # iterate over all domain Values
        for val in domainVals:
            
            if flag== True:
                domainVals.remove(val)
            # runs recursively if value is consistent with the assignment
            if checkConstraints(marks,val)== True:
                     counter+=1
                     marks.append(val)
                     result,counter=RecBT(L,M,marks,domainVals,flag,counter)
                     if len(result)==M:
                         return result,counter
            #if domainVals has just one value left      
            if len(domainVals)==1:
                 
                 flag=False
                 domainVals=[i for i in range(0,length+1) if i not in marks]
                 #pops the last element
                 result=marks[:-1]                         
                 counter+=1
                 result,counter=RecBT(L,M,result,domainVals,flag,counter)
                 
                 if len(result)==M:
                   return result,counter
    return marks,counter
            
         
 

def checkConstraints(checkMarks,val):
    
   
    checkMarks.append(val)
    checkConstraintOutput=[]

    # 1.marking starts at 0 and should end at length
    
    if checkMarks[0]==0:
        checkConstraintOutput.append(1)
    else:
        checkConstraintOutput.append(0)
    
   
    
    # 2. value of marks should be ascending order 
    for i in range(len(checkMarks)-1):
        
        if checkMarks[i] < checkMarks[i+1]:
            checkConstraintOutput.append(1)
        else:
            checkConstraintOutput.append(0)
            
        

    # 3. distances between marks should be different
    distances = []
    for i in range(len(checkMarks)-1):
        for j in range(i + 1, len(checkMarks)):
            distances.append(checkMarks[j] - checkMarks[i])
    
    if  len(distances) == len(set(distances)):
        checkConstraintOutput.append(1)
    else:
        checkConstraintOutput.append(0)

    
    #print('ou',checkConstraintOutput)
    if checkConstraintOutput.count(0)>=1:
        checkMarks.remove(val)
        return False
    else:
        checkMarks.remove(val)
        return True
    
def FCcheckConstraints(checkMarks):
    
   
    
    checkConstraintOutput=[]

    # 1.marking starts at 0 and should end at length
    
    if checkMarks[0]==0:
        checkConstraintOutput.append(1)
    else:
        checkConstraintOutput.append(0)
    
   
    
    # 2. value of marks should be ascending order 
    for i in range(len(checkMarks)-1):
        
        if checkMarks[i] < checkMarks[i+1]:
            checkConstraintOutput.append(1)
        else:
            checkConstraintOutput.append(0)
            
        

    # 3. distances between marks should be different
    distances = []
    for i in range(len(checkMarks)-1):
        for j in range(i + 1, len(checkMarks)):
            distances.append(checkMarks[j] - checkMarks[i])
    
    if  len(distances) == len(set(distances)):
        checkConstraintOutput.append(1)
    else:
        checkConstraintOutput.append(0)

    
    #print('ou',checkConstraintOutput)
    if checkConstraintOutput.count(0)>=1:
        
        return False
    else:
       
        return True      

#Your backtracking+Forward checking function implementation
def FC(L, M,counter):

    # adds all legal values to assignments
    marks=[[i for i in range(1,L+1)] for j in range(0,M)]
    conflictedVars=[]
     
       
    checkMarks=[]
    checkMarks.append(0)
    for mark in marks:        
        for val in mark:           
           if (val not in conflictedVars and val not in maxConflictedVar)and val not in checkMarks:
                checkMarks.append(val)
                # removes values which are not consistent with the assignment
                if FCcheckConstraints(checkMarks)== True:
                    counter+=1
                    removeValues(val,marks)
                    break
                else:                                      
                    conflictedVars.append(val)
                    
                    checkMarks.remove(val)
    
    if checkMarks[-1] not in maxConflictedVar:
        maxConflictedVar.append(checkMarks[-1])

    #checks whether the assignment is complete
    
    if len(checkMarks)==M:
       
        print('Forward Checking result:', checkMarks)
        print('Consistency Check', counter)
        return checkMarks,counter
    else:
        # iterates if the assignment is not complete
        FC(L,M,counter)
   
    


    
    "*** YOUR CODE HERE ***"
   
def removeValues(val,marks):
    for mark in marks:       
        mark.remove(val)
        

#Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]


if __name__ == "__main__":
    print('First enter order and then length values')
    
    if len(sys.argv) > 2:
        #order = int(sys.argv[1])
        #length= int(sys.argv[2])

        order = int(sys.argv[2])
        length= int(sys.argv[1])

        
         
        BTresult,counter=BT(length,order)
    
        print('BackTracking result:',BTresult)
        print('Consistency Check',counter)
   
        FC(length,order,0)

