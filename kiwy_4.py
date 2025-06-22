from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

pears = 0


class ScrButton(Button):
    def __init__(self, screen, direction="right", goal="main", **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation="vertical", padding=8, spacing=8)
        hl = BoxLayout()
        txt = Label(text="Вибери екран", color = "black")
        vl.add_widget(ScrButton(self, direction="down", goal="first", text="Button"))
        vl.add_widget(ScrButton(self, direction="left", goal="second", text="Password"))
        vl.add_widget(ScrButton(self, direction="up", goal="third", text="pears_counter"))
        vl.add_widget(ScrButton(self, direction="right", goal="fourth", text="pear_clicker"))
        hl.add_widget(txt)
        hl.add_widget(vl)
        self.add_widget(hl)


class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation="vertical", size_hint=(.5, .5), pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn = Button(text="Вибір: 1", size_hint=(.5, 1), pos_hint={"left": 0})
        btn_back = ScrButton(self, direction="up", goal="main", text="Назад", size_hint=(.5, 1), pos_hint={"right": 1})
        vl.add_widget(btn)
        vl.add_widget(btn_back)
        self.add_widget(vl)


class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation="vertical")
        self.txt = Label(text="Вибір: 2", color = "black")
        vl.add_widget(self.txt)

        hl_0 = BoxLayout(size_hint=(0.8, None), height="30sp")
        lbl1 = Label(text="Введіть пароль:", halign="right", color = "black")
        self.input = TextInput(multiline=False)

        hl_0.add_widget(lbl1)
        hl_0.add_widget(self.input)
        vl.add_widget(hl_0)

        hl = BoxLayout(size_hint=(0.5, 0.2), pos_hint={"center_x": 0.5})
        btn_false = Button(text="OK!")
        btn_back = ScrButton(self, direction="right", goal="main", text="Назад")

        hl.add_widget(btn_false)
        hl.add_widget(btn_back)
        vl.add_widget(hl)
        self.add_widget(vl)
        btn_false.on_press = self.change_text

    def change_text(self):
        self.txt.text = self.input.text + "? Не спрацювало ..."


class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vp = BoxLayout(orientation="vertical")
        self.pears_text = Label(text="щоб побачити груші натисніть на кнопку оновити", color = "black")
        self.btn_back = ScrButton(self, direction="down", goal="main", text="Назад", size_hint=(1.0, 0.15))
        self.btn_update = ScrButton(self, text="оновити груші", size_hint=(1.0, 0.15))
        self.btn_update.on_press = self.update_pear
        self.vp.add_widget(self.pears_text)
        self.vp.add_widget(self.btn_back)
        self.vp.add_widget(self.btn_update)
        self.add_widget(self.vp)
    def update_pear(self):
        global pears
        self.pears_text.text = str(pears)

class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vp = BoxLayout(orientation="vertical")
        pear_btn = ScrButton(self, background_normal="pear.png", text="груша")
        btn_back = ScrButton(self, direction="left", goal="main", text="Назад",size_hint=(1.0, 0.15))
        pear_btn.on_press = self.add_pear
        vp.add_widget(pear_btn)
        vp.add_widget(btn_back)
        self.add_widget(vp)
    def add_pear(self):
        global pears
        pears += 1
        print(pears)

class MyApp(App):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(MainScr(name="main"))
        sm.add_widget(FirstScr(name="first"))
        sm.add_widget(SecondScr(name="second"))
        sm.add_widget(ThirdScr(name="third"))
        sm.add_widget(FourthScr(name="fourth"))
        Window.clearcolor = (5, 5, 5, 5)
        return sm


MyApp().run()