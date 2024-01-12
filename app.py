from PIL import Image
import pytesseract

#Tesseract extension
tesseract_path = r'C:\Users\biuro\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_path

def read_data_from_frame(frame_path):
    frame = Image.open(frame_path)
    text_content = pytesseract.image_to_string(frame)
    return text_content

# First of tousands frames
# To do self delete shoots
one_frame_from_many = r'C:\Users\biuro\Pictures\test.png'
result = read_data_from_frame(one_frame_from_many)

print("Readed content", result)
