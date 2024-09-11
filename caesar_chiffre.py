import tkinter as tk
from tkinter import scrolledtext

# Funktion zum Entschlüsseln des Cäsar-Chiffres
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Bestimme den ASCII-Code der Basis (A oder a)
            base = ord('A') if char.isupper() else ord('a')
            # Verschiebe den Buchstaben und stelle sicher, dass er im Alphabet bleibt
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Funktion zum Generieren aller möglichen Entschlüsselungen
def all_caesar_decryptions(ciphertext):
    solutions = []
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        solutions.append(f"Shift {shift}: {decrypted_text}")
    return solutions

# Funktion, die aufgerufen wird, wenn der Button geklickt wird
def show_decryptions():
    ciphertext = entry.get()
    solutions = all_caesar_decryptions(ciphertext)
    result_text.delete(1.0, tk.END)
    for solution in solutions:
        result_text.insert(tk.END, solution + "\n")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Cäsar-Chiffre Entschlüssler")

# Eingabefeld für den verschlüsselten Text
tk.Label(root, text="Verschlüsselter Text:").pack()
entry = tk.Entry(root, width=50)
entry.pack()

# Button zum Generieren der Entschlüsselungen
decrypt_button = tk.Button(root, text="Entschlüsselungen anzeigen", command=show_decryptions)
decrypt_button.pack()

# Textfeld zum Anzeigen der Entschlüsselungen
result_text = scrolledtext.ScrolledText(root, width=70, height=20)
result_text.pack()

# GUI-Schleife starten
root.mainloop()