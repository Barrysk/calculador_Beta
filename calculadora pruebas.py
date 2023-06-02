from tkinter import *
import tkinter.messagebox as messagebox
import math

def perform_operation(choice, num1, num2):
    if choice == 1:
        result = num1 + num2
        messagebox.showinfo("Resultado", f"El resultado de la suma es: {result}")

    elif choice == 2:
        result = num1 - num2
        messagebox.showinfo("Resultado", f"El resultado de la resta es: {result}")

    elif choice == 3:
        result = num1 * num2
        messagebox.showinfo("Resultado", f"El resultado de la multiplicación es: {result}")

    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
            messagebox.showinfo("Resultado", f"El resultado de la división es: {result}")
        else:
            messagebox.showerror("Error", "No se puede dividir entre cero.")

    elif choice == 5:
        result = math.sqrt(num1)
        messagebox.showinfo("Resultado", f"El resultado de la raíz cuadrada es: {result}")

    elif choice == 6:
        result = num1 ** num2
        messagebox.showinfo("Resultado", f"El resultado de la potencia es: {result}")

    elif choice == 7:
        if num1 > 0:
            area = math.pi * num1**2
            perimeter = 2 * math.pi * num1
            messagebox.showinfo("Resultado", f"Área: {area}\nPerímetro: {perimeter}")
        else:
            messagebox.showerror("Error", "El radio debe ser mayor que cero.")

    elif choice == 8:
        if num1 > 0:
            area = num1 * num1
            perimeter = 4 * num1
            messagebox.showinfo("Resultado", f"Área: {area}\nPerímetro: {perimeter}")
        else:
            messagebox.showerror("Error", "El lado debe ser mayor que cero.")

    elif choice == 9:
        area = num1 * num2
        perimeter = 2 * (num1 + num2)
        messagebox.showinfo("Resultado", f"Área: {area}\nPerímetro: {perimeter}")

    elif choice == 10:
        base = num1
        height = num2
        area = (base * height) / 2
        perimeter = num2 * 3
        messagebox.showinfo("Resultado", f"Área: {area}\nPerímetro: {perimeter}")

    elif choice == 11:
        angulo = num1
        seno = math.sin(angulo)
        coseno = math.cos(angulo)
        tangente = math.tan(angulo)
        messagebox.showinfo("Resultado", f"Seno: {seno}\nCoseno: {coseno}\nTangente: {tangente}")

def show_calculator():
    window = Tk()
    window.title("Calculadora")
    
    label_num1 = Label(window, text="Número 1:")
    label_num1.pack()
    entry_num1 = Entry(window)
    entry_num1.pack()
    
    def calculate():
        choice = choice_var.get()
        num1 = float(entry_num1.get())
        num2 = 0 if choice in [7, 8] else float(entry_num2.get())
        perform_operation(choice, num1, num2)
    
    choice_var = IntVar()
    choice_var.set(1)
    
    option_frame = Frame(window)
    option_frame.pack()
    
    option_suma = Radiobutton(option_frame, text="Suma", variable=choice_var, value=1)
    option_suma.pack(anchor=W)
    
    option_resta = Radiobutton(option_frame, text="Resta", variable=choice_var, value=2)
    option_resta.pack(anchor=W)
    
    option_multiplicacion = Radiobutton(option_frame, text="Multiplicación", variable=choice_var, value=3)
    option_multiplicacion.pack(anchor=W)
    
    option_division = Radiobutton(option_frame, text="División", variable=choice_var, value=4)
    option_division.pack(anchor=W)
    
    option_raiz = Radiobutton(option_frame, text="Raíz cuadrada", variable=choice_var, value=5)
    option_raiz.pack(anchor=W)
    
    option_potencia = Radiobutton(option_frame, text="Potencia", variable=choice_var, value=6)
    option_potencia.pack(anchor=W)
    
    option_circulo = Radiobutton(option_frame, text="Perímetro y Área de un círculo", variable=choice_var, value=7)
    option_circulo.pack(anchor=W)
    
    option_cuadrado = Radiobutton(option_frame, text="Perímetro y Área de un cuadrado", variable=choice_var, value=8)
    option_cuadrado.pack(anchor=W)
    
    option_rectangulo = Radiobutton(option_frame, text="Perímetro y Área de un rectángulo", variable=choice_var, value=9)
    option_rectangulo.pack(anchor=W)
    
    option_triangulo = Radiobutton(option_frame, text="Perímetro y Área de un triángulo", variable=choice_var, value=10)
    option_triangulo.pack(anchor=W)
    
    option_trigonometria = Radiobutton(option_frame, text="Trigonometría", variable=choice_var, value=11)
    option_trigonometria.pack(anchor=W)
    
    label_num2 = Label(window, text="Número 2:")
    label_num2.pack()
    entry_num2 = Entry(window)
    entry_num2.pack()
    
    button_calcular = Button(window, text="Calcular", command=calculate)
    button_calcular.pack(pady=10)
    
    window.mainloop()

show_calculator()
