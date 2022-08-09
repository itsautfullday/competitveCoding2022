import math

def LCS(stringA, stringB,dp):
    #if either of the strings is "", LCS = 0
    # print("Checking ",stringA, len(stringA), stringB, len(stringB))
    if(stringA == "" or stringB == ""):
        return 0
    indexOfInterestA = len(stringA) - 1
    indexOfInterestB = len(stringB) - 1

    if(dp[indexOfInterestB][indexOfInterestA] != -1):
        return dp[indexOfInterestB][indexOfInterestA]

    
    if(stringA[indexOfInterestA] == stringB[indexOfInterestB]):
    #If the last character is the same in both cases, it necessarily has to be the end of LCS
    # therefore LCS(A,B) in case the last char is same --> LCS(A-1,B-1) + 1
        dp[indexOfInterestB][indexOfInterestA] =  LCS(stringA[0:indexOfInterestA],stringB[0:indexOfInterestB],dp) + 1
        # print("indexOfInterestB",indexOfInterestB,"indexOfInterestA",indexOfInterestA, dp[indexOfInterestB][indexOfInterestA])
    else:
    #If the last char is not the same LCS(A,B) definitely cannot include last char of either
    #But the second to last char can be compared in such sequences : hence use that for comparison!
        dp[indexOfInterestB][indexOfInterestA] = max(LCS(stringA,stringB[0:indexOfInterestB],dp),LCS(stringA[0:indexOfInterestA],stringB,dp))
        # print("indexOfInterestB",indexOfInterestB,"indexOfInterestA",indexOfInterestA, dp[indexOfInterestB][indexOfInterestA])
    return dp[indexOfInterestB][indexOfInterestA]

def main():
    stringA = input()
    stringB = input()
    dp = [[ -1 for i in range(len(stringA))] for j in range(len(stringB))]
    for i in dp:
        print(i)
    print("Ans:",LCS(stringA, stringB,dp))

if __name__ == "__main__":
    main()

"""
things to learn
split a string into an array and convert array to string
"".join(arr) --> join
"".split(<delim") --> split


abc
ac
[-1, -1, -1]
[-1, -1, -1]
Checking  abc 3 ac 2
Checking  ab 2 a 1
Checking  ab 2  0
Checking  a 1 a 1
Checking   0  0
indexOfInterestB 0 indexOfInterestA 1
Checking  a 1  0
Checking   0 a 1
indexOfInterestB 0 indexOfInterestA 0
indexOfInterestB 0 indexOfInterestA 0
indexOfInterestB 1 indexOfInterestA 1
Checking  abc 3 a 1
Checking  abc 3  0
Checking  ab 2 a 1
indexOfInterestB 0 indexOfInterestA 0
Checking  ab 2 ac 2
Checking  ab 2 a 1
Checking  a 1 ac 2
Checking  a 1 a 1
Checking   0 ac 2
indexOfInterestB 1 indexOfInterestA 0
indexOfInterestB 1 indexOfInterestA 0
indexOfInterestB 1 indexOfInterestA 0
"""