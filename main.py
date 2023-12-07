import streamlit as st

# Set the website layouts
st.set_page_config(
    page_title='RAUL Y ZANYA',
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

# "# Center an image when in fullscreen"
# "Images (and most elements in general) are always aligned to the left"
# st.image('inputs/Home.png')
left_co, cent_co, last_co = st.columns([1, 8, 1])
with cent_co:
    st.image('inputs/Home.png')
    streamlit_style = """
    			<style>
    			@import url('https://fonts.googleapis.com/css2?family=Hedvig+Letters+Serif:opsz@12..24&display=swap');

    			html, body, [class*="css"]  {
    			font-family: 'Hedvig Letters Serif', serif;
    			font-size: 20px
    			}
    			</style>

    			"""

    st.markdown(streamlit_style, unsafe_allow_html=True)
    original_title = '<p style="font-family:Hedvig Letters Serif; text-align: center; color:black; font-size: 60px;">Zanya y Raul</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    # st.markdown("<h1 style='text-align: center; color: black;'>Zanya y Raul</h1>", unsafe_allow_html=True)

    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')
    st.markdown('RAUL Y ZANYA', unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: red;'>Zanya y Raul</h1>", unsafe_allow_html=True)

    # st.image('inputs/Home.png')