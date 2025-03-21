"""Simple object oriented graphics library

The library is designed to make it very easy for novice programmers to
experiment with computer graphics in an object oriented fashion. It is
written by John Zelle for use with the book "Python Programming: An
Introduction to Computer Science" (Franklin, Beedle & Associates).
"""

import time, os, sys
import tkinter as tk


class GraphicsError(Exception):
    """Generic error class for graphics module exceptions."""
    pass

class Canvas:
    """A Canvas represents a drawing surface."""

    def __init__(self, width, height):
        """Create a Canvas with the given width and height."""
        self.width = width
        self.height = height
        
        # Create the root window
        self.root = tk.Tk()
        self.root.title("Graphics Window")
        
        # Create the canvas widget
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack()
        
        # Set up mouse and key events
        self.mouse_x = 0
        self.mouse_y = 0
        self.last_click_x = None
        self.last_click_y = None
        self.last_key = ""
        
        self.canvas.bind("<Motion>", self._update_mouse)
        self.canvas.bind("<Button-1>", self._handle_click)
        self.root.bind("<Key>", self._handle_key)
        
        # Update the display
        self.root.update()

    def _update_mouse(self, event):
        """Update mouse coordinates."""
        self.mouse_x = event.x
        self.mouse_y = event.y
        
    def _handle_click(self, event):
        """Handle mouse click events."""
        self.last_click_x = event.x
        self.last_click_y = event.y
        
    def _handle_key(self, event):
        """Handle keyboard events."""
        self.last_key = event.char
        
    def get_mouse_x(self):
        """Get current mouse x coordinate."""
        self.root.update()
        return self.mouse_x
        
    def get_mouse_y(self):
        """Get current mouse y coordinate."""
        self.root.update()
        return self.mouse_y
        
    def get_last_click(self):
        """Get coordinates of last mouse click."""
        return (self.last_click_x, self.last_click_y)
        
    def get_last_key_press(self):
        """Get the last key pressed."""
        self.root.update()
        key = self.last_key
        self.last_key = ""
        return key

    def create_rectangle(self, x1, y1, x2, y2, color):
        """Create a rectangle with the given coordinates and color."""
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
        
    def set_color(self, item, color):
        """Set the color of the given item."""
        self.canvas.itemconfig(item, fill=color, outline=color)
        
    def find_overlapping(self, x1, y1, x2, y2):
        """Find all items that overlap with the given rectangle."""
        return self.canvas.find_overlapping(x1, y1, x2, y2)
        
    def moveto(self, item, x, y):
        """Move an item to a new position."""
        try:
            # Get current position
            coords = self.canvas.coords(item)
            if coords:
                # Calculate width and height
                width = coords[2] - coords[0]
                height = coords[3] - coords[1]
                # Move to new position
                self.canvas.coords(item, x, y, x + width, y + height)
                self.root.update()
        except Exception:
            pass
        
    def wait_for_click(self):
        """Wait for a mouse click."""
        self.last_click_x = None
        self.last_click_y = None
        while self.last_click_x is None:
            self.root.update()
            time.sleep(0.1) 