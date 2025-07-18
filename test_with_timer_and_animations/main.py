
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from instructions import txt_instruction, txt_test1, txt_test3, txt_sits
from ruffier import test
from seconds import Seconds

from kivy.core.window import Window  # ⬅️⬅️⬅️
from sits import Sits  # ⬅️⬅️⬅️
from runner import Runner  # ⬅️⬅️⬅️


theme = 0
# btn_background_normal = "images/img.png"  # ⬅️⬅️⬅️
# btn_background_down = "images/down.png"  # ⬅️⬅️⬅️


age = 7
name = ""
p1, p2, p3 = 0, 0, 0


def check_int(str_num):
    # повертає число або False, якщо рядок не конвертується
    try:
        return int(str_num)
    except:
        return False


# головний екран із поясненням і привітанням
# вводимо ім'я вік
class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.instr = Label(text=txt_instruction, color="#CBBFBB")
        self.lbl1 = Label(text="Введіть ім'я:", halign="right", color="#CBBFBB")
        self.in_name = TextInput(multiline=False)
        self.lbl2 = Label(text="Введіть вік:", halign="right", color="#CBBFBB")
        self.in_age = TextInput(multiline=False)
        self.btn = Button(
            text="Почати", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
        )
        self.btn_theme = Button(
            text="світлий фон", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
        )

        self.btn.on_press = self.next
        self.btn_theme.on_press = self.next_theme

        self.line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        self.line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        self.line1.add_widget(self.lbl1)
        self.line1.add_widget(self.in_name)
        self.line2.add_widget(self.lbl2)
        self.line2.add_widget(self.in_age)
        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.outer.add_widget(self.instr)
        self.outer.add_widget(self.line1)
        self.outer.add_widget(self.line2)
        self.outer.add_widget(self.btn)
        self.outer.add_widget(self.btn_theme)
        self.add_widget(self.outer)

        self.set_style()

    def next(self):
        global name, age
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if age == False or age < 7:
            age = 7

        else:
            self.manager.current = "pulse1"

    def next_theme(self):
        global theme

        if theme == 1:
            theme = 0
        else:
            theme = 1
        self.set_style()

    def set_style(self):
        if theme == 0:
            Window.clearcolor = "#493843"  # ⬅️⬅️⬅️
            self.btn_color = "#8A7C7F"
            self.btn_color_presed = "#AB9E9D"
            self.instr.color = self.lbl1.color = self.lbl2.color = "#CBBFBB"
        else:
            Window.clearcolor = "#CBBFBB"  # ⬅️⬅️⬅️
            self.btn_color = "#CBBFBB"
            self.btn_color_presed = "#493843"
            self.instr.color = self.lbl1.color = self.lbl2.color = "#493843"

        self.btn.background_color = self.btn_color  # ⬅️⬅️⬅️
        self.btn.background_down = self.btn_color_presed  # ⬅️⬅️⬅️
        self.btn_theme.background_color = self.btn_color  # ⬅️⬅️⬅️
        self.btn_theme.background_down = self.btn_color_presed  # ⬅️⬅️⬅️

# введення пульсу у спокійному стані
class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if theme == 0:
            Window.clearcolor = "#493843"  # ⬅️⬅️⬅️
            self.btn_color = "#8A7C7F"
            self.btn_color_presed = "#AB9E9D"
            self.next_screen = False
            self.lbl_sec = Seconds(15)
            self.lbl_sec.bind(done=self.sec_finished)

            self.instr = Label(text=txt_test1, color="#CBBFBB")

            self.line = BoxLayout(size_hint=(0.8, None), height="30sp")
            self.lbl_result = Label(text="Введіть результат:", halign="right", color="#CBBFBB")
            self.in_result = TextInput(multiline=False)
            self.in_result.set_disabled(True)

            self.line.add_widget(self.lbl_result)
            self.line.add_widget(self.in_result)
            self.btn = Button(
                text="Запустити таймер", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
            )
        else:
            Window.clearcolor = "#CBBFBB"
            self.btn_color = "#CBBFBB"
            self.btn_color_presed = "#8A7C7F"
            self.next_screen = False
            self.lbl_sec = Seconds(15)
            self.lbl_sec.bind(done=self.sec_finished)

            self.instr = Label(text=txt_test1, color="#493843")

            self.line = BoxLayout(size_hint=(0.8, None), height="30sp")
            self.lbl_result = Label(text="Введіть результат:", halign="right", color="#493843")
            self.in_result = TextInput(multiline=False)
            self.in_result.set_disabled(True)

            self.line.add_widget(self.lbl_result)
            self.line.add_widget(self.in_result)
            self.btn = Button(
                text="Запустити таймер", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
            )
        self.btn.background_color = self.btn_color  # ⬅️⬅️⬅️
        self.btn.background_down = self.btn_color_presed  # ⬅️⬅️⬅️
        self.btn.on_press = self.next
        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.outer.add_widget(self.instr)
        self.outer.add_widget(self.lbl_sec)
        self.outer.add_widget(self.line)
        self.outer.add_widget(self.btn)
        self.add_widget(self.outer)

    # якщо дорахувалися секунди, то треба розблокувати все
    def sec_finished(self, *args):
        self.next_screen = True
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = "Продовжити"

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p1
            p1 = check_int(self.in_result.text)
            if p1 == False or p1 <= 0:
                p1 = 0
                self.in_result.text = str(p1)
            else:
                self.manager.current = "sits"


