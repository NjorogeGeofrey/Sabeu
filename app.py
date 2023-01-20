from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Sabeu Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
    
    
def local_css(file_name):
      with open(file_name) as f:
         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")         
    
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_sabeu = Image.open("images/IMG_2932.jpg")


with st.container():
    st.subheader("Hello and welcome to sabeu :wave:")
    st.title("STATISTICS ANALYSIS BUREAU EGERTON")
    st.write("We are a registered profesional association with the Dean of Students at Egerton University.")
 
  
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we offer")
        st.write("##")
        st.write(
        """
        Our mandate is to promote professionalism in Statistics through various training.
        Every semester we offer enrolment in various statistical packages at pocket friendly prices.
        We offer:
        - EXCEL  @2000,
        - SPSS   @1000,
        - STATA  @1000,
        - R programing  @2000.
        """
        )

with right_column:
     st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("SABEU")
    st.write("##")
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(img_sabeu)
    
    
with text_column:
    st.subheader("Join us and become a data GURU")
    st.write("""
    Want to learn more about data, let SABEU be your first stepping stone in your data journey.
    Remember Data is the new oil.
    
    You can reach us through :
    - Odambo Michael: +254713605461
    - Alphida Namulata: +254757560736
    - Kanju Anderson: +254798327969
    """)
    
with st.container():
    st.write("---")
    st.header("Get In Touch with Us")
    st.write("##")
    
    
    contact_form = """
    <form action="https://formsubmit.co/njorogegeofrey347@gmail.com" method="POST">
    <input type="hidden" name"_captcha" value="false">
     <input type="text" name="name"  placeholder="Your name"required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message"  placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
   </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
    
    
