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
        layout = FloatLayout()

        # Logo
        logo = Image(source='logo.jpeg',
                     size_hint=(None, None),
                     size=(150, 150),
                     pos_hint={'center_x': 0.9, 'top': 1})
        layout.add_widget(logo)

        titulo = Image(source='titulo.jpeg',
                       size_hint=(None, None),
                       size=(300, 300),
                       pos_hint={'center_x': 0.5, 'top': 1.1})
        layout.add_widget(titulo)
        
        imc2 = Image(source='imc.jpeg',
                     size_hint=(None, None),
                     size=(500, 500),
                     pos_hint={'center_x': 0.5, 'top': 1.10})
        layout.add_widget(imc2)
        
        self.imc_category_label = Label(text="CATEGORIA:",
                                        color=(0.4, 0.8, 0.4, 1),
                                        font_size=20,
                                        bold=True,
                                        size_hint=(None, None),
                                        size=(400, 50),
                                        pos_hint={'center_x': 0.3, 'top': 0.65})
        self.imc_value_label = Label(text="IMC:",
                                     color=(0.4, 0.8, 0.4, 1),
                                     font_size=20,
                                     bold=True,
                                     size_hint=(None, None),
                                     size=(400, 50),
                                     pos_hint={'center_x': 0.7, 'top': 0.65})
        layout.add_widget(self.imc_category_label)
        layout.add_widget(self.imc_value_label)

        # Labels to display calculated IMC and category
        self.imc_category_value_label = Label(text="",
                                              color=(0, 0, 0, 1),
                                              font_size=18,
                                              size_hint=(None, None),
                                              size=(400, 50),
                                              pos_hint={'center_x': 0.3, 'top': 0.60})
        self.imc_value_display_label = Label(text="",
                                             color=(0, 0, 0, 1),
                                             font_size=18,
                                             size_hint=(None, None),
                                             size=(400, 50),
                                             pos_hint={'center_x': 0.7, 'top': 0.60})
        layout.add_widget(self.imc_category_value_label)
        layout.add_widget(self.imc_value_display_label)

        # Inputs
        self.altura_input = TextInput(hint_text="ALTURA (m)",
                                      font_size=18,
                                      multiline=False,
                                      background_color=(144/255, 238/255, 144/255, 1),  # Cor de fundo em formato RGB
                                      size_hint=(None, None),
                                      size=(380, 50),
                                      pos_hint={'center_x': 0.5, 'top': 0.50})
        self.peso_input = TextInput(hint_text="PESO (kg)",
                                    font_size=18,
                                    multiline=False,
                                    background_color=(144/255, 238/255, 144/255, 1),  # Cor de fundo em formato RGB
                                    size_hint=(None, None),
                                    size=(380, 50),
                                    pos_hint={'center_x': 0.5, 'top': 0.40})
        layout.add_widget(self.altura_input)
        layout.add_widget(self.peso_input)

        # Gender Dropdown
        self.gender_dropdown = DropDown()
        self.gender_button = Button(text="GÊNERO",
                                    size_hint=(None, None),
                                    size=(380, 50),
                                    background_color=(144/255, 238/255, 144/255, 1),  # Cor de fundo em formato RGB
                                    pos_hint={'center_x': 0.5, 'top': 0.30})
        self.gender_button.bind(on_release=self.gender_dropdown.open)
        genders = ["Masculino", "Feminino", "Prefiro Não Informar"]
        for gender in genders:
            btn = Button(text=gender, size_hint_y=None, height=44, background_color=(144/255, 238/255, 144/255, 1))  # Cor de fundo em formato RGB
            btn.bind(on_release=lambda btn: self.on_select(btn.text))
            self.gender_dropdown.add_widget(btn)
        layout.add_widget(self.gender_button)

        # Warning Label
        self.warning_label = Label(text="",
                                   color=(1, 0, 0, 1),
                                   font_size=14,
                                   size_hint=(None, None),
                                   size=(380, 30),
                                   pos_hint={'center_x': 0.5, 'top': 0.25})
        layout.add_widget(self.warning_label)

        # Calculate Button
        calculate_button = Button(text="CALCULAR",
                                  size_hint=(None, None),
                                  size=(380, 50),
                                  background_color=(0.4, 0.5, 0.6, 1),
                                  pos_hint={'center_x': 0.5, 'top': 0.15})
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
            self.warning_label.pos_hint = {'center_x': 0.5, 'top': 0.2}  # Adjusted position
            return

        try:
            altura = float(altura_text)
            peso = float(peso_text)
        except ValueError:
            self.warning_label.text = "Por favor, insira valores válidos"
            self.warning_label.pos_hint = {'center_x': 0.5, 'top': 0.2}  # Adjusted position
            return

        imc = peso / (altura * altura)
        imc = round(imc, 2)

        genero = self.gender_button.text
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

        self.imc_category_value_label.text = category
        self.imc_value_display_label.text = f"{imc}"
        self.warning_label.text = ""

if __name__ == '__main__':
    Window.size = (400, 550)  # Define o tamanho inicial da janela
    Window.bind(on_resize=resize_window)
    IMCCalculator().run()