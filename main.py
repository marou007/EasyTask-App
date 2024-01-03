from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import MDGridLayout

class TaskWidget(BoxLayout):
    def __init__(self, task_name, task_description, due_date, **kwargs):
        super(TaskWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = dp(150)

        with self.canvas.before:
            Color(250 / 255, 229 / 255, 118 / 255, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self._update_rect, pos=self._update_rect)

        self.checkbox = MDCheckbox()
        self.checkbox.bind(active=self.on_checkbox_active)
        self.add_widget(self.checkbox)

        task_name_label = MDLabel(text=f"[b]Task Name:[/b] {task_name}", markup=True, height=dp(40), color=[0, 0, 0, 1])
        task_description_label = MDLabel(text=f"[b]Description:[/b] {task_description}", markup=True, height=dp(40), color=[0, 0, 0, 1])
        due_date_label = MDLabel(text=f"[b]Due Date:[/b] {due_date}", markup=True, height=dp(40), color=[0, 0, 0, 1])


        self.add_widget(task_name_label)
        self.add_widget(task_description_label)
        if due_date:
            self.add_widget(due_date_label)

        delete_button = MDRectangleFlatButton(text='Delete', size_hint=(1, None), height=dp(30), padding=dp(10))
        delete_button.bind(on_release=self.delete_task)
        self.add_widget(delete_button)
        delete_button.theme_text_color = 'Custom'  # Set text color to a custom value
        delete_button.text_color = [4 / 255, 88 / 255, 232 / 255, 1]  # Set text color to #17328D
        delete_button.line_color = [4 / 255, 88 / 255, 232 / 255, 1]  # Set outline color to #17328D


    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_checkbox_active(self, checkbox, value):
        if value:
            pass

    def delete_task(self, instance):
        if self.parent:
            self.parent.remove_widget(self)

class EasyTask(MDApp):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))
        header = MDLabel(text='EasyTask', height=dp(30), font_size=40, halign='center', color=[0, 0, 0, 1])
        main_layout.add_widget(header)

        field_section = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(150))
        task_input = MDTextField(hint_text='Enter task name', height=dp(40))
        description_input = MDTextField(hint_text='Enter task description', height=dp(40))
        due_date_input = MDTextField(hint_text='Enter due date (optional)', height=dp(40))
        field_section.add_widget(task_input)
        field_section.add_widget(description_input)
        field_section.add_widget(due_date_input)
        main_layout.add_widget(field_section)

        added_task_section = ScrollView()
        self.task_container = MDGridLayout(cols=1, spacing=dp(10), padding=dp(10), size_hint=(1, None))
        self.task_container.bind(minimum_height=self.task_container.setter('height'))
        added_task_section.add_widget(self.task_container)
        main_layout.add_widget(added_task_section)

        add_task_button = MDRectangleFlatButton(text='Add Task', height=dp(40), size_hint=(1, None))
        add_task_button.theme_text_color = 'Custom'  # Set text color to a custom value
        add_task_button.text_color = [4 / 255, 88 / 255, 232 / 255, 1]  # Set text color to #0458E8
        add_task_button.line_color = [4 / 255, 88 / 255, 232 / 255, 1]  # Set outline color to #0458E8
        add_task_button.background_color = [1, 0.5, 0, 1]
        def add_task(instance):
            task_widget = TaskWidget(task_input.text, description_input.text, due_date_input.text)
            self.task_container.add_widget(task_widget)
            task_input.text = ""
            description_input.text = ""
            due_date_input.text = ""

        add_task_button.bind(on_press=add_task)
        field_section.add_widget(add_task_button)

        return main_layout

if __name__ == '__main__':
    EasyTask().run()
