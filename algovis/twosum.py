from manim import *

class TwoSumAnimation(Scene):
    def construct(self):
        # --- Setup ---
        n = 3
        nums = [2, 7, 11, 15]
        target = 9

        # Create the numbers as circles
        num_circles = [Circle(r=0.5, color=YELLOW) for num in nums]
        num_circles[0].move_to(UP * 1.5)
        num_circles[1].move_to(UP * 0.8)
        num_circles[2].move_to(UP * 0.4)
        num_circles[3].move_to(UP * 0.2)

        target_circle = Circle(r=0.5, color=RED)
        target_circle.move_to(UP * 0.8)

        # --- Animation Steps ---

        # Step 1: Highlight the first number
        self.play(FadeIn(*num_circles[:1]))
        self.wait(1)

        # Step 2: Highlight the second number
        self.play(FadeIn(*num_circles[1:]))
        self.wait(1)

        # Step 3: Highlight the target
        self.play(FadeIn(target_circle))
        self.wait(1)

        # Step 4: Show the question
        question_text = Text("Find two numbers that add up to " + str(target),
                           font_size=30, color=GREEN)
        question_text.move_to(UP * 1.5)
        self.play(question_text.animate.fade_in)
        self.wait(2)

        # Step 5:  Highlight the numbers that sum to the target
        num1_index = 0
        num2_index = 1

        self.play(
            *[
                Circle.animate.fill(color=BLUE)
                for i in range(n)
                if i == num1_index or i == num2_index
            ]
        )
        self.wait(1)

        # Step 6:  Reveal the answer
        self.play(
            FadeOut(*num_circles[:2])
        )
        self.play(
            FadeIn(Text("2 + 7 = 9", font_size=30, color=GREEN))
        )
        self.wait(2)

        # Step 7:  Fade out everything
        self.play(*[obj.animate.fade_out() for obj in [question_text, target_circle, target.text,
num_circles[0], num_circles[1]]])
        self.wait(1)