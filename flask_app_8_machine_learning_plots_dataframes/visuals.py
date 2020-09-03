import json
import plotly
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import pandas as pd 

# size
height=500
width=800

# theme
colors_tableau = {
    "BLUE" : "#4E79A7",
    "GREEN" : "#59A14F",
    "RED" : "#E15759",
    "ORANGE" : "#F28E2B",
    "PURPLE" : "#B07AA1",
    "YELLOW" : "#EDC948",
}
color_cycle_custom = [
    colors_tableau["BLUE"],
    colors_tableau["GREEN"],
    colors_tableau["RED"],
    colors_tableau["ORANGE"],
    colors_tableau["PURPLE"],
]
pio.templates["custom_theme"] = go.layout.Template({
    'layout' : {
        'colorway' : color_cycle_custom,
    }
})
pio.templates.default = "simple_white+custom_theme"

def create_histogram(df):
    # pre-process data
    df_iris_melt = df.melt(
        value_vars=['sepal_length', 'sepal_width','petal_length', 'petal_width']
    )
    # create figure
    fig = px.histogram(
        data_frame=df_iris_melt, 
        x='value', color='variable', 
        barmode="overlay",
        title="<b>Histogram Title</b>",  
        labels={
            "value" : "Feature Value",
            "variable" : ""
        },
        nbins=50,
        opacity=0.8,
        width=width+92, 
        height=height
    )
    # convert to json
    fig_json = json.dumps(
        fig, 
        cls=plotly.utils.PlotlyJSONEncoder
    )
    return fig_json

def create_scatterplot(df):
    # create figure 
    fig = px.scatter(
        data_frame=df, 
        x='sepal_width', 
        y='sepal_length', 
        color='species', 
        size='petal_length',
        title="<b>Scatterplot</b>", 
        labels={
            "sepal_width" : "sepal_width value", 
            "sepal_length" : "sepal_length value",
            "species" : ""
        },
        opacity=0.6,
        width=width+72, 
        height=height
    )
    # convert to json
    fig_json = json.dumps(
        fig, 
        cls=plotly.utils.PlotlyJSONEncoder
    )
    return fig_json


def create_barplot(df):
    # pre-process data
    bar_data = df.groupby("species").mean()
    bar_data["species"] = bar_data.index
    bar_data.reset_index(drop=True, inplace=True)
    bar_data_melt = bar_data.melt(
        id_vars=['species'], 
        value_vars=['sepal_length', 'sepal_width','petal_length', 'petal_width']
    )
    bar_data_melt.columns = ["Species","Feature","Value"]
    # create figure
    fig = px.bar(
        data_frame=bar_data_melt, 
        x="Feature", y="Value", color="Species", 
        title="<b>Bar Plot Title</b>", 
        labels={
            "Feature" : "",
            "Species" : "",
            "Value" : "Mean Value",
        },
        barmode='group',
        opacity=0.9, 
        width=width+72, 
        height=height
    )
    # convert to json
    fig_json = json.dumps(
        fig, 
        cls=plotly.utils.PlotlyJSONEncoder
    )
    return fig_json
    