from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import WipeTransition,SwapTransition,FadeTransition,CardTransition

kv=Builder.load_file("my2.kv")

class My2App(App):
    def build(self):
        return kv

app=My2App()
app.run()