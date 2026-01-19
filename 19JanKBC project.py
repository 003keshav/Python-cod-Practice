ques=[
        {"Question":"Who is Father of nation ?",
        "Option":["A. Narendra Modi", "B. Mahatma Gandhi",
                    "C. Jawahr Lal Nehru", "D. Rajendra Prasad"],
                    "Answer":"B", "Amount":1000},
        {"Question":"Who is Iron Man of India ?",
        "Option":["A. Sardar Valabh Bhai Patel", "B. Narendra Modi",
                    "C. Bhagat Singh", "D. Rajendra Prasad"],
                    "Answer": "A", "Amount":5000}]
x=0
total=0
for k in ques:
    print(f"Aapke saamne pesh h Question {x+1} for Amount {k["Amount"]}\n", k["Question"])
    for opt in k["Option"]:
        print(opt)

    user_input=input("Choose your Answer from A B C D:")
    if user_input==k["Answer"]:
        total+=k["Amount"]
        print("Next Question")

    else:
        print("AApka jawab galat h Aap haar chuke h ")
        break
    x+=1
print(f"Aap ne jeete h Kon Bnega Crore Pati m amount {total}")

