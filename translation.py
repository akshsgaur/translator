from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from transformers import pipeline

class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        
        self.text_box = TextInput(
            hint_text="Enter your text here...",
            multiline=False,
            size_hint=(1, 0.2),
            font_size=20
        )
        self.add_widget(self.text_box)

        
        self.translate_button = Button(
            text="Translate",
            size_hint=(1, 0.2),
            font_size=20
        )
        self.translate_button.bind(on_press=self.on_translate)
        self.add_widget(self.translate_button)

        
        self.result_label = Label(
            text="Translated text will appear here.",
            size_hint=(1, 0.2),
            font_size=16
        )
        self.add_widget(self.result_label)

    def on_translate(self, instance):
        # Get text from the TextInput
        input_text = self.text_box.text
        print(input_text)


        
        pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
        translated_text_model = pipe(input_text)
        translated_text = translated_text_model[0]["translation_text"]
        print(translated_text)

       
        self.result_label.text = f"Translated: {translated_text}"

        # Save the input text to a file
        with open("saved_text.txt", "w") as file:
            file.write(input_text)

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == "__main__":
    MyApp().run()






