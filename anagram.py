def anagram(p,s):
    a=3
    p=["abc","bca","cab","acb","bac"]
    #Split the string to the 3rd character and have list of substring
    res=[s[y-a:y] for y in range(a, len(s)+a,a)]
    if p in res:
        print(res.find(p))
   
        

     
  
      


