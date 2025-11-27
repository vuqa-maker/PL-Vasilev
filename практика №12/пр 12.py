from tkinter import messagebox
import requests
import json
import tkinter as tk
window = tk.Tk()
window.title("Информация о пользователе")
def user():
    name = entry.get()
    if not name:
        messagebox.showerror("Ошибка")
        return
    url = f"https://api.github.com/users/{name}"
    try:
        response = requests.get(url)
        data = response.json()
        p = ['company', 'created_at', 'email', 'id', 'name', 'url']
        data = {field: data.get(field) for field in p}
        file= f"{name.replace('/', ' ')}.json"
        with open(name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=0, indent=4)
        messagebox.showinfo("Выполнено", f"Данные сохранены в {file}")
    except requests.RequestException as e:
        messagebox.showerror("Ошибка", f"Пользователя не существует")
tk.Label(window, text="Введите пользователя:").pack(padx=10, pady=5)
entry = tk.Entry(window, width=20)
entry.pack(padx=5, pady=5)
button = tk.Button(window, text="Поиск", command=user)
button.pack(padx=5, pady=5)
window.mainloop()
