import ttkbootstrap as tb


class App:
    def __init__(self):
        self.root = tb.Window(themename='superhero')
        self.root.title('TTK Bootstrap')
        self.root.geometry('500x350')

        self.counter = 0

        self.my_label = tb.Label(text="Hello, World!",
                                 font='Helvetica 28',
                                 style='danger, inverse')
        self.my_label.pack(pady=50)

        self.my_button = tb.Button(text="Click Me!", style='success, outline',
                                   command=self.changer)
        self.my_button.pack(pady=20)

    def changer(self):
        self.counter += 1
        if self.counter % 2 == 0:
            self.my_label.config(text='Hello, World!')
        else:
            self.my_label.config(text='Goodbye, World!')

    def run(self):
        self.root.mainloop()


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
