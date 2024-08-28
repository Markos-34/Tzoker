Lottery Ticket Image Generator
This Python project automates the process of generating and printing a lottery ticket image with randomly placed "X" marks on predefined coordinates, simulating a filled-out lottery ticket.

Features
Image Creation: Generates a blank white image representing a lottery ticket.
Coordinate Parsing: Parses predefined coordinates from an HTML-like format to place "X" marks.
Random "X" Placement: Randomly selects and places a specified number of "X" marks in each section of the ticket.
Customizable Parameters: Adjust the size of the "X" marks and the number of "X" marks per section.
Automatic Printing: Sends the generated image directly to a printer using the CUPS printing system.
How It Works
Coordinate Parsing: The script parses coordinate strings, representing different areas of the ticket, and converts them into usable coordinates.
Drawing "X" Marks: Based on the parsed coordinates, "X" marks are drawn on the image at the center of each area.
Image Generation: A blank white image is created, and "X" marks are added based on random selections from the coordinate sets.
Printing: The final image is sent to a configured printer via CUPS, formatted according to specified print options.
Setup
Prerequisites:

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

Notes
The script assumes a single printer is configured via CUPS.
Ensure the image size and print options are set according to your specific printer and paper size.
Contribution
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License - see the LICENSE file for details.
