import json

with open('FAQ.json', 'r') as f:
    file = json.load(f)

correct_answer_for_chat_gpt = []
correct_example = {'prompt': '', 'completion': ''}


for i in file:
    questions = [j for j in i['Question_original_alternatives']]
    questions.extend([j for j in i['Question_short_alternatives']])
    questions.extend([j for j in i['Keywords']])
    questions.extend([i['Question_short'], i['Question_original']])
    for question in questions:
        correct_answer_for_chat_gpt.append({'completion': i['Answer_plain_text'], 'prompt': question})

with open('FAQ_correct.json', 'w') as f:
    f.write(json.dumps(correct_answer_for_chat_gpt))

