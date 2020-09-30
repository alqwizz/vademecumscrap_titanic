# TITANIC
# Vamos a intentar resolver el problema con un solo modelo o funcion objetivo
import csv
import time

# IMPORTAMOS LOS DATOS TRAIN DESDE EL CSV
with open('train.csv', newline='') as csvfile:
    data_bruta = list(csv.reader(csvfile))

# CADA ENTRADA DE LA LISTA TIENE LA SIGUIENTE CONFIGURACION 
# ['0.PassengerId', '1.Survived', '2.Pclass', '3.Name', '4.Sex', '5.Age', '6.SibSp', '7.Parch', '8.Ticket', '9.Fare', '10.Cabin', '11.Embarked']
print(data_bruta[0])
print(' ')
TOTAL_DATOS = len(data_bruta) - 1
print('Existe un total de' , TOTAL_DATOS, 'individuos a estudiar en el TRAIN SET')
print(' ')
time.sleep(1.5)

# 1 - VAMOS A HACER EL ESTUDIO PREVIO DE LOS DATOS
print('ESTUDIO DE LOS DATOS ORIGINALES')

# Calculamos primero datos globales de supervivencia
Rate_survive = 0
for x in data_bruta:
    if x[1] == '1':
        Rate_survive = Rate_survive + 1
print('Sobreviven', Rate_survive, 'personas (', Rate_survive / TOTAL_DATOS * 100, '% de los navegantes)')
print(' ')

# -> PCLASS (Variable sencilla de estudiar)
print(' -PCLASS')
PR_Pclass = [0, 0, 0]
N_Pclass = [0, 0, 0]
for x in data_bruta:
    if x[2] == '1':
        N_Pclass[0] = N_Pclass[0] + 1
        if x[1] == '1':
            PR_Pclass[0] = PR_Pclass[0] + 1
    if x[2] == '2':
        N_Pclass[1] = N_Pclass[1] + 1
        if x[1] == '1':
            PR_Pclass[1] = PR_Pclass[1] + 1
    if x[2] == '3':
        N_Pclass[2] = N_Pclass[2] + 1
        if x[1] == '1':
            PR_Pclass[2] = PR_Pclass[2] + 1
N_suman = N_Pclass[0] + N_Pclass[1] + N_Pclass[2]
if TOTAL_DATOS > N_suman:
    print(' * Hay' , TOTAL_DATOS - N_suman, 'datos perdidos')
PR_Pclass[0] = PR_Pclass[0] / N_Pclass[0]
PR_Pclass[1] = PR_Pclass[1] / N_Pclass[1]
PR_Pclass[2] = PR_Pclass[2] / N_Pclass[2]
print(' ', PR_Pclass)
print(' ', N_Pclass)
print('')
time.sleep(1.5)

# -> GENDER or SEX (Variable sencilla de estudiar)
print(' -GENDER')
PR_gender = [0, 0]
N_gender = [0, 0]
for x in data_bruta:
    if x[4] == 'female':
        N_gender[0] = N_gender[0] + 1
        if x[1] == '1':
            PR_gender[0] = PR_gender[0] + 1
    if x[4] == 'male':
        N_gender[1] = N_gender[1] + 1
        if x[1] == '1':
            PR_gender[1] = PR_gender[1] + 1
N_suman = N_gender[0] + N_gender[1]
if TOTAL_DATOS > N_suman:
    print(' * Hay' , TOTAL_DATOS - N_suman, 'datos perdidos')
PR_gender[0] = PR_gender[0] / N_gender[0]
PR_gender[1] = PR_gender[1] / N_gender[1]
print(' ', PR_gender)
print(' ', N_gender)
time.sleep(1.5)
print('')

# -> EMBARKED (Variable sencilla de estudiar)
print(' -EMBARKED')
PR_embarked = [0, 0, 0]
N_embarked = [0, 0, 0]
for x in data_bruta:
    if x[11] == 'C':
        N_embarked[0] = N_embarked[0] + 1
        if x[1] == '1':
            PR_embarked[0] = PR_embarked[0] + 1
    if x[11] == 'Q':
        N_embarked[1] = N_embarked[1] + 1
        if x[1] == '1':
            PR_embarked[1] = PR_embarked[1] + 1
    if x[11] == 'S':
        N_embarked[2] = N_embarked[2] + 1
        if x[1] == '1':
            PR_embarked[2] = PR_embarked[2] + 1
