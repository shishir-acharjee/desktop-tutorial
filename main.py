import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        # Main layout of the app
        self.operators = ["+", "-", "*", "/"]
        self.last_was_operator = False
        self.last_button = None
        
        self.main_layout = BoxLayout(orientation="vertical")
        
        # Create the display
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        self.main_layout.add_widget(self.solution)
        
        # Create the buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.main_layout.add_widget(h_layout)
        
        equals_button = Button(
            text="=",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        self.main_layout.add_widget(equals_button)
        
        return self.main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == "C":
            # Clear the solution text
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                # Prevent consecutive operators
                return
            elif current == "" and button_text in self.operators:
                # Prevent starting the expression with an operator
                return
            else:
                # Append button text to the current expression
                new_text = current + button_text
                self.solution.text = new_text
        
        # Update the operator state
        self.last_was_operator = button_text in self.operators
        self.last_button = button_text

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                # Calculate the result and display it
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except Exception as e:
                self.solution.text = "Error"

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
