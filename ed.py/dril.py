from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image

def resize_window(*args):
    Window.size = (400, 550)

Window.clearcolor = (1, 1, 1, 1)  # Cor de fundo da janela

class IMCCalculator(App):
    def build(self):
        return FloatLayout()

    def on_select(self, text):
        self.root.ids.gender_button.text = text
        self.root.ids.gender_dropdown.dismiss()

    def calcular_imc(self, instance):
        altura_text = self.root.ids.altura_input.text
        peso_text = self.root.ids.peso_input.text

        if not altura_text or not peso_text:
            self.root.ids.warning_label.text = "Ops, preencha todos os campos"
            return

        try:
            altura = float(altura_text)
            peso = float(peso_text)
        except ValueError:
            self.root.ids.warning_label.text = "Por favor, insira valores válidos"
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

        self.root.ids.imc_category_label.text = f"CATEGORIA: {category}"
        self.root.ids.imc_value_label.text = f"IMC: {imc}"
        self.root.ids.detalhes_label.text = category
        self.root.ids.warning_label.text = ""

if __name__ == '__main__':
    Window.size = (400, 550)  # Define o tamanho inicial da janela
    Window.bind(on_resize=resize_window)
    IMCCalculator().run()

