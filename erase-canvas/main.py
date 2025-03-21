from graphics import Canvas
import time
import sys
from typing import List, Optional

CANVAS_WIDTH: int = 1000
CANVAS_HEIGHT: int = 1000

CELL_SIZE: int = 40
ERASER_SIZE: int = 20

def erase_objects(canvas: Canvas, eraser: int) -> None:
    """
    Erase objects in contact with the eraser
    
    Args:
        canvas: The canvas object to draw on
        eraser: The ID of the eraser object
    """
    try:
        # Get mouse info to help us know which cells to delete
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        
        # Calculate where our eraser is
        left_x = mouse_x
        top_y = mouse_y
        right_x = left_x + ERASER_SIZE
        bottom_y = top_y + ERASER_SIZE
        
        # Find things that overlap with our eraser
        overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
        
        # For everything that overlaps with our eraser (that isn't our eraser), change
        # its color to white
        for overlapping_object in overlapping_objects:
            if overlapping_object != eraser:
                canvas.set_color(overlapping_object, 'white')
    except Exception as e:
        print(f"Error in erase_objects: {e}")

def create_grid(canvas: Canvas) -> None:
    """
    Create the initial grid of blue squares
    
    Args:
        canvas: The canvas object to draw on
    """
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            
            try:
                canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
            except Exception as e:
                print(f"Error creating grid cell at ({row}, {col}): {e}")

def main() -> None:
    try:
        # Initialize canvas
        canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    except Exception as e:
        print(f"Error initializing canvas: {e}")
        sys.exit(1)

    try:
        # Create the initial grid
        create_grid(canvas)
        
        print("Click anywhere to start. Press 'q' to quit.")
        canvas.wait_for_click()
        
        last_click_x, last_click_y = canvas.get_last_click()
        
        # Create our eraser
        eraser = canvas.create_rectangle(
            last_click_x, 
            last_click_y, 
            last_click_x + ERASER_SIZE, 
            last_click_y + ERASER_SIZE, 
            'pink'
        )
        
        # Move the eraser, and erase what it's touching
        while True:
            # Check for quit key
            key = canvas.get_last_key_press()
            if key == 'q':
                print("Quitting...")
                break
                
            # Get where our mouse is and move the eraser to there
            mouse_x = canvas.get_mouse_x()
            mouse_y = canvas.get_mouse_y()
            canvas.moveto(eraser, mouse_x, mouse_y)
            
            # Erase anything touching the eraser
            erase_objects(canvas, eraser)
            
            time.sleep(0.05)
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Add any cleanup code here if needed
        print("Program finished")
        sys.exit(0)

if __name__ == '__main__':
    main()