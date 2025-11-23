import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Başlık
st.title("Student Performance Dashboard")

# CSV dosyasını oku
df = pd.read_csv("data/student_performance.csv")


# ----------------------------- SIDEBAR ---------------------------------
school_option = st.sidebar.multiselect(
    "Select School Type:",
    options=df["School_Type"].unique(),
    default=df["School_Type"].unique()
)

# Apply the filter
filtered_df = df[df["School_Type"].isin(school_option)]

# ----------------------------- BOX PLOT: TEACHER QUALITY VS ATTENDANCE ---------------------------------
st.subheader("Box Plot: Attendance Rate by Teacher Quality Level")

# Make the Box Plot (X: Teacher Quality, Y: Attendance Rate)
fig_box = px.box(
    filtered_df,
    x="Teacher_Quality", # X-axis is the teacher's quality level
    y="Attendance", # Y-axis is the attendance score (e.g., percentage)
    color="Teacher_Quality", # Color the boxes based on Teacher Quality
    category_orders={'Teacher_Quality': ['Low', 'Medium', 'High']}, # Ensure categories are ordered correctly
    points="all", # Show all the tiny data points
    hover_data=["Hours_Studied", "Exam_Score", "Parental_Involvement"] # Show extra info when hovering
)

# Fix up the Graph Looks
fig_box.update_layout(
    title="Student Attendance Rate Distribution Grouped by Teacher Quality",
    xaxis_title="Teacher Quality Level",
    yaxis_title="Attendance Rate (%)",
    boxmode="group" # Ensures the boxes are displayed as a group
)

st.plotly_chart(fig_box)

  
# ----------------------------- TREEMAP ---------------------------------
st.subheader("Treemap: School Type → Parental Education → Gender")

treemap_df = df.groupby(
    ["School_Type", "Parental_Education_Level", "Gender"], as_index=False
)["Exam_Score"].mean()

fig2 = px.treemap(
    treemap_df,
    path=["School_Type", "Parental_Education_Level", "Gender"],
    values="Exam_Score",
    color="Exam_Score",
    color_continuous_scale="Blues",
    hover_data=["Exam_Score"]
)

fig2.update_layout(margin=dict(t=50, l=25, r=25, b=25))
st.plotly_chart(fig2)

# ----------------------------- PARALLEL COORDINATES ---------------------------------
st.subheader("Parallel Coordinates Chart")

# Outlier toggle
remove_outliers = st.checkbox("Remove Outliers", value=False)

parallel_df = filtered_df.copy()

# --> OUTLIER FUNCTION
def remove_outliers_iqr(data, cols):
    clean_df = data.copy()
    for col in cols:
        if col in clean_df.columns and pd.api.types.is_numeric_dtype(clean_df[col]):
            Q1 = clean_df[col].quantile(0.25)
            Q3 = clean_df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            clean_df = clean_df[(clean_df[col] >= lower) & (clean_df[col] <= upper)]
    return clean_df

# Eğer ON ise numeric kolonlarda outlier kes
if remove_outliers:
    numeric_cols = ["Hours_Studied", "Attendance", "Sleep_Hours", "Previous_Scores", "Exam_Score"]
    parallel_df = remove_outliers_iqr(parallel_df, numeric_cols)

# Motivation_Level kategorik ise numeric yap
if parallel_df["Motivation_Level"].dtype.name == "category" or parallel_df["Motivation_Level"].dtype == object:
    parallel_df["Motivation_Level_Num"] = parallel_df["Motivation_Level"].astype("category").cat.codes
    color_col = "Exam_Score"
    dimensions = ["Hours_Studied", "Attendance", "Sleep_Hours", "Previous_Scores", "Motivation_Level_Num", "Exam_Score"]
    motivation_col = "Motivation_Level_Num"
else:
    color_col = "Exam_Score"
    dimensions = ["Hours_Studied", "Attendance", "Sleep_Hours", "Previous_Scores", "Motivation_Level", "Exam_Score"]
    motivation_col = "Motivation_Level"

# Numeric range filtering sliders
st.write("**Filter Ranges:**")

col1, col2 = st.columns(2)

