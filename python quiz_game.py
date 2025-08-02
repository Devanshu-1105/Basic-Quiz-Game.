questions = [
    ["who is the first PM of India?" , "P.Nehru", "N.Modi", "Atal Bihari Vajpayee", "Narsimha Rao" , 1] ,
    ["what is the capital of Italy?","Paris","Washington DC","Rome","Amsterdam",3],
    ["what is the sqaure of 16?","19","4","32","16",2],
    ["Who is Manoj Bajpayee?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["Which planet is known as the Red Planet?", "Mars", "Earth", "Venus", "Jupiter", 1]
    
            ]

prizes = ["Free trip vouchers", "$70000", "$100000", "$2500000"," $3000000"]
 
i = 0
for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")
    
#Checking if the answer is correct or not

    a = int(input("Enter your answer, 1 for a, 2 for b, 3 for c, and 4 for d\n"))

    if (question[5]==a):
     print("correct Answer!")
    else:
     print (f"OOps,That was the wrong Answer.The correct answer was {question[5]}")
     print("Better Luck Next time!")
     break
    print(f"You won {prizes[i]}")
    i += 1
