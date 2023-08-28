#sample login page designed by me..


#main.py

from kivy.app import App
from kivy.graphics.svg import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

Window.clearcolor = (0,1,1/2,0.3)
Window.size = (360, 600)  #mobile screen size


class MyApp(App):
    def build(self):
        layout = BoxLayout( orientation = 'vertical',spacing = 15, padding = 100)


        self.img = Image(source='aotvlogog.png', size_hint=(0.8, 1), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.label = Label(text="Hello..!!, This is chinmay Wali ", font_size="20sp", bold=True,  color=(1/10,23/19,23/19, 1))

        self.Uname = TextInput(text ='enter the username',size_hint = (None,None) ,width = 300 , height = 50, pos_hint = {'center_x' : 0.5 , 'center_y' : 0.8})
        self.passs = TextInput(text ='enter the password', size_hint = (None,None),width = 300 , height = 50, pos_hint = {'center_x' : 0.5 , 'center_y' : 0.6 })
        sub = Button(text = 'submit' , size_hint = (None,None) , width = 100 , height = 50,
                      pos_hint = {'center_x': .5 } ,on_press = self.submit)


        layout.add_widget(self.img)
        layout.add_widget(self.label)
        layout.add_widget(self.Uname)
        layout.add_widget(self.passs)
        layout.add_widget(sub)

        return layout

    def submit(self,obj):    
        print("Data Saved..")


MyApp().run()
