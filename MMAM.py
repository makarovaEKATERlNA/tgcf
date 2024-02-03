from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
    pass
class MyApp(App):
    def build(self):
        return MyGridLayout()
app=MyApp()
app.run()