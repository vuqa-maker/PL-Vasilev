import tkinter as tk
from tkinter import ttk, messagebox, filedialog
window = tk.Tk()
window.title("Васильев Станислав Сергеевич")
tab_control = ttk.Notebook(window)
tab_control.pack(expand=1, fill='both')
#1
def calculator():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        znak = combo_znak.get()
        if znak == '+':  result = num1 + num2
        elif znak == '-':  result = num1 - num2
        elif znak == '*':  result = num1 * num2
        elif znak == '/':   result = num1 / num2
        label.config(text=f"Ответ: {result}")
    except ValueError:
        label.config(text="Ошибка")
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Калькулятор")
entry_num1 = tk.Entry(tab1)
entry_num1.grid(row=0, column=0, padx=5, pady=5)
combo_znak = ttk.Combobox(tab1, values=["+", "-", "*", "/"], width=3)
combo_znak.current(0)
combo_znak.grid(row=0, column=1, padx=5, pady=5)
entry_num2 = tk.Entry(tab1)
entry_num2.grid(row=0, column=2, padx=5, pady=5)
button_calculator = tk.Button(tab1, text="Вычислить", command=calculator)
button_calculator.grid(row=0, column=3, padx=5, pady=5)
label= tk.Label(tab1, text="Результат:")
label.grid(row=1, column=0, columnspan=4)
#2
def vibor():
    vibor = []
    if v1.get():
        vibor.append("первый вариант")
    if v2.get():
        vibor.append("второй вариант")
    if v3.get():
        vibor.append("третий вариант")
    if vibor:
        messagebox.showinfo("выбор", "Вы выбрали " + ", ".join(vibor))
    else:
        messagebox.showinfo("выбор", "ничего")
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Чекбоксы")
v1 = tk.BooleanVar()
v2 = tk.BooleanVar()
v3 = tk.BooleanVar()
checkbutton1 = tk.Checkbutton(tab2, text="Первый вариант", variable=v1)
checkbutton2 = tk.Checkbutton(tab2, text="Второй вариант", variable=v2)
checkbutton3 = tk.Checkbutton(tab2, text="Третий вариант", variable=v3)
checkbutton1.pack(anchor='w', padx=1, pady=5)
checkbutton2.pack(anchor='w', padx=1, pady=5)
checkbutton3.pack(anchor='w', padx=1, pady=5)
button_vibor = tk.Button(tab2, text="Выбрать", command=vibor)
button_vibor.pack(pady=10)
#3
def text():
    filepath = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as f:
            text.delete("1.0", tk.END)
            text.insert(tk.END, f.read())
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text="Текст")
button_text = tk.Button(tab3, text="Загрузить текст", command=text)
button_text.pack(pady=5)
text = tk.Text(tab3, wrap='word')
text.pack(expand=1, fill='both', padx=1, pady=5)
window.mainloop()


