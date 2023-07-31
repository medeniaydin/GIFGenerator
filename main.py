from PIL import Image

# Adding the pictures to the list.
image_path_list = ['dog-1.jpg', 'dog-2.jpg', 'dog-3.jpg']

# Create a list of image objects
image_list = [Image.open(file) for file in image_path_list]

# Save the first image as a GIF file
image_list[0].save(
            'animation.gif',
            save_all=True,
            append_images=image_list[1:], # append rest of the images
            duration=500,#milliseconds
            loop=0)