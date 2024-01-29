import streamlit as st
import base64
import databutton as db
from openai import OpenAI
from PIL import Image
from io import BytesIO

# Function to encode the image to base64
def encode_image(image_file):
    return base64.b64encode(image_file.getvalue()).decode("utf-8")

# Function to generate the prompt text for individual analysis
def generate_individual_prompt(chart_name, additional_details=""):
    prompt_text = (
        "You are a highly knowledgeable financial analyst equipped with a risk assessment skillset. "
        f"Your task is to examine the {chart_name} stock chart image in detail. "
        "Provide a comprehensive and accurate explanation of what the chart depicts. "
        "Highlight key elements and their significance in terms of stock price movement, trends, volume, and potential market signals. "
        "Present your analysis in a clear, well-structured markdown format, "
        "Based on the analysis, offer investment advice tailored to risk-averse, risk-loving, and risk-neutral investors. "
        "Clearly indicate whether each type of investor should consider investing in this stock, providing reasons for your recommendations. "
        "Present your analysis and advice in clear, well-structured markdown format, using relevant financial terminology. "
        "Assume the reader has a basic understanding of stock market concepts."
        "Additionally, create a detailed image caption in bold, summarizing the investment advice."
    )

    if additional_details:
        prompt_text += f"\n\nAdditional Context Provided by the User:\n{additional_details}"

    return prompt_text

# Function to generate the prompt text for comparative analysis
def generate_comparative_prompt():
    return (
        "Based on the analyses of the two stock chart images, compare and contrast the performance of the two stocks. "
        "Highlight differences and similarities in their patterns, trends, volume, and technical indicators. "
        "Which stock appears to be performing better based on historical patterns? "
        "Explain in clear, well-structured markdown format, using relevant financial terminology."
    )

# Streamlit page setup
st.set_page_config(page_title="Stock Price Analyst", layout="centered", initial_sidebar_state="collapsed")
st.title("📈 Comparative Stock Price Analyst: `GPT-4 Turbo with Vision` 👀")

# Retrieve the OpenAI API Key from secrets
api_key = db.secrets.get(name="OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# File uploaders for two stock chart images
uploaded_file1 = st.file_uploader("Upload the first stock chart image", type=["jpg", "png", "jpeg"], key="file_uploader1")
uploaded_file2 = st.file_uploader("Upload the second stock chart image", type=["jpg", "png", "jpeg"], key="file_uploader2")

# Toggle for showing additional details input
show_details = st.checkbox("Add details about the stock charts", value=False)

additional_details = ""
if show_details:
    additional_details = st.text_area(
        "Add any additional details or context about the stock charts here:",
        disabled=not show_details
    )

# Button to trigger the analysis
analyze_button = st.button("Analyze and Compare the Stock Charts", type="secondary")

# Function to display uploaded images
def display_uploaded_image(image_file, caption):
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption=caption)

# Function to perform analysis on a single stock chart with error handling
def analyze_stock_chart(image, chart_name, additional_details):
    try:
        with st.spinner(f"Analyzing the {chart_name} stock chart..."):
            base64_image = encode_image(image)
            prompt_text = generate_individual_prompt(chart_name, additional_details)

            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt_text},
                        {
                            "type": "image_url",
                            "image_url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    ],
                }
            ]

            response = client.chat.completions.create(
                model="gpt-4-vision-preview", messages=messages, 
                max_tokens=500
            )
            return response.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred during analysis: {e}")

# Function to perform comparative analysis with error handling
def compare_stock_charts(chart1_analysis, chart2_analysis):
    try:
        with st.spinner("Comparing the two stock charts..."):
            prompt_text = generate_comparative_prompt()

            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt_text},
                        {"type": "text", "text": chart1_analysis},
                        {"type": "text", "text": chart2_analysis}
                    ],
                }
            ]

            response = client.chat.completions.create(
                model="gpt-4-vision-preview", messages=messages, 
                max_tokens=500
            )
            return response.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred during comparison: {e}")

# Perform analysis and comparison if both images are uploaded and the button is pressed
if uploaded_file1 and uploaded_file2 and api_key and analyze_button:
    display_uploaded_image(uploaded_file1, "First Stock Chart")
    display_uploaded_image(uploaded_file2, "Second Stock Chart")

    chart1_analysis = analyze_stock_chart(uploaded_file1, "first", additional_details)
    chart2_analysis = analyze_stock_chart(uploaded_file2, "second", additional_details)
    
    comparative_analysis = compare_stock_charts(chart1_analysis, chart2_analysis)

    st.subheader("Analysis of the First Stock Chart")
    st.write(chart1_analysis)
    st.subheader("Analysis of the Second Stock Chart")
    st.write(chart2_analysis)
    st.subheader("Comparative Analysis")
    st.write(comparative_analysis)
else:
    if not (uploaded_file1 and uploaded_file2) and analyze_button:
        st.warning("Please upload both stock chart images.")
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
