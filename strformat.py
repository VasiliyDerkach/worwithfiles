team1_num= int(input('Введите количество участников в команде Мастера '))
print("В команде Мастера кода участников: %d ! "%(team1_num))
team2_num= int(input('Введите количество участников в команде Волшебников '))
team_num= team2_num+team1_num
print("Итого сегодня в командах участников:  %d и %d ! "%(team1_num,team2_num))
score_2=int(input('Введите количество задач решённых командой 2 '))
print("Команда Волшебники данных решила задач: {} !".format(score_2))
team2_time= float(input('Введите время за которое команда 2 решила задачи '))
print("Волшебники данных решили задачи за {0:10.2f} с !".format(team2_time))
score_1=int(input('Введите количество задач решённых командой 1 '))
print(f"Команды решили {score_1} и {score_2} задач.")
team1_time= float(input('Введите время за которое команда 1 решила задачи '))
print(f"Команда Мастера данных решили задачи за {team1_time:10.2f} с !")

tasks_total= score_1+score_2
time_avg= (team2_time+team1_time)/tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:5.2f} секунды на задачу!.')
time_avg1=team1_time/score_1/team1_num
time_avg2=team2_time/score_2/team2_num
if time_avg1<time_avg2:
    print('Победа команды Мастера кода!')
elif time_avg1>time_avg2:
    print('Победа команды Волшебники Данных!')
else:
    print('Ничья!')
