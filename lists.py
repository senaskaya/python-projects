'''
1- Write a function that flattens a list. Its elements may consist of multi-layered lists (such as [[3],2]) or non-scalar data. 
For example:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]
'''

def flatten(the_list):
    flatted_list = []
    
    for i in the_list:
        if isinstance(i, list):
            flatted_list.extend(flatten(i))
        else:
            flatted_list.append(i)
    
    return flatted_list

'''
2- Write a function that reverses the elements in the given list. If the elements inside the list also contain the list, reverse their elements as well. 
For example:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
'''

def reverse(the_list):
    the_list.reverse()
    for i in the_list:
        if isinstance(i, list):
            reverse(i)
    return the_list

    

