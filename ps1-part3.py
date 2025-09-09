def heart_rate(age, goal):
    max_HR=220-age
    print (f'Your maximum heart rate is: {max_HR}')
    if goal==' S':
        low_HR=0.8*max_HR
        high_HR=max_HR
        print (f'Your target heart rate is between {low_HR} and {high_HR}')
    if goal==' E':
        low_HR=0.6*max_HR
        high_HR=0.8*max_HR
        print (f'Your target heart rate is between {low_HR} and {high_HR}')
    

user_age=int(input('What is your age?'))
user_goal=str(input('Is your goal speed (S) or endurance (E)?'))

heart_rate(user_age, user_goal)
