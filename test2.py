import random

code = {
    1:{
        1:{1:"Phenylalanine", 2:"Phenylalanine", 3: "Leucine", 4: "Leucine"}, 
        2:{1:"Serine", 2:"Serine", 3:"Serine", 4:"Serine"},
        3:{1:"Tyrosine", 2:"Tyrosine", 3:"STOP", 4:"STOP"},
        4:{1:"Cysteine", 2:"Cysteine", 3:"STOP", 4:"Tryptophan"}
    },
    2:{
        1:{1:"Leucine", 2:"Leucine", 3:"Leucine", 4:"Leucine"},
        2:{1:"Proline", 2:"Proline", 3:"Proline", 4:"Proline"},
        3:{1:"Histidine", 2:"Histidine", 3:"Glutamine", 4:"Glutamine"},
        4:{1:"Arginine", 2:"Arginine", 3:"Arginine", 4:"Arginine"}
    },
    3:{
        1:{1:"Isoleucine", 2:"Isoleucine", 3:"Isoleucine", 4:"Methionine"},
        2:{1:"Threonine", 2:"Threonine", 3:"Threonine", 4:"Threonine"},
        3:{1:"Asparagine", 2:"Asparagine", 3:"Lysine", 4:"Lysine"},
        4:{1:"Serine", 2:"Serine", 3:"Arginine", 4:"Arginine"}
    },
    4:{
        1:{1:"Valine", 2:"Valine", 3:"Valine", 4:"Valine"},
        2:{1:"Alanine", 2:"Alanine", 3:"Alanine", 4:"Alanine"},
        3:{1:"Aspartic Acid", 2:"Aspartic Acid", 3:"Glutamic Acid", 4:"Glutamic Acid"},
        4:{1:"Glycine", 2:"Glycine", 3:"Glycine", 4:"Glycine"}
    }
}

def main():
    playing = input("\nWelcome to this genetic code table quiz game.\n \nIn this game the genetic code will be given while you will guess the amino acid associated with it.\n\nAre you ready(yes/no)? ")
    if playing.lower() != "yes":
        print("\nHave a nice day (❁´◡`❁)")
        quit()

    name = input("\nName: ")

    while True:
        questions = get_questions()
        if questions == 0:
            print("\nNot a valid input")
            pass
        elif questions > 64:
            print("\nNot a valid input")
            pass
        else:
            break

    print("\nLet the game begin (●'◡'●)")
    point = 0

    i = 0
    while i < questions:
        rn1 = random.randint(1, 4)
        rn2 = random.randint(1, 4)
        rn3 = random.randint(1, 4)

        a = rn1
        b = rn2
        c = rn3

        num = [a, b, c]
        n = 0
        while n < 3:
            def let(n):
                if num[n] == 1:
                    let = "U"
                    return let
                elif num[n] == 2:
                    let ="C"
                    return let
                elif num[n] == 3:
                    let = "A"
                    return let
                else:
                    let = "G"
                    return let
            num[n] = let(n)
            n += 1
        
        answer = input("\n" + str(i + 1) + ". " + "What is the amino acid of the sequence " + num[0] + num[1] + num[2] +" ? ")
    
        if answer.lower() == code[a][b][c].lower():
            point += 1
            if point == 1:
                print("\nYou got the correct answer.\nYour current score is " + str(point) + " point.")
            else:
                print("\nYou got the correct answer.\nYour current score is " + str(point) + " points.")
        else:
            if point == 1:
                print("\nYou got the wrong answer. The correct answer is "+ code[a][b][c] + "\nYour current score is " + str(point) + " point.")
            else:
                print("\nYou got the wrong answer. The correct answer is "+ code[a][b][c] + "\nYour current score is " + str(point) + " points.")
        i += 1

    if i == questions:
        if questions == 1:
            if point == 0:
                print("\nSorry(┬┬﹏┬┬), "+ name + " you got a score of " + str(point) + " point out of " + str(questions) + " item.\nBetter luck next time. OwO\n")
            else:
                print("\nCongratulations "+ name + " you got a score of " + str(point) + " point out of " + str(questions) + " item.\n")
        else:
            if point == 1:
                print("\nCongratulations "+ name + " you got a score of " + str(point) + " point out of " + str(questions) + " items.\n")
            elif point == 0:
                print("\nSorry(┬┬﹏┬┬), "+ name + " you got a score of " + str(point) + " point out of " + str(questions) + " items.\nBetter luck next time. OwO\n")
            else:
                print("\nCongratulations "+ name + " you got a score of " + str(point) + " points out of " + str(questions) + " items.\n")
        
def get_questions():
    while True:
        try:
            return int(input("\nThere are a total of 64 questions.\n\nPlease input the number of question/s you want to answer. "))
        except ValueError:
            print("\nNot a valid input")
            pass

main()