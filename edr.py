from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.lang import Builder

def resize_window(*args):
    Window.size = (400, 550)

Window.clearcolor = (1, 1, 1, 1)

class IMCCalculator(App):

    def build(self):
        self.gender_dropdown = DropDown()
        genders = ["Masculino", "Feminino", "Prefiro Não Informar"]
        for gender in genders:
            btn = Button(text=gender, size_hint_y=None, height=44, background_color=(144/255, 238/255, 144/255, 1))
            btn.bind(on_release=lambda btn: self.on_select(btn.text))
            self.gender_dropdown.add_widget(btn)
        
        return Builder.load_file('imccalculator.kv')

    def on_select(self, text):
        self.root.ids.gender_button.text = text
        self.gender_dropdown.dismiss()

    def calcular_imc(self):
        altura_text = self.root.ids.altura_input.text
        peso_text = self.root.ids.peso_input.text

        if not altura_text or not peso_text:
            self.root.ids.warning_label.text = "Ops, preencha todos os campos"
            self.root.ids.warning_label.pos_hint = {'center_x': 0.5, 'top': 0.2}
            return

        try:
            altura = float(altura_text)
            peso = float(peso_text)
        except ValueError:
            self.root.ids.warning_label.text = "Por favor, insira valores válidos"
            self.root.ids.warning_label.pos_hint = {'center_x': 0.5, 'top': 0.2}
            return

        imc = peso / (altura * altura)
        imc = round(imc, 2)

        genero = self.root.ids.gender_button.text
        category = ""

        if genero == "Feminino":
            if imc < 18.5:
                category = 'Abaixo do peso'
            elif 18.5 <= imc < 24.9:
                category = 'Peso Saudável'
            elif 25 <= imc < 29.9:
                category = 'Sobrepeso ou Pré-Obeso'
            elif 30 <= imc < 34.9:
                category = 'Obeso'
            else:
                category = 'Severamente obeso'
        else:
            if imc < 18.5:
                category = 'Abaixo do peso'
            elif 18.5 <= imc < 24.9:
                category = 'Peso Saudável'
            elif 25 <= imc < 29.9:
                category = 'Sobrepeso ou Pré-Obeso'
            elif 30 <= imc < 34.9:
                category = 'Obeso'
            else:
                category = 'Severamente obeso'

        self.root.ids.imc_category_value_label.text = category
        self.root.ids.imc_value_display_label.text = f"{imc}"
        self.root.ids.warning_label.text = ""

if __name__ == '__main__':
    Window.size = (400, 550)
    Window.bind(on_resize=resize_window)
    IMCCalculator().run()