with col1:
    hours_range = st.slider(
        "Hours Studied",
        min_value=float(parallel_df["Hours_Studied"].min()),
        max_value=float(parallel_df["Hours_Studied"].max()),
        value=(float(parallel_df["Hours_Studied"].min()), float(parallel_df["Hours_Studied"].max())),
        step=0.1
    )
    sleep_range = st.slider(
        "Sleep Hours",
        min_value=float(parallel_df["Sleep_Hours"].min()),
        max_value=float(parallel_df["Sleep_Hours"].max()),
        value=(float(parallel_df["Sleep_Hours"].min()), float(parallel_df["Sleep_Hours"].max())),
        step=0.1
    )

with col2:
    attendance_range = st.slider(
        "Attendance",
        min_value=float(parallel_df["Attendance"].min()),
        max_value=float(parallel_df["Attendance"].max()),
        value=(float(parallel_df["Attendance"].min()), float(parallel_df["Attendance"].max())),
        step=0.1
    )
    motivation_range = st.slider(
        "Motivation Level",
        min_value=float(parallel_df[motivation_col].min()),
        max_value=float(parallel_df[motivation_col].max()),
        value=(float(parallel_df[motivation_col].min()), float(parallel_df[motivation_col].max())),
        step=0.1
    )

# Apply filters
parallel_df_filtered = parallel_df[
    (parallel_df["Hours_Studied"] >= hours_range[0]) & (parallel_df["Hours_Studied"] <= hours_range[1]) &
    (parallel_df["Attendance"] >= attendance_range[0]) & (parallel_df["Attendance"] <= attendance_range[1]) &
    (parallel_df["Sleep_Hours"] >= sleep_range[0]) & (parallel_df["Sleep_Hours"] <= sleep_range[1]) &
    (parallel_df[motivation_col] >= motivation_range[0]) & (parallel_df[motivation_col] <= motivation_range[1])
]

# DRAW PARALLEL COORDINATES
fig3 = px.parallel_coordinates(
    parallel_df_filtered,
    dimensions=dimensions,
    color=color_col,
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=parallel_df_filtered["Exam_Score"].mean() 
        if not parallel_df_filtered.empty 
        else parallel_df["Exam_Score"].mean()
)

st.plotly_chart(fig3, width='stretch')

# ----------------------------- 3D SCATTER PLOT ---------------------------------
st.subheader("3D Scatter Plot: Hours Studied - Previous Scores - Exam Score")

# Prepare dataframe by removing rows with missing values
df_scatter3d = df.dropna(subset=["Hours_Studied", "Previous_Scores", "Exam_Score"])

# --- Interaktif filtreleme ---
st.write("**Filter 3D Scatter Plot Ranges:**")
col1, col2, col3 = st.columns(3)

with col1:
    hours_range = st.slider(
        "Hours Studied",
        min_value=float(df_scatter3d["Hours_Studied"].min()),
        max_value=float(df_scatter3d["Hours_Studied"].max()),
        value=(float(df_scatter3d["Hours_Studied"].min()), float(df_scatter3d["Hours_Studied"].max())),
        step=0.1,
        key="hours_scatter"
    )

with col2:
    prev_range = st.slider(
        "Previous Scores",
        min_value=float(df_scatter3d["Previous_Scores"].min()),
        max_value=float(df_scatter3d["Previous_Scores"].max()),
        value=(float(df_scatter3d["Previous_Scores"].min()), float(df_scatter3d["Previous_Scores"].max())),
        step=0.1,
        key="prev_scatter"
    )

with col3:
    exam_range = st.slider(
        "Exam Score",
        min_value=float(df_scatter3d["Exam_Score"].min()),
        max_value=float(df_scatter3d["Exam_Score"].max()),
        value=(float(df_scatter3d["Exam_Score"].min()), float(df_scatter3d["Exam_Score"].max())),
        step=0.1,
        key="exam_scatter"
    )

# Apply filters
df_scatter3d_filtered = df_scatter3d[
    (df_scatter3d["Hours_Studied"] >= hours_range[0]) & (df_scatter3d["Hours_Studied"] <= hours_range[1]) &
    (df_scatter3d["Previous_Scores"] >= prev_range[0]) & (df_scatter3d["Previous_Scores"] <= prev_range[1]) &
    (df_scatter3d["Exam_Score"] >= exam_range[0]) & (df_scatter3d["Exam_Score"] <= exam_range[1])
]

# --- Renk seçimi ---
color_option = st.selectbox(
    "Color points by:",
    options=["Exam_Score", "Gender", "Motivation_Level"],
    index=0,
    key="scatter_color_option"
)

