# To write a program on grading system with 5 subjects
print('Enter the marks that obtained in 5 subjects')
english = float(input('English : '))
math = float(input('Math : '))
chemistery = float(input('Chemistery : '))
biology = float(input('Biology : '))
physics = float(input('Physics : '))
average =(english+math+chemistery+biology+physics) / 5
if (average >=81) & (average <=100):
    print('Grade A')
elif (average >=61) & (average <=80):
    print('Grade B')
elif (average >=41) & (average <=60):
    print('Grade C')
elif (average >=21) & (average <=40):
    print('Grade D')
elif (average >=0) & (average <=20):
    print('Grade F')