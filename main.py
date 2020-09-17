from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.lang import Builder

Window.clearcolor = get_color_from_hex('#454343')


class WelcomeWindow(Screen, FloatLayout):
    pass


class MainWindow(Screen, BoxLayout):
    pass


class ResultWindow(Screen, BoxLayout):
    pass


class WindowManager(ScreenManager):
    pass


builder = Builder.load_file('pizzacalc.kv')


class PizzaCalcApp(App):
    def build(self):
        return builder


if __name__ == '__main__':
    PizzaCalcApp().run()
