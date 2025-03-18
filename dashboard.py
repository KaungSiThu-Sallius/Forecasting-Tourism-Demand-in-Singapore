import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go

# Data Loading
df = pd.read_csv('data/inter_arrival_df.csv')  
df2 = pd.read_csv('data/clean_data.csv')
df3 = pd.read_csv('data/inter_arrival_df_total.csv')
purpose_visit_df = pd.read_csv('data/purpose_visit.csv')
arrival_age = pd.read_csv('data/inter_arrival_age.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Data Preparation
df['date'] = pd.to_datetime(df['date'])

df3['date'] = pd.to_datetime(df3['date'])
df3['year'] = df3['date'].dt.year
df3['month'] = df3['date'].dt.month_name()

avg_visitors_per_year = round(df3.groupby('year')['visitor_arrivals'].sum().mean(), 2)
peak_month = df3.groupby('month')['visitor_arrivals'].sum().idxmax()
most_visited_country = df.groupby('category_value')['visitor_arrivals'].sum().idxmax()

# For Graph 1
trend_tourism_fig = px.line(df3, x='date', y='visitor_arrivals', labels={'date': 'Date', 'visitor_arrivals': 'Visitors Count'})
trend_tourism_fig.update_layout(title={'text': 'Visitor Arrivals over Time', 'font': {'size': 20, 'family': 'Arial', 'weight': 'bold'}})

# For Graph 2
purpose_df_fig = px.pie(purpose_visit_df, values='count', names='purpose')
purpose_df_fig.update_layout(title={'text': 'Purpose of Visit per Arrivals', 'font': {'size': 20, 'family': 'Arial', 'weight': 'bold'}})

# For Graph 3
arrival_age_fig = px.bar(arrival_age, x='age', y='visitor_arrivals', labels={'age': 'Age', 'visitor_arrivals': 'Visitors Count'})
arrival_age_fig.update_layout(title={'text': 'Visitor Arrivals by Age Group', 'font': {'size': 20, 'family': 'Arial', 'weight': 'bold'}})

# Forecasting Preparation
forecast_df = df3[['date', 'visitor_arrivals']].copy()
forecast_df.rename(columns={'date': 'ds', 'visitor_arrivals': 'y'}, inplace=True)

model = Prophet(changepoint_prior_scale=0.1, interval_width=0.8)
model.fit(forecast_df)

# App Layout
app.layout = dbc.Container([
    html.H1('Singapore Tourism Demand Dashboard', className='text-center my-5'),

    # Overview Section
    dbc.Row([
        dbc.Col(dbc.Card([
            html.H3('Avg Annual Visitors', className='text-center'),
            html.H4(f"{avg_visitors_per_year:,.0f}", className='text-center')
        ], className='p-3 shadow-sm'), width=4),

        dbc.Col(dbc.Card([
            html.H3('Peak Month', className='text-center'),
            html.H4(peak_month, className='text-center')
        ], className='p-3 shadow-sm'), width=4),

        dbc.Col(dbc.Card([
            html.H3('Most Visited Country', className='text-center'),
            html.H4(most_visited_country, className='text-center')
        ], className='p-3 shadow-sm'), width=4)
    ], className='mb-4'),

    # Interactive Graphs
    dbc.Row([
        dbc.Col(dcc.Graph(id='tourism-trend-graph', figure=trend_tourism_fig, className='shadow_box'), width=12)
    ], className='mt-5'),

    dbc.Row([
        dbc.Col(dcc.Graph(id='purpose_visit', figure=purpose_df_fig, className='shadow_box'), width=5),
        dbc.Col(dcc.Graph(id='arrival_age', figure=arrival_age_fig, className='shadow_box'), width=7)
    ], className='mt-5'),

    # Forecast Section
    html.Hr(),
    html.H2('Forecasting Section', className='text-center mt-5'),
     dbc.Row([
        dbc.Col([
            html.Label('Select Forecast Year:'),
            dcc.Dropdown(
                id='forecast-year-dropdown',
                options=[
                    {'label': '2025', 'value': 2025},
                    {'label': '2026', 'value': 2026},
                    {'label': '2027', 'value': 2027},
                    {'label': '2028', 'value': 2028},
                    {'label': '2029', 'value': 2029},
                    {'label': '2030', 'value': 2030}
                ],
                value=2025,
                clearable=False,
                
            ),
            dcc.Graph(id='forecast-graph', className='shadow_box mt-4')
        ], width=12)
    ], className='mt-5'),
], className='mb-5')

@app.callback(
    Output('forecast-graph', 'figure'),
    [Input('forecast-year-dropdown', 'value')]
)
def update_forecast(selected_year):
    if selected_year == 2025:
        periods = 12
    elif selected_year == 2026:
        periods = 24
    elif selected_year == 2027:
        periods = 36
    elif selected_year == 2028:
        periods = 48
    elif selected_year == 2029:
        periods = 60
    else:
        periods = 72
    
    future = model.make_future_dataframe(periods=periods, freq='ME')
    forecast = model.predict(future)

    fig = go.Figure()
    
    # Actual Data
    fig.add_trace(go.Scatter(x=forecast_df['ds'], y=forecast_df['y'], mode='lines', name='Actual Data'))

    # Forecast Data
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast', line=dict(dash='dash')))

    fig.update_layout(title={'text': 'Visitor Arrivals Forecast',
                        'font': {'size': 20, 'family': 'Arial', 'weight': 'bold'}},
                        xaxis_title='Date',
                        yaxis_title='Visitor Arrivals',
                        legend_title='')

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)