import PySimpleGUI as sg
import information_table

headings = ['Cliente','Produto','Categoria','Quantidade']
lancar_dados_array =[]


layout = [[sg.Text("Nome do Cliente:"),sg.Input(key='-CLIENTE-',do_not_clear=False,size=(20, 1))],
           [sg.Text("Produto:             "),sg.Input(key='-PRODUTO-',do_not_clear=False,size=(20,1))],
           [sg.Text("Categoria:          "),sg.Input(key='-CATEGORIA-',do_not_clear=False,size=(20,1))],
           [sg.Text("Quantidade:       "),sg.Input(key='-QUANTIDADE-',do_not_clear=False,size=(5,1))],
           [sg.Button('Salvar'),sg.Button('Lançamentos'),sg.Exit('Sair')]]

window = sg.Window("Salvar",layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED,'Sair'):
        break
    elif event == 'Salvar':
        info_lancamento = [values['-CLIENTE-'],values['-PRODUTO-'],values['-CATEGORIA-'],values['-QUANTIDADE-']]
        lancar_dados_array.append(info_lancamento)
        sg.popup("Dados salvos com sucesso!")
    elif event == 'Lançamentos':
        information_table.create(lancar_dados_array, headings)