# присідаємо
class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if theme == 0:
            Window.clearcolor = "#493843"  # ⬅️⬅️⬅️
            self.btn_color = "#8A7C7F"
            self.btn_color_presed = "#AB9E9D"
            self.next_screen = False  # ⬅️⬅️⬅️
            self.instr = Label(text=txt_sits, color="#CBBFBB")

            self.lbl_sits = Sits(30)  # ⬅️⬅️⬅️
            self.run = Runner(total=30, steptime=1.5, size_hint=(0.4, 1))  # ⬅️⬅️⬅️
            self.run.bind(finished=self.run_finished)  # ⬅️⬅️⬅️

            self.line = BoxLayout()  # ⬅️⬅️⬅️
            self.vlay = BoxLayout(orientation='vertical', size_hint=(0.3, 1))  # ⬅️⬅️⬅️
            self.vlay.add_widget(self.lbl_sits)  # ⬅️⬅️⬅️
            self.line.add_widget(self.instr)  # ⬅️⬅️⬅️
            self.line.add_widget(self.vlay)  # ⬅️⬅️⬅️
            self.line.add_widget(self.run)  # ⬅️⬅️⬅️

            self.btn = Button(
                text="Продовжити", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
            )
        else:
            Window.clearcolor = "#CBBFBB"  # ⬅️⬅️⬅️
            self.btn_color = "#CBBFBB"
            self.btn_color_presed = "#8A7C7F"
            self.next_screen = False  # ⬅️⬅️⬅️
            self.instr = Label(text=txt_sits, color="#493843")

            self.lbl_sits = Sits(30)  # ⬅️⬅️⬅️
            self.run = Runner(total=30, steptime=1.5, size_hint=(0.4, 1))  # ⬅️⬅️⬅️
            self.run.bind(finished=self.run_finished)  # ⬅️⬅️⬅️

            self.line = BoxLayout()  # ⬅️⬅️⬅️
            self.vlay = BoxLayout(orientation='vertical', size_hint=(0.3, 1))  # ⬅️⬅️⬅️
            self.vlay.add_widget(self.lbl_sits)  # ⬅️⬅️⬅️
            self.line.add_widget(self.instr)  # ⬅️⬅️⬅️
            self.line.add_widget(self.vlay)  # ⬅️⬅️⬅️
            self.line.add_widget(self.run)  # ⬅️⬅️⬅️

            self.btn = Button(
                text="Продовжити", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
            )
        self.btn.background_color = self.btn_color  # ⬅️⬅️⬅️
        self.btn.background_down = self.btn_color_presed
        self.btn.on_press = self.next
        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        # self.outer.add_widget(self.instr)  # ❌❌❌
        self.outer.add_widget(self.line)  # ⬅️⬅️⬅️
        self.outer.add_widget(self.btn)
        self.add_widget(self.outer)

    def run_finished(self, instance, value):  # ⬅️⬅️⬅️
        self.btn.set_disabled(False)
        self.btn.text = "Продовжити"
        self.next_screen = True

    def next(self):  # 🔁🔁🔁
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.run.start()
            self.run.bind(value=self.lbl_sits.next)
        else:
            self.manager.current = "pulse2"


# двічі вводимо пульс
class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if theme == 0:
            Window.clearcolor = "#493843"  # ⬅️⬅️⬅️
            self.btn_color = "#8A7C7F"
            self.btn_color_presed = "#AB9E9D"
            self.next_screen = False
            self.stage = 0

            self.instr = Label(text=txt_test3, color="#CBBFBB")

            self.lbl_sec = Seconds(15)
            self.lbl_sec.bind(done=self.sec_finished)
            self.lbl1 = Label(text="Рахуйте пульс")

            self.line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
            self.lbl_result1 = Label(text="Результат:", halign="right", color="#CBBFBB")
            self.in_result1 = TextInput(multiline=False)
            self.in_result1.set_disabled(True)

            self.line1.add_widget(self.lbl_result1)
            self.line1.add_widget(self.in_result1)
            self.line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
            self.lbl_result2 = Label(text="Результат після відпочинку:", halign="right", color="#CBBFBB")
            self.in_result2 = TextInput(multiline=False)
            self.in_result2.set_disabled(True)

            self.line2.add_widget(self.lbl_result2)
            self.line2.add_widget(self.in_result2)
            self.btn = Button(
                text="Завершити", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
            )
        else:
            Window.clearcolor = "#CBBFBB"  # ⬅️⬅️⬅️
            self.btn_color = "#CBBFBB"
            self.btn_color_presed = "#8A7C7F"
            self.next_screen = False
            self.stage = 0

            self.instr = Label(text=txt_test3, color="#493843")

            self.lbl_sec = Seconds(15)
            self.lbl_sec.bind(done=self.sec_finished)
            self.lbl1 = Label(text="Рахуйте пульс")

            self.line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
            self.lbl_result1 = Label(text="Результат:", halign="right", color="#493843")
            self.in_result1 = TextInput(multiline=False)
            self.in_result1.set_disabled(True)

            self.line1.add_widget(self.lbl_result1)
            self.line1.add_widget(self.in_result1)
            self.line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
            self.lbl_result2 = Label(text="Результат після відпочинку:", halign="right", color="#493843")
            self.in_result2 = TextInput(multiline=False)
            self.in_result2.set_disabled(True)

            self.line2.add_widget(self.lbl_result2)
            self.line2.add_widget(self.in_result2)
            self.btn = Button(
                text="Завершити", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
            )
        self.btn.background_color = self.btn_color  # ⬅️⬅️⬅️
        self.btn.background_down = self.btn_color_presed  # ⬅️⬅️⬅️
        self.btn.on_press = self.next
        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.outer.add_widget(self.instr)
        self.outer.add_widget(self.lbl1)
        self.outer.add_widget(self.lbl_sec)
        self.outer.add_widget(self.line1)
        self.outer.add_widget(self.line2)
        self.outer.add_widget(self.btn)
        self.add_widget(self.outer)

    def sec_finished(self, *args):
        if self.lbl_sec.done:
            if self.stage == 0:
                # закінчили перший підрахунок, відпочиваємо
                self.lbl1.text = "Відчивайте"
                self.lbl_sec.restart(30)
                self.in_result1.set_disabled(False)
                self.stage = 1
            elif self.stage == 1:
                # закінчили відпочинок, вважаємо
                self.lbl1.text = "Рахуйте пульс"
                self.lbl_sec.restart(15)
                self.stage = 2

            elif self.stage == 2:
                self.in_result2.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn.text = "Завершити"
                self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p2, p3
            p2 = check_int(self.in_result1.text)
            p3 = check_int(self.in_result2.text)
            if p2 == False:
                p2 = 0
                self.in_result1.text = str(p2)
            elif p3 == False:
                p3 = 0
                self.in_result2.text = str(p3)
            else:
                # переходим
                self.manager.current = "result"


# результат тестування
class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.instr = Label(text="")
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)
        self.on_enter = self.before

    def before(self):
        global name
        self.instr.text = name + "\n" + test(p1, p2, p3, age)


class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name="instr"))
        sm.add_widget(PulseScr(name="pulse1"))
        sm.add_widget(CheckSits(name="sits"))
        sm.add_widget(PulseScr2(name="pulse2"))
        sm.add_widget(Result(name="result"))
        return sm


app = HeartCheck()
app.run()
