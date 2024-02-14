import PySimpleGUI as sg
import xlsxwriter

def generate_excel_worksheet(table_array, headings):
    excel_table_array = [headings] + table_array
    workbook = xlsxwriter.Workbook('Lancamentos.xlsx')
    worksheet = workbook.add_worksheet()

    row_index = 0
    column_index = 0

    for row in excel_table_array:
        for column in row:
            worksheet.write(row_index,column_index, column)
            column_index += 1
        column_index = 0
        row_index += 1

    workbook.close()
    return row_index

def create(lancar_dados_array, headings):
    lancar_dados_window_layout= [
        [sg.Table(values=lancar_dados_array,headings=headings, max_col_width=35,
                auto_size_columns=True,
                display_row_numbers=True,
                justification='right',
                num_rows=10,
                key='-TABLE-',
                row_height=35,
                tooltip='Dados armazenados!')],
        [sg.Button('Exportar os dados para o Excel')]
                
    ]
    
    information_dados_window = sg.Window("Dados",
    lancar_dados_window_layout,modal=True)

    while True:
        event, values = information_dados_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == 'Exportar os dados para o Excel':
            generate_excel_worksheet(lancar_dados_array, headings)


    information_dados_window.close()
