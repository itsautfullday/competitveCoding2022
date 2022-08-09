import math

def minMovesHelper(target, current, doubles,hmap):
    
    if(target == current):
        # print("returning 0 target == current",target,current)
        return 0
    if(target == current + 1):
        # print("returning 1 target == current + 1",target,current)
        return 1
    if(target == current * 2 and doubles > 0):
        # print("returning 1 target == current * 2",target,current,doubles)
        return 1
    if(doubles == 0 or current * 2 > target):
        # print("returning target - current",target - current,target,current,doubles)
        return target - current
    else:
        key = str(current) + "_"+str(doubles)
        if(key not in hmap):
            print(hmap.keys(), key)
            hmap[key] = min(minMovesHelper(target, current + 1, doubles,hmap), minMovesHelper(target, current * 2, doubles - 1,hmap)) + 1
        return hmap[key]


def main():
    print("Min moves "+str(minMovesHelper(10,1,4,{})))

if __name__ == "__main__":
    main()