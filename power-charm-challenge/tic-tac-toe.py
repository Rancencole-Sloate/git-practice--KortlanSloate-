def p(b):
 for r in b:
  print(" | ".join(r))
  print("-"*5)
 
 
def c_w(b,p):
 for i in range(3):
  if all(b[i][j]==p for j in range(3)) or all(b[j][i]==p for j in range(3)):
   return True
 if all(b[i][i]==p for i in range(3)) or all(b[i][2-i]==p for i in range(3)):
  return True
 return False
 
 
def f(b):
 return all(c!=" " for r in b for c in r)
 
 
def t():
 b=[[" "for _ in range(3)]for _ in range(3)]
 p=["X","O"]
 print("Tic-Tac-Toe Game")
 p(b)
 for t in range(9):
  pl=p[t%2]
  while 1:
   try:
    r,c=map(int,input(f"P {pl}, row col (0-2): ").split())
    if b[r][c]==" ":
     b[r][c]=pl
     break
    else:
     print("Nope. Again.")
   except:
    print("Wrong. 0-2 pls.")
  p(b)
  if c_w(b,pl):
   print(f"P {pl} wins!")
   return
  if f(b):
   print("Draw!")
   return
 print("Draw!")
 
 
t() 