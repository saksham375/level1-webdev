from manim import *
class my(Scene):
    def construct(self):
        t =Text("Hello World", color = WHITE, font_size = 25)
        self.play(Create(t))