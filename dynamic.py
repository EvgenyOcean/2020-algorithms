'''
Как узнать какие элементы нужно взять, если есть сумка (размером - bag_capacity) и таблица (items), при том, чтобы стоимость выбранных элементов была максимальной из всех возможных вариантов?
1. Если помещается - кладем, но перед этим макс(ячейка сверху or 1.1)
1.1. Если помещается и есть свободное место, то:
1.2. добавить col - (col - free_space), но если col - (col - free_space) уже есть в массиве taken(хоть один из эл), то поднимаемся на 1 ряд вверх до тех пор пока не найдем то, чего нет, после - добавляем
2. Если не помещется, то берем с верхнего ряда, НО 
2.1. Если ряд и есть верхний то вставляем 0

=> Находим подзадачу, которую сразу можем решить. Далее, зная полученный результат, решаем более сложную подзадачу и так до тех пор, пока не будет решена основная задача. 
=> Такая же логика, чтобы написать Fib(n), при условии, что нужно сохранять уже полученные результаты, таким образом вместо О(n2), можно получить O(2n + 1)
'''

items = {
    'Oscar': [4, 4000],
    'Laptop': [3, 2500],
    'Wallet': [1, 1500], 
    'Diamond': [2, 3500],
    'Iphone': [1, 2000],
}

for name, info in items.items():
    info[0] = round(info[0])

def worth_taking(bag_capacity, items):
    get_item_name = [item for item in items] #we need the ability to look back at the previous results, so it's better to work with indexes, knowing the index we can find out what item is being processed
    def current_wl_value(current_item, this_bag_capacity, row_num): #current + weight_left value (1.1)
        taken = [current_item] #we might need to go backwards several times and we don't want to take one item multiple times
        to_take = [] #considered items to be taken, we will take them later if none of the items in a cell hasn't already been taken 
        free_room = this_bag_capacity - items[current_item][0] #weight left in a bag
        if free_room == 0: return taken #meaning the item took up all available room, we can't proceed and take sth else (extra check if the item in the cell above turns out to be more valuable will be run later)
        prev_bag = table[row_num][free_room] #check max valuable thing we found, having free_room available space in the bag. Basically each column represents best possible option for specific bag_capacity and if we happen to have some free room, all we need to do is to get what we have already calculated.
        while prev_bag: #previous bag (meaning bag with less capacity) might look like [{'thing': [weight, value]}]
            for item in prev_bag:
                if item == 0: return taken
                item_name = list(item.keys())[0] #nothing to take, return what we have so far
                if item_name in taken: #if one item is taken, we will consider the whole best previous combination invalid. What do we have to do after that? We must check best option in the above cell (1.2) and so on...
                    break 
                else: 
                    to_take.extend([key for key in item.keys()]) #in case everything is smooth
            else: 
                taken.extend(to_take)
                prev_bag = None #no need to check other bags, because fillin in department did its work ;) 
                return taken
            #just a prep for check other bags
            to_take = [] 
            row_num -= 1
            if row_num < 0: return taken
            prev_bag = table[row_num][free_room]
                        
        return taken

    #table to story prveious results (what's the best for n-capacity bag)
    #needs to solve subtasks of the main task
    table = [[[] for i in range(bag_capacity + 1)] for i in range(len(items))]

    for row_num in range(len(table)):
        current_item = get_item_name[row_num]
        current_item_value = items[current_item][1]
        current_item_weight = items[current_item][0]
        row = table[row_num]

        if row_num == 0:  #filling in first row
            for col_num in range(len(row)):
                if col_num >= current_item_weight:
                    table[row_num][col_num].append({current_item:items[current_item]})
                else:
                    table[row_num][col_num].append(0)
            continue
        
        for col_num in range(len(row)):
            if col_num >= current_item_weight:
                max_prev_col_sum = 0
                max_prev_row_sum = 0

                for i in range(len(table[row_num - 1][col_num])): #sum of prev items in the same-size bag
                    prev_row_value = table[row_num - 1][col_num][i]
                    if type(prev_row_value) == dict: #could be 0
                        for item in prev_row_value:
                            max_prev_row_sum += items[item][1]

                prev_cols_value = current_wl_value(current_item, col_num, row_num) #filling in spare room
                for item in prev_cols_value:
                    max_prev_col_sum += items[item][1] 

                result = max(max_prev_col_sum, max_prev_row_sum) #(1)
                if result == max_prev_row_sum:
                    table[row_num][col_num] = table[row_num - 1][col_num]
                else: 
                    for item in prev_cols_value:
                        table[row_num][col_num].append({item:items[item]}) 
    
            else: #doen't fit, so prev value is the best 
                table[row_num][col_num].extend(table[row_num - 1][col_num])

    return table[len(table)-1][len(table[0])-1]


picked_things = worth_taking(4, items)

for thing in picked_things:
    for thing_name, thing_info in thing.items():
        print('We should take {0} its value is {1[1]:.2f}$'.format(thing_name, thing_info))
lucre = []
[lucre.append(value[1]) for thing in picked_things for value in thing.values()]
print('Total lucre => %.2f$' %sum(lucre))