from manim import *
import textdistance

class Letter:
    def __init__(self, char, index):
        self.char = char
        self.index = index
    
    def __str__(self):
        return self.char

class SlidingWindow:
    def __init__(self, text, size):
        self.letters = [Letter(char, i) for i, char in enumerate(text)]
        self.size = size
        self.current_pos = 0
    
    def get_current_text(self):
        return ''.join(str(letter) for letter in self.letters[self.current_pos:self.current_pos + self.size])
    
    def get_similarity(self, target):
        current = self.get_current_text()
        return textdistance.levenshtein.normalized_similarity(current, target)
    
    def move_next(self):
        if self.current_pos < len(self.letters) - self.size:
            self.current_pos += 1
            return True
        return False

class SlidingWindowScene(Scene):
    def __init__(self, reference_text="", target_text="", window_size=1, **kwargs):
        super().__init__(**kwargs)
        self.reference_text = reference_text
        self.target_text = target_text
        self.window_size = min(window_size, len(reference_text))  # Prevent window size larger than text
        self.sliding_window = SlidingWindow(reference_text, self.window_size)

    def construct(self):
        # Calculate cell size based on text length
        CELL_SIZE = min(0.4, 4 / len(self.reference_text))  # Adjust cell size based on text length
        grid_width = len(self.reference_text)
        
        # Create groups for organizing objects
        grid = VGroup()
        chars = VGroup()
        indices = VGroup()
        cells = []  # Store cells for window alignment
        
        # First create all text objects to find maximum size
        char_texts = [Text(char, font_size=24) for char in self.reference_text]
        index_texts = [Text(str(i), font_size=20) for i in range(grid_width)]
        
        # Find maximum height for characters and indices
        max_char_height = max(text.height for text in char_texts)
        max_index_height = max(text.height for text in index_texts)
        
        # Calculate scale factors
        char_scale = CELL_SIZE * 0.6 / max_char_height
        index_scale = CELL_SIZE * 0.4 / max_index_height
        
        # Create cells and add characters and indices
        for i in range(grid_width):
            # Create cell
            cell = Rectangle(
                width=CELL_SIZE,
                height=CELL_SIZE,
                stroke_width=DEFAULT_STROKE_WIDTH/4,
                stroke_color=GRAY
            )
            cell.shift(i * CELL_SIZE * RIGHT)
            cells.append(cell)  # Store cell for later use
            
            # Add character with uniform scale
            char = char_texts[i]
            char.scale(char_scale)
            # Center the character in the cell
            char.move_to(cell.get_center())
            chars.add(char)
            
            # Add index with uniform scale
            index = index_texts[i]
            index.scale(index_scale)
            index_cell = cell.copy()
            index_cell.shift(CELL_SIZE * UP)
            # Center the index in the cell
            index.move_to(index_cell.get_center())
            indices.add(index)
            
            grid.add(cell, index_cell)
        
        # Group everything and center it
        full_grid = VGroup(grid, chars, indices)
        full_grid.move_to(ORIGIN)
        
        # Create target text and scale it
        target_text = Text(self.target_text, font_size=24, color=YELLOW)
        target_text.scale_to_fit_width(min(4, len(self.target_text) * CELL_SIZE))  # Scale target text
        target_text.next_to(full_grid, UP, buff=0.5)
        
        # Create sliding window
        window = Rectangle(
            width=CELL_SIZE * len(self.target_text),
            height=CELL_SIZE,
            stroke_color=BLUE,
            stroke_width=DEFAULT_STROKE_WIDTH/4,
            fill_color=BLUE,
            fill_opacity=0.2
        )
        # Position window at first cell
        window.move_to(cells[0])
        
        # Add elements to scene
        self.add(full_grid, target_text, window)
        
        # Animate window sliding
        while self.sliding_window.move_next():
            # Get similarity score
            similarity = self.sliding_window.get_similarity(self.target_text)
            
            # Calculate color based on similarity (green for high similarity, red for low)
            color = interpolate_color(RED, GREEN, similarity)
            
            # Create animation for window movement and color change
            self.play(
                window.animate.move_to(cells[self.sliding_window.current_pos]).set_color(color).set_fill(color, opacity=0.2),
                run_time=0.4
            )

        self.wait(3)
