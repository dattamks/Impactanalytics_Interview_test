import itertools
def interview_test(n):
    
    
    x = list(itertools.product([0,1],repeat = n))   

    # function to check sequence
    def count_sequence(lst, seq):
        status = False
        len_seq = len(seq)
        upper_bound = len(lst)-len_seq+1
        for i in range(upper_bound):
            if lst[i:i+len_seq] == seq:
                status = True
        return status
    # function to separate entries with more than 4 absents continiously
    def total_ways(n,x):
        total_ways = 0
        new_x = []
        y = []
        if n<=4:
            total_ways = 0
            
        else:
            for i in range(len(x)):
                if count_sequence(x[i],(0,0,0,0)) == True:
                    total_ways +=1
                else:
                    new_x.append(x[i])

        # loop through previous output and chech if candidate is absent on day on ceremony
        count = 0
        for i in new_x:
            if i[len(i)-1] == 0:
                count +=1
        return total_ways,new_x,count

        
    total_ways,new_x,count = total_ways(n,x)



    #print(count)
    print("{}/{}".format(count,len(x)-total_ways))

# collect input
while True:
    try:        
        n = int(input("Enter some numerical value(Ex:1,5,18...): "))
    except ValueError:
        print("Sorry, Invalid Input.")
        #better try again... Return to the start of the loop
        continue
    else:        
        break



# cal function
interview_test(n)