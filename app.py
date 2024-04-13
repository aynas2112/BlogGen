import streamlit as st
import google.generativeai as genai
from apikey import gemini,open_ai_api
# from openai._client import OpenAI
# client=OpenAI(api_key=open_ai_api)

genai.configure(api_key=gemini)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

# Create a new model
model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

st.set_page_config(layout="wide")
# title
st.title('Blog Crafter')
# header
st.subheader('Create your blog here')  
# sidebar for user input
with st.sidebar:
    st.title("User Input") 
    st.subheader("Enter your blog content here")
    # blog title
    blog_title = st.text_input("Blog Title")
    # keywords
    keywords = st.text_input("Keywords(comma-separated)")
    # number of words
    numWords=st.slider("Number of words", min_value=250,max_value= 1000, step=250)
    # number of img
    numImg=st.number_input("Number of images", min_value=0,max_value= 5, step=1)
    # blog content
    convo =[f"Generate a comprehensive blog post relevant to given title \"{blog_title}\" and keywords \"{keywords}\".Make sure to incorporate keywords in the blog. The blog should be approximately {numWords} words in length,suitable for online audience.Ensure content is original,informative and maintains a consistent tone throughout."]
    response=model.generate_content(convo)

    # submit button
    submitted = st.button('Let Crafting Begin')
if submitted:
    # st.image("https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRE08onY3lfpMtMtMmBAr92tHSVGShHDWKTsgEcDpd-WgIL2WEk")
    # imgResponse = client.images.generate(
    # model="dall-e-3",
    # prompt="a white siamese cat",
    # size="1024x1024",
    # quality="standard",
    # n=1,
    # )
    # image_url = response.data[0].url
    # st.image(image_url,caption="Generated Image")
    st.title("Your Blog Post")
    st.write(response.text)