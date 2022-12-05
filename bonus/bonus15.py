import json

with open("files/questions.json", 'r') as file:
    data = json.load(file)

# print(json.dumps(data, indent=4))

for question in data:
    text = question['question_text']
    print(text)
    for index, alternative in enumerate(question['alternatives']):
        print(index + 1, alternative)

    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data, 1):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "CORRECT |"
    else:
        result = "WRONG   |"
    print(index, result, "Your Answer   : ", question["user_choice"])
    print(index, result, "Correct Answer: ", question["correct_answer"])
    print()
print("score: ", score, "/", len(data))

