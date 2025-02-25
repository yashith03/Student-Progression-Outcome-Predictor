# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 2051623      iit id 20230311
# Date: 13/12/2023
# UKWATTA LIYANAGE YASHITH CHANDEEPA GIMNATH





from graphics import *
CreditRange = [120,100,80,60,40,20,0]
def progression():
  Total_Entries = 0
  Progress = 0
  Trailer = 0
  Retriever = 0  
  Exclude1 = 0
  DataList = []

  

  while True:
      try:
          
          passCredit = int(input("Please enter your Credits at pass: "))
          deferCredit = int(input("Please enter your Credits at defer: "))
          failCredit = int(input("Please enter your Credits at fail: "))
          Total = passCredit + deferCredit + failCredit 
      except ValueError:
           Outcome = "-Integer Required-"
           print(Outcome)
           continue

      if Total !=120:
         Outcome = "-Total Incorrect-"
         print(Outcome)
         continue
      if (passCredit not in CreditRange) or (deferCredit not in CreditRange) or (failCredit not in CreditRange):
         Outcome = "-Not in Range-"
         print(Outcome)
         continue
    
      if Total == 120:
       Total_Entries = Total_Entries +1

      if   passCredit ==120:
           Progress = Progress + 1
           Outcome = "-Progress-"
           DataList.append([Outcome, passCredit, deferCredit, failCredit])
         
      elif passCredit == 100 and ((deferCredit == 0 and failCredit ==20) or (failCredit ==0 and deferCredit ==20)):
            Trailer = Trailer + 1
            Outcome = "-Progress Module Trailer-"
            DataList.append([Outcome, passCredit, deferCredit, failCredit])
            
      elif passCredit <=40 and failCredit >=80:
            Exclude1 = Exclude1 + 1
            Outcome = "-Exclude-"
            DataList.append([Outcome, passCredit, deferCredit, failCredit])
          
      else:
           Outcome = "-Do not Progress(module retriever)-"
           Retriever = Retriever + 1
           DataList.append([Outcome, passCredit, deferCredit, failCredit])
         
      print(Outcome)
      print("")
    
      print("Would you like another set of data ? ")
      Cont = input("Enter any key to 'continue' or 'q' to 'quit' and view results: ").lower()
      print("")
    
    
      if Cont != "q":
          continue
      if Cont== "q":
          break
    # Print the data from the list
  print(" Part 2:")
  for Data in DataList:
      print(f"{Data[0]} = {Data[1]}, {Data[2]}, {Data[3]}")
      

  # Write the data to a text file
  with open('progression_data(student&staff).txt', 'w') as f:
      f.write(" Part 3:\n")
      for Data in DataList:
          f.write(f"{Data[0]} = {Data[1]}, {Data[2]}, {Data[3]}\n")

  # Calculate heights after collecting all data
  Height = (370/Total_Entries)
  HeightP = Progress * Height
  HeightT = Trailer * Height
  HeightR = Retriever * Height  
  HeightE = Exclude1 * Height

  def main():
      win=GraphWin("Histogram", 800,600)
      win.setBackground("thistle1")

      Xaxis = Line(Point(50,510),Point(750,510))
      Xaxis.setWidth(2)
      Xaxis.draw(win)

      Title = Text(Point(170,50),"RESULTS GRAPH")
      Title.setSize(23)
      Title.setStyle("bold")
      Title.setTextColor("Navy Blue")
      Title.draw(win)

      Total = Text(Point(190,550),f"TOTAL ENTRIES : {Total_Entries}")
      Total.setSize(23)
      Total.setStyle("bold")
      Total.setTextColor("Navy Blue")
      Total.draw(win)

      Prog = Rectangle(Point(100,485),Point(200,485-HeightP))
      Prog.setFill("blue3")
      Prog.setOutline("Black")
      Prog.draw(win)
      Prog_text = Text(Point(150,497),"Progress")
      Prog_text_up = Text(Point(150,475-HeightP),f"{Progress}")
      Prog_text_up.setSize(11)
      Prog_text_up.setStyle("bold")
      Prog_text.setSize(13)
      Prog_text.setStyle("bold")
      Prog_text.draw(win)
      Prog_text_up.draw(win)

      Prog_Mod_Trailer = Rectangle(Point(335,485), Point(235,485-HeightT))
      Prog_Mod_Trailer.setFill("blueviolet") 
      Prog_Mod_Trailer.setOutline("Black")
      Prog_Mod_Trailer.draw(win)
      Prog_Mod_Trailer_text = Text(Point(285,497),"Trailer")
      Prog_Mod_Trailer_text_up = Text(Point(280,475-HeightT),f"{Trailer}")
      Prog_Mod_Trailer_text_up.setSize(11)
      Prog_Mod_Trailer_text_up.setStyle("bold")
      Prog_Mod_Trailer_text.setSize(13)
      Prog_Mod_Trailer_text.setStyle("bold")
      Prog_Mod_Trailer_text.draw(win)
      Prog_Mod_Trailer_text_up.draw(win)

      DN_Progress = Rectangle(Point(470,485), Point(370,485-HeightR))
      DN_Progress.setFill("chartreuse1")
      DN_Progress.setOutline("Black")
      DN_Progress.draw(win)
      DN_Progress_text = Text(Point(420,497),"Retriever")
      DN_Progress_text_up = Text(Point(418,475-HeightR),f"{Retriever}")
      DN_Progress_text_up.setSize(11)
      DN_Progress_text_up.setStyle("bold")
      DN_Progress_text.setSize(13)
      DN_Progress_text.setStyle("bold")
      DN_Progress_text.draw(win)
      DN_Progress_text_up.draw(win)

      Exclude = Rectangle(Point(505,485), Point(605,485-HeightE))
      Exclude.setFill("deeppink2")
      Exclude.setOutline("Black")
      Exclude.draw(win)
      Exclude_text = Text(Point(550,497),"Exclude")
      Exclude_text_up = Text(Point(550,475-HeightE),f"{Exclude1}")
      Exclude_text_up.setSize(11)
      Exclude_text_up.setStyle("bold")
      Exclude_text.setSize(13)
      Exclude_text.setStyle("bold")
      Exclude_text.draw(win)
      Exclude_text_up.draw(win)
    

    

      try:
        win.getMouse()
        win.close()
       
      except GraphicsError:
        pass
        

  main()

