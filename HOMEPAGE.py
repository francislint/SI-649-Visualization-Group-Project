import pandas as pd
import altair as alt
import streamlit as st
import time

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("## Social Media Platforms Comparisons! 👋")
st.image('imgs/social media.jpeg')
st.sidebar.success("Select a Visualization Above.")


st.write('We are interested in exploring the top 1000 influencers in different social media platforms, i.e. **Instagram**, **YouTube** and **Tiktok**. ')
