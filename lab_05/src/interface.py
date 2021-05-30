import tkinter as tk
from solve import get_result, show_graph


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self._tau = None
        self._interior = tk.IntVar()
        self._interior.set(0)
        self._external = tk.IntVar()
        self._external.set(0)
        self._m = None
        self._n = None

        self.add_interface()

    def add_interface(self):
        tk.Label(self, text='Введите \u03C4: ', font='Times 14').grid(row=0, column=0, padx=5, pady=5)
        self._tau = tk.Entry(self, font='Times 14')
        self._tau.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

        tk.Label(self, text='Внешний метод:', font='Times 14').grid(row=1, column=0, padx=5, pady=5)
        tk.Radiobutton(self, variable=self._interior, value=0, text='Гаусса', font='Times 14').grid(row=1, column=1,
                                                                                                    padx=5, pady=5)
        tk.Radiobutton(self, variable=self._interior, value=1, text='Симпсона', font='Times 14').grid(row=1, column=2,
                                                                                                      padx=5, pady=5)

        tk.Label(self, text='Внутренний метод:', font='Times 14').grid(row=2, column=0, padx=5, pady=5)
        tk.Radiobutton(self, variable=self._external, value=0, text='Гаусса', font='Times 14').grid(row=2, column=1,
                                                                                                    padx=5, pady=5)
        tk.Radiobutton(self, variable=self._external, value=1, text='Симпсона', font='Times 14').grid(row=2, column=2,
                                                                                                      padx=5, pady=5)

        tk.Label(self, text='Введите N: ', font='Times 14').grid(row=3, column=0, padx=5, pady=5)
        self._n = tk.Entry(self, font='Times 14')
        self._n.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        tk.Label(self, text='Введите M: ', font='Times 14').grid(row=4, column=0, padx=5, pady=5)
        self._m = tk.Entry(self, font='Times 14')
        self._m.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

        tk.Button(self, text='Посчитать результат', font='Times 14', command=lambda: get_result(self)).grid(
            row=5, column=0, columnspan=3, padx=5, pady=5)
        tk.Button(self, text='Вывести график', font='Times 14', command=show_graph).grid(
            row=6, column=0, columnspan=3, padx=5, pady=5)

    @property
    def tau(self):
        return self._tau.get()

    @property
    def interior(self):
        if self._interior.get() == 0:
            return 'gauss'
        else:
            return 'simpson'

    @property
    def external(self):
        if self._external.get() == 0:
            return 'gauss'
        else:
            return 'simpson'

    @property
    def n(self):
        return self._n.get()

    @property
    def m(self):
        return self._m.get()


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Алгоритмы численного интегрирования')
        self.resizable(False, False)
        self.geometry('390x300')
        MainFrame(self).grid()
