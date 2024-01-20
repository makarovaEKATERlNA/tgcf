from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App): #наследование родительского класса app
    def build(self):
        layout1=GridLayout(cols=4)
        button1=Button(text="1")
        button2 = Button(text="2")
        button3 = Button(text="3")
        button4 = Button(text="*")
        button5 = Button(text="4")
        button6 = Button(text="5")
        button7 = Button(text="6")
        button8 = Button(text="-")
        button9 = Button(text="7")
        button10 = Button(text="8")
        button11= Button(text="9")
        button12 = Button(text="+")
        button13 = Button(text="//")
        button14 = Button(text="0")
        button15 = Button(text=",")
        button16 = Button(text="=")
        button17 = Button(text="%")
        button18 = Button(text="C")
        button19 = Button(text="X**2")
        button20 = Button(text="<-")

        result_layout=BoxLayout()
        result=Label(text="0")
        result_layout.add_widget(result)


        layout1.add_widget(button17)
        layout1.add_widget(button19)
        layout1.add_widget(button18)
        layout1.add_widget(button20)
        layout1.add_widget(button1)
        layout1.add_widget(button2)
        layout1.add_widget(button3)
        layout1.add_widget(button4)
        layout1.add_widget(button5)
        layout1.add_widget(button6)
        layout1.add_widget(button7)
        layout1.add_widget(button8)
        layout1.add_widget(button9)
        layout1.add_widget(button10)
        layout1.add_widget(button11)
        layout1.add_widget(button12)
        layout1.add_widget(button13)
        layout1.add_widget(button14)
        layout1.add_widget(button15)
        layout1.add_widget(button16)
        #layout1.add_widget(label2)

        main_layout=BoxLayout(orientation="vertical")
        main_layout.add_widget(result_layout)
        main_layout.add_widget(layout1)

        return main_layout
app=MyApp()
app.run()