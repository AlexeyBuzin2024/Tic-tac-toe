pole = list(range(1, 10))  # Создаю игровое поле

win_comb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9),
            (3, 5, 7)]  # Список выйгрышных комбинаций


def draw_pole():  # Функция отрисовки поля
    print('-------------')
    for i in range(3):
        print('|', pole[0 + i * 3], '|', pole[1 + i * 3], '|', pole[2 + i * 3], '|')
        print('-------------')


def win_control():  # Функция проверки условий победы
    for j in win_comb:
        if (pole[j[0] - 1]) == (pole[j[1] - 1]) == (pole[j[2] - 1]):
            return pole[j[0] - 1]
    else:
        return False


def step(player_icon):  # Функция регистрации хода
    while True:
        temp = int(input("Куда Вы совершаете ход: " + player_icon + "? "))
        if temp < 1 or temp > 9:  # проверка введённого значения на соответствие диапазону игрового поля
            print("Ошибочный индекс клетки, попробуйте ещё раз.")
            continue
        if str(pole[temp - 1]) in 'XO':  # проверка ячейки пуста/занята
            print("Клетка с этим индексом уже занята")
            continue
        pole[temp - 1] = player_icon  # регистрация хода
        break


def main():   # Основная функция
    count_step = 0  # Переменная счётчика ходов
    while True:
        draw_pole() # Вызов функции отрисовки игрового поля
        if count_step % 2 == 0: # Выбор игрока совершающего следующий ход
            step("X")
        else:
            step("O")
        if count_step > 3:  # Блок определения победителя (начинает работать с третьего хода)
            winner = win_control()
            if winner:
                draw_pole()
                print(winner, "победил!")
                break
        count_step += 1
        if count_step > 8:  # Заполнение поля без победителя следовательно "Ничья"
            draw_pole()
            print("Ничья!")
            break

main() # Вызов основной функции
