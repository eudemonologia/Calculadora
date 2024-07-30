import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Calculadora")
    root.iconbitmap("calculadora.ico")
    root.resizable(False, False)

    # Variables
    entry = tk.StringVar(value="0")

    # Funciones
    def calculate():
        try:
            # Separo la entrada en numeros y operadores
            result = entry.get().split()
            # Realizo la operacion con los numeros, eliminando los ceros del principio
            result = [value.lstrip("0") for value in result]
            print(result)
            # Evaluo la operacion
            result = eval("".join(result))
            # Muestro el resultado
            entry.set(str(result))
        except:
            entry.set("Error")

    def set_number(text):
        if entry.get() == "0":
            entry.set(text)
        else:
            entry.set(entry.get() + text)

    def set_operator(text):
        if entry.get()[-1] in [" "]:
            entry.set(entry.get()[:-3] + text)
        else:
            entry.set(entry.get() + text)

    # Frame resultado
    frame_result = tk.Frame(root)
    frame_result.grid(column=0, row=0, columnspan=4, sticky="nsew")
    entry_result = tk.Entry(
        frame_result,
        textvariable=entry,
        state="readonly",
        justify="right",
        font=("Arial", 20),
    )
    entry_result.grid(column=0, row=0, columnspan=4, sticky="nsew")

    # Frame botones
    frame_buttons = tk.Frame(root)
    frame_buttons.grid(column=0, row=1, columnspan=4, sticky="nsew")
    for i in range(4):
        frame_buttons.columnconfigure(i, weight=1)
    for i in range(5):
        frame_buttons.rowconfigure(i, weight=1)

    # Botones
    button_c = tk.Button(frame_buttons, text="C", command=lambda: entry.set("0"))
    button_c.grid(column=0, row=0, sticky="nsew", columnspan=3)
    button_div = tk.Button(frame_buttons, text="/", command=lambda: set_operator(" / "))
    button_div.grid(column=3, row=0, sticky="nsew")
    for i in range(1, 10):
        button = tk.Button(
            frame_buttons,
            text=str(i),
            command=lambda i=i: set_number(str(i)),
        )
        button.grid(column=(i - 1) % 3, row=(i - 1) // 3 + 1, sticky="nsew")
    button_mult = tk.Button(
        frame_buttons, text="*", command=lambda: set_operator(" * ")
    )
    button_mult.grid(column=3, row=1, sticky="nsew")
    button_sub = tk.Button(frame_buttons, text="-", command=lambda: set_operator(" - "))
    button_sub.grid(column=3, row=2, sticky="nsew")
    button_sum = tk.Button(
        frame_buttons, text="+", command=lambda: entry.set(entry.get() + " + ")
    )
    button_sum.grid(column=3, row=3, sticky="nsew")
    button_igual = tk.Button(frame_buttons, text="=", command=calculate)
    button_igual.grid(column=3, row=4, sticky="nsew")
    button_punto = tk.Button(
        frame_buttons, text=".", command=lambda: entry.set(entry.get() + ".")
    )
    button_punto.grid(column=2, row=4, sticky="nsew")
    button_0 = tk.Button(
        frame_buttons, text="0", command=lambda: entry.set(entry.get() + "0")
    )
    button_0.grid(column=0, row=4, sticky="nsew", columnspan=2)

    root.mainloop()


if __name__ == "__main__":
    main()
