from datetime import date, datetime, timedelta
import tkinter as tk
from tkinter import messagebox

# Dados do funcionário
salario_base = 1500
horas_base = 46
valor_hora_extra = salario_base / horas_base

# Função para calcular as horas trabalhadas em um dia


def calcular_horas_trabalhadas(dia, entrada_manha, saida_manha, entrada_tarde, saida_tarde):
    total_horas = 0

    # Calcula as horas trabalhadas na parte da manhã
    if entrada_manha and saida_manha:
        entrada = datetime.combine(dia, entrada_manha)
        saida = datetime.combine(dia, saida_manha)
        total_horas += (saida - entrada).total_seconds() / 3600

    # Calcula as horas trabalhadas na parte da tarde
    if entrada_tarde and saida_tarde:
        entrada = datetime.combine(dia, entrada_tarde)
        saida = datetime.combine(dia, saida_tarde)
        total_horas += (saida - entrada).total_seconds() / 3600

    return total_horas

# Função para calcular o salário do funcionário em um mês


def calcular_salario_mes(ano, mes, horarios):
    dias_no_mes = (date(ano, mes + 1, 1) - timedelta(days=1)).day
    horas_mes = 0

    # Calcula as horas trabalhadas em cada dia do mês
    for dia in range(1, dias_no_mes + 1):
        # Obtém o dia da semana
        data = date(ano, mes, dia)
        dia_semana = data.weekday()

        # Define os horários de trabalho do dia
        if dia_semana == 5:  # sábado
            entrada_manha = datetime.strptime("9:00", "%H:%M").time()
            saida_manha = datetime.strptime("11:00", "%H:%M").time()
            entrada_tarde = datetime.strptime("12:30", "%H:%M").time()
            saida_tarde = datetime.strptime("16:00", "%H:%M").time()
        else:  # segunda a sexta
            entrada_manha = datetime.strptime("8:30", "%H:%M").time()
            saida_manha = datetime.strptime("11:00", "%H:%M").time()
            entrada_tarde = datetime.strptime("12:30", "%H:%M").time()
            saida_tarde = datetime.strptime("18:00", "%H:%M").time()

        # Calcula as horas trabalhadas no dia
        if data in horarios:
            entrada_manha, saida_manha, entrada_tarde, saida_tarde = horarios[data]
        horas_dia = calcular_horas_trabalhadas(
            data, entrada_manha, saida_manha, entrada_tarde, saida_tarde)
        horas_mes += horas_dia

    # Calcula o pagamento do mês
    if horas_mes <= horas_base:
        salario_mes = salario_base
    else:
        horas_extras = horas_mes - horas_base
        salario_mes = salario_base + (horas_extras * valor_hora_extra)

    return salario_mes


def calcular():
# Obtém os valores do formulário
    mes = int(mes_label.get())
    ano = int(ano_label.get())
    horarios = {}
    for i in range(31):
        dia_entry = dia_entries[i]
        entrada_manha_entry = entrada_manha[i]
        saida_manha_entry = saida_manha[i]
        entrada_tarde_entry = entrada_tarde[i]
        saida_tarde_entry = saida_tarde[i]
    if dia_entry.get():
        dia = int(dia_entry.get())
        entrada_manha = datetime.strptime(entrada_manha_entry.get(
        ), "%H:%M").time() if entrada_manha_entry.get() else None
        saida_manha = datetime.strptime(saida_manha_entry.get(
        ), "%H:%M").time() if saida_manha_entry.get() else None
        entrada_tarde = datetime.strptime(entrada_tarde_entry.get(
        ), "%H:%M").time() if entrada_tarde_entry.get() else None
        saida_tarde = datetime.strptime(saida_tarde_entry.get(
        ), "%H:%M").time() if saida_tarde_entry.get() else None

    horarios[date(ano, mes, dia)] = (
        entrada_manha, saida_manha, entrada_tarde, saida_tarde)

    # Calcula o salário do funcionário
    salario_mes = calcular_salario_mes(ano, mes, horarios)

    # Exibe o resultado
    messagebox.showinfo(
        "Salário", f"O salário do funcionário no mês {mes}/{ano} é de R$ {salario_mes:.2f}.")

# Cria a janela principal
window = tk.Tk()
window.title("Calculadora de Salário")

# Cria o rótulo e a entrada de texto para o ano
ano_label = tk.Label(window, text="Ano:")
ano_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
ano_entry = tk.Entry(window)
ano_entry.grid(row=0, column=1, padx=5, pady=5)

# Cria o rótulo e a entrada de texto para o mês
mes_label = tk.Label(window, text="Mês:")
mes_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
mes_entry = tk.Entry(window)
mes_entry.grid(row=1, column=1, padx=5, pady=5)

# Cria os rótulos e entradas de texto para os dias do mês
dia_labels = []
dia_entries = []
for i in range(31):
    dia_label = tk.Label(window, text=f"Dia {i+1}:")
    dia_label.grid(row=i+2, column=0, padx=5, pady=5, sticky=tk.E)
    dia_entry = tk.Entry(window)
    dia_entry.grid(row=i+2, column=1, padx=5, pady=5)
    dia_labels.append(dia_label)
    dia_entries.append(dia_entry)

# Cria as entradas de texto para os horários de trabalho do dia
entrada_manha_label = tk.Label(window, text="Entrada Manhã:")
entrada_manha_label.grid(row=i+2, column=2, padx=5, pady=5, sticky=tk.E)
entrada_manha_entry = tk.Entry(window)
entrada_manha_entry.grid(row=i+2, column=3, padx=5, pady=5)

saida_manha_label = tk.Label(window, text="Saída Manhã:")
saida_manha_label.grid(row=i+3, column=2, padx=5, pady=5, sticky=tk.E)
saida_manha_entry = tk.Entry(window)
saida_manha_entry.grid(row=i+3, column=3, padx=5, pady=5)

entrada_tarde_label = tk.Label(window, text="Entrada Tarde:")
entrada_tarde_label.grid(row=i+4, column=2, padx=5, pady=5, sticky=tk.E)
entrada_tarde_entry = tk.Entry(window)
entrada_tarde_entry.grid(row=i+4, column=3, padx=5, pady=5)

saida_tarde_label = tk.Label(window, text="Saída Tarde:")
saida_tarde_label.grid(row=i+5, column=2, padx=5, pady=5, sticky=tk.E)
saida_tarde_entry = tk.Entry(window)
saida_tarde_entry.grid(row=i+5, column=3, padx=5, pady=5)

# Cria o botão de calcular
calcular_button = tk.Button(window, text="Calcular", command=calcular)
calcular_button.grid(row=i+6, column=3, padx=5, pady=5)