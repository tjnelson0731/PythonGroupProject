print('This is a math quiz that assesses your abilities in addition, multiplication, and division.')
# Function that displays an addition math problem
def first_problem(answer=True):
    import random
    while answer:
        addition1 = random.randint(1,100)
        addition2 = random.randint(1,100)
        print(addition1, '+', addition2)
        problem1 = int(input('What would be the answer to this problem? '))
        if problem1 == addition1 + addition2:
            answer = False
            print('Congratulations! You are correct!')
        else:
            print('Sorry, try again.')
# Function that displays a multiplication math problem
def second_problem(answer=True):
    while answer:
        import random
        multiply1 = random.randint(1,10)
        multiply2 = random.randint(1,10)
        print(multiply1, 'x', multiply2)
        problem2 = float(input('What would be the answer to this problem? '))
        if problem2 == multiply1 * multiply2:
            answer = False
            print('Congratulations! You are correct!')
        else:
            print('Sorry, try again.')
# Function that displays a division math problem
def third_problem(answer=True):
    while answer:
        import random
        division1 = random.randint(1,50)
        division2 = 2
        print(division1, '/', division2)
        problem3 = float(input('What would be the answer to this problem? '))
        if problem3 == division1 / division2:
            answer = False
            print('Congratulations! You are correct!')
        else:
            print('Sorry, try again.')
first_problem()
second_problem()
third_problem()
print('You have finished the quiz!')