def checkAnswers(q, ans):
    return q[1] == ans.lower()


def main():
    global questions

    questions = [
        ['What does CPU stand for? ', 'central processing unit'], 
        ['What does GPU stand for? ', 'graphics processing unit'],
        ['What does RAM stand for? ', 'random access memory'],
        ['What does PSU stand for? ', 'power supply unit']
    ]
    score = 0

    for q in questions:
        ans = input(q[0])
        if(checkAnswers(q, ans)):
            score+=1
            print('Correct!')
        else:
            print('Incorrect!')

    print('Your final score is: ' + str(score))
    print('You got', str(score / len(questions) * 100), '%')


if __name__ == '__main__':
    main()