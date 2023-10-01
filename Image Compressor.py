import PIL
from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Ask the user to select an image file to compress
file_path = askopenfilename()

# Check if the user canceled the file selection
if not file_path:
    exit()

# Open the selected image
img = PIL.Image.open(file_path)
myWidth, myHeight = img.size  # Corrected the order

# Ask the user to specify the save path and filename for the compressed image
save_path = asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])

# Check if the user canceled the save dialog
if not save_path:
    exit()

# Resize and save the image
img = img.resize((myWidth, myHeight), PIL.Image.LANCZOS)
img.save(save_path)