while True:
  print("\n")
  print("-----------------------------------------------------------------")
  print(" Part 1:")
  print("Are you a student or teacher?")
  Person = input('Enter "S" for student or "T" for teacher: ').upper()

  if Person == "S":
      try:
          passCredit = int(input("Please enter your Credits at pass: "))
          deferCredit = int(input("Please enter your Credits at defer: "))
          failCredit = int(input("Please enter your Credits at fail: "))
          Total = passCredit + deferCredit + failCredit 
      except ValueError:
           Outcome = "-Integer Required-"
           print(Outcome)
           continue

      if Total !=120:
         Outcome = "-Total Incorrect-"
         print(Outcome)
         continue
      if (passCredit not in CreditRange) or (deferCredit not in CreditRange) or (failCredit not in CreditRange):
         Outcome = "-Not in Range-"
         print(Outcome)
         continue
    

      if   passCredit ==120:
           Outcome = "-Progress-"
           
         
      elif passCredit == 100 and ((deferCredit == 0 and failCredit ==20) or (failCredit ==0 and deferCredit ==20)):
            Outcome = "-Progress Module Trailer-"
            
            
      elif passCredit <=40 and failCredit >=80:
            Outcome = "-Exclude-"
            print("")
            
          
      else:
           Outcome = "-Do not Progress(module retriever)-"
           
         
      print(Outcome)
      print("")
      break

  elif Person == "T":
      progression()
      continue
  else:
      print("Invalid")
      continue
      
    
    
    
