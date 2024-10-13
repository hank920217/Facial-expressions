from PIL import Image

def enlarge_image(input_image_path, output_image_path, scale):
    with Image.open(input_image_path) as img:
        width, height = img.size
        new_size = (int(width*scale), int(height*scale))
        new_img = img.resize(new_size, Image.LANCZOS)
        new_img.save(output_image_path)

for i in range(1, 201):
    input_path = f"C:\\Users\\stone\\MediaPipe\\data\\sad\\test({i}).jpg"
    output_path = f"C:\\Users\\stone\\MediaPipe\\data\\sad\\test({i}).jpg"
    enlarge_image(input_path, output_path, 5.0)

