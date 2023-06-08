from BarBendingScheduler import BarBendingScheduler
from Logger import Logger

import kivy
kivy.require('2.2.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RebarReader(App):
    def build(self, **kwargs):
        layout = BoxLayout(padding=10, orientation="vertical")
        self.path_label = Label(
            text = "DXF File Location:",
            size_hint = (1, None),
            font_size=15,
            height = 20
        )

        self.path = TextInput(
            multiline=False, 
            readonly=False, halign="right", 
            font_size=15, 
            size_hint = (1, None), 
            height = 50,
            text = "tests/dxf_samples/text_test_3.dxf"
            )
        
        self.save_path_label = Label(
            text = "CSV Save File Location:",
            size_hint = (1, None),
            font_size=15,
            height = 20
        )

        self.save_path = TextInput(
            multiline=False, 
            readonly=False, halign="right", 
            font_size=15, 
            size_hint = (1, None), 
            height = 50,
            text = "{dxf_path}-BBS-output.csv"
            )
        
        self.create_btn = Button(
            text="Create BBS", size_hint = (0.5, None), height = 40, pos_hint = ({'x': .25})
            )
        
        self.create_btn.bind(on_press = self.create) 

        self.console_label = Label(
            text = "Console:",
            size_hint = (1, None),
            font_size=15,
            height = 20
        )

        self.console = TextInput(
            multiline=True, readonly=True, halign="right", font_size=15, size_hint = (1, 0.6)
        )

        self.open_btn = Button(
            text="Open BBS", size_hint = (0.5, None), height = 40, pos_hint = ({'x': .25})
            )
        
        self.open_btn.bind(on_press = self.open) 
        

        
        layout.add_widget(self.path_label)
        layout.add_widget(self.path)
        layout.add_widget(self.save_path_label)
        layout.add_widget(self.save_path)
        layout.add_widget(self.create_btn)
        layout.add_widget(self.console_label)
        layout.add_widget(self.console)
        layout.add_widget(self.open_btn)
        return layout
    
    def create(self, button):
        log = Logger()
        bbs = BarBendingScheduler(logger = log)     

        dxf_path = self.path.text
        csv_path = self.save_path.text 

        bbs.createBarQuantitiesCsv(dxf_path, csv_path)
        self.console.text = log.getAllAsString()

    def open(self, button):
        log = Logger()
        bbs = BarBendingScheduler(logger = log)

        csv_path = self.save_path.text 
        dxf_path = self.path.text
        csv_path = csv_path.replace("{dxf_path}", dxf_path[0:-4]) # expand csv_path out

        try:
            results = bbs.getBarQuantitiesCsv(csv_path)
            self.console.text = self.prettifyDicts(results)
        except:
            self.console.text = log.getAllAsString()

    def prettifyDicts(self, ds):
        result = ''
        for d in ds:
            result = result + self.prettifyDict(d) + '\n'
        return result 

    def prettifyDict(self, d):
        result = ''
        for key, value in d.items():
            result = result +'\t' * 1 + str(key)
            if isinstance(value, dict):
                prettifyDict(value, 1+1)
            else:
                result = result + '\t' * (1+1) + str(value)
        return result



if __name__ == '__main__':
    RebarReader().run()







