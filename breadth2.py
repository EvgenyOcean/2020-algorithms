from collections import deque

friends = {
    'Me': ['Jessica', 'Julia', 'Steven', 'Megan', 'Dustin'], 
    'Jessica': ['Paul', 'Johny', 'Steven', 'Me'],
    'Alice': ['Rabbit'], 
    'Julia': ['Roma', 'Ivan', 'Me'],
    'Steven': ['Me', 'Jessica', 'Rocky', 'Me'],
    'Rocky': [],
    'Johny': ['Ivan', 'Jessica'],
    'Paul': ['Jessica'],
    'Roma': [],
    'Rabbit': ['Alice'],
    'Megan': ['Me'],
    'Ivan': ['Austin', 'Alice'], 
    'Dustin': ['Me', 'Austin', 'Anthony', 'Eugine'],
    'Eugine': ['Dustin', 'Megan'], 
    'Anthony': ['Eugine'],
    'Austin': ['Dustin']
}

path = deque() 
checked = []

def finding_tom(friends, start):
    path.append([[start], friends[start]]) #adding an array with friend of the friend history 
    checked.append(start) #adding an initial dude to the checked, because his friends were just added to the queue
    while path: #while there's someone to check 
        complect = path.popleft() #taking friends with its idk 'friend-line'
        for friend in complect[1]: #going through the friends
            if friend in checked: 
                continue
            if friend == 'Tom': 
                final_path = [*complect[0], friend]
                return final_path
            path.append([[*complect[0], friend], friends[friend]]) #if the conditions above weren't met, we append the friends and its 'friend-line' to the queue
            checked.append(friend)
    return 'The person wasn\'t found'
        
print(finding_tom(friends, 'Me'))


    