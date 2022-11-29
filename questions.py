import random

def get_question(data):
    num_questions = len(data)//5
    question_num = random.randint(0, num_questions-1)*5
    return data[question_num], data[question_num+1], data[question_num+2:question_num+5]


def generate_question(data):
    '''data is assumed to be in the format: QUESTION, CORRECT_ANSWER, WRONG, WRONG, WRONG, QUESTION...'''
    question, correct_answer, other_answers = get_question(data)
    random.shuffle(other_answers)
    correct_answer_number = random.randint(0, 3)
    all_answers = other_answers
    all_answers.insert(correct_answer_number, correct_answer)
    all_answers = [f'{i1}. {i2}' for i1, i2 in zip(range(1, 5), all_answers)]
    return question, correct_answer_number+1, '\n'.join(all_answers)


