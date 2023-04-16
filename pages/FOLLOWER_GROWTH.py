import pandas as pd
import altair as alt
import streamlit as st
import time

st.markdown("### Influencer Follower Growth on Different Platforms Over the Past 3 Years")

def plot_animation(df):
    dots = alt.Chart(df).mark_circle().encode(
        x=alt.X('Date:T',axis=alt.Axis(title='Date')),
        y=alt.Y('# of followers:Q',axis=alt.Axis(title='Number of Followers')),
        color='Influencer:N'
     ).interactive()

    lines = alt.Chart(df).mark_line().encode(
        x=alt.X('Date:T',axis=alt.Axis(title='Date')),
        y=alt.Y('# of followers:Q',axis=alt.Axis(title='Number of Followers')),
        color='Influencer:N'
     ).properties(
        width=600,
        height=300,
        title='Follower Growth of the Top 5 Influencers'
     )

    return dots+lines


def preprocessDF(df):
    names_list = list(df.columns)[1:]
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
youtube_top_5 = pd.read_excel('data/Youtube top 5.xlsx')
tiktok_top_5 = pd.read_excel('data/Tiktok top 5.xlsx')

lines_ins = plot_animation(preprocessDF(ins_top_5))
lines_youtube = plot_animation(preprocessDF(youtube_top_5))
lines_tiktok = plot_animation(preprocessDF(tiktok_top_5))

number_of_influencer = 5
N = ins_top_5.shape[0] # number of elements in the dataframe
burst = 6       # number of elements (months) to add to the plot
size = burst     # size of the current dataset

st.write('Press the Start button below to animate the plot!')

start_btn = st.button('Start')

tab_ins, tab_youtube, tab_tiktok = st.tabs(["Instagram", 
                                            "YouTube", 
                                            "Tiktok"])

with tab_ins:
    line_plot_ins = st.altair_chart(lines_ins, use_container_width=True)
with tab_youtube:
    line_plot_youtube = st.altair_chart(lines_youtube, use_container_width=True)
with tab_tiktok:
    line_plot_tiktok = st.altair_chart(lines_tiktok, use_container_width=True)


if start_btn:
    for i in range(1,N):
        step_df_ins = generate_step_df(preprocessDF(ins_top_5), size)
        step_df_youtube = generate_step_df(preprocessDF(youtube_top_5), size)
        step_df_tiktok = generate_step_df(preprocessDF(tiktok_top_5), size)

        lines_ins = plot_animation(step_df_ins)
        lines_youtube = plot_animation(step_df_youtube)
        lines_tiktok = plot_animation(step_df_tiktok)

        with tab_ins:
            line_plot_ins = line_plot_ins.altair_chart(lines_ins, use_container_width=True)
        with tab_youtube:
            line_plot_youtube = line_plot_youtube.altair_chart(lines_youtube, use_container_width=True)
        with tab_tiktok:
            line_plot_tiktok = line_plot_tiktok.altair_chart(lines_tiktok, use_container_width=True)

        size = i + burst
        if size >= N: 
            size = N - 1
        time.sleep(0.2)


