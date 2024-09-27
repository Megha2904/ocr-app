import streamlit as st
import pytesseract
from PIL import Image

# Title and instructions
st.title("OCR and Keyword Search")
st.write("Upload an image containing text in Hindi and English, and search for keywords.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner('Performing OCR...'):
        try:
            # Perform OCR
            extracted_text = pytesseract.image_to_string(image, lang='eng+hin')
            st.write("Extracted Text:")
            st.write(extracted_text)
        except Exception as e:
            st.error(f"Error during OCR: {e}")
            extracted_text = ""

    # Input for keyword
    keyword = st.text_input("Enter a keyword to search for:")

    if keyword:
        # Perform keyword search
        if keyword.lower() in extracted_text.lower():
            st.success(f"Keyword '{keyword}' found!")
        else:
            st.error(f"Keyword '{keyword}' not found.")
