import tkinter as tk
from tkinter import filedialog

TILE_SIZE = 20

# Paleta VGA 16 cores
VGA_COLORS = {
    'a': '#000000',  # preto
    'b': '#0000AA',  # azul
    'c': '#00AA00',  # verde
    'd': '#00AAAA',  # ciano
    'e': '#AA0000',  # vermelho
    'f': '#AA00AA',  # magenta
    'g': '#AA5500',  # castanho
    'h': '#AAAAAA',  # cinza claro
    'i': '#555555',  # cinza escuro
    'j': '#5555FF',  # azul claro
    'k': '#55FF55',  # verde claro
    'l': '#55FFFF',  # ciano claro
    'm': '#FF5555',  # vermelho claro
    'n': '#FF55FF',  # magenta claro
    'o': '#FFFF55',  # amarelo
    'p': '#FFFFFF',  # branco
}

def load_level():
    filename = filedialog.askopenfilename(
        title="Abrir nível",
        filetypes=[("Text files", "*.txt")]
    )
    if not filename:
        return

    with open(filename, "r") as f:
        lines = [line.strip().lower() for line in f if line.strip()]

    height = len(lines)
    width = max(len(line) for line in lines)

    canvas.config(
        width=width * TILE_SIZE,
        height=height * TILE_SIZE
    )
    canvas.delete("all")

    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            color = VGA_COLORS.get(chr(ord(ch)+65), "#000000")
            x1 = x * TILE_SIZE
            y1 = y * TILE_SIZE
            x2 = x1 + TILE_SIZE
            y2 = y1 + TILE_SIZE

            canvas.create_rectangle(
                x1, y1, x2, y2,
                fill=color,
                outline=""
            )

# GUI
root = tk.Tk()
root.title("VGA Terrain Viewer")

canvas = tk.Canvas(root, bg="black")
canvas.pack(fill=tk.BOTH, expand=True)

root.after(100, load_level)
root.mainloop()

