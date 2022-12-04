import PySimpleGUI as sg

def calculate(num1, num2):
    return int(num1) + int(num2)

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Калькулятор коммунальных платежей')],
            [sg.Text('Прошлый месяц')],
            [sg.Text('Число 1')],
            [sg.InputText(key='-n1-')],
            [sg.Text('Число 2')],
            [sg.InputText(key='-n2-')],
            [sg.Button('Рассчитать', key='-calc-')],
            [sg.Text(key='-res-')] ]

# Create the Window
window = sg.Window('Калькулятор коммуналки 0.0.1', layout, size=(300, 600))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    if event == '-calc-':
        window['-res-'].update("Результат расчетов: " + str(calculate(values['-n1-'], values['-n2-'])))

window.close()