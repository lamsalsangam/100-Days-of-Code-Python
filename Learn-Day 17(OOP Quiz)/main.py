from question_model import Question
from quiz_brian import QuizBrain
from data import question_data

question_bank = []
# for i in range(len(question_data)):
#     question_bank.append(
#         Question(question_data[i]["text"], question_data[i]["answer"]))
for question in question_data:
    question_bank.append(
        Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
