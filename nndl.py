from bs4 import BeautifulSoup
import re
import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text.strip()

def replace_text_in_html(html_content, old_text, new_text):
    return re.sub(re.escape(old_text), new_text, html_content)

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def replace_html_text_from_image(file_path, image_path):
    html_content = read_html_file(file_path)
    text_from_image = extract_text_from_image(image_path)
    
    soup = BeautifulSoup(html_content, 'html.parser')
    text_elements = soup.find_all(text=True)
    
    for element in text_elements:
        old_text = element.strip()
        if old_text:
            new_text = replace_text_in_html(html_content, old_text, text_from_image)
            html_content = new_text
    
    return html_content

file_path = r"C:\Users\thesu\Downloads\html1.html"
image_path = r"C:\Users\thesu\Downloads\png1.png"

new_html_content = replace_html_text_from_image(file_path, image_path)
print(new_html_content)
