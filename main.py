from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class MainInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Defining main layout orientation property
        self.orientation = 'vertical'
        
        #Declaring layouts inside of my main layout
        self.myHeader = Header()
        self.myMainSection = MainSection()
        self.myResultSection = ResultSection()

        #Defining size proportion of the children layouts
        self.myHeader.size_hint = (1, .2)
        self.myMainSection.size_hint = (1, .5)
        self.myResultSection.size_hint = (1, .3)

        #Binding interface buttons to their functions
        self.myMainSection.converterButton.bind(on_press = self.convertBinaryToDecimal)
        
        #Adding children layouts to main layout
        self.add_widget(self.myHeader)
        self.add_widget(self.myMainSection)
        self.add_widget(self.myResultSection)
    
    #Functions
    def convertBinaryToDecimal(self, instance):
        '''
        Sets the result label text to the equivalent decimal number of the binary number imputed.
        '''
        def recursiveFunction(number): return int(number) if len(number) == 1 else int(number[0]) * 2 ** (len(number)-1) + recursiveFunction(number[1:])
        
        try:
            #Resets the result label and the from the input field if there's nothing typed into the input field
            if self.myMainSection.numberInput.text == '' : 
                self.myResultSection.resultLabel.text = 'Your Result Will Appear Here'
                self.myMainSection.numberInput.hint_text = 'Type your binary number here'
            else:
                #Checks if the binary number is valid
                for digit in self.myMainSection.numberInput.text :
                    if digit not in ('0', '1'): 
                        self.myMainSection.numberInput.hint_text = 'Invalid input'
                        self.myMainSection.numberInput.text = ''
                        self.myResultSection.resultLabel.text = 'Your Result Will Appear Here'
                #Sets the equivalent decimal number to the text property of the result label
                self.myResultSection.resultLabel.text = str( recursiveFunction(self.myMainSection.numberInput.text) )
                #Resets the input field text property
                self.myMainSection.numberInput.text = ''
                #Resets the hint text from the input field
                self.myMainSection.numberInput.hint_text = 'Type your binary number here'
        except: pass

class Header(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Title possibilities (Used in the title label of this layout)
        self.conversionTypes = ["Binary to decimal", "Decimal to binary"]

        #Declaring layout properties
        self.titleLabel = Label(text = self.conversionTypes[0])
        self.conversionTypeChangerButton = Button(text = " --->\n<---")

        #Adding layout properties
        self.add_widget(self.titleLabel)
        self.add_widget(self.conversionTypeChangerButton)

class MainSection(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Declaring layout properties
        self.titleLabel = Label(text = "Your binary number:")
        self.numberInput = TextInput(hint_text = 'Type your binary number here', multiline = False)
        self.converterButton = Button(text = "To convert")

        #Adding layout properties
        self.add_widget(self.titleLabel)
        self.add_widget(self.numberInput)
        self.add_widget(self.converterButton)

class ResultSection(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Title possibilities (Used in the title label of this layout)
        self.numberTypes = ["Decimal number", "Binary number"]

        #Declaring layout properties
        self.titleLabel = Label(text = self.numberTypes[0])
        self.resultLabel = Label(text = "Your result will appear here")

        #Adding layout properties
        self.add_widget(self.titleLabel)
        self.add_widget(self.resultLabel)

class CalculatorApp(App):
    def build(self): return MainInterface()

if __name__ == '__main__':
    CalculatorApp().run()