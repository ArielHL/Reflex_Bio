import reflex as rx

class ImageFocusState(rx.State):
  
    base_image_src: str = '/images/almost_me_2.png'
    focused_image_src: str = '/images/ahl_avatar.jpeg'
    active_src: str = base_image_src
    
    base_message: str = "Who is that? 🤔 Click 👇 and Find out"
    focused_message: str = "Yeah, That's me! 🤗 Thanks ChatGPT!"
    active_message: str = base_message


    def toggle_focus(self):
        # Toggle focus state
        if self.active_src == self.base_image_src:
            self.active_src = self.focused_image_src
            self.active_message = self.focused_message
            
        else:
            self.active_src = self.base_image_src
            self.active_message = self.base_message
            
        