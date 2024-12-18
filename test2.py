import tkinter as tk

# Define the function to be executed when the canvas "button" is clicked
def on_canvas_click(event):
    print("Canvas button clicked!")
    # Unbind the click event to disable further clicks
    canvas.tag_unbind(image_id, "<Button-1>")

# Create the main window
root = tk.Tk()
root.title("Canvas Button Example")

# Create a canvas
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Add an image to the canvas (simulating a button)
# Replace 'your_image.png' with your actual image file path if using an image
image = tk.PhotoImage("MyKao.png", width=100, height=50)  # Dummy image
image_id = canvas.create_image(100, 100, image=image)

# Bind a click event to the image
canvas.tag_bind(image_id, "<Button-1>", on_canvas_click)

# Run the Tkinter event loop
root.mainloop()