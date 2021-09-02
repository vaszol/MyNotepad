from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

Window.size = (300, 100)
Window.clearcolor = (0 / 255, 77 / 255, 64 / 255, 1)
Window.title = "Приложение"


class MainApp(App):
    def build(self):
        box = BoxLayout()
        btn = Button(text='Это кнопка!')
        label = Label(text='Это текст')
        box.add_widget(label)
        box.add_widget(btn)

        return box


MainApp().run()
