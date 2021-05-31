print("WELCOME TO NUMBER CHARETERISTIC APP 'ROX'.DEVELOPED BY RISHAV ROY CHOWDHURY.")
x = input("WRITE YOUR NAME AND PRESS ENTER: ")
print("HELLO",x )
def ui():
  print("FINISH!WILL YOU CONSIDER RATING ME ON GitHub?")
def yu():
  Y = input("ENTER A NUMBER= ")
  try :
    if float(Y) < 0:
     print("NEGATIVE")
     ui()
    if float(Y) > 0:
     print("POSITIVE")
     ui()
    if float(Y) == 0:
     print("THAT'S 0 BRO!")
     ui()
  except :
     print("I DON'T MAKE OUT WHAT YOU ARE SAYING ;<")     
  x = input("PRESS 'ENTER' TO USE AGAIN")
while str(x):
  yu()
