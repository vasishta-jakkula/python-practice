#from fizz buzz.py 

for count in range(1,101):
   
  if count % 3 == 0 and count % 5 == 0:
        print("fizzbuzz")
  
  elif count % 3 == 0:
      print("fizz")

  elif count % 5 == 0:
      print("buzz")     
  else:
      print(count)

    
