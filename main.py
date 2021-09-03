from random import randint

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

Window.size = (300, 100)
Window.clearcolor = (0 / 255, 77 / 255, 64 / 255, 1)
Window.title = "Приложение"


class MainApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='Это текст')

    def btn_pressed(self, *args):
        print("Случайный цвет!")
        self.label.color = (randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255, 1)

    def build(self):
        box = BoxLayout()
        btn = Button(text='Это кнопка!')
        btn.bind(on_press=self.btn_pressed)
        box.add_widget(self.label)
        box.add_widget(btn)

        return box


MainApp().run()
