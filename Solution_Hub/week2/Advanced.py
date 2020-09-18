####################
### output is not completing finished!
def listToString(newText):
    str = " "
    return str.join(newText)
def main():
  for a in range(int(input())):
      N = int(input())
      li = list( input().split())
  
      # li = sorted(lis)
      # print(li)
      # print(lis)
      S = input()
      newText = list()
      # print(len(li))
      i = 0
      for x in range(len(li)) :
         
          if li[i] in S :
              newText.append(li[i])
              del(li[i])
              i = 0
          else:
            i = i +1
          # print(li)
      print("case :",a,"(",listToString(newText),")")
if __name__ == "__main__":
    main()
