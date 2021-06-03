def anagram(p,s):
    a=3
    p=["abc","bca","cab","acb","bac"]
    #Split the string to the 3rd character
    res=[s[y-a:y] for y in range(a, len(s)+a,a)]
    for i in res:
        if i==p:
            print(res[i])
  
      


