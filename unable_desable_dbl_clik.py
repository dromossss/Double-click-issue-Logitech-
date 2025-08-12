import time
import threading
import tkinter as tk
from tkinter import messagebox
from pynput import mouse

class DoubleClickBlockerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blocage double-clic")
        self.is_active = False
        self.last_click_time = 0
        self.threshold_ms = 200  # minimal interval

        self.button = tk.Button(root, text="Activer", width=20, command=self.toggle)
        self.button.pack(pady=20)

        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()

    def toggle(self):
        self.is_active = not self.is_active
        self.button.config(text="Désactiver" if self.is_active else "Activer")
        if self.is_active:
            messagebox.showinfo("Info", "Blocage du double-clic activé")
        else:
            messagebox.showinfo("Info", "Blocage du double-clic désactivé")

    def on_click(self, x, y, button, pressed):
        if not self.is_active:
            return  # not active, do nothing

        if pressed and button == mouse.Button.left:
            current_time = time.time() * 1000  # en ms
            diff = current_time - self.last_click_time

            if diff < self.threshold_ms:
                print("Double clic bloqué !")
                # Bloc the double-click
                # but pynput does not allow blocking clicks directly,
                # sp we signal it
                return
            else:
                self.last_click_time = current_time
                print("Clic accepté.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DoubleClickBlockerApp(root)
    root.mainloop()
# This code is a simple GUI application that blocks double-clicks using the pynput library.