import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Social Media Platforms Comparisons! 👋")

st.sidebar.success("Select a Visualization Above.")

import pandas as pd
import altair as alt
import streamlit as st
import time

def plot_animation(df):
    lines = alt.Chart(df).mark_line().encode(
        x=alt.X('Date:T',axis=alt.Axis(title='Date')),
        y=alt.Y('# of followers:Q',axis=alt.Axis(title='Number of Followers')),
        color='Influencer:N'
     ).properties(
        width=600,
        height=300,
        title='Follower Growth of the Top 5 Influencers on Instagram'
     ) 
    return lines


def preprocessDF(df):
    names_list = list(ins_top_5.columns)[1:]
    Influencer_list = []
    value_list = []
    for name in names_list:
        Influencer_list += [name]*len(df)
        value_list += list(df[name])
    date_list = list(df['Date'])*len(names_list)
    
    new_df = pd.DataFrame(data={'Date': date_list,
                                'Influencer': Influencer_list,
                                '# of followers': value_list})
    
    return new_df

def generate_step_df(df, size):
    new_step_df = df.iloc[0:size]
    for i in range(1, number_of_influencer):
        new_step_df = pd.concat([new_step_df, df.iloc[i*N:i*N + size]])
    
    return new_step_df.reset_index(drop=True)


ins_top_5 = pd.read_excel('data/Ins top 5.xlsx')

lines = alt.Chart(preprocessDF(ins_top_5)).mark_line().encode(
     x=alt.X('Date:T',axis=alt.Axis(title='Date')),
     y=alt.Y('# of followers:Q',axis=alt.Axis(title='Number of Followers')),
     color='Influencer:N'
).properties(
    title='Follower Growth of the Top 5 Influencers on Instagram',
    width=600,
    height=300,
)

number_of_influencer = 5
N = ins_top_5.shape[0] # number of elements in the dataframe
burst = 6       # number of elements (months) to add to the plot
size = burst     # size of the current dataset

line_plot = st.altair_chart(lines)
start_btn = st.button('Start')


if start_btn:
    for i in range(1,N):
        step_df = generate_step_df(preprocessDF(ins_top_5), size)
        lines = plot_animation(step_df)
        line_plot = line_plot.altair_chart(lines)
        size = i + burst
        if size >= N: 
            size = N - 1
        time.sleep(0.2)



st.markdown(
    """
    blabla
"""
)