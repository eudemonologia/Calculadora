import tkinter as tk


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x450")
        self.resizable(False, False)
        self.iconbitmap("calculadora.ico")
        self.entry = tk.StringVar(value="0")

        self._frame_result()
        self._frame_buttons()

    def _frame_result(self):
        frame_result = tk.Frame(self)
        frame_result.pack(fill=tk.BOTH, pady=0)

        entry_result = tk.Entry(
            frame_result,
            textvariable=self.entry,
            state="readonly",
            justify="right",
            font=("Arial", 30, "bold"),
        )
        entry_result.pack(fill=tk.BOTH, expand=True, ipady=15)

    def _frame_buttons(self):
        frame_buttons = tk.Frame(self)
        frame_buttons.pack(fill=tk.BOTH, expand=True)
        for i in range(4):
            frame_buttons.columnconfigure(i, weight=1)
        for i in range(5):
            frame_buttons.rowconfigure(i, weight=1)

        button_c = tk.Button(frame_buttons, text="C", command=self._clear)
        button_c.grid(column=0, row=0, sticky="nsew", columnspan=3)
        button_div = tk.Button(
            frame_buttons, text="/", command=lambda: self._set_operator(" / ")
        )
        button_div.grid(column=3, row=0, sticky="nsew")
        for i in range(1, 10):
            button = tk.Button(
                frame_buttons,
                text=str(i),
                command=lambda i=i: self._set_number(str(i)),
            )
            button.grid(column=(i - 1) % 3, row=(i - 1) // 3 + 1, sticky="nsew")
        button_mult = tk.Button(
            frame_buttons, text="*", command=lambda: self._set_operator(" * ")
        )
        button_mult.grid(column=3, row=1, sticky="nsew")
        button_sub = tk.Button(
            frame_buttons, text="-", command=lambda: self._set_operator(" - ")
        )
        button_sub.grid(column=3, row=2, sticky="nsew")
        button_sum = tk.Button(
            frame_buttons, text="+", command=lambda: self._set_operator(" + ")
        )
        button_sum.grid(column=3, row=3, sticky="nsew")
        button_igual = tk.Button(frame_buttons, text="=", command=self._calculate)
        button_igual.grid(column=3, row=4, sticky="nsew")
        button_punto = tk.Button(frame_buttons, text=".", command=self._set_point)
        button_punto.grid(column=2, row=4, sticky="nsew")
        button_0 = tk.Button(
            frame_buttons,
            text="0",
            command=lambda: self._set_number("0"),
        )
        button_0.grid(column=0, row=4, sticky="nsew", columnspan=2)

    def _calculate(self):
        try:
            result = self.entry.get().split()
            result = [value.lstrip("0") for value in result]
            result = eval("".join(result))
            self.entry.set(str(result))
        except Exception as e:
            print(e)
            self.entry.set("Error")

    def _clear(self):
        self.entry.set("0")

    def _set_number(self, text):
        if self.entry.get() == "0":
            self.entry.set(text)
        else:
            self.entry.set(self.entry.get() + text)

    def _set_point(self):
        if self.entry.get()[-1] not in [".", " "]:
            self.entry.set(self.entry.get() + ".")

    def _set_operator(self, text):
        if self.entry.get()[-1] in [" "]:
            self.entry.set(self.entry.get()[:-3] + text)
        else:
            self.entry.set(self.entry.get() + text)


if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.mainloop()
