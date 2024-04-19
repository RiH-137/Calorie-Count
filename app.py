### Health Management APP
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text




#conversion of image data to bytes
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()  # Read the file into bytes

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(page_title="Calorie Counter  🍔", layout="centered", initial_sidebar_state="expanded")


#abou the author
if st.button("About the author"):
    # Display information about the author or code description
    st.write("# About the Author")
    st.write("This Streamlit app is created by Rishi Ranjan.")
    st.write("""
    Date-->  19/04/2024
        🌟 **About Me:**
        https://www.linkedin.com/in/rishi-rih/

🚀 Hey there! I'm Rishi, a passionate 2nd year Computer Science & Engineering Undergraduate with a keen interest in the vast world of technology. Currently specializing in AI and Machine Learning, I'm on a perpetual quest for knowledge and thrive on learning new skills.

💻 My journey in the tech realm revolves around programming, problem-solving, and staying on the cutting edge of emerging technologies. With a strong foundation in Computer Science, I'm driven by the exciting intersection of innovation and research.

🔍 Amidst the digital landscape, I find myself delving into the realms of Blockchain, crafting Android Applications, and ML projects.
 JAVA and Python . 
My GitHub profile (https://github.com/RiH-137) showcases my ongoing commitment to refining my craft and contributing to the tech community.

🏎️ Outside the digital realm, I'm a fervent Formula 1 enthusiast, experiencing the thrill of high-speed pursuits. When I'm not immersed in code or cheering for my favorite F1 team, you might find me strategizing moves on the chessboard.

📧 Feel free to reach out if you're as passionate about technology as I am. You can connect with me at 101rishidsr@gmail.com.

Let's build, innovate, and explore the limitless possibilities of technology together! 🌐✨
        
    
    """)
    if st.button("close"):
        pass






st.header("Calorie Count  🍔")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me the total calories")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----


"""

## If submit button is clicked

if submit:
    if uploaded_file:
        image_data=input_image_setup(uploaded_file)
        response=get_gemini_repsonse(input_prompt,image_data,input)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the image to get the response, as the image is not uploaded.")

