import PySimpleGUI as sg

sg.theme('LightGreen')

historic = []
result = ''

def Calculator():
    calculator_layout = [
        [sg.Txt(''*10)],
        [sg.Text('', size=(15,1), font=('Helvetica',18), text_color='black', key='input-after', background_color='White',pad=((4,4),(4,0)))],
        [sg.Text('', size=(15,1), font=('Helvetica',18), text_color='black', key='input-current', background_color='White',pad=((4,4),(0,4)))],
        [sg.Txt(''*10)],
        [sg.ReadFormButton('C',size=(5,2)),sg.ReadFormButton('CE',size=(5,2)), sg.ReadFormButton('<<',size=(5,2)), sg.ReadFormButton('/',size=(5,2))],
        [sg.ReadFormButton('7',size=(5,2)), sg.ReadFormButton('8',size=(5,2)), sg.ReadFormButton('9',size=(5,2)), sg.ReadFormButton('*',size=(5,2))],
        [sg.ReadFormButton('4',size=(5,2)), sg.ReadFormButton('5',size=(5,2)), sg.ReadFormButton('6',size=(5,2)), sg.ReadFormButton('-',size=(5,2))],
        [sg.ReadFormButton('1',size=(5,2)), sg.ReadFormButton('2',size=(5,2)), sg.ReadFormButton('3',size=(5,2)), sg.ReadFormButton('+',size=(5,2))],
        [sg.ReadFormButton('.',size=(5,2)), sg.ReadFormButton('0',size=(5,2)), sg.ReadFormButton('<->',size=(5,2)), sg.ReadFormButton('=',size=(5,2))]
    ]
    window = sg.Window('Calculator', layout=calculator_layout, size=(250,370), finalize=True)
    return window
def Historic(hist): 
    historic_layout = [
        [sg.Listbox(hist,key='display',size=(15,11), font=('Helvetica',18), background_color='white')],
        [sg.ReadFormButton("<-",size=(5,2)), sg.ReadFormButton("Clear",size=(5,2))]
    ]
    window = sg.Window('Historic', layout=historic_layout, size=(250,370), finalize=True)
    return window

calculator_window, historic_window = Calculator(), None

while True:
    window, event, values = sg.read_all_windows()
    if window == (calculator_window or historic_window) and event == sg.WIN_CLOSED:
        break
    # Historic window
    elif window == historic_window:
        if event == "<-":
            historic_window.hide()
            calculator_window.un_hide()
            if values['display']:
                result = ''.join(values['display'])
                result = result[1+result.index('='):]
                calculator_window['input-current'].update(result)

        elif event == "Clear":
            historic.clear()
            historic_window['display'].update('')
    # Calculator window
    elif window == calculator_window:
        if event == "<->":
            historic_window = Historic(historic)
            calculator_window.hide()
        elif event == 'CE':
            result = ''
            window['input-current'].update(result)
        elif event == 'C':
            result = ''
            window['input-after'].update(result)
            window['input-current'].update(result)
        elif event == '<<':
            result = result[:-1]
            window['input-current'].update(result)
        elif len(result) > 16:
            pass
        elif event == '=':
            window['input-after'].update(result)
            try:
                Answer = eval(result)
                Answer = str(Answer)
                window['input-current'].update(Answer)
                historic.append(result+"="+Answer)
                result= Answer
            except:
                window['input-current'].update("[ERRO]")
        else:
            result += event
            window['input-current'].update(result)

calculator_window.close()