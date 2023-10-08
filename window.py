from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.solution = TextInput(multiline=False, readonly=False, halign="right", font_size=55, input_filter="float")
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]

        for row in buttons:
            horizontal_layout = BoxLayout()
            for lable in row:
                button = Button(text=lable, pos_hint={"center_x": 0.5, "center_y": 0.5})
                horizontal_layout.add_widget(button)
            main_layout.add_widget(horizontal_layout)

        return main_layout

if __name__ == '__main__':
    MainApp().run()