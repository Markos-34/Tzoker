import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tzoker import main  # Assuming main function is in tzoker.py
from option_menu import print_papers

def print_image():
    try:
        # Call the main function from tzoker.py to generate the modified image
        main()

        # Path to the generated modified image
        output_path = '/Users/httpsmavroudi/UI_tzoker/modified_image_with_random_Xs.png'

        # Load the modified image using PIL
        modified_image = Image.open(output_path)

        # Create a new window for displaying the image
        image_window = tk.Toplevel(app)
        image_window.title("Modified Image Display")

        # Set a larger initial window size for the image window
        initial_width = 1000
        initial_height = 1000
        screen_width = image_window.winfo_screenwidth()
        screen_height = image_window.winfo_screenheight()
        x_position = (screen_width - initial_width) // 2
        y_position = (screen_height - initial_height) // 2
        image_window.geometry(f"{initial_width}x{initial_height}+{x_position}+{y_position}")

        # Display the image on a Tkinter label in the new window
        photo = ImageTk.PhotoImage(modified_image)
        label = tk.Label(image_window, image=photo)
        label.image = photo
        label.pack(pady=10)

    except Exception as e:
        # Display error message if any exception occurs
        messagebox.showerror("Error", f"Error: {e}")

def handle_print():
    selected_option = selected_option_var.get()
    print_papers(selected_option)
    print_image()  # Call print_image after printing papers

# Create the main Tkinter application window
app = tk.Tk()
app.title("Lucky Draws")

# Set a larger initial window size for the main window
initial_width = 800
initial_height = 600
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_position = (screen_width - initial_width) // 2
y_position = (screen_height - initial_height) // 2
app.geometry(f"{initial_width}x{initial_height}+{x_position}+{y_position}")

# Options for number of papers to print
paper_options = ["1 paper", "2 papers", "3 papers", "4 papers", "5 papers"]

# Variable to store selected option
selected_option_var = tk.StringVar(app)
selected_option_var.set(paper_options[0])  # Set default option

# Option menu to choose number of papers
option_menu = tk.OptionMenu(app, selected_option_var, *paper_options)
option_menu.pack(pady=20)

# Load and resize the image to be displayed in the middle
middle_image_path = '/Users/httpsmavroudi/UI_tzoker/Scan1.jpeg'  # Update with your image path
middle_image = Image.open(middle_image_path)
image_width, image_height = middle_image.size
max_width, max_height = 400, 400  # Set maximum width and height

# Resize the image if it's too large
if image_width > max_width or image_height > max_height:
    resize_ratio = min(max_width / image_width, max_height / image_height)
    new_size = (int(image_width * resize_ratio), int(image_height * resize_ratio))
    middle_image = middle_image.resize(new_size, Image.LANCZOS)

middle_photo = ImageTk.PhotoImage(middle_image)

# Create a label to display the middle image
middle_image_label = tk.Label(app, image=middle_photo)
middle_image_label.image = middle_photo
middle_image_label.pack(pady=20)

# Create a button to trigger printing the selected number of papers
print_button = tk.Button(app, text="Print Papers", command=handle_print)
print_button.pack(side=tk.BOTTOM, pady=20)

# Start the Tkinter main loop
app.mainloop()
