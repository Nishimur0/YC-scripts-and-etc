import tkinter as tk
from tkcalendar import DateEntry

def toggle_date_entry():
    if unlock_var.get() == 1:
        date_entry.configure(state='normal')
    else:
        date_entry.configure(state='disabled')
        date_entry.set_date(None)

def print_selected_date():
    selected_date = date_entry.get_date()
    if selected_date is not None:
        formatted_date = selected_date.strftime("%Y-%m-%d")
        print(formatted_date)

window = tk.Tk()
window.title("Выбор даты")

unlock_var = tk.IntVar(value=0)

unlock_checkbox = tk.Checkbutton(window, text="Разблокировать", variable=unlock_var, command=toggle_date_entry)
unlock_checkbox.pack()

date_label = tk.Label(window, text="Выберите дату:")
date_label.pack()

date_entry = DateEntry(window, width=12, background='darkblue', foreground='white', borderwidth=2, state='disabled', date_pattern='yyyy-mm-dd')
date_entry.pack()

print_button = tk.Button(window, text="Вывести дату", command=print_selected_date)
print_button.pack()

window.mainloop()
