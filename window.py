from  kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.solution = TextInput(multiline=False, readonly=False, haling="right", font_size=55, input_filter="float")
        main_layout.add_widget(self.solution)

        return main_layout

if __name__ == '__main__':
    MainApp().run()