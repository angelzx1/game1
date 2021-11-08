def cabrobro(x):
    
     if (x == 1):
        print("Good!!")

     elif(x == 2): 
        print("meus parabéns")
    
     elif (x == 3):
        print("Nice!!")

     elif (x == 4):
        print("Baum baum!!")

     elif (x == 5):
        print("Continue assim!!")

     elif (x == 6):
        print("Comesse bem!!")
     else:
        print("Vai fazer alguma coisa!!")

print("1) Acordar cedo ")
print("2) Hidratar-se") 
print("3) Estudar ") 
print("4) Boa refeição ")
print("5) Fazer afazeres")
print("6) Lanche de noite")
print("7) Dormir cedo")

while True:
    cabrobro(int(input("Qual das tarefas que você tem feito? ")))