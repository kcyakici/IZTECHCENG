with open("07correctAnswers.txt", "r") as f:
    correctAnswers = f.readlines()

with open("07candidateAnswers.txt", "r") as f:
    candidateAnswers = f.readlines()

correctCount = 20
wrongAnswersList = []
for i in range(len(correctAnswers)):
    if correctAnswers[i] != candidateAnswers[i]:
        correctCount -= 1
        dotIndex = correctAnswers[i].index(".")
        wrongAnswerNumber = correctAnswers[i][:dotIndex]
        wrongAnswersList.append(wrongAnswerNumber)

wrongCount = 20 - correctCount

if len(wrongAnswersList) > 5:
    print("Candidate has failed the exam.")
else:
    print("Candidate has passed the exam")

print(f"Number of correct answers: {correctCount}\nNumber of wrong answers: {wrongCount}\nThe questions answered wrongly: {wrongAnswersList}")
