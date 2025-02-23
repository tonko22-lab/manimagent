from manim import *

class SlidingWindowSearch(Scene):
    def construct(self):
        # Исходный текст (модельный пример с токенами)
        tokens = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
        search_word = "fox"  # Искомое слово

        # Создаем текстовую строку из токенов
        text = " ".join(tokens)
        text_mobject = Text(text, font_size=48)
        self.play(Write(text_mobject))
        self.wait(1)

        # Определяем позиции слов
        words = text.split(" ")
        word_positions = []
        x_offset = -text_mobject.width / 2  # Начальная позиция X

        for word in words:
            word_width = Text(word, font_size=48).width  # Определяем ширину слова
            word_positions.append((word, x_offset + word_width / 2))  # Центр слова
            x_offset += word_width + 0.2  # Смещение (добавляем интервал)

        # Создаем "скользящее окно"
        window_width = Text(search_word, font_size=48).width + 0.3
        window_rect = Rectangle(width=window_width, height=1, color=YELLOW)
        window_rect.move_to(text_mobject.get_center() + LEFT * (text_mobject.width / 2 - window_width / 2))

        self.play(Create(window_rect))
        self.wait(0.5)

        # Анимация скользящего окна
        found = False
        for word, pos_x in word_positions:
            self.play(window_rect.animate.move_to(text_mobject.get_center() + RIGHT * pos_x), run_time=0.5)
            if word == search_word:
                found = True
                # Подсветка найденного слова
                highlight_word = Text(word, font_size=48, color=GREEN)
                highlight_word.move_to(text_mobject.get_center() + RIGHT * pos_x)
                self.play(Transform(Text(word, font_size=48), highlight_word), run_time=0.5)
                break  # Прекращаем поиск после нахождения

        # Убираем окно после поиска
        self.play(FadeOut(window_rect))
        self.wait(1)