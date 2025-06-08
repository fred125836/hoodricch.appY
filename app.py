from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Hello World", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/fc0153da-fac2-4fdb-bebb-7baf6d15a175/91AkjmPx5Y.json")
img_contact_form = Image.open("images/krm.jpg")
img_lottie_animation = Image.open("images/krm b.jpg")
# ---- HEADER SECTION ----
with st.container():
    st.subheader("My name is Onwuegbuna Okwuchukwu :wave:")
    st.title("I am a Typist, Graphic Designer, and Forex Trader from Nigeria")
    st.write("i am from anambra state")
    st.write("I am passionate about Web Development")
    st.write("you are welcome to my page")
    st.write("[contact me on whatsapp >](https://wa.me/message/CL576QP54YBPP1)")

# ----WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What i do")
        st.write("##")
        st.write(
            """
            After finding my website:
            - contact me for any graphic designing job.
            """
        )

with right_column:
    st_lottie(lottie_coding, height=400, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("MY PROJECT")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("CONTACT ME TO LEARN GRAPHIC DESIGNING AND WEB DEVELOPMENT")
        st.write(
            """
            WHAT YOU WILL BE LEARNING FROM ME
            - I WILL TEACH YOU HOW TO DEVELOP WEBSITE WITH PYTHON USING PYCHARM
            - I WILL TEACH YOU GRAPHIC DESIGN WITH CORELDRAW AND CANVA
            - I WILL TEACH YOU HOW TO USE MICROSOFT OFFICES (WORD, EXCEL AND POWERPOINT)
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("WHAT YOU WILL BE LEARNING IN THE MICROSOFT OFFICE PACKAGE")
        st.write(
            """
            - LEARN HOW TO TYPE AND EDIT DOCUMENT IN MICROSOFT WORD
            - LEARN HOW TO MAKE ANIMATION WITH POWERPOINT
            - LEARN HOW TO USE SPREADSHEET WITH EXCEL
            """
        )
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/jessicasmith22025@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
