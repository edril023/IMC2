from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window

def resize_window(*args):
    Window.size = (400, 550)

Window.clearcolor = (1, 1, 1, 1)  # Cor de fundo da janela

class IMCCalculator(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Banner
        banner_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=150)
        banner_layout.add_widget(Label(text="Calculadora", color=(0.4, 0.8, 0.4, 1), font_size=40, bold=True))
        banner_layout.add_widget(Label(text="DE IMC", color=(0.4, 0.8, 0.4, 1), font_size=20, bold=True))
        layout.add_widget(banner_layout)

        # Result Display
        result_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=400, spacing=10)
        self.result_image = Image(source='logo.jpeg', size_hint=(None, None), size=(150, 150), pos_hint={'center_x': 0.7, 'center_y': 1})
        result_layout.add_widget(self.result_image)
        self.imc_info_label = Label(text="SEU IMC É?", color=(0, 0, 0, 1), font_size=24, bold=True)
        self.imc_category_label = Label(text="CATEGORIA:", color=(0.4, 0.8, 0.4, 1), font_size=20, bold=True)
        self.imc_value_label = Label(text="IMC:", color=(0.4, 0.8, 0.4, 1), font_size=20, bold=True)
        self.detalhes_label = Label(text="", color=(0, 0, 0, 1), font_size=20)
        result_layout.add_widget(self.imc_info_label)
        result_layout.add_widget(self.imc_category_label)
        result_layout.add_widget(self.imc_value_label)
        result_layout.add_widget(self.detalhes_label)
        
        
        layout.add_widget(result_layout)

        # Inputs
        input_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=150, spacing=10)
        self.altura_input = TextInput(hint_text="ALTURA (m)", font_size=18, multiline=False, background_color=(0.8, 1, 0.8, 1))
        input_layout.add_widget(self.altura_input)
        self.peso_input = TextInput(hint_text="PESO (kg)", font_size=18, multiline=False, background_color=(0.8, 1, 0.8, 1))
        input_layout.add_widget(self.peso_input)
        layout.add_widget(input_layout)

        # Gender Dropdown
        gender_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        self.gender_dropdown = DropDown()
        self.gender_button = Button(text="GÊNERO", size_hint_y=None, height=44, background_color=(0.8, 1, 0.8, 1))
        self.gender_button.bind(on_release=self.gender_dropdown.open)
        genders = ["Masculino", "Feminino", "Prefiro Não Informar"]
        for gender in genders:
            btn = Button(text=gender, size_hint_y=None, height=44, background_color=(0.8, 1, 0.8, 1))
            btn.bind(on_release=lambda btn: self.on_select(btn.text))
            self.gender_dropdown.add_widget(btn)
        gender_layout.add_widget(self.gender_button)
        layout.add_widget(gender_layout)

        # Warning Label
        self.warning_label = Label(text="", color=(1, 0, 0, 1), font_size=14)
        layout.add_widget(self.warning_label)

        # Calculate Button
        calculate_button = Button(text="CALCULAR", size_hint_y=None, height=50, background_color=(0.4, 0.5, 0.6, 1))
        calculate_button.bind(on_press=self.calcular_imc)
        layout.add_widget(calculate_button)

        return layout

    def on_select(self, text):
        self.gender_button.text = text
        self.gender_dropdown.dismiss()

    def calcular_imc(self, instance):
        altura_text = self.altura_input.text
        peso_text = self.peso_input.text

        if not altura_text or not peso_text:
            self.warning_label.text = "Ops, preencha todos os campos"
            return

        try:
            altura = float(altura_text)
            peso = float(peso_text)
        except ValueError:
            self.warning_label.text = "Por favor, insira valores válidos"
            return

        imc = peso / (altura * altura)
        imc = round(imc, 2)

        genero = self.gender_button.text
        category = ""

        if genero == "Feminino":
            if imc < 18.5:
                self.result_image.source = "10.png"
                category = 'Abaixo do peso'
            elif 18.5 <= imc < 24.9:
                self.result_image.source = "8.png"
                category = 'Peso Saudável'
            elif 25 <= imc < 29.9:
                self.result_image.source = "6.png"
                category = 'Sobrepeso ou Pré-Obeso'
            elif 30 <= imc < 34.9:
                self.result_image.source = "4.png"
                category = 'Obeso'
            else:
                self.result_image.source = "2.png"
                category = 'Severamente obeso'
        else:
            if imc < 18.5:
                self.result_image.source = "9.png"
                category = 'Abaixo do peso'
            elif 18.5 <= imc < 24.9:
                self.result_image.source = "7.png"
                category = 'Peso Saudável'
            elif 25 <= imc < 29.9:
                self.result_image.source = "5.png"
                category = 'Sobrepeso ou Pré-Obeso'
            elif 30 <= imc < 34.9:
                self.result_image.source = "3.png"
                category = 'Obeso'
            else:
                self.result_image.source = "1.png"
                category = 'Severamente obeso'

        self.imc_category_label.text = f"CATEGORIA: {category}"
        self.imc_value_label.text = f"IMC: {imc}"
        self.detalhes_label.text = category
        self.warning_label.text = ""


if __name__ == '__main__':
    Window.size = (400, 550)  # Define o tamanho inicial da janela
    Window.bind(on_resize=resize_window)
    IMCCalculator().run()
