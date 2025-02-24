import io
from kivymd.toast import toast
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screenmanager import ScreenManager
import os, json
from plyer import filechooser
Window.keyboard_anim_args ={'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"
class login_app(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("welcome_page.kv"))
        screen_manager.add_widget(Builder.load_file("sign_up.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        
        return screen_manager
    def login_now(self, user_name, password):
        print(user_name, password)
        pass
    def sigin_now(user_name, user_mail, user_password,password_confirm, user_number, picture):
        if user_name or user_mail or user_password or password_confirm or user_number!="":
            print(user_name, user_mail,password_confirm, user_number)
        else:
            toast("Veuiller entrer vos informations!")
            pass
    def sign_now(self, user_name, user_mail,password_confirm, user_number, telegram="", job="", picture=""):
        all_info = {
            "user_name": user_name,
            "password": password_confirm,
            "job": job,
            "picture": picture,
            "email": user_mail,
            "user_number": user_number,
            "telegram" : telegram,
        }
        with open("user_info.json", "w") as file:
            json.dump(all_info, file, indent=4)
    def add_picture(self):
        screen_manager.get_screen("sign_in").picture.source=""
        filechooser.open_file(on_selection= self.choose_picture)
    def choose_picture(self, selected):
        if selected:
            if os.path.isfile(selected[0]):
                try:
                    screen_manager.get_screen("sign_in").picture.source=selected[0]
                    toast(f"{selected[0]} ajoutée avec succès ...")
                    screen_manager.get_screen("sign_in").icon_add.icon =""
                    screen_manager.get_screen("sign_in").ajouter_photo.text =""
                except:
                    pass
    def back(self):
        screen_manager.transition.direction = "right"
        screen_manager.current = "welcome_page"
    def login_up(self):
        screen_manager.transition.direction = "left"
        screen_manager.current = "login_page"
    def sign_in(self):
        screen_manager.transition.direction = "left"
        screen_manager.current = "sign_in"
if __name__ == "__main__":
    login_app().run()