N_suman = N_embarked[0] + N_embarked[1] + N_embarked[2]
if TOTAL_DATOS > N_suman:
    print(' * Hay' , TOTAL_DATOS - N_suman, 'datos perdidos')
PR_embarked[0] = PR_embarked[0] / N_embarked[0]
PR_embarked[1] = PR_embarked[1] / N_embarked[1]
PR_embarked[2] = PR_embarked[2] / N_embarked[2]
print(' ', PR_embarked)
print(' ', N_embarked)
time.sleep(1.5)
print('')

# -> HONOUR (forma parte del nombre y se refiere al estatus del viajero, sencillo de estudiar)
print(' -HONOUR')
Honours = ('Mr.', 'Mrs.', 'Miss.', 'Master.', 'Rev.', 'Ms.', 'Don.', 'Mme.', 'Major.', 'Dr.', 'Col.', 'Mlle.', 'Capt.')
print(' ', Honours)
PR_honour = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
N_honour = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = -1
for x in Honours:
    i = i + 1
    j = 0
    for y in data_bruta:
        j = j + 1
        if y[3].__contains__(x):
            N_honour[i] = N_honour[i] + 1
            if y[1] == '1':
                PR_honour[i] = PR_honour[i] + 1
N_suman = sum(N_honour)
if TOTAL_DATOS > N_suman:
    print(' * Hay' , TOTAL_DATOS - N_suman, 'datos perdidos')
i = -1
for x in PR_honour:
    i = i + 1
    PR_honour[i] = x / N_honour[i]
print(' ', PR_honour)
print(' ', N_honour)
time.sleep(1.5)
print('')

# -> SIBLINGS AND SPOUSES ()
print(' -SIBLING AND SPOUSE')
SSValues = ('0', '1', '2', '3', '4', '5', '6', '7', '8')
PR_SSValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]
N_SSValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]
i = -1
for x in SSValues:
    i = i + 1
    j = 0
    for y in data_bruta:
        j = j + 1
        if y[6] == x:
            N_SSValues[i] = N_SSValues[i] + 1
            if y[1] == '1':
                PR_SSValues[i] = PR_SSValues[i] + 1
N_suman = sum(N_SSValues)
if TOTAL_DATOS > N_suman:
    print(' * Hay' , TOTAL_DATOS - N_suman, 'datos perdidos')
i = -1
for x in PR_SSValues:
    i = i + 1
    if N_SSValues[i] == 0:
        PR_SSValues[i] = 0
    if N_SSValues[i] != 0:
        PR_SSValues[i] = x / N_SSValues[i]
print(' ', PR_SSValues)
print(' ', N_SSValues)
time.sleep(1.5)
print('')

# -> PARENTS AND CHILDRENS ()
print(' -PARENTS AND CHILDRENS')
PCValues = ('0', '1', '2', '3', '4', '5', '6')
PR_PCValues = [0, 0, 0, 0, 0, 0, 0]
N_PCValues = [0, 0, 0, 0, 0, 0, 0]
i = -1
for x in PCValues:
    i = i + 1
    j = 0
    for y in data_bruta:
        j = j + 1
        if y[7] == x:
            N_PCValues[i] = N_PCValues[i] + 1
            if y[1] == '1':
                PR_PCValues[i] = PR_PCValues[i] + 1
N_suman = sum(N_PCValues)
if TOTAL_DATOS > N_suman:
    print(' * Hay' , TOTAL_DATOS - N_suman, 'datos perdidos')
i = -1
for x in PR_PCValues:
    i = i + 1
    if N_PCValues[i] == 0:
        PR_PCValues[i] = 0
    if N_PCValues[i] != 0:
        PR_PCValues[i] = x / N_PCValues[i]
print(' ', PR_PCValues)
print(' ', N_PCValues)
time.sleep(1.5)
print('')

# -> AGE (Intentaremos crear diferentes grupos de edad con un numero de muestras similar)
Grupos = [0, 11, 22, 40, 100]
PR_Age = [0, 0, 0, 0]
N_Age = [0, 0, 0, 0]
i = -1
for x in Grupos:
    i = i + 1
    j = 0
    if i > 0:
        for y in data_bruta:
            j = j + 1
            if j > 1:
                edad = float(y[5])
                print(edad)

                
def ff(x):
    return x[1] + x[2] + x[3] + x[4] 
