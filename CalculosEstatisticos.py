import tkinter as tk
import math
from tkinter import messagebox

def calcular_valores_estatisticos():
    # Obter os dados do campo de entrada
    dados = entrada_dados.get()
    dados = dados.split(";")
    dados = [float(x.strip()) for x in dados]

    # Obter o valor do erro instrumental do campo de entrada
    erro_instrumental = float(entrada_erro_instrumental.get())

    # Verificar se há pelo menos dois dados
    if len(dados) < 2:
        messagebox.showerror("Dados Insuficientes", "Insira pelo menos dois dados para realizar os cálculos estatísticos.")
        return

    # Calcular os valores estatísticos
    media = sum(dados) / len(dados)
    desvio_absoluto = sum(abs(x - media) for x in dados) / len(dados)
    desvio_quadratico = math.sqrt(sum((x - media) ** 2 for x in dados) / len(dados))
    desvio_padrao = math.sqrt(sum((x - media) ** 2 for x in dados) / (len(dados) - 1))
    variancia = sum((x - media) ** 2 for x in dados) / (len(dados) - 1)
    erro_padrao = desvio_padrao / math.sqrt(len(dados))
    erro_total = math.sqrt(erro_instrumental ** 2 + erro_padrao ** 2)
    erro_estatistico = math.sqrt(erro_instrumental ** 2 + (erro_padrao ** 2) / len(dados))

    # Exibir os resultados na interface gráfica
    resultado_media.config(text=f"Média: {media:.2f}")
    resultado_desvio_absoluto.config(text=f"Desvio Absoluto: {desvio_absoluto:.2f}")
    resultado_desvio_quadratico.config(text=f"Desvio Quadrático: {desvio_quadratico:.2f}")
    resultado_desvio_padrao.config(text=f"Desvio Padrão: {desvio_padrao:.2f}")
    resultado_variancia.config(text=f"Variância: {variancia:.2f}")
    resultado_erro_padrao.config(text=f"Erro Padrão: {erro_padrao:.2f}")
    resultado_erro_total.config(text=f"Erro Total: {erro_total:.2f}")
    resultado_erro_estatistico.config(text=f"Erro Estatístico: {erro_estatistico:.2f}")

def reiniciar():
    # Limpar os campos de entrada
    entrada_dados.delete(0, tk.END)
    entrada_erro_instrumental.delete(0, tk.END)

    # Limpar os resultados
    resultado_media.config(text="")
    resultado_desvio_absoluto.config(text="")
    resultado_desvio_quadratico.config(text="")
    resultado_desvio_padrao.config(text="")
    resultado_variancia.config(text="")
    resultado_erro_padrao.config(text="")
    resultado_erro_total.config(text="")
    resultado_erro_estatistico.config(text="")

def fechar_programa():
    if messagebox.askokcancel("Fechar", "Deseja fechar o programa?"):
        janela.destroy()

def mostrar_ajuda():
    messagebox.showinfo("Ajuda", "Para inserir os dados, separe-os por ponto e vírgula (;).\nUse ponto (.) para separar as casas decimais.\nInsira pelo menos dois dados para realizar os cálculos estatísticos.\nNão há necessidade de informar unidade de medida, os resultados virão na unidade utilizada.")

# Cria a janela da interface gráfica
janela = tk.Tk()
janela.title("Cálculos Estatísticos")

# Configurações de estilo
bg_color = "#f2f2f2"
button_bg_color = "#007fff"
button_fg_color = "white"
button_active_bg_color = "blue"
label_font = ("Arial", 13)
entry_font = ("Arial", 12)

# Configuração de cor de fundo
janela.configure(bg=bg_color)

# Cria os elementos da interface
tk.Label(janela, text="Cálculos Estatísticos", font=label_font, bg=bg_color).pack(pady=5)
tk.Label(janela, text="Insira ao menos dois dados:", font=label_font, bg=bg_color).pack(pady=5)
entrada_dados = tk.Entry(janela, width=50, font=entry_font, bd=2)
entrada_dados.pack(pady=5)

tk.Label(janela, text="Erro Instrumental:", font=label_font, bg=bg_color).pack(pady=5)
entrada_erro_instrumental = tk.Entry(janela, width=10, font=entry_font, bd=2)
entrada_erro_instrumental.pack(pady=5)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular_valores_estatisticos, width=20, font=label_font, bg=button_bg_color, fg=button_fg_color, activebackground=button_active_bg_color, relief=tk.RAISED, bd=2)
botao_calcular.pack(pady=10)

botao_ajuda = tk.Button(janela, text="Ajuda", command=mostrar_ajuda, width=20, font=label_font, bg=button_bg_color, fg=button_fg_color, activebackground=button_active_bg_color, relief=tk.RAISED, bd=2)
botao_ajuda.pack(pady=10)

resultado_media = tk.Label(janela, text="", font=label_font, bg=bg_color)
resultado_media.pack()

resultado_desvio_absoluto = tk.Label(janela, text="", font=label_font, bg=bg_color)
resultado_desvio_absoluto.pack()

resultado_desvio_quadratico = tk.Label(janela, text="", font=label_font, bg=bg_color)
resultado_desvio_quadratico.pack()

resultado_desvio_padrao = tk.Label(janela, text="", font=label_font, bg=bg_color)
resultado_desvio_padrao.pack()

resultado_variancia = tk.Label(janela, text="", font=label_font, bg=bg_color)
resultado_variancia.pack()

resultado_erro_padrao = tk.Label(janela, text="", font=label_font, bg=bg_color)
resultado_erro_padrao.pack()

resultado_erro_total = tk.Label(janela, text="", font=label_font, bg=bg_color)
resultado_erro_total.pack()

resultado_erro_estatistico = tk.Label(janela, text="", font=label_font, bg=bg_color)
resultado_erro_estatistico.pack()

botao_reiniciar = tk.Button(janela, text="Limpar Dados", command=reiniciar, width=20, font=label_font, bg="black", fg=button_fg_color, activebackground=button_active_bg_color, relief=tk.RAISED, bd=2)
botao_reiniciar.pack(pady=10)

botao_fechar = tk.Button(janela, text="Fechar", command=fechar_programa, width=20, font=label_font, bg="red", fg=button_fg_color, activebackground="red", relief=tk.RAISED, bd=2)
botao_fechar.pack(side=tk.BOTTOM, pady=10)



# Define o tamanho e posição da janela
largura_janela = 1280
altura_janela = 720
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = (largura_tela - largura_janela) // 2
posicao_y = (altura_tela - altura_janela) // 2
janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

# Executa a interface gráfica
janela.mainloop()

