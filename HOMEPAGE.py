import pandas as pd
import altair as alt
import streamlit as st
import time

st.set_page_config(
    page_title="Social Media Cimparision",
    page_icon="👋",
)

st.write("## BATTLE OF SOCIAL MEDIA GIANTS: COMPARING TIKTOK, INSTAGRAM, YOUTUBE👋")
st.image('imgs/social media.jpeg')
st.sidebar.success("Select a Visualization Above.")

st.write('### Brief Caption')

st.write('In this project, our focus is on exploring the top 1000 influencers across diverse social media platforms, i.e. **Instagram**, **YouTube**, and **TikTok**, with a specific emphasis on the following aspects: ')
st.write('''
- The **category distribution** of influencers and the **number of followers in each category** on Instagram & YouTube
- The **audience engagement** (e.g. average views, averege likes and average comments) on Tiktok & Instagram
- The **fluctuations in the follower count** of the leading 5 influencers on all platforms over the past 3 years
- The **influencer distribution** for Instagram & YouTube
        ''')
st.write('### Data Source')
st.write('')
st.write('### Methods')
st.write('''
- Pandas for Data Processing
- Seaborn for Static Visualization
        ‘’‘)
