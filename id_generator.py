import string

def idGenerator():
    id=[0,0,0,0,0]
    id_map=string.ascii_uppercase + string.digits    
    max_index=len(id_map)
    while True:
        carryover=1
        index=0
        while carryover == 1:
            if id[index]<max_index-1:
                id[index]+=carryover
                carryover=0
            else:
                carryover=1
                id[index]=0
            index+=1
        yield id_map[id[4]]+id_map[id[3]]+id_map[id[2]]+id_map[id[1]]+id_map[id[0]]+"-FF"
FFEventId=idGenerator()  
for i in range(1296):
    print(next(FFEventId))
print(next(FFEventId))