# Categorical renkler için özel skalalar
color_map = None
if color_option == "Gender":
    color_map = {"Male": "blue", "Female": "pink"}
    color_col = color_option
elif color_option == "Motivation_Level":
    color_map = {"Low": "red", "Medium": "yellow", "High": "green"}
    color_col = color_option
else:
    color_col = color_option  # Numeric için default scale

# Create an interactive 3D scatter plot using Plotly
fig_3d = px.scatter_3d(
    df_scatter3d_filtered,
    x="Hours_Studied",
    y="Previous_Scores",
    z="Exam_Score",
    color=color_col,
    size="Hours_Studied",
    opacity=0.75,
    hover_data=["Gender", "Motivation_Level"],
    color_discrete_map=color_map  # categorical için uygulanır, numeric ise ignore edilir
)

fig_3d.update_layout(
    title="3D Scatter Plot of Student Performance",
    scene=dict(
        xaxis_title="Hours Studied",
        yaxis_title="Previous Scores",
        zaxis_title="Exam Score",
    )
)

st.plotly_chart(fig_3d, width="stretch")


# -----------------------------  CORRELATION HEATMAP ---------------------------------
st.subheader(" CORRELATION HEATMAP")

all_numeric_cols = filtered_df.select_dtypes(include="number").columns.tolist()

selected_cols = st.multiselect(
    "Select columns to display in correlation matrix:",
    options=all_numeric_cols,
    default=all_numeric_cols
)

if len(selected_cols) < 2:
    st.warning("Please select at least two columns.")
else:
    corr = filtered_df[selected_cols].corr()

    threshold = st.slider(
        "Highlight correlations above threshold (absolute value):",
        0.0, 1.0, 0.5, 0.05
    )

    fig_heatmap = go.Figure()

    # Use a diverging color scale: red for negative, blue for positive
    # 'RdBu' starts with red at -1, blue at +1
    fig_heatmap.add_trace(go.Heatmap(
        z=corr.values,
        x=corr.columns,
        y=corr.index,
        colorscale="RdBu",
        zmin=-1, zmax=1,
        hovertemplate="<b>%{x} & %{y}</b><br>Correlation: %{z:.3f}<extra></extra>"
    ))

    shapes = []
    for i, row in enumerate(corr.values):
        for j, val in enumerate(row):
            if abs(val) >= threshold:
                shapes.append(dict(
                    type="rect",
                    x0=j - 0.5, x1=j + 0.5,
                    y0=i - 0.5, y1=i + 0.5,
                    line=dict(color="red", width=3)
                ))

    fig_heatmap.update_layout(
        title=f"Correlation Heatmap (Highlight ≥ {threshold})",
        width=800, height=700,
        shapes=shapes,
        xaxis=dict(side="bottom")
    )

    st.plotly_chart(fig_heatmap, width='stretch')

# ----------------------------- SANKEY DIAGRAM ---------------------------------
st.subheader(" SANKEY DIAGRAM")

filtered_df["Score_Level"] = pd.cut(
    filtered_df["Exam_Score"],
    bins=[0, 50, 75, 100],
    labels=["Low", "Medium", "High"]
)

if "Study_Hours_Group" not in filtered_df.columns:
    filtered_df["Study_Hours_Group"] = pd.cut(
        filtered_df["Hours_Studied"],
        bins=[0, 2, 5, 8, 12],
        labels=["0-2", "2-5", "5-8", "8-12"]
    )

motivation_filter = st.multiselect(
    "Filter Motivation Levels:",
    options=sorted(filtered_df["Motivation_Level"].unique()),
    default=sorted(filtered_df["Motivation_Level"].unique())
)

score_filter = st.multiselect(
    "Filter Score Levels:",
    options=["Low", "Medium", "High"],
    default=["Low", "Medium", "High"]
)

df_sankey = filtered_df[
    (filtered_df["Motivation_Level"].isin(motivation_filter)) &
    (filtered_df["Score_Level"].isin(score_filter))
]

labels = list(df_sankey["Study_Hours_Group"].cat.categories) + \
         sorted(df_sankey["Motivation_Level"].unique()) + \
         list(df_sankey["Score_Level"].cat.categories)

def idx(val):
    return labels.index(val)

source, target, value, hover_text = [], [], [], []
highlight_links = []

