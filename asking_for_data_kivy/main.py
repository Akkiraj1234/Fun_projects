from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import random

class LoveMeApp(App):
    def build(self):
        # Set window size with a 9:16 aspect ratio
        window_width = 360  # Adjust according to your preference
        window_height = 640  # Adjust according to your preference
        Window.size = (window_width, window_height)

        # Main layout
        layout = FloatLayout()

        # Pink wallpaper
        wallpaper = Image(source='Sourse\\wallpaper.jpg', size_hint=(None, None), allow_stretch=True)
        wallpaper.size = (800,1400)
        wallpaper.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        
        # Love me question
        question = Image(source='Sourse\\giphy (8).gif', size_hint=(None, None), size=(200, 200), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Animation for yes button
        question_label = Label(text="Do you love me ^^ ?", size_hint=(None, None), size=(350, 100), pos_hint={'center_x': 0.5, 'center_y': 0.65})
        question_label.font_name = 'Sourse\\The Heart Maze Demo.ttf'
        question_label.color = (0, 0, 0, 1)  # Black color with full opacity
        question_label.bold = True
        question_label.font_size=30
        
        # Set white border and shadow
        question_label.outline_color = (1, 1, 1, 1)  # White border color
        question_label.outline_width = 1  # Width of the white border
        question_label.shadow_color = (0, 0, 0, 1)  # Black shadow color
        question_label.shadow_offset = (1, -1)  # Offset of the shadow

        # Animation for no button
        current_question_index = 0
        def animate_no(widget, question, no_button):
            list1 = ['giphy (1).gif','giphy (2).gif','giphy (3).gif','giphy (4).gif','giphy (5).gif','giphy (9).gif','giphy (7).gif','giphy (6).gif']
            nonlocal current_question_index  # Ensure we're modifying the outer variable
            if current_question_index == len(list1) - 1:
                current_question_index = 0  # Reset index if it reaches the end
            else:
                current_question_index += 1  # Increment index
            
            # Change the question image
            question.source = 'Sourse\\'+list1[current_question_index]
            
            # Randomly generate new position for the button within layout bounds
            new_x = random.uniform(0.1, 0.9)  # Adjust these values according to your layout
            new_y = random.uniform(0.1, 0.9)  # Adjust these values according to your layout

            # Set the new position for the button
            no_button.pos_hint = {'x': new_x, 'y': new_y}

            # Blink the "No" button in red
            widget.background_color = (1, 0, 0, 1)  # Red color
            Clock.schedule_once(lambda dt: setattr(widget, 'background_color', (1, 0, 1, 1)), 0.5)  # Return to original color after 0.5 seconds

        # No button
        no_button = Button(text='No', background_color=(1, 0, 1, 1), background_normal='', background_down='')
        no_button.size_hint = (None, None)
        no_button.size = (50, 50)
        no_button.pos_hint = {'x': 0.6, 'y': 0.25}  # Adjusted position relative to window width and height
        no_button.border_radius = [20, 20, 20, 20]  # Set border radius to make edges smooth
        no_button.bind(on_press=lambda x: animate_no(no_button, question, no_button))  # Bind the function to the button's on_press event

        # Animation for yes button
        def animate_yes(widget, question_image, no_button):
            anim = Animation(size=(50, 50), duration=0.5) + Animation(size=(170, 50), duration=0.5)
            anim.repeat = False
            anim.start(widget)
            widget.text = "I love u too"
            Animation.cancel_all(no_button)
            no_button.opacity = 0
            question.source = 'Sourse\\giphy.gif'

        # Yes button
        yes_button = Button(text='Yes', background_color=(1, 0, 1, 1), background_normal='', background_down='')
        yes_button.size_hint = (None, None)
        yes_button.size = (50, 50)
        yes_button.pos_hint = {'x': 0.3, 'y': 0.25}  # Adjusted position relative to window width and height
        yes_button.border_radius = [10, 10, 10, 10]  # Set border radius to make edges smooth
        yes_button.bind(on_press=lambda x: animate_yes(yes_button, question, no_button))

        # Add widgets to the main layout
        layout.add_widget(wallpaper)
        layout.add_widget(question)
        layout.add_widget(yes_button)
        layout.add_widget(question_label)
        layout.add_widget(no_button)

        return layout

if __name__ == '__main__':
    LoveMeApp().run()

