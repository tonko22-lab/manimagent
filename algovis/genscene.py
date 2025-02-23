# Here's the Manim code to implement a sliding window of size 6 across the given sequence of letters, highlighting the "coffee" subsequence in green:


from manim import *

class GenScene(Scene):
    def construct(self):
        text = Text("bdhsjfbcoffeeasdfd", font_size=36)
        self.add(text)

        window = Rectangle(width=2.4, height=0.7, color=BLUE)
        window.move_to(text[0:6])

        self.play(Create(window))

        for i in range(len(text) - 5):
            if i == 7:
                self.play(
                    window.animate.set_color(GREEN),
                    text[i:i+6].animate.set_color(GREEN)
                )
            else:
                self.play(
                    window.animate.move_to(text[i:i+6]),
                    run_time=0.5
                )

        self.wait()