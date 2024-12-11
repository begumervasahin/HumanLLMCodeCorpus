
b1 = [
    {
        "Question": "Am I eligible for financial Aid?",
        "Answer": "Virtually every student qualifies for some type of financial aid. See our HOW TO APPLY information and visit the PAIS (Preliminary Aid Information System) web site for the financial aid eligibility worksheet."
    },
    {
        "Question": "What is an Academic Year?",
        "Answer": "The Academic Year begins with the fall semester. For example: the fall 2014 + spring 2015 b2 = one academic year."
    },
]
def fonk1(query):
    b3 = [item for item in b1 if query.lower() in item['Question'].lower()]
    return b3
def fonk2():
    print("Welcome to the FAQ System!")
    print("You can ask questions to get answers. Enter 'exit' to quit.")
    while True:
        b4 = input("Your question: ")
        if b4.lower() == 'exit':
            print("Exiting...")
            break
        b3 = fonk1(b4)
        if b3:
            for item in b3:
                print(f"Question: {item['Question']}")
                print(f"Answer: {item['Answer']}\n")
        else:
            print("No matching question found. Please try again.")
if b5 = = "__main__":
    fonk2()