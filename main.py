
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout


class WidgetExample(GridLayout):
    counter = 1
    my_text = StringProperty("Hello!")
    count_enabled = BooleanProperty(False)

    def on_button_click(self):
        print("Button clicked")
        if self.count_enabled:
            self.my_text = str(self.counter)
            self.counter += 1
        else:
            pass

    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch:", str(widget.active))

    def on_slider_value(self, widget):
        print("Slider:", int(widget.value))


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(0, 100):
            # size = dp(100) + i * 10
            size = dp(100)
            b = Button(text=str(i + 1),
                       size_hint=(None, None),
                       size=(size, size))
            self.add_widget(b)


class GridLayoutExample(GridLayout):
    pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
#    def __init__(self, **kwargs):
#        super().__init__(**kwargs)
#        self.orientation = "vertical"
#        b1 = Button(text="A")
#        b2 = Button(text="B")
#        b3 = Button(text="C")
#
#        self.add_widget(b1)
#        self.add_widget(b2)
#        self.add_widget(b3)


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
