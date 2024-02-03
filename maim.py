from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MyApp(App): #наследование родительского класса app
    current_operation=""
    first_number=""
    second_number=""
    def button_press(self,obj):
        if obj.text in "0123456789":
            if self.current_operation=="":
                self.first_number+=obj.text
                self.result.text+=obj.text
            else:
                self.second_number+=obj.text
                self.result.text+=obj.text
        elif obj.text in "+-/*C":
            self.current_operation=obj.text
            self.result.text=""
        elif obj.text=="=":
            a=int(self.first_number)
            b=int(self.second_number)
            if self.current_operation=="+":
                r=a+b
                self.result.text=str(r)
            if self.current_operation == "-":
                r = a - b
                self.result.text = str(r)
            if self.current_operation=="*":
                r=a*b
                self.result.text=str(r)
            if self.current_operation=="/":
                r=a//b
                self.result.text=str(r)
            if self.current_operation=="X**2":
                r=a**2
                self.result.text=str(r)
            if self.current_operation == "C":
                r=0
                self.first_number = ""
                self.second_number = ""
                self.curent_operation = ""
                self.result.text = str(r)
            self.first_number=str(r)
            self.second_number=""
            self.curent_operation=""
    def build(self):
        layout1=GridLayout(cols=4)
        button1=Button(text="1",on_press=self.button_press)
        button2 = Button(text="2",on_press=self.button_press)
        button3 = Button(text="3",on_press=self.button_press)
        button4 = Button(text="*",on_press=self.button_press)
        button5 = Button(text="4",on_press=self.button_press)
        button6 = Button(text="5",on_press=self.button_press)
        button7 = Button(text="6",on_press=self.button_press)
        button8 = Button(text="-",on_press=self.button_press)
        button9 = Button(text="7",on_press=self.button_press)
        button10 = Button(text="8",on_press=self.button_press)
        button11= Button(text="9",on_press=self.button_press)
        button12 = Button(text="+",on_press=self.button_press)
        button13 = Button(text="/",on_press=self.button_press)
        button14 = Button(text="0",on_press=self.button_press)
        button15 = Button(text=",",on_press=self.button_press)
        button16 = Button(text="=",on_press=self.button_press)
        button17 = Button(text="%",on_press=self.button_press)
        button18 = Button(text="C",on_press=self.button_press)
        button19 = Button(text="X**2",on_press=self.button_press)
        button20 = Button(text="<-",on_press=self.button_press)

        result_layout=BoxLayout()
        self.result=Label(text="")
        result_layout.add_widget(self.result)

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