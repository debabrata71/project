import tkinter as tk
from PIL import Image, ImageTk
import random
import time
from playsound import playsound
import threading

class CoinFlipApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coin Flip Simulator")
        self.root.resizable(False, False)

        # Load images
        self.head_img = ImageTk.PhotoImage(Image.open("head.png").resize((150, 150)))
        self.tail_img = ImageTk.PhotoImage(Image.open("tail.png").resize((150, 150)))

        self.image_label = tk.Label(root, image=self.head_img)
        self.image_label.pack(pady=10)

        self.result_label = tk.Label(root, text="Click to Flip!", font=("Arial", 20))
        self.result_label.pack()

        self.flip_button = tk.Button(root, text="Flip Coin", command=self.animate_flip, font=("Arial", 14))
        self.flip_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_counts, font=("Arial", 12))
        self.reset_button.pack()

        self.counts_label = tk.Label(root, text="Heads: 0   Tails: 0", font=("Arial", 14))
        self.counts_label.pack()

        self.prob_label = tk.Label(root, text="Heads: 0.0%   Tails: 0.0%", font=("Arial", 12))
        self.prob_label.pack(pady=5)

        self.heads_count = 0
        self.tails_count = 0

    def animate_flip(self):
        self.flip_button.config(state="disabled")

        def run_animation():
            try:
                playsound("flip.wav", block=False)
            except:
                pass

            for _ in range(10):
                self.image_label.config(image=random.choice([self.head_img, self.tail_img]))
                time.sleep(0.1)

            result = random.choice(["Head", "Tail"])
            if result == "Head":
                self.image_label.config(image=self.head_img)
                self.heads_count += 1
            else:
                self.image_label.config(image=self.tail_img)
                self.tails_count += 1

            self.update_display(result)
            self.flip_button.config(state="normal")

        threading.Thread(target=run_animation).start()

    def update_display(self, result):
        total = self.heads_count + self.tails_count
        head_pct = (self.heads_count / total) * 100 if total > 0 else 0
        tail_pct = (self.tails_count / total) * 100 if total > 0 else 0

        self.result_label.config(text=f"It's a {result}!")
        self.counts_label.config(text=f"Heads: {self.heads_count}   Tails: {self.tails_count}")
        self.prob_label.config(text=f"Heads: {head_pct:.1f}%   Tails: {tail_pct:.1f}%")

    def reset_counts(self):
        self.heads_count = 0
        self.tails_count = 0
        self.result_label.config(text="Click to Flip!")
        self.counts_label.config(text="Heads: 0   Tails: 0")
        self.prob_label.config(text="Heads: 0.0%   Tails: 0.0%")
        self.image_label.config(image=self.head_img)

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = CoinFlipApp(root)
    root.mainloop()
