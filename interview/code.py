#создать плоский список из списка любой глубины

def flat_list(example):
    result = []
    while(example):
        itm = example.pop(0)
        print('111', itm)
        if isinstance(itm, list):
            itm.extend(example)
            print('item' , itm)
            print('ex', example)
            example = itm
        else:
            result.append(itm)
    return result

#print(flat_list([[1,2],[[3,5],[6,7]]]))

