import random
u_test=0
sc_rm=[]
sc_ml=[]
rm_c=0
ml_c=0
while u_test<100:
    n = random.randint(2,10)
    #print(n)
    task=[]
    M=[]
    delta=6
    C_worst=[]
    smc=0
    c_total=0
    t=random.randint(50,100)
    for i in range(0,n):
     pair=[]
     W=random.randint(2,20)
     L=W
     w=[]
     c=random.randint(10,50) 
     cs=W/delta
 
     if (int(cs)==cs):
         ca=c+cs
         smc=smc+cs
     else:
         ca=c+int(cs)+1
         smc=smc+int(cs)+1
     #print(ca)
     C_worst.append(ca)
     c_total=c_total+ca
     #print(task)
     #print("weight", W)
     #print("weight", M)
     for i in range (L):
        w.append(W/L)
     M.append(w)
     pair.append(int(c))
     pair.append(int(t))
     pair.append(w)
     task.append(pair)
    task.sort(key=lambda x:x[1])
    #print(task)
    #print(C_worst)
    #print(c_total)
    #print("weight", w)
    #print("weight", M)
    #print(C_worst)
    sum=0
    set_counter=0
    k=0
    i=0
    while i<n:
        #print("its i in line 29",i)
        #if(k==1):
         #   i=i-1
          #  set_counter=set_counter+1   
        j=len(task[i][2])
        if(j==0):
            #break
            i=i+1
        #print("its j",j)
        while j>0:
            j=j-1
            sum=sum+task[i][2][j]
            sum1=sum+task[i][2][j]    
            hold=task[i][2]
           # print(hold)
            hold.pop(0)
            #print(hold)
            #print(task[i])
            #print(sum)
            #if (j==0 and sum1<delta):
             #   j=j=len(task[i][2])
              #  i=i+1
            if sum1>delta:
                k=1
                #i=i+1
                #print("its i",i)
                set_counter=set_counter+1
                sum=0
                break
            if (j==0):
                i=i+1
        
    if (sum1<=delta):
        set_counter=set_counter+1
        #print("its set_counter",set_counter)
    else:
        set_counter=set_counter
        #print("its set_counter",set_counter)

    #print("its SMC",smc)
    n_save=smc-set_counter
    #print("its SMC save", n_save)
    u=0
    for i in range(0,n):
        u=u+(task[i][0]/task[i][1])
            #u=(n*((2**(1/n))-1))
    u= round(u, 2)
    #print(u)
    #tasktable(task,n,lcm,SC)
    if (u!=1):
        continue
    else:
        u_test=u_test+1
        if(c_total<=t):
            #print("its RM Schedulable");
            sc_rm.append(1)
            rm_c=rm_c+1
        if(c_total-(n_save*2)<=t):
            #print("its also ML schedulable")
            sc_ml.append(1)
            ml_c=ml_c+1

#print(sc_rm)
#print(sc_ml)
print(rm_c)
print(ml_c)