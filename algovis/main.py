from manim import *
from sliding_window import SlidingWindowScene

class DefaultTemplate(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.flip(RIGHT)  # flip horizontally
        square.rotate(-3 * TAU / 8)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class SlidingWindowExample(SlidingWindowScene):
    def __init__(self):
        super().__init__(
            reference_text="утренний кофе бодрит",
            target_text="кофе",
            window_size=4
        )
