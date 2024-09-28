import streamlit as st
import easyocr
from PIL import Image, ImageEnhance, ImageFilter
import re

# Initialize the EasyOCR reader for Hindi and English
reader = easyocr.Reader(['en', 'hi'])  # Specify languages as needed

# Title and instructions
st.title("OCR and Keyword Search with Highlighting")
st.write("Upload an image containing text in Hindi and English, and search for keywords.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image to improve OCR accuracy
    image = image.convert('L')  # Convert to grayscale
    image = image.filter(ImageFilter.SHARPEN)  # Sharpen the image
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Increase contrast

    # Perform OCR using EasyOCR
    extracted_text = reader.readtext(image, detail=0, paragraph=True)
    extracted_text = ' '.join(extracted_text)  # Join list into a single string
    st.write("Extracted Text:")

    # Input for keyword
    keyword = st.text_input("Enter a keyword to search for:")

    if keyword:
        # Use inline CSS to colorize the keyword
        def highlight_keyword(text, keyword):
            pattern = re.compile(f"({re.escape(keyword)})", re.IGNORECASE)
            return pattern.sub(r'<span style="color:red;"><b>\1</b></span>', text)

        highlighted_text = highlight_keyword(extracted_text, keyword)

        # Use markdown to display the highlighted text
        st.markdown(f"<p>{highlighted_text}</p>", unsafe_allow_html=True)

        # Keyword search result
        if re.search(re.escape(keyword), extracted_text, re.IGNORECASE):
            st.success(f"Keyword '{keyword}' found and highlighted!")
        else:
            st.error(f"Keyword '{keyword}' not found.")
    else:
        # Display the plain extracted text if no keyword is entered
        st.text(extracted_text)
