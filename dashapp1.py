import dash
import pandas as pd
from dash import dcc, html, Input, Output, State
from joblib import load

# Load the Model
model = load('Concrete Strength Predictive Model.pkl')

# Load the Scaler
scaler = load('scaler.pkl')

# Read the Data
concrete = pd.read_csv('Concrete Data.csv')

# Dash Web App
app = dash.Dash()
server = app.server
app.layout = html.Div([
    html.H1('Concrete Compressive Strength Prediction'),
    html.P([
        'Concrete is the most common material used in construction of structures. Concrete is made from several '
        'ingredients including ',
        html.Span(
            'Cement, Water, Fly Ash, Slag, Superplasticizer, Coarse Aggregate, Fine Aggregate and Concrete Curing '
            'Period. ',
            style={'color': 'red'}),
        'Different proportions of these ingredients results in different strength of the concrete. This predictive '
        'model allows to predict concrete compressive strength based on different proportion of ingredients and '
        'curing period.'
    ]),
    html.Div([
        html.Label('Enter Quantity of Cement (kg)')],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '5px'}),
    html.Div([
        dcc.Input(id='cement', value='', type='number', min=concrete['cement'].min(), max=concrete['cement'].max())],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '20px'}),
    html.Div([
        html.Label('Enter Quantity of Slag (kg)')],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '5px'}),
    html.Div([
        dcc.Input(id='slag', value='', type='number', min=concrete['slag'].min(), max=concrete['slag'].max())],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '20px'}),
    html.Div([
        html.Label('Enter Quantity of Fly Ash (kg)')],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '5px'}),
    html.Div([
        dcc.Input(id='fly-ash', value='', type='number', min=concrete['fly_ash'].min(), max=concrete['fly_ash'].max())],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '20px'}),
    html.Div([
        html.Label('Enter Quantity of Water (kg)')],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '5px'}),
    html.Div([
        dcc.Input(id='water', value='', type='number', min=concrete['water'].min(), max=concrete['water'].max())],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '20px'}),
    html.Div([
        html.Label('Enter Quantity of Superplasticizer (kg)')],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '5px'}),
    html.Div([
        dcc.Input(id='sp', value='', type='number', min=concrete['superplasticizer'].min(),
                  max=concrete['superplasticizer'].max())],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '20px'}),
    html.Div([
        html.Label('Enter Quantity of Coarse Aggregate (kg)')],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '5px'}),
    html.Div([
        dcc.Input(id='coarse-agg', value='', type='number', min=concrete['coarse_aggregate'].min(),
                  max=concrete['coarse_aggregate'].max())],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '20px'}),
    html.Div([
        html.Label('Enter Quantity of Fine Aggregate (kg)')],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '5px'}),
    html.Div([
        dcc.Input(id='fine-agg', value='', type='number', min=concrete['fine_aggregate'].min(),
                  max=concrete['fine_aggregate'].max())],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '20px'}),
    html.Div([
        html.Label('Enter Curing Period (days)')], style={'color': 'blue', 'display': 'block', 'margin-bottom': '5px'}),
    html.Div([
        dcc.Input(id='age', value='', type='number', min=concrete['age'].min(), max=concrete['age'].max())],
        style={'color': 'blue', 'display': 'block', 'margin-bottom': '20px'}),
    html.Div([
        html.Button('Predict', id='predict-button')], style={'margin-bottom': '10px'}),
    html.Div(id='prediction', style={'fontSize': 24, 'color': 'blue'}),
    html.H2('Model Limitations'),
    html.P(
        '1. The model does not take into account different environmental conditions in which concrete can be prepared.',
        style={'margin-bottom': '5px'}),
    html.P(
        "2. The quality of the materials can be different based on it's source which can affect the strength of the "
        "concrete")
])


@app.callback(Output(component_id='prediction', component_property='children'),
              [Input(component_id='predict-button', component_property='n_clicks')],
              [State(component_id='cement', component_property='value'),
               State(component_id='slag', component_property='value'),
               State(component_id='fly-ash', component_property='value'),
               State(component_id='water', component_property='value'),
               State(component_id='sp', component_property='value'),
               State(component_id='coarse-agg', component_property='value'),
               State(component_id='fine-agg', component_property='value'),
               State(component_id='age', component_property='value')])
def predict_concrete_strength(n_clicks, cement, slag, fly_ash, water, sp, coarse_agg, fine_agg, age):
    if n_clicks:
        feature_vector = [
            [float(cement), float(slag), float(fly_ash), float(water), float(sp), float(coarse_agg), float(fine_agg),
             float(age)]]  # Prepare the feature vector for prediction
        feature_vector_scaled = scaler.transform(feature_vector)
        prediction = model.predict(feature_vector_scaled)[0].round(2)
        result = f'The Compressive Strength of Concrete Mix is Predicted to be {prediction} MPa After {float(age)} Days'
        return html.Div(result, style={'fontSize': 24, 'color': 'green'})


if __name__ == '__main__':
    app.run_server()
