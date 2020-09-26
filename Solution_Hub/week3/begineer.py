
s = input()

test = "hello"
N = len(test)
testCase = 0

check = 0
for i in range(len(s)):
    if s[i] == test[testCase]:
        testCase = testCase + 1
    if testCase == N:
        print("YES")
        check = 1
        break
if (check==False):
    print("NO")
    