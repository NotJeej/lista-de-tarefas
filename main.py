import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class JanelaNovaTarefa(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.app: "Aplicativo" = master
        self.title("Nova tarefa")
        self.geometry("300x600")

        self.grab_set()

        azul = ctk.ThemeManager.theme["CTkButton"]["fg_color"]
        azul_escuro = ctk.ThemeManager.theme["CTkButton"]["hover_color"]

        # Configuração das colunas e linhas
        self.grid_columnconfigure((0, 1), weight=1)

        self.jt_titulo_label = ctk.CTkLabel(
            self,
            text="Título:"
        )
        self.jt_titulo_label.grid(
            row=0,
            column=0,
            sticky = "w",
            padx="10"
        )

        self.jt_titulo_entry = ctk.CTkEntry(
            self,
            placeholder_text="Ex.: Estudar"
        )
        self.jt_titulo_entry.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10
        )

        self.jt_detalhes_label = ctk.CTkLabel(
            self,
            text="Detalhes:"
        )
        self.jt_detalhes_label.grid(
            row=2,
            column=0,
            sticky="w",
            padx=10,
            pady=(20,0)
        )

        self.jt_detalhes_textbox = ctk.CTkTextbox(
            self,
            height=80,
            wrap="word"
        )
        self.jt_detalhes_textbox.grid(
            row=3,
            column=0,
            sticky="nsew",
            columnspan=2,
            padx=20
        )

        self.jt_preview_label = ctk.CTkLabel(
            self,
            text="Preview:"
        )
        self.jt_preview_label.grid(
            row=4,
            column=0,
            sticky="w",
            padx=10
        )

        self.jt_preview_freme = ctk.CTkFrame(
            self,
            fg_color=azul
        )
        self.jt_preview_freme.grid(
            row=5,
            column=0,
            columnspan=2,
            sticky = "nswe",
            padx=10
        )
        self.jt_preview_freme.grid_columnconfigure(0, weight=1)

        self.jt_cancelar_button = ctk.CTkButton(
            self,
            text="Cancelar",
            fg_color="#c0392b",
            hover_color="#962d22",
            command=self.destroy
        )
        self.jt_cancelar_button.grid(
            row=6,
            column=0,
            padx=10,
            sticky="ew"
        )

        self.jt_salvar_button = ctk.CTkButton(
            self,
            text="Salvar",
            fg_color="#27ae60",
            hover_color="#1e8449",
            command=self.salvar
        )
        self.jt_salvar_button.grid(
            row=6,
            column=1,
            padx=10,
            sticky = "ew"
        )

        self.jt_preview_titulo_label = ctk.CTkLabel(
            self.jt_preview_freme,
            text="",
            anchor="w"
        )
        self.jt_preview_titulo_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=10
        )

        self.jt_preview_textbox = ctk.CTkTextbox(
            self.jt_preview_freme,
            height=80,
            wrap = "word",
            fg_color=azul_escuro
        )
        self.jt_preview_textbox.grid(
            row=1,
            column=0,
            padx=10,
            pady=(0, 10),
            sticky= "nsew"
        )
        self.jt_preview_textbox.configure(state="disabled")

        self.jt_titulo_entry.bind("<KeyRelease>", self.atualizar_preview)
        self.jt_detalhes_textbox.bind("<KeyRelease>", self.atualizar_preview)


    def salvar(self):
        titulo = self.jt_titulo_entry.get()
        detalhes = self.jt_detalhes_textbox.get("1.0","end-1c")

        l_titulo = " ".join(titulo.strip().split())
        l_detalhes = " ".join(detalhes.strip().split())

        if not titulo:
            return

        self.app.adicionar_tarefa(l_titulo, l_detalhes)
        self.destroy()

    def atualizar_preview(self, event=None):
        titulo = self.jt_titulo_entry.get()
        detalhes = self.jt_detalhes_textbox.get("1.0","end-1c")

        l_titulo = " ".join(titulo.strip().split())
        l_detalhes = " ".join(detalhes.strip().split())

        self.jt_preview_titulo_label.configure(text=l_titulo)

        self.jt_preview_textbox.configure(state="normal")
        self.jt_preview_textbox.delete("1.0", "end")
        self.jt_preview_textbox.insert("1.0", l_detalhes)
        self.jt_preview_textbox.configure(state="disabled")


class Aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Tarefas")
        self.geometry("300x600")

        # configuração das partes
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Parte de cima
        self.parte_cima_Frame = ctk.CTkFrame(self, width=300)
        self.parte_cima_Frame.grid(row=0, column=0, sticky="nsew")
        self.parte_cima_Frame.grid_propagate(True)

        self.janela_nova = None
        self.tarefas = []

        self.construir_parte_cima()

        # Parte de Lista
        self.parte_lista_ScrollableFrame = ctk.CTkScrollableFrame(self, width=300,)
        self.parte_lista_ScrollableFrame.grid(row=1, column=0, sticky="nsew", pady=10)

    def adicionar_tarefa(self, titulo, detalhes):
        tarefa = {
            "titulo": titulo,
            "detalhes": detalhes,
            "concluida": False
        }
        self.tarefas.append(tarefa)
        print(self.tarefas)

    # Abrir a janela no qual o usuário registra a tarefa.
    def abrir_janela(self):
            if self.janela_nova is None or not self.janela_nova.winfo_exists():
                self.janela_nova = JanelaNovaTarefa(self)
            else:
                self.janela_nova.focus()

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
            text = "Adicionar Tarefa.",
            command=self.abrir_janela
        )
        self.adicionar_tarefa_button.grid(row = 0, column = 1, rowspan = 2)


janela = Aplicativo()
janela.mainloop()
