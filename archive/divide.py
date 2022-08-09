

def main():
    result = []
    string = input()
    k = int(input())
    lengthString = len(string)
    quotient = lengthString // k
    if(lengthString % k != 0):
        quotient = lengthString // k
        remainingStr = string[quotient * k : len(string)]
        strToAdd = k - len(remainingStr)
        arr = ["x" for i in range(strToAdd)]
        remainingStr += ''.join(arr)
        print("appending "+ remainingStr)
        result.append(remainingStr)
        
    for i in range(quotient):
        print("appending "+ string[i*k:(i*k)+k])
        result.append(string[i*k:(i*k)+k])
    return sorted(result)



    

if __name__ == "__main__":
    main()
