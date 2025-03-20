from dataclasses import dataclass
from PIL import Image, ImageDraw, ImageFont


@dataclass
class Rectangle:
    x: int
    y: int
    width: int
    height: int
    color: tuple
    text: str
    text_color: tuple


def add_rectangle_with_text(image, rect: Rectangle):
    """Adds a rectangle with text to the image."""
    draw = ImageDraw.Draw(image)

    # Draw rectangle
    draw.rectangle(
        [rect.x, rect.y, rect.x + rect.width, rect.y + rect.height],
        fill=rect.color
    )

    # Add text inside the rectangle
    font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), rect.text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = rect.x + (rect.width - text_width) // 2
    text_y = rect.y + (rect.height - text_height) // 2
    draw.text((text_x, text_y), rect.text, fill=rect.text_color, font=font)


def main():
    # Load the base image
    image = Image.open("salvador-result.jpeg")

    # Define rectangles
    rectangles = [
        Rectangle(50, 50, 150, 100, (0, 0, 0), "We are learning Python", (255, 255, 255)),
        Rectangle(220, 50, 150, 100, (255, 255, 0), "We are learning Python", (0, 0, 0)),
        Rectangle(50, 200, 150, 100, (0, 0, 255), "We are learning Python", (255, 255, 255)),
    ]

    # Add rectangles to image
    for rect in rectangles:
        add_rectangle_with_text(image, rect)

    # Save the processed image
    image.save("processed_image.jpeg")
    image.show()


if __name__ == "__main__":
    main()