for s in df_sankey["Study_Hours_Group"].cat.categories:
    for m in sorted(df_sankey["Motivation_Level"].unique()):
        c = len(df_sankey[(df_sankey["Study_Hours_Group"] == s) &
                          (df_sankey["Motivation_Level"] == m)])
        if c > 0:
            source.append(idx(s))
            target.append(idx(m))
            value.append(c)
            hover_text.append(f"Study: {s}<br>Motivation: {m}<br>Count: {c}")
            highlight_links.append(m in motivation_filter)

for m in sorted(df_sankey["Motivation_Level"].unique()):
    for sc in df_sankey["Score_Level"].cat.categories:
        c = len(df_sankey[(df_sankey["Motivation_Level"] == m) &
                          (df_sankey["Score_Level"] == sc)])
        if c > 0:
            source.append(idx(m))
            target.append(idx(sc))
            value.append(c)
            hover_text.append(f"Motivation: {m}<br>Score: {sc}<br>Count: {c}")
            highlight_links.append(m in motivation_filter)

link_colors = [
    "rgba(0,100,200,0.8)" if h else "rgba(200,200,200,0.2)"
    for h in highlight_links
]

fig_sankey = go.Figure(data=[go.Sankey(
    node=dict(
        label=labels,
        pad=25,
        thickness=25,
        color="rgba(0,0,0,0.7)"
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
        color=link_colors,
        customdata=hover_text,
        hovertemplate="%{customdata}<extra></extra>"
    )
)])

fig_sankey.update_layout(
    title="Advanced Sankey Diagram: Study → Motivation → Score",
    font=dict(size=12)
)

st.plotly_chart(fig_sankey, width='stretch')

# ----------------------------- SPLIT VIOLIN PLOT ---------------------------------
st.subheader("Split Violin: Exam Score vs Motivation Level (Gender-Split Inside)")

mot_levels = df["Motivation_Level"].unique()
fig = go.Figure()

for mot in mot_levels:
    sub = df[df["Motivation_Level"] == mot]

    # Female → left side
    fig.add_trace(go.Violin(
        x=[mot] * len(sub[sub["Gender"] == "Female"]),
        y=sub[sub["Gender"] == "Female"]["Exam_Score"],
        name=f"{mot} - Female",
        side="negative",
        line_color="pink",
        fillcolor="pink",
        opacity=0.6,
        width=0.9,
        points=False
    ))

    # Male → right side
    fig.add_trace(go.Violin(
        x=[mot] * len(sub[sub["Gender"] == "Male"]),
        y=sub[sub["Gender"] == "Male"]["Exam_Score"],
        name=f"{mot} - Male",
        side="positive",
        line_color="blue",
        fillcolor="blue",
        opacity=0.6,
        width=0.9,
        points=False
    ))

fig.update_layout(
    title="Split Violin: Exam Score vs Motivation Level (Gender Comparison)",
    xaxis_title="Motivation Level",
    yaxis_title="Exam Score",
    violingap=0,
    violinmode="overlay",
    showlegend=True
)

st.plotly_chart(fig)

# ----------------------------- PIE CHART ---------------------------------
st.subheader("Pie Chart: Peer Influence Distribution")

# Sidebar filter for Gender
gender_options = df["Gender"].unique()
selected_genders = st.sidebar.multiselect(
    "Filter Pie Chart by Gender:",
    options=gender_options,
    default=list(gender_options)
)

# Filter dataframe by selected genders
df_pie = df[df["Gender"].isin(selected_genders)]

peer_counts = df_pie["Peer_Influence"].value_counts().reset_index()
peer_counts.columns = ["Peer_Influence", "Count"]

# color mapping
color_map = {
    "Negative": "red",
    "Neutral": "yellow",
    "Positive": "green"
}

# map colors (fallback = gray)
pie_colors = [
    color_map.get(cat, "lightgray") 
    for cat in peer_counts["Peer_Influence"]
]

fig_pie = px.pie(
    peer_counts,
    names="Peer_Influence",
    values="Count",
    title="Peer Influence Categories (%)",
    color="Peer_Influence",
    color_discrete_map=color_map
)

st.plotly_chart(fig_pie)

  #----------------------------- MARIMEKKO CHART ---------------------------------
st.subheader("Marimekko Chart: Distance vs. Extra Tutoring Sessions")

