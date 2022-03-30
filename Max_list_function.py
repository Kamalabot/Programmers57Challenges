#Max of the list function
from typing import List

def chek_biglist(num_list:List[float]) -> float:
    """Function takes in a list of numbers and provides
    the biggest number in it"""
    tmp_1 = 0 #external var from the loop
    tmp_2 = 0
    ind = 0

    l_len = len(num_list)
    while ind < l_len - 2:
        #print(ind)    
        if num_list[ind] > num_list[ind + 1]:
            tmp_1 = num_list[ind]
        else:
            tmp_1 = num_list[ind + 1]

        if num_list[ind + 2] > tmp_1:
            tmp_1 = num_list[ind + 2]

        if tmp_1 > tmp_2:
            tmp_2 = tmp_1
        else:
            tmp_1 = tmp_2
        
        ind = ind + 1
        #print(f"tpm1 {tmp_1}")
        #print(f"tmp2 {tmp_2}")
    return tmp_1

our_list = [6,18,7,9,5,3,2,10]

#print(f"The max value is {chek_biglist(our_list)}")
