def program2():
  f = open('ami.txt', 'w')
  f.write('Lorem code is here are the code for there>')
  f.close()  
  

  f = open("./ami.txt", 'r')
  F =f.read()
  count_small=0
  count_digit=0
  count_big =0

  for value in F:
    if value.islower():
        count_small += 1
    
    if value.isdigit():
        count_digit +=1
    
    if value.isupper():
        count_big += 1
    

  print("Total number of small number :", count_small);
  print("Total number of small number :", count_digit);
  print("Total number of captial number :", count_big);

  f.close()  
program2()