# 1. Filter out NaN values from Distance_from_Home (as requested: "I don't want unknown to show")
mekko_df = df.dropna(subset=['Distance_from_Home']).copy()

# 2. Update Grouping: Group 'Tutoring_Sessions' into '4+' for 4 and above
def categorize_sessions(session):
    try:
        session = int(session)
    except ValueError:
        return 'Other' 
        
    if session >= 0 and session <= 3:
        return str(session)
    else:
        # Group 4 and above as '4+'
        return '4+'

mekko_df['Extra Tutoring Sessions'] = mekko_df['Tutoring_Sessions'].apply(categorize_sessions)

# 3. Calculate X-Axis Proportions and Cumulative Positions
distance_counts = mekko_df['Distance_from_Home'].value_counts()
total_students = len(mekko_df)
distance_proportions = distance_counts / total_students
distance_percentages = (distance_proportions * 100).to_dict()

# Calculate cumulative widths and bar centers
cumulative_width = distance_proportions.cumsum()
x_starts = cumulative_width.shift(fill_value=0)
x_centers = x_starts + (distance_proportions / 2)

# Create the final DataFrame structure for plotting
plot_data = []

# Define the category order for correct stacking and legend order
session_order = ['0', '1', '2', '3', '4+']

# Color map for the sessions
color_map_sessions = {
    '0': '#800080', # Purple (No Sessions)
    '1': '#f04e38', # Orange-Red
    '2': '#ffc107', # Gold/Yellow
    '3': '#17a2b8', # Cyan
    '4+': '#28a745', # Green (High Sessions)
}


# 4. Calculate Conditional Percentages (Y-Heights) and create traces
contingency_table = pd.crosstab(
    mekko_df['Distance_from_Home'],
    mekko_df['Extra Tutoring Sessions']
)
# Calculate Row Percentages (Conditional Percentage - Y Height)
conditional_percentages = contingency_table.apply(lambda x: x / x.sum() * 100, axis=1)

# Sort conditional percentages by session order for proper stacking
conditional_percentages = conditional_percentages[session_order]

# Create custom data array for tooltips
# Ensure both arrays have the same shape and are ordered by distance_counts.index
distance_categories = distance_counts.index.values # This gives the category names (e.g., 'Far', 'Moderate')
distance_share_values = np.array([distance_percentages[cat] for cat in distance_categories]) 
customdata = np.stack((distance_categories, distance_share_values), axis=-1)
# --- End of Fix ---

# Iterate through session types to create stack layers
fig_mekko = go.Figure()
# This line requires the 'np' alias (numpy)
bottom_stack = np.zeros(len(distance_counts)) 

for session_category in session_order:
    heights = conditional_percentages[session_category].values
    
    # Create the proportional bar trace
    fig_mekko.add_trace(go.Bar(
        x=x_centers.values,
        y=heights,
        width=distance_proportions.values, # This controls the proportional width
        base=bottom_stack, # Stack on top of the previous category
        name=session_category,
        marker_color=color_map_sessions[session_category],
        text=heights,
        texttemplate='%{text:.1f}%',
        textposition='inside',
        hoverinfo='name+y',
        # Reference customdata using customdata[0] (Category Name) and customdata[1] (Share %)
        hovertemplate=f"Distance: %{{customdata[0]}}<br>Share: %{{customdata[1]:.1f}}%<br>Sessions: {session_category}<br>Conditional %: %{{y:.1f}}%<extra></extra>",
        customdata=customdata, # Use the correctly shaped customdata array
    ))
    # Update the bottom_stack for the next layer
    bottom_stack += heights


# 5. Format the Mekko Chart
# Set X-axis to display categories centered in their proportional width
fig_mekko.update_layout(
    barmode='stack',
    title='Marimekko Chart: Extra Tutoring Sessions Distribution by Distance from Home',
    xaxis=dict(
        tickvals=x_centers.values,
        ticktext=[f"{cat} ({distance_percentages[cat]:.1f}%)" for cat in distance_counts.index],
        showgrid=False,
        title='Distance from Home Category (Bar Width is Total Share %)'
    ),
    yaxis=dict(
        range=[0, 100],
        title='Extra Tutoring Sessions (Y-Axis, Conditional %)',
        ticksuffix="%"
    ),
    plot_bgcolor='white',
    legend_title_text='Sessions Count',
)

st.plotly_chart(fig_mekko)