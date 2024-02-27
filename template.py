import ttkbootstrap as tb


class App:
    def __init__(self):
        self.root = tb.Window(themename='superhero')
        self.root.title('TTK Bootstrap')
        self.root.geometry('500x350')

    def run(self):
        self.root.mainloop()


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
