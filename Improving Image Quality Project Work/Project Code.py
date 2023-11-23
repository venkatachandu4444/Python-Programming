from PIL import Image, ImageEnhance, ImageFilter

def enhance_image(input_path, output_path):
    # Open the image file
    image = Image.open(input_path)

    # Adjust brightness
    brightness_factor = 1.5
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)

    # Adjust contrast
    contrast_factor = 1.5
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)

    # Adjust saturation
    saturation_factor = 1.5
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(saturation_factor)

    # Sharpen the image
    sharpness_factor = 2.0
    image = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

    # Reduce noise
    image = image.filter(ImageFilter.MedianFilter(size=3))

    # Save the enhanced image
    image.save(output_path)

# Example usage
input_image_path = "image1.jpg"
output_image_path = "enhancedimage1.jpg"

enhance_image(input_image_path, output_image_path)
