def palindrome_check(string):
  string = list(string)
  temp = []
  
  
  #removing spaces
  for x in range(0, len(string)):
    if(string[x] != " "):
      temp.append(string[x].lower())
      
      
  #reversing strings
  a1 = []
  i = 0
  j = len(temp)-1
  
  while(i < len(temp)):
    a1.append(temp[j])
    i += 1
    j -= 1
    
    
  #checking if a1 is equal to the string
  counter = 0
  for x in range(0, len(temp)):
    if(temp[x] == a1[x]):
      counter += 1
      
      
  #if the counter is equal to the length of the string then the word is the same
  if(counter ==len(temp)):
    return True
  
  return False
print(palindrom_check("abcdcba")
