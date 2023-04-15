import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames.
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
)

import pandas as pd
import altair as alt


# add selection 
single = alt.selection_single(on='mouseover')

# object conversion function
def convert_units(x):
    """
    This function converts a string with a suffix 'M' or 'K' to a float,
    multiplying by 1 million or 1000, respectively.
    """
    if isinstance(x, str):
        if 'M' in x:
            return float(x.replace('M', '')) * 1000000
        elif 'K' in x:
            return float(x.replace('K', '')) * 1000
    return x

# yotube dataset processing
yt = pd.read_csv('data/social media influencers - youtube.csv')
yt['Subscribers'] = yt['Subscribers'].apply(convert_units)

yt_cate = yt.groupby('Category').agg({'Subscribers': 'sum', 'channel name': 'count'}).reset_index()
yt_cate = yt_cate.rename(columns={'Subscribers': 'Total Subscribers', 'channel name': 'Count'})

# yotube piecharts
yt_pie_chart = alt.Chart(yt_cate).mark_arc(innerRadius=25, stroke="#fff").encode(
    theta=alt.Theta('Count:Q', stack=True),
    color=alt.Color('Category:N'),
    opacity=alt.condition(
        single,
        alt.value(1),
        alt.value(0.3)
    ),
    tooltip=[alt.Tooltip('Category:N', title='Influencer Category'), alt.Tooltip('Count:Q', title='Number of Influencers')]
).properties(
    width=250,
    height=250,
    title = alt.TitleParams(text='Category VS Influencers', fontSize=20, anchor='start')
).add_selection(
    single
)

yt_bar_chart = alt.Chart(yt_cate).mark_bar().encode(
    x= alt.X('Category:N', sort='-y',title=None),
    y=alt.Y('Total Subscribers:Q', title = None),
    color = alt.Color('Category:N'),
    opacity=alt.condition(
        single,
        alt.value(1),
        alt.value(0.3)
    ),
    tooltip=[alt.Tooltip('Category:N', title='Influencer Category'), alt.Tooltip('Total Subscribers:Q', title='Number of Subscribers')]
).properties(
    width=500,
    height=250,
    title = alt.TitleParams(text='Category VS Subscribers', fontSize=20, anchor='start')
).add_selection(
    single
)



# instagram dataset processing
ins = pd.read_csv('data/social media influencers - instagram.csv')
ins['Followers'] = ins['Followers'].apply(convert_units)

ins_cate = ins.groupby('category_1').agg({'Followers': 'sum', 'instagram name': 'count'}).reset_index()
ins_cate = ins_cate.rename(columns={'category_1':'Category','Followers': 'Total Followers', 'instagram name': 'Count'})

# instagram charts
ins_pie_chart = alt.Chart(ins_cate).mark_arc(innerRadius=25, stroke="#fff").encode(
    theta=alt.Theta('Count:Q', stack=True),
    color=alt.Color('Category:N'),
    opacity=alt.condition(
        single,
        alt.value(1),
        alt.value(0.3)
    ),
    tooltip=[alt.Tooltip('Category:N', title='Influencer Category'), alt.Tooltip('Count:Q', title='Number of Influencers')]
).properties(
    width=250,
    height=250,
    title = alt.TitleParams(text='Category VS Influencers', fontSize=20, anchor='start')
).add_selection(
    single
)

ins_bar_chart = alt.Chart(ins_cate).mark_bar().encode(
    x=alt.X('Category:N', sort='-y',title=None),
    y=alt.Y('Total Followers:Q', title = None),
    color = alt.Color('Category:N'),
    opacity=alt.condition(
        single,
        alt.value(1),
        alt.value(0.3)
    ),
    tooltip=[alt.Tooltip('Category:N', title='Influencer Category'), alt.Tooltip('Total Followers:Q', title='Number of Followers')]
).properties(
    width=500,
    height=250,
    title = alt.TitleParams(text='Category VS Followers', fontSize=20, anchor='start')
).add_selection(
    single
)

yt_combined = (yt_pie_chart | yt_bar_chart).properties(title='Youtube').configure_title(fontSize=36, anchor='middle')
ins_combined = (ins_pie_chart | ins_bar_chart).properties(title='Instagram').configure_title(fontSize=36, anchor='middle')


# streamlit visualization
st.altair_chart(yt_combined)
st.altair_chart(ins_combined)
# st.altair_chart(ins_combined, theme="streamlit", use_container_width=True)
