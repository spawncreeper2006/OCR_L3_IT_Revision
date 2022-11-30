import questions as q

topic_dict = {'1': 'System Architecture.txt',
             '2': 'CPU Performance Factors.txt'}


def valid(x:str, num_topics:int):
    if x.isdigit():
        x = int(x)
        if x > 0 and x <= num_topics:
            return True

    return False

def menu():
    k, v = topic_dict.keys(), topic_dict.values()
    num_topics = len(k)
    topics = '\n'.join([f'{i1}. {i2[:-4]}' for i1, i2 in zip(k, v)])+'\n'
    topic = input(topics)
    while not valid(topic, num_topics):
        topic = input('Enter a valid value: ')

    return topic_dict[topic]
    
def get_data(fn:str):
    with open(fn) as f:
        data = f.read().split('\n')
    return data

def mul_choice_test(fn:str, num_questions=10):
    score = 0
    data = get_data(fn)
    for x in range(1, num_questions+1):
        question, correct_answer_num = q.generate_question(data)


        user_answer = input(question)
        if user_answer == correct_answer_num:
            print ('correct\n')
            score += 1
        else:
            print ('incorrect\n')

    print (f'{score}/{num_questions}')

def main():
    topic = menu()
    mul_choice_test(topic)

if __name__ == '__main__':
    main()
    
