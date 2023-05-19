import tkinter as tk

class VendingMachine:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Vending Machine")

        self.cola = 1.00
        self.chips = 0.50
        self.candy = 0.75

        self.money_label = tk.Label(self.root, text="Insert Money:")
        self.money_label.pack()

        self.money_entry = tk.Entry(self.root)
        self.money_entry.pack()

        self.cola_button = tk.Button(self.root, text="Cola (${0:.2f})".format(self.cola), command=lambda: self.select_product("Cola", self.cola))
        self.cola_button.pack()

        self.chips_button = tk.Button(self.root, text="Chips (${0:.2f})".format(self.chips), command=lambda: self.select_product("Chips", self.chips))
        self.chips_button.pack()

        self.candy_button = tk.Button(self.root, text="Candy (${0:.2f})".format(self.candy), command=lambda: self.select_product("Candy", self.candy))
        self.candy_button.pack()

        self.message_label = tk.Label(self.root, text="")
        self.message_label.pack()

        self.root.mainloop()

    def select_product(self, product, price):
        money = float(self.money_entry.get())
        if money >= price:
            change = money - price
            self.message_label.config(text="Enjoy your {0}! Your change is ${1:.2f}".format(product, change))
        else:
            self.message_label.config(text="Not enough money. Please insert more.")

if __name__ == "__main__":
    vending_machine = VendingMachine()
