import time
from pynput import mouse
import threading
import tkinter as tk
from tkinter import messagebox

class DoubleClickDetector:
    def __init__(self, threshold_ms=200):
        self.last_click_time = 0
        self.threshold = threshold_ms  # limit interval in millisecondes

    def on_click(self, x, y, button, pressed):
        if pressed and button == mouse.Button.left:
            current_time = time.time() * 1000  # time in ms
            diff = current_time - self.last_click_time

            if diff <= self.threshold:
                # Double click detected
                threading.Thread(target=self.show_popup).start()
            self.last_click_time = current_time

    def show_popup(self):
        # tkinter window  
        root = tk.Tk()
        root.withdraw()  # withdrawing main window
        messagebox.showinfo("Double clic détecté", "Double clic possible !")
        root.destroy()

if __name__ == "__main__":
    detector = DoubleClickDetector(threshold_ms=200)
    with mouse.Listener(on_click=detector.on_click) as listener:
        print("Écoute les clics de souris... (fermez avec Ctrl+C)")
        listener.join()
