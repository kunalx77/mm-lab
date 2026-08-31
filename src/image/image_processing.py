from PIL import Image, ImageFilter, ImageEnhance
import os


def resize_image(input_path, output_path, width, height):
    """Resize an image."""
    image = Image.open(input_path)
    resized = image.resize((width, height))
    resized.save(output_path)
    print(f"Image resized and saved to: {output_path}")


def grayscale_image(input_path, output_path):
    """Convert an image to grayscale."""
    image = Image.open(input_path)
    grayscale = image.convert("L")
    grayscale.save(output_path)
    print(f"Grayscale image saved to: {output_path}")


def blur_image(input_path, output_path, radius=5):
    """Apply blur effect to an image."""
    image = Image.open(input_path)
    blurred = image.filter(ImageFilter.GaussianBlur(radius))
    blurred.save(output_path)
    print(f"Blurred image saved to: {output_path}")


def adjust_brightness(input_path, output_path, factor=1.5):
    """Adjust image brightness."""
    image = Image.open(input_path)
    enhancer = ImageEnhance.Brightness(image)
    enhanced = enhancer.enhance(factor)
    enhanced.save(output_path)
    print(f"Brightness adjusted image saved to: {output_path}")


if __name__ == "__main__":
    input_file = "../../input/sample.jpg"

    if os.path.exists(input_file):
        grayscale_image(
            input_file,
            "../../output/grayscale.jpg"
        )
    else:
        print("Please put sample.jpg inside the input folder.")
