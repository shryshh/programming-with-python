#Check whether a list is sorted

def sort_check(l):
    
    #checking whether the list is empty
    if len(l) == 0:
        print("list is empty")
        return

    #checking ascending sort:
    n=l[0]
    a_check=False
    for i in l:
        if i>n:
            a_check=True
            n=i
        elif i<n:
            a_check=False
            break
    if a_check==True:
        print("list is sorted (ascending)")


    #checking descending sort
    if a_check==False:
        n=l[0]
        d_check=False
        for i in l:
            if i<n:
                d_check=True
                n=i
            elif i>n:
                d_check=False
                break
        if d_check==True:
            print("list is sorted (descending)")
        
    #checking if there's only one element or if all elements are equal:
        if d_check==False:
            c=0
            for j in l:
                if j==l[0]:
                    c=c+1
            if c==1:
                print("list is sorted (there's only one element)")
            elif c==len(l):
                print("list is sorted (all elements are same)")
            else:
                print("list is not sorted")


#checking the logic
sort_check([1,3,5,7])
sort_check([1,1,3,4,4,5])
sort_check([1, 2, 3, 4, 5])
sort_check([5, 4, 3, 2, 1])
sort_check([1, 3, 2, 4, 5])
sort_check([3,3,3])
sort_check([3,3,3,4])
sort_check([3,3,3,2])
sort_check([3,3,3,2,4])
sort_check([4,4,4,4])
sort_check([1,3,2])
sort_check([])
sort_check([2,4])
sort_check([2,3,5,11,100])
sort_check([2,1,3])
sort_check([200,156,7,6,0,-7])
sort_check([-7,-6,-5])
sort_check([5])