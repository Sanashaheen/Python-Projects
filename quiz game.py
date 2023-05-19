print ("***Wellcome to my Computer Quiz***")
choice = input("Do you want to play? ")
score = 0
if choice == "yes":
    print("ok lets play....")
else:
    quit()

question = print ("Q1. The earth is the fourth planet from the sun")
op = input("A.True\nB.False\n ")
if op == "A":
    score += 1
else:
    print("Wrong answer")

question = print("Q2. Who is the National Poet of our Nation?")
op = input("A.Allama Iqbal\nB.Quaid-e-Azam\nC.Imran Khan\nD.None of the above\n ")

if op == "A":
    score += 1
else:
    print("Wrong answer")

question = print("Q3. Who invented Computer?")
op = input("A.Ghandhi\nB.Charles Babbage\nC.Imran Khan\nD.None of the above\n ")
if op == "B":
    score += 1
else:
    print("Wrong answer")

question = print("Q4. Who developed Python Programming Language?")
op = input("A.Wick van Rossum\nB.Rasmus Lerdorf\nC.Guido van Rossum\nD.Niene Stom\n ")
if op == "C":
    score += 1
else:
    print("Wrong answer")

question = print("Q5. Which type of Programming does Python support?")
op = input("A.object-oriented programming\nB.structured programming\nC. functional programming\nD. all of the mentioned\n ")
if op == "D":
    score += 1
else:
    print("Wrong answer")

question = print("Q6. All keywords in Python are in ")
op = input("A.Capitalized\nB.lower case\nC.UPPER CASE\nD.None of the mentioned\n ")
if op == "D":
    score += 1
else:
    print("Wrong answer")

question = print("Q7. MS-Word is an example of")
op = input("A.An operating system\nB.A processing device\nC.Application software\nD.An input device\n ")
if op == "C":
    score += 1
else:
    print("Wrong answer")

question = print("Q8. Junk e-mail is also called")
op = input("A.Spam\nB.Spoof\nC.Sniffer script\nD.Spool\n ")
if op == "A":
    score += 1
else:
    print("Wrong answer")


question = print("Q9. Scientific Name of Computer?")
op = input("A.Compiler\nB.Sillico sapiens\nC.Application software\nD.An input device\n ")
if op == "B":
    score += 1
else:
    print("Wrong answer")


question = print("Q10. Which of the following character is used to give single-line comments in Python?")
op = input("A.//\nB.$\nC.#\nD.*\n ")
if op == "C":
    score += 1
else:
    print("Wrong answer")

print("Your correct Answers are " + str(score))
print("You got " + str(score/10 * 100) + "%. ")
