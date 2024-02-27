import ttkbootstrap as tb


class App:
    def __init__(self):
        self.root = tb.Window(themename='superhero')
        self.root.title('TTK Bootstrap')
        self.root.geometry('500x350')

        self.my_entry = tb.Entry()
        self.my_entry.pack(pady=50)

        self.my_button = tb.Button(text="Click Me!",
                                   style='success, outline',
                                   command=self.speak)
        self.my_button.pack(pady=20)

        self.my_label = tb.Label(text='Hello, World!', style='info')
        self.my_label.pack(pady=20)

    def speak(self):
        text = f'You typed {self.my_entry.get()}'
        self.my_label.config(text=text)

    def run(self):
        self.root.mainloop()


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
