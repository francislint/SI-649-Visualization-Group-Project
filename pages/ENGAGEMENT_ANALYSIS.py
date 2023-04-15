import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.markdown("### Audience Engagement Analysis on TikTok and Instagram")
# st.sidebar.header("DataFrame Demo")

import streamlit as st
from PIL import Image

# Define a dictionary that maps options to image URLs
option_images = {
    'Correlations Heatmap': ['imgs/tiktok_cor.png', 'imgs/ins_cor.png'],
    'Views V.S. Likes': ['imgs/tiktok_vl.png', 'imgs/ins_vl.png'],
    'Views V.S. Comments': ['imgs/tiktok_vc.png', 'imgs/ins_vc.png'],
    'Likes V.S. Comments': ['imgs/tiktok_lc.png', 'imgs/ins_lc.png'],
}

# Create a dropdown box to select the option
selected_option = st.selectbox("Select an Comparision", list(option_images.keys()))

# Load the images for the selected option
image1_url, image2_url = option_images[selected_option]
image1 = Image.open(image1_url)
image2 = Image.open(image2_url)

# Display the images side by side
col1, col2 = st.columns(2)
with col1:
    st.image(image1, use_column_width=True)
with col2:
    st.image(image2, use_column_width=True)
