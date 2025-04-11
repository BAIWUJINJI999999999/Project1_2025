from gpiozero import LED,Button
from time import sleep
from random import uniform
led = LED(4)
right_button = Button(15)
left_button = Button(14)
left_name = input('left player name is')
right_name = input('right player name is')
left_score = 0
right_score = 0
rounds = int(input('The number of rounds is'))
def pressed(button):
    global left_score, right_score
    if button.pin.number == 14:
        left_score += 1
        print(f'\n{left_name} won the game! {left_name} {left_score}-{right_score} {right_name}')
    else:
        right_score += 1
        print(f'\n{right_name} won the game! {left_name} {left_score}-{right_score} {right_name}')
    check_game_end()
def check_game_end():
    if (left_score + right_score) >= rounds:
        print('\n===END===')
        print(f'The final score:{left_name} {left_score}-{right_score} {right_name}')
        if left_score > right_score:
            print(f'{left_name} won the game!')
        elif right_score > left_score:
            print(f'{right_name} won the game!')
        else:
            print('Draw!')
        exit()
right_button.when_pressed = pressed
left_button.when_pressed = pressed
while True:
    print('\n===New Round===')
    led.on()
    delay = uniform(5,10)
    sleep(delay)
    led.off()
    sleep(3)
    if led.is_lit == False:
        print('Nothing responds.')
exit()
