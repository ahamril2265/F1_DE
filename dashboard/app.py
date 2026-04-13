import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import time

from utils.config import DB_URI


# ✅ DB wait logic
def get_engine():
    for _ in range(10):
        try:
            engine = create_engine(DB_URI)
            conn = engine.connect()
            conn.close()
            return engine
        except OperationalError:
            print("Waiting for DB...")
            time.sleep(3)
    raise Exception("Database not available")


engine = get_engine()

app = dash.Dash(__name__)

# ✅ Load data
df = pd.read_sql("SELECT * FROM lap_times", engine)

# ✅ Fix missing column
if 'lap_time_sec' not in df.columns:
    df['laptime'] = pd.to_timedelta(df['laptime'], errors='coerce')
    df['lap_time_sec'] = df['laptime'].dt.total_seconds()

# Drop nulls
df = df.dropna(subset=['lap_time_sec'])

drivers = sorted(df['driver'].unique())

# ---------------- LAYOUT ---------------- #

app.layout = html.Div([
    html.H1("🏎️ F1 Race Analytics Dashboard"),

    # 🔽 Controls
    html.Div([
        dcc.Dropdown(
            id='driver-dropdown',
            options=[{'label': d, 'value': d} for d in drivers],
            value=drivers[:3],
            multi=True
        ),

        dcc.RangeSlider(
            id='lap-slider',
            min=int(df['lapnumber'].min()),
            max=int(df['lapnumber'].max()),
            step=1,
            value=[1, int(df['lapnumber'].max())],
            marks={i: str(i) for i in range(1, int(df['lapnumber'].max())+1, 5)}
        )
    ], style={'margin': '20px'}),

    # 📈 Graphs
    dcc.Graph(id='lap-time-graph'),
    dcc.Graph(id='position-graph'),
    dcc.Graph(id='avg-lap-bar'),

    # ⚡ Stats
    html.Div(id='stats', style={'fontSize': 20, 'margin': '20px'})
])


# ---------------- CALLBACK ---------------- #

@app.callback(
    [
        Output('lap-time-graph', 'figure'),
        Output('position-graph', 'figure'),
        Output('avg-lap-bar', 'figure'),
        Output('stats', 'children')
    ],
    [
        Input('driver-dropdown', 'value'),
        Input('lap-slider', 'value')
    ]
)
def update_dashboard(selected_drivers, lap_range):

    filtered = df[
        (df['driver'].isin(selected_drivers)) &
        (df['lapnumber'] >= lap_range[0]) &
        (df['lapnumber'] <= lap_range[1])
    ]

    # 📈 Lap Time Trend
    fig1 = px.line(
        filtered,
        x="lapnumber",
        y="lap_time_sec",
        color="driver",
        title="Lap Time Trend"
    )

    # 🏎️ Position Chart
    if 'position' in filtered.columns:
        fig2 = px.line(
            filtered,
            x="lapnumber",
            y="position",
            color="driver",
            title="Position Changes"
        )
    else:
        fig2 = px.line(title="Position data not available")

    # 📊 Average Lap Time
    avg_df = filtered.groupby('driver')['lap_time_sec'].mean().reset_index()

    fig3 = px.bar(
        avg_df,
        x="driver",
        y="lap_time_sec",
        title="Average Lap Time"
    )

    # ⚡ Stats
    fastest = filtered.loc[filtered['lap_time_sec'].idxmin()]
    stats = f"🔥 Fastest Lap: Driver {fastest['driver']} - {fastest['lap_time_sec']:.2f}s"

    return fig1, fig2, fig3, stats


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)