import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Set default plotly template to "plotly_white"
pio.templates.default = "plotly_white"

# Function to remove unnamed columns from DataFrames
def remove_unnamed(df):
    return df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Function to read data from source file
def read_data(file_path):
    return remove_unnamed(pd.read_csv(file_path))

# Load data from source
data = read_data("t20-world-cup-22.csv")
print(data.info())

# Visualize number of matches won by each team
fig_team_wins = px.bar(data, x="winner", title="Number of Matches Won by Teams in T20 World Cup 2022")
fig_team_wins.show()

# Visualize number of matches won by batting first or second
fig_matches_won = go.Figure(data=[go.Pie(labels=data["won by"].value_counts().index, 
                                        values=data["won by"].value_counts().values,
                                        hoverinfo='label+percent',
                                        textinfo='value',
                                        textfont_size=30,
                                        marker=dict(colors=['gold', 'lightgreen'],
                                                    line=dict(color='black', width=3)))])
fig_matches_won.update_layout(title_text='Number of Matches Won By Runs Or Wickets')
fig_matches_won.show()

# Visualize toss decisions by teams
fig_toss_decision = go.Figure(data=[go.Pie(labels=data["toss decision"].value_counts().index, 
                                            values=data["toss decision"].value_counts().values,
                                            hoverinfo='label+percent',
                                            textinfo='value',
                                            textfont_size=30,
                                            marker=dict(colors=['skyblue', 'yellow'],
                                                        line=dict(color='black', width=3)))])
fig_toss_decision.update_layout(title_text='Toss Decisions by Teams')
fig_toss_decision.show()

# Visualize the top scorers
fig_top_scorers = px.bar(data, 
                         x="top scorer", 
                         y="highest score", 
                         color="highest score",
                         title="Top Scorers")
fig_top_scorers.show()

# Visualize player of the match awards
fig_player_of_the_match = px.bar(data, x="player of the match", title="Player of the Match Awards")
fig_player_of_the_match.show()

# Compare the runs scored in the first innings and second innings in every stadium
fig_innings_runs = go.Figure()
fig_innings_runs.add_trace(go.Bar(x=data["venue"], y=data["first innings score"], name='First Innings Runs', marker_color='blue'))
fig_innings_runs.add_trace(go.Bar(x=data["venue"], y=data["second innings score"], name='Second Innings Runs', marker_color='red'))
fig_innings_runs.update_layout(barmode='group', xaxis_tickangle=-45, title="Best Stadiums to Bat First or Chase")
fig_innings_runs.show()

# Compare the number of wickets lost in the first innings and second innings in every stadium
fig_innings_wickets = go.Figure()
fig_innings_wickets.add_trace(go.Bar(x=data["venue"], y=data["first innings wickets"], name='First Innings Wickets', marker_color='blue'))
fig_innings_wickets.add_trace(go.Bar(x=data["venue"], y=data["second innings wickets"], name='Second Innings Wickets', marker_color='red'))
fig_innings_wickets.update_layout(barmode='group', xaxis_tickangle=-45, title="Best Stadiums to Bowl First or Defend")
fig_innings_wickets.show()
