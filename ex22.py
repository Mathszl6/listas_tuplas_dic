## Removendo elementos duplicados
list = [1,1,2,3,3,4,5]

def uniques(complete_list):
    unic_list = []
    for n in complete_list:
        if n not in unic_list:
            unic_list.append(n)
    return unic_list

total = uniques(list)
print(total)

## Ou, apenas exibindo os elementos únicos

list = [1,1,2,3,3,4,5]

def uniques(complete_list):
    unic_list = [n for n in complete_list if complete_list.count(n) == 1]
    
    return unic_list

total = uniques(list)
print(total)