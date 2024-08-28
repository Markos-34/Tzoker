# Tzoker.py file:

##Lottery Ticket Image Generator
*This Python project automates the process of generating and printing a lottery ticket image with randomly placed "X" marks on predefined coordinates, simulating a filled-out lottery ticket.

##Features
*Image Creation: Generates a blank white image representing a lottery ticket.
Coordinate Parsing: Parses predefined coordinates from an HTML-like format to place "X" marks.
Random "X" Placement: Randomly selects and places a specified number of "X" marks in each section of the ticket.
Customizable Parameters: Adjust the size of the "X" marks and the number of "X" marks per section.
Automatic Printing: Sends the generated image directly to a printer using the CUPS printing system.
##How It Works
*Coordinate Parsing: The script parses coordinate strings, representing different areas of the ticket, and converts them into usable coordinates.
Drawing "X" Marks: Based on the parsed coordinates, "X" marks are drawn on the image at the center of each area.
Image Generation: A blank white image is created, and "X" marks are added based on random selections from the coordinate sets.
Printing: The final image is sent to a configured printer via CUPS, formatted according to specified print options.
##Setup
*Prerequisites:

Python 3.x
Pillow library for image creation and manipulation.
pycups for interacting with CUPS to print images.
Installation:

bash
Copy code
pip install pillow pycups
Running the Script:

bash
Copy code
python lottery_ticket_generator.py
Configuration:

Modify the coordinate strings and number of "X" marks in the script as needed.
Ensure your printer is configured and connected to CUPS.
Example Output
The generated image will contain randomly placed "X" marks across predefined boxes, similar to a lottery ticket. It can be directly printed out via the configured printer.

##Notes
*The script assumes a single printer is configured via CUPS.
Ensure the image size and print options are set according to your specific printer and paper size.
Contribution
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

##License
*This project is licensed under the MIT License - see the LICENSE file for details.

#Ui.py file:

*The code provided sets up a graphical user interface (GUI) using Tkinter that allows a user to select a number of papers to "print" (based on options), then displays a modified image generated by the main function from the tzoker.py module. Additionally, it also displays an image in the middle of the window.

##Here’s a brief explanation of what the code does and how it works:

*Code Explanation
Importing Modules:

tkinter is imported as tk for creating the GUI.
messagebox is used to display error messages.
PIL.Image and PIL.ImageTk are used for image handling.
main function is imported from tzoker.py to generate the modified image.
print_papers is imported from option_menu.py to handle printing papers.
print_image() Function:

*Calls main() from tzoker.py to generate a modified image.
Loads the image using PIL.Image.
Creates a new Tkinter window to display the image.
Resizes and centers the new window on the screen.
handle_print() Function:

*Gets the selected number of papers from the option menu.
Calls print_papers() from option_menu.py.
Then calls print_image() to display the generated image.
Tkinter Application Setup:

*The main Tkinter window is set up with a larger initial size.
A list of options for the number of papers is provided.
An option menu is created allowing the user to choose how many papers to print.
An image (from a specified path) is loaded, resized, and displayed in the middle of the main window.
A button at the bottom of the window triggers the handle_print() function.
Main Event Loop:

*The app.mainloop() starts the Tkinter main loop, waiting for user interaction.
##Notes
Paths: Ensure that the paths to the images (e.g., /Users/httpsmavroudi/UI_tzoker/Scan1.jpeg and /Users/httpsmavroudi/UI_tzoker/modified_image_with_random_Xs.png) are correct and the files exist at those locations.
Image Resizing: The middle image is resized to fit within a 400x400 area if it’s larger.
Error Handling: If any exceptions occur during the image display, an error message will be shown.
Code Implementation
Ensure that your directory structure is correct and the images and Python scripts are in the correct locations. To run this code, simply ensure you have the Pillow library installed for image handling:

bash
Copy code
pip install pillow
Then, run your script as usual. This GUI application will allow you to interactively choose the number of papers, generate, and display a modified image.
