def flatten(k):
    
    for i in k:
        if isinstance(i,list):
            flatten(i)
        else:
            empty_list.append(i)

k =  [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
empty_list = []
flatten(k)
print(empty_list)             