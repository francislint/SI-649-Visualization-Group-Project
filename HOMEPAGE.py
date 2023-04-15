import pandas as pd
import altair as alt
import streamlit as st
import time

st.set_page_config(
    page_title="Social Media Vis",
    page_icon="👋",
)

st.write("## Social Media Platforms Comparisons! 👋")
st.image('imgs/social media.jpeg')
st.sidebar.success("Select a Visualization Above.")


st.write('In this project, our focus is on exploring the top 1000 influencers across diverse social media platforms, i.e. **Instagram**, **YouTube**, and **TikTok**, with a specific emphasis on the following aspects: ')

st.write('- The **category distribution** of influencers and the **number of followers in each category** on Instagram & YouTube')
st.write('- The **audience engagement** (e.g. average views, averege likes and average comments) on Tiktok & Instagram')
st.write('- The **fluctuations in the follower count** of the leading 5 influencers on all platforms over the past 3 years ')
st.write('- The **influencer distribution** for Instagram & YouTube')
