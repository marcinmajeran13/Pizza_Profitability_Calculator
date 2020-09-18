from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager, SwapTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.popup import Popup


Window.clearcolor = get_color_from_hex('#ade6a3')
Window.size = (375, 675)


class WelcomeWindow(Screen, FloatLayout):
    pass


class P(Screen, FloatLayout):
    pass


class MainWindow(Screen, BoxLayout):

    def change_pic1(self):
        if self.ids.quan1.text == '1':
            self.ids.one.source = '1pizza.png'
        elif self.ids.quan1.text == '2':
            self.ids.one.source = '2pizzas.png'
        else:
            self.ids.one.source = 'morepizzas.png'

    def change_pic2(self):
        if self.ids.quan2.text == '1':
            self.ids.two.source = '1pizza.png'
        elif self.ids.quan2.text == '2':
            self.ids.two.source = '2pizzas.png'
        else:
            self.ids.two.source = 'morepizzas.png'

    def calculate(self):
        try:
            result1 = float(self.ids.quan1.text) * (3.14 * ((float(self.ids.size1.text)/2)**2))
            result2 = float(self.ids.quan2.text) * (3.14 * ((float(self.ids.size2.text)/2)**2))

            price1 = float(self.ids.price1.text) * float(self.ids.quan1.text)
            price2 = float(self.ids.price2.text) * float(self.ids.quan2.text)

        except:
            show_popup()

    def clear_inputs(self):
        self.ids.quan1.text = ''
        self.ids.quan2.text = ''
        self.ids.price1.text = ''
        self.ids.price2.text = ''
        self.ids.size1.text = ''
        self.ids.size2.text = ''


class ResultWindow(Screen, BoxLayout):
    pass


class WindowManager(ScreenManager):
    pass


builder = Builder.load_file('pizzacalc.kv')


class PizzaCalcApp(App):
    def build(self):
        return builder


def show_popup():
    show = P()

    popupWindow = Popup(title='Error', content=show
                        , size_hint=(None, None), size=(300, 200))

    popupWindow.open()


if __name__ == '__main__':
    PizzaCalcApp().run()
