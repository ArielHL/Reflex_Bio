import reflex as rx
import asyncio
import time

class ImageSwapState(rx.State):
    # image setting
    gpt_image: str = '/images/ahl_avatar_gpt.webp'
    orig_image: str = '/images/ahl_avatar.jpeg'
    active_src: str = gpt_image
    
    # message setting
    gpt_message: str = "Who is that? 🤔 Click 👇 and Find out"
    orig_message: str = "Yeah, That's me! 🤗 Thanks ChatGPT!"
    active_message: str = gpt_message
    
    
    def swap_images(self):
            self.active_src = self.gpt_image if self.active_src == self.orig_image else self.orig_image
            self.active_message = self.gpt_message if self.active_message == self.orig_message else self.orig_message



