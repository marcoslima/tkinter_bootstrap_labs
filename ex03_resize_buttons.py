import ttkbootstrap as tb


class App:
    def __init__(self):
        self.root = tb.Window(themename='superhero')
        self.root.title('TTK Bootstrap')
        self.root.geometry('500x350')

        button_style = self._make_style('danger.Outline.TButton',
                                        font=('Helvetica', 28))
        self.my_button = tb.Button(text='Hello World!',
                                   style=button_style,
                                   width=20)
        self.my_button.pack(pady=40)

    @staticmethod
    def _make_style(style: str, **kwargs) -> str:
        my_style = tb.Style()
        my_style.configure(style, **kwargs)
        return style

    def run(self):
        self.root.mainloop()


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
