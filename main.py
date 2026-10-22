import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class Aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Lista de Tarefas"
        self.geometry("300x600")

        # configuração das partes
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Parte de cima
        self.parte_cima_Frame = ctk.CTkFrame(self, width=300)
        self.parte_cima_Frame.grid(row=0, column=0, sticky="nsew")
        self.parte_cima_Frame.grid_propagate(True)

        self.construir_parte_cima()

        # Parte de Lista
        self.parte_lista_ScrollableFrame = ctk.CTkScrollableFrame(self, width=300,)
        self.parte_lista_ScrollableFrame.grid(row=1, column=0, sticky="nsew", pady=10)


    def construir_parte_cima(self):
        self.mintr_txt_Label = ctk.CTkLabel(
            self.parte_cima_Frame,
            text = "Minhas Tarefas",
            font = ctk.CTkFont(size= 15)
        )
        self.mintr_txt_Label.grid(
            row = 0,
            column = 0,
            padx=10,
            pady=(10,0),
            sticky="w"
        )

        ctk_tarefas = ctk.StringVar(value="0 de 0 tarefas concluídas")
        self.tarefas_concluidas_Label = ctk.CTkLabel(
            self.parte_cima_Frame,
            textvariable=ctk_tarefas,
            font = ctk.CTkFont(size= 15)
        )
        self.tarefas_concluidas_Label.grid(
            row = 1,
            column = 0,
            padx = 10,
            pady = (0,10),
            sticky="w"
        )

        self.adicionar_tarefa_button = ctk.CTkButton(
            self.parte_cima_Frame,
            text = "Adicionar Tarefa."
        )
        self.adicionar_tarefa_button.grid(row = 0, column = 1, rowspan = 2)


janela = Aplicativo()
janela.mainloop()
