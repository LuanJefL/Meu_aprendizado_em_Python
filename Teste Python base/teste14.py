def spam(divideBy):
   try:
      return(42 / divideBy)
   except:
      return'Error: Invalid argument.' 
   else:
      print
   finally:
      print("Tarefa realizada")
print(spam(1))