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


class MainWindow(Screen):
    result1 = result2 = price1 = price2 = 0

    def change_pic1(self):
        if self.ids.quan1.text == '1':
            self.ids.one.source = '1pizza.png'
            self.ids.one.size_hint = (0.27, 0.27)
        elif self.ids.quan1.text == '2':
            self.ids.one.source = '2pizzas.png'
            self.ids.one.size_hint = (0.27, 0.27)
        elif self.ids.quan1.text == '0' or self.ids.quan1.text == '':
            self.ids.one.size_hint = (0, 0)
        else:
            self.ids.one.source = 'morepizzas.png'
            self.ids.one.size_hint = (0.27, 0.27)

    def change_pic2(self):
        if self.ids.quan2.text == '1':
            self.ids.two.source = '1pizza.png'
            self.ids.two.size_hint = (0.27, 0.27)
        elif self.ids.quan2.text == '2':
            self.ids.two.source = '2pizzas.png'
            self.ids.two.size_hint = (0.27, 0.27)
        elif self.ids.quan2.text == '0' or self.ids.quan2.text == '':
            self.ids.two.size_hint = (0,0)
        else:
            self.ids.two.source = 'morepizzas.png'
            self.ids.two.size_hint = (0.27, 0.27)

    def calculate(self):
        try:
            self.result1 = float(self.ids.quan1.text) * (3.14 * ((float(self.ids.size1.text)/2)**2))
            self.result2 = float(self.ids.quan2.text) * (3.14 * ((float(self.ids.size2.text)/2)**2))

            self.price1 = float(self.ids.price1.text) * float(self.ids.quan1.text)
            self.price2 = float(self.ids.price2.text) * float(self.ids.quan2.text)

            self.ids.tarea1.text = f'{str(round(self.result1, 2))} cm\u00B2'
            self.ids.tarea2.text = f'{str(round(self.result2, 2))} cm\u00B2'
            self.ids.tprice1.text = f'{str(round(self.price1, 2))} :-'
            self.ids.tprice2.text = f'{str(round(self.price2, 2))} :-'

            self.ids.tarea.font_size = '14dp'
            self.ids.tprice.font_size = '14dp'

            if self.result1 > self.result2:
                self.ids.tarea1.color = get_color_from_hex('#1fe800')
                self.ids.tarea2.color = get_color_from_hex('#e80000')
                self.ids.res1.source = 'right.png'
                self.ids.res1.size_hint = (0.15, 0.15)
                self.ids.res2.source = 'wrong.png'
                self.ids.res2.size_hint = (0.15, 0.15)

            elif self.result1 == self.result2:
                self.ids.tarea1.color = get_color_from_hex('#d6890d')
                self.ids.tarea2.color = get_color_from_hex('#d6890d')
            else:
                self.ids.tarea2.color = get_color_from_hex('#1fe800')
                self.ids.tarea1.color = get_color_from_hex('#e80000')
                self.ids.res2.source = 'right.png'
                self.ids.res1.size_hint = (0.15, 0.15)
                self.ids.res1.source = 'wrong.png'
                self.ids.res2.size_hint = (0.15, 0.15)

            if self.price1 < self.price2:
                self.ids.tprice1.color = get_color_from_hex('#1fe800')
                self.ids.tprice2.color = get_color_from_hex('#e80000')
            elif self.price1 == self.price2:
                self.ids.tprice1.color = get_color_from_hex('#d6890d')
                self.ids.tprice2.color = get_color_from_hex('#d6890d')
            else:
                self.ids.tprice2.color = get_color_from_hex('#1fe800')
                self.ids.tprice1.color = get_color_from_hex('#e80000')


        except:
            show_popup()

    def clear_inputs(self):
        self.ids.quan1.text = ''
        self.ids.quan2.text = ''
        self.ids.price1.text = ''
        self.ids.price2.text = ''
        self.ids.size1.text = ''
        self.ids.size2.text = ''

        self.ids.tarea1.text = ''
        self.ids.tarea2.text = ''
        self.ids.tprice1.text = ''
        self.ids.tprice2.text = ''

        self.ids.res1.size_hint = (0, 0)
        self.ids.res2.size_hint = (0, 0)
        self.ids.one.size_hint = (0, 0)
        self.ids.two.size_hint = (0, 0)

        self.ids.tarea.font_size = '0dp'
        self.ids.tprice.font_size = '0dp'


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
