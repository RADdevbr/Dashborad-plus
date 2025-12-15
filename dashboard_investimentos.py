import tkinter as tk
from tkinter import ttk, messagebox
import math

class InvestmentRow:
    def __init__(self, master, row):
        self.frame = ttk.Frame(master)

        ttk.Label(self.frame, text=f"Investimento {row+1}").grid(column=0, row=0, padx=5)

        ttk.Label(self.frame, text="Valor inicial:").grid(column=0, row=1, sticky="w")
        self.initial = ttk.Entry(self.frame, width=12)
        self.initial.grid(column=1, row=1)

        ttk.Label(self.frame, text="Aporte mensal:").grid(column=2, row=1, sticky="w")
        self.monthly = ttk.Entry(self.frame, width=12)
        self.monthly.grid(column=3, row=1)

        ttk.Label(self.frame, text="Taxa anual (%):").grid(column=4, row=1, sticky="w")
        self.rate = ttk.Entry(self.frame, width=12)
        self.rate.grid(column=5, row=1)

        ttk.Label(self.frame, text="Tempo:").grid(column=6, row=1, sticky="w")
        self.time = ttk.Entry(self.frame, width=12)
        self.time.grid(column=7, row=1)

        self.time_unit = ttk.Combobox(self.frame, values=["Meses", "Anos"], width=8)
        self.time_unit.current(0)
        self.time_unit.grid(column=8, row=1, padx=5)

        self.frame.pack(pady=5)

    def get_values(self):
        try:
            initial = float(self.initial.get())
            monthly = float(self.monthly.get())
            rate = float(self.rate.get()) / 100
            time = int(self.time.get())
            if self.time_unit.get() == "Anos":
                time *= 12
            return initial, monthly, rate, time
        except:
            return None


class InvestmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Investimentos")

        self.rows_frame = ttk.Frame(root)
        self.rows_frame.pack(pady=10)

        self.rows = []
        self.add_row()

        ttk.Button(root, text="Adicionar linha", command=self.add_row).pack(pady=5)
        ttk.Button(root, text="Calcular", command=self.calculate).pack(pady=5)

        self.result_label = ttk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def add_row(self):
        row = InvestmentRow(self.rows_frame, len(self.rows))
        self.rows.append(row)

    def calculate(self):
        total = 0
        details = ""

        for i, row in enumerate(self.rows):
            values = row.get_values()
            if not values:
                messagebox.showerror("Erro", f"Preencha corretamente os valores da linha {i+1}.")
                return

            initial, monthly, rate, months = values
            monthly_rate = (1 + rate) ** (1/12) - 1

            # Fórmula de juros compostos com aportes mensais
            future_value = (
                initial * (1 + monthly_rate) ** months +
                monthly * (((1 + monthly_rate) ** months - 1) / monthly_rate)
            )

            total += future_value
            details += f"Investimento {i+1}: R$ {future_value:,.2f}\n"

        details += f"\nTOTAL: R$ {total:,.2f}"
        self.result_label.config(text=details)


root = tk.Tk()
app = InvestmentApp(root)
root.mainloop()