from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="La Copa del Mundo de Diego",
    page_icon="🏆",
    layout="wide",
)

# Hide Streamlit's default chrome and padding so the game fills the page.
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .stApp {background: #0a0f1c;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] > .main {padding: 0 !important;}
      [data-testid="stHeader"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).parent.joinpath("index.html").read_text(encoding="utf-8")

# The game is a tall single page; give the iframe a generous height and let it
# scroll internally. Adjust this number if you want more/less on screen.
components.html(html, height=4200, scrolling=True)
