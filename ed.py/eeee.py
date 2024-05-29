from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

def resize_window(*args):
    Window.size = (400, 550)

Window.clearcolor = (1, 1, 1, 1)  # Cor de fundo da janela

class IMCCalculator(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Banner
        self.warning_label = Label(text="", color=(0.9, 0.3, 0.1, 1), size_hint_y=None, height=50)
        layout.add_widget(self.warning_label)

        # Inputs
        input_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=150, spacing=10)
        input_layout.add_widget(Label(text="Altura", color=(0.2, 0.2, 0.2, 1), font_size=16, halign='center'))
        self.altura_input = TextInput(hint_text="Por favor insira sua altura", font_size=16, multiline=False)
        input_layout.add_widget(self.altura_input)
        input_layout.add_widget(Label(text="Peso", color=(0.2, 0.2, 0.2, 1), font_size=16, halign='center'))
        self.peso_input = TextInput(hint_text="Por favor insira seu peso", font_size=16, multiline=False)
        input_layout.add_widget(self.peso_input)
        layout.add_widget(input_layout)

        # Gender Dropdown
        gender_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        self.gender_dropdown = DropDown()
        genders = ["Masculino", "Feminino", "Prefiro Não Informar"]
        for gender in genders:
            btn = Button(text=gender, size_hint_y=None, height=44, background_color=(0, 1, 1))
            btn.bind(on_release=lambda btn: self.on_select(btn.text))
            self.gender_dropdown.add_widget(btn)
        gender_button = Button(text="Gênero", size_hint_y=None, height=44, background_color=(0, 1, 1))
        gender_button.bind(on_release=self.gender_dropdown.open)
        gender_layout.add_widget(gender_button)
        layout.add_widget(gender_layout)

        # Calculate Button
        calculate_button = Button(text="Calcular IMC", size_hint_y=None, height=50, background_color=(0, 1, 1))
        calculate_button.bind(on_press=self.calcular_imc)
        layout.add_widget(calculate_button)

        # Result Display
        result_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=200, spacing=10)
        
        self.imc_info_label = Label(text="Seu IMC é", color=(0.2, 0.2, 0.2, 1), font_size=20, halign='center', pos_hint={'center_x': 0.5, 'center_y': 4})
        self.imc_label = Label(text="", color=(0.2, 0.2, 0.2, 1), font_size=25, halign='center', pos_hint={'center_x': 0.5, 'center_y': 4})
        self.detalhes_label = Label(text="", color=(0.2, 0.2, 0.2, 1), font_size=20, halign='center', pos_hint={'center_x': 0.5, 'center_y': 4})
        result_layout.add_widget(self.imc_info_label)
        result_layout.add_widget(self.imc_label)
        result_layout.add_widget(self.detalhes_label)
        
        self.result_image = Image(source='logo.jpeg', size_hint=(None, None), size=(200,200), pos_hint={'center_x': 0.5, 'center_y': 1})
        result_layout.add_widget(self.result_image)
        
        layout.add_widget(result_layout)

        return layout

    def on_select(self, text):
        gender_button = self.root.children[2].children[0]
        gender_button.text = text
        self.gender_dropdown.dismiss()

    def calcular_imc(self, instance):
        altura_text = self.altura_input.text
        peso_text = self.peso_input.text

        if not altura_text or not peso_text:
            self.warning_label.text = "Ops, preencha todos os campos"
            return

        altura = float(altura_text)
        peso = float(peso_text)
        genero = self.root.children[3].children[0].text

        imc = peso / (altura * altura)
        imc = round(imc, 2)

        self.imc_label.text = f"{imc}"
        self.imc_info_label.text = "Seu IMC é"  # Adicionando a mensagem aqui
        self.warning_label.text = ""

        if genero == "Feminino":
            if imc < 18.5:
                self.result_image.source = "10.png"
                self.detalhes_label.text = 'Abaixo do peso'
            elif 18.5 <= imc < 24.9:
                self.result_image.source = "8.png"
                self.detalhes_label.text = 'Peso Saudável'
            elif 25 <= imc < 29.9:
                self.result_image.source = "6.png"
                self.detalhes_label.text = 'Sobrepeso ou Pré-Obeso'
            elif 30 <= imc < 34.9:
                self.result_image.source = "4.png"
                self.detalhes_label.text = 'Obeso'
            else:
                self.result_image.source = "2.png"
                self.detalhes_label.text = 'Severamente obeso'
        else:
            if imc < 18.5:
                self.result_image.source = "9.png"
                self.detalhes_label.text = 'Abaixo do peso'
            elif 18.5 <= imc < 24.9:
                self.result_image.source = "7.png"
                self.detalhes_label.text = 'Peso Saudável'
            elif 25 <= imc < 29.9:
                self.result_image.source = "5.png"
                self.detalhes_label.text = 'Sobrepeso ou Pré-Obeso'
            elif 30 <= imc < 34.9:
                self.result_image.source = "3.png"
                self.detalhes_label.text = 'Obeso'
            else:
                self.result_image.source = "1.png"
                self.detalhes_label.text = 'Severamente obeso'

if __name__ == '__main__':
    Window.size = (400, 550)  # Define o tamanho inicial da janela
    Window.bind(on_resize=resize_window)
    IMCCalculator().run()

