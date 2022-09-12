# %%
# import plotly.express as px
import altair as alt
import pandas as pd
import plotly.express as px


# %% IMPORT DATA
# path = '../sample_data.csv'
path = '../Data/Open Data Five System Total.csv'

df = pd.read_csv(path)




# %% PLOTLY

df_px = df.copy()

df_px['data_period'] = df_px['data_period'].astype('datetime64')

df_px = df_px.rename(
    {
        'DHS Total Unique Count': 'DHS',
        'HRA DV Total Unique Count': 'HRA DV', 
        'HRA HASA Total Unique Count': 'HRA HASA', 
        'DYCD Total Unique Count': 'DYCD', 
        'HPD Total Unique Count (105% Est.)': 'HPD (Est)'
    }, axis=1)

df_px['Five System Total'] = df_px[
    [
    'DHS', 
    'HRA DV', 
    'HRA HASA', 
    'DYCD', 
    'HPD (Est)'
    ]
].sum(axis=1)

fig = px.bar(
    df_px, 
    x='data_period', 
    y=[
        'DHS', 
        'HRA DV', 
        'HRA HASA', 
        'DYCD', 
        'HPD (Est)', 
    ],
    title='Five System Totals',
    color_discrete_map={
        'DHS': '#5cb8b2',
        'HRA DV': '#F99D1B',
        'HRA HASA': '#5cc8c2',
        'DYCD': '#5cd8d2',
        'HPD (Est)': '#5ce8e2',
    },
    labels={
        'data_period': 'Month/Year of Data',
        'variable': 'Shelter System',
        'value': 'Unique Count',
    },
    custom_data=['Five System Total'],
    # hover_name='Five System Total',
    # width=800, height=400 # Using this for comparison with altair
)

print("plotly express hovertemplate:", fig.data[0].hovertemplate)

fig.update_traces(
    marker_line_width=0,
    hovertemplate="Shelter System=%{customdata[0]}<br>Month/Year of Data=%{x}<br>Unique Count=%{y}<extra></extra>"
)

fig.update_xaxes(
    fixedrange=True,
    ticks='outside',
    # tickwidth=2,
    tickcolor='white',
    ticklen=5
    )
fig.update_yaxes(
    fixedrange=True,
    ticks='outside',
    # tickwidth=2,
    tickcolor='white',
    ticklen=5
    )


fig.update_layout(
    {
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        # 'hovermode': "x",
        # 'font_family': 'Lato',
    },
    xaxis_hoverformat='%B %Y',
)

fig.write_html('plotly_chart.html')


# # %% ALTAIR

# df_alt = df.melt(
#     id_vars='data_period',
#     var_name='Shelter System',
#     value_name='Unique Count'
#     )

# df_alt['data_period'] = df_alt['data_period'].astype('datetime64')

# df_alt['tooltip'] = df_alt.apply(lambda x: f"{x['Unique Count']} ({x['Shelter System']})", axis=1)

# sort_order_map = {
#     'DHS Total Unique Count': 1,
#     'HRA DV Total Unique Count': 3,
#     'HRA HASA Total Unique Count': 2,
#     'DYCD Total Unique Count': 5,
#     'HPD Total Unique Count (105% Est.)': 4,
# }

# df_alt['sort_order'] = df_alt.apply(lambda x: sort_order_map[x['Shelter System']], axis=1)

# color_map = {
#     'DHS Total Unique Count': '#5cb8b2',
#     'HRA DV Total Unique Count': '#F99D1B',
#     'HRA HASA Total Unique Count': '#3fb0d9',
#     'DYCD Total Unique Count': '#1d7595',
#     'HPD Total Unique Count (105% Est.)': '#6ac2e2',
# }

# df_alt['color'] = df_alt.apply(lambda x: color_map[x['Shelter System']], axis=1)

# chart = alt.Chart(df_alt).mark_bar().encode(
#     x=alt.X('data_period', axis=alt.Axis(title='Data Period')),
#     y=alt.Y('sum(Unique Count)', axis=alt.Axis(title='Unique Count')),
#     # color='color',
#     tooltip='tooltip',
#     order=alt.Order(
#         'sort_order',
#         sort='ascending'
#     ),
#     color=alt.Color('color', scale=None, title='Shelter System')
# ).configure_axis(
#     grid=False
# ).configure_view(
#     strokeWidth=0
# )



# chart.save('altair_chart.html')

# # %%

# %%
