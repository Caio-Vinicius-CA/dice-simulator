import tkinter as tk
import random

class DiceSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Dados")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")  # Fundo claro

        # Centralizar a janela
        self.center_window(400, 300)

        # Título
        self.label = tk.Label(
            root, 
            text="Clique no botão para rolar o dado 🎲", 
            font=("Arial", 14, "bold"),
            bg="#f0f0f0"
        )
        self.label.pack(pady=20)

        # Botão estilizado
        self.button = tk.Button(
            root, 
            text="Rolar Dado", 
            command=self.roll_dice,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",       # Verde
            fg="white",         # Texto branco
            activebackground="#45a049",  
            activeforeground="white",
            relief="raised",
            width=15,
            height=2,
            cursor="hand2"
        )
        self.button.pack(pady=10)

        # Label de resultado
        self.result_label = tk.Label(
            root, 
            text="", 
            font=("Arial", 24, "bold"), 
            bg="#f0f0f0"
        )
        self.result_label.pack(pady=30)

    def roll_dice(self):
        number = random.randint(1, 6)

        # Cores diferentes dependendo do número
        colors = {
            1: "red",
            2: "orange",
            3: "blue",
            4: "purple",
            5: "teal",
            6: "green"
        }

        self.result_label.config(
            text=f"🎲 {number} 🎲", 
            fg=colors[number]
        )

    def center_window(self, width, height):
        """Centraliza a janela na tela"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.root.geometry(f"{width}x{height}+{x}+{y}")
