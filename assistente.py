import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import pyperclip
from datetime import datetime
import sys
import os

def saudacao():
    hora = datetime.now().hour
    if hora < 12:
        return "Bom dia"
    elif hora < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

mensagens = {
    "Atividade concluída": """{saudacao}, atividade concluída com sucesso.

Caso ainda precisem de suporte, estamos à disposição.
Se necessário, a atividade poderá ser reaberta a qualquer momento.""",

    "Sem resposta": """{saudacao},
Como não recebemos retorno, o ticket será encerrado por ora.

Caso ainda precisem de suporte, estamos à disposição.
Se necessário, a atividade poderá ser reaberta a qualquer momento.""",

    "Ausência de evidências": """{saudacao},

Devido a ausência de evidencias ou informações, o ticket será encerrado por ora.

Caso ainda precisem de suporte, estamos à disposição.
Se necessário, a atividade poderá ser reaberta a qualquer momento, caso deseje inserir.""",

    "Complementar chamado": """{saudacao}!
Poderia, por gentileza, complementar o chamado com mais detalhes?
Não consegui compreender totalmente a solicitação e preciso de mais informações para poder lhe ajudar da melhor forma possível.

Fico no aguardo.""",

    "Confirmação solução": """{saudacao}, tudo bem?
Realizamos os ajustes necessários no ambiente. Poderia, por gentileza, confirmar se o problema foi solucionado em sua operação?

Caso ainda precise de suporte técnico, o chamado poderá ser reaberto.""",

    "Encerramento pós-correção": """{saudacao},
A correção foi aplicada e validada com sucesso.

Devido ao problema ter sido resolvido, o ticket será encerrado por ora.
Se necessário, a atividade poderá ser reaberta a qualquer momento.""",

    "Solicitação de detalhes": """{saudacao}!
Verificamos o seu chamado, mas precisamos de mais informações para dar continuidade.
Poderia, por favor, nos informar os passos realizados antes da ocorrência do erro?

Ficamos no aguardo do seu retorno.""",

    "Procedimento local": """{saudacao}, tudo bem?
Identificamos que o erro estava relacionado a configurações locais.
Sugerimos, por gentileza, limpar o cache e reiniciar o navegador para validar.

Se o problema persistir, reabrir o chamado para que possamos atuar novamente.""",

    "Ambiente normalizado": """{saudacao},
O ambiente já se encontra normalizado e estável após a instabilidade temporária.

Devido ao problema ter sido solucionado, o ticket será encerrado.
Caso necessário, poderá ser reaberto a qualquer momento.""",

    "Encerramento falta retorno": """{saudacao},
Como não tivemos retorno em relação ao chamado, o ticket será encerrado.

Caso ainda precise de suporte, estaremos à disposição.
Se necessário, basta reabrir o ticket a qualquer momento."""
}

def copiar_texto(chave):
    texto = mensagens[chave].format(saudacao=saudacao())
    pyperclip.copy(texto)

janela = tk.Tk()
janela.title("Suite de Respostas - Tickets")
janela.geometry("860x720")
janela.configure(bg="#1E1E1E")

# --- Ajuste para logo funcionar no exe ---
def resource_path(relative_path):
    """Retorna o caminho correto do recurso, mesmo dentro do .exe"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

logo_path = resource_path("qualix-logo-transparente.png")
try:
    logo = PhotoImage(file=logo_path)
    logo_label = tk.Label(janela, image=logo, bg="#1E1E1E")
    logo_label.pack(pady=10)
except:
    logo_label = tk.Label(janela, text="LOGO", font=("Arial", 24, "bold"), fg="white", bg="#1E1E1E")
    logo_label.pack(pady=10)

style = ttk.Style()
style.theme_use("clam")

style.configure("TButton",
                font=("Arial", 12, "bold"),
                padding=12,
                relief="flat",
                borderwidth=1,
                background="#333333",
                foreground="white")
style.map("TButton",
          background=[("active", "#0F761D")],
          foreground=[("active", "white")])

frame = ttk.Frame(janela, padding=20)
frame.pack(expand=True, fill="both")
frame.configure(style="TFrame")
style.configure("TFrame", background="#1E1E1E")

lin, col = 0, 0
for i, chave in enumerate(mensagens):
    botao = ttk.Button(frame, text=chave, style="TButton",
                       command=lambda c=chave: copiar_texto(c))
    botao.grid(row=lin, column=col, padx=10, pady=10, sticky="nsew")
    col += 1
    if col > 2:  
        col = 0
        lin += 1

for c in range(3):
    frame.grid_columnconfigure(c, weight=1)

sair_btn = ttk.Button(janela, text="Fechar", style="TButton", command=janela.destroy)
sair_btn.pack(pady=15, fill="x", padx=20)

rodape = tk.Label(janela, text="Feito por Vitor Odorico", font=("Arial", 10, "italic"),
                  fg="gray", bg="#1E1E1E")
rodape.pack(pady=10)

janela.mainloop()
