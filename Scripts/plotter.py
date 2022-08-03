import plotly.express as px

fig = px.bar(x=["and", "b", "c"], y=[1, 3, 2])
fig.write_html("test_file.html")