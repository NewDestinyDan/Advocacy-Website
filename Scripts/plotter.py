#%%
# import plotly.express as px
import altair as alt
import pandas as pd
import plotly.express as px


# %% IMPORT DATA
df = pd.read_csv(
    '../sample_data.csv'
)


# %% PLOTLY

df_px = df.copy()

df_px['data_period'] = df_px['data_period'].astype('datetime64')

df_px['Five System Total'] = df_px[
    [
    'DHS Total Uniqe Count', 
    'HRA DV Total Unique Count', 
    'HRA HASA Total Unique Count', 
    'DYCD Total Unique Count', 
    'HPD Total Unique Count (105% Est.)'
    ]
].sum(axis=1)

fig = px.bar(
    df_px, 
    x='data_period', 
    y=[
        'DHS Total Uniqe Count', 
        'HRA DV Total Unique Count', 
        'HRA HASA Total Unique Count', 
        'DYCD Total Unique Count', 
        'HPD Total Unique Count (105% Est.)'
    ],
    color_discrete_map={
        'DHS Total Uniqe Count': '#5cb8b2',
        'HRA DV Total Unique Count': '#F99D1B',
        'HRA HASA Total Unique Count': '#5cc8c2',
        'DYCD Total Unique Count': '#5cd8d2',
        'HPD Total Unique Count (105% Est.)': '#5ce8e2',
    },
    labels={
        'data_period': 'Month/Year of Data',
        'variable': 'Shelter System',
        'value': 'Unique Count',
    },
    hover_name='Five System Total',
    width=800, height=400 # Using this for comparison with altair
)

fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    # 'font_family': 'Lato',
})

fig.write_html('plotly_chart.html')


# %% ALTAIR


df_alt = df.melt(
    id_vars='data_period',
    var_name='Shelter System',
    value_name='Unique Count'
    )

df_alt['data_period'] = df_alt['data_period'].astype('datetime64')

df_alt['tooltip'] = df_alt.apply(lambda x: f"{x['Unique Count']} ({x['Shelter System']})", axis=1)

sort_order_map = {
    'DHS Total Uniqe Count': 1,
    'HRA DV Total Unique Count': 3,
    'HRA HASA Total Unique Count': 2,
    'DYCD Total Unique Count': 5,
    'HPD Total Unique Count (105% Est.)': 4,
}

df_alt['sort_order'] = df_alt.apply(lambda x: sort_order_map[x['Shelter System']], axis=1)

color_map = {
    'DHS Total Uniqe Count': '#5cb8b2',
    'HRA DV Total Unique Count': '#F99D1B',
    'HRA HASA Total Unique Count': '#3fb0d9',
    'DYCD Total Unique Count': '#1d7595',
    'HPD Total Unique Count (105% Est.)': '#6ac2e2',
}

df_alt['color'] = df_alt.apply(lambda x: color_map[x['Shelter System']], axis=1)

chart = alt.Chart(df_alt).mark_bar().encode(
    x=alt.X('data_period', axis=alt.Axis(title='Data Period')),
    y=alt.Y('sum(Unique Count)', axis=alt.Axis(title='Unique Count')),
    # color='color',
    tooltip='tooltip',
    order=alt.Order(
        'sort_order',
        sort='ascending'
    ),
    color=alt.Color('color', scale=None, title='Shelter System')
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
)



chart.save('altair_chart.html')

# %%
