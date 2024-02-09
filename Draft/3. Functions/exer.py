def highest_even(li):
    


    # assuming that biggest number is first list 
    max = li[0]
    for Index_number in li:
        if(Index_number %2 == 0):
            if(Index_number > max):
                max = Index_number
                

    return max

print(highest_even([10, 2, 3, 4, 8, 11]))