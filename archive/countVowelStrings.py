def countVowelStrings(n: int) -> int:
    table = [[0 for i in range(5)] for j in range(50)]
    for i in range(5):
        table[0][i] = 1
    previousRowSum = 5  
    for j in range(1,50):
        for i in range(5):
            if(i == 0):
                table[j][i] = previousRowSum
            else:
                table[j][i] = table[j][i-1] - table[j-1][i-1]
                previousRowSum += table[j][i]
    
    return sum(table[n-1])

def main():
    n = input()
    print("Ans :",countVowelStrings(n))

if __name__ == "__main__":
    main()