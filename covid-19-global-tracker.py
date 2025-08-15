import pandas as pd
import plotly.express as px

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

countries = ['South Africa', 'United States', 'India', 'Brazil', 'Germany']
df_filtered = df[df['location'].isin(countries)]
df_filtered = df_filtered[['location', 'date', 'new_cases', 'new_deaths']]
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

fig_cases = px.line(df_filtered, x='date', y='new_cases', color='location',
                    title='Daily New COVID-19 Cases')
fig_cases.show()

fig_deaths = px.line(df_filtered, x='date', y='new_deaths', color='location',
                     title='Daily New COVID-19 Deaths')
fig_deaths.show()