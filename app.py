import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

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

# Filtre uygula
filtered_df = df[df["School_Type"].isin(school_option)]

# ----------------------------- BOX PLOT ---------------------------------
st.subheader("Box Plot: Exam Score by Gender")

fig = px.box(
    filtered_df,
    x="Gender",
    y="Exam_Score",
    color="Gender",
    points="all",
    hover_data=["Hours_Studied", "Attendance", "Parental_Involvement"]
)

fig.update_layout(
    title="Exam Score Distribution by Gender",
    xaxis_title="Gender",
    yaxis_title="Exam Score",
    boxmode="group"
)

st.plotly_chart(fig)

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

num_cols = ["Hours_Studied", "Attendance", "Sleep_Hours",
            "Previous_Scores", "Motivation_Level", "Exam_Score"]

fig3 = px.parallel_coordinates(
    df,
    dimensions=num_cols,
    color="Exam_Score",
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=df["Exam_Score"].mean()
)
st.plotly_chart(fig3)

# ----------------------------- SCATTER PLOT ---------------------------------
st.subheader("Scatter Plot: Hours Studied vs Exam Score")

fig4 = px.scatter(
    df,
    x="Hours_Studied",
    y="Exam_Score",
    color="Gender",
    hover_data=["Attendance", "Sleep_Hours"],
    title="Study Hours vs Exam Score"
)
st.plotly_chart(fig4)

# ----------------------------- CORRELATION HEATMAP ---------------------------------
st.subheader("Correlation Heatmap")

fig5, ax = plt.subplots(figsize=(8, 6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="YlGnBu", ax=ax)
st.pyplot(fig5)

# ----------------------------- SANKEY DIAGRAM ---------------------------------
st.subheader("Sankey Diagram: Study Hours → Motivation → Exam Score Level")

# Exam Score kategorik hale getir
df["Score_Level"] = pd.cut(
    df["Exam_Score"],
    bins=[0, 50, 75, 100],
    labels=["Low", "Medium", "High"]
)

# Eğer dataset'te Study_Hours_Group yoksa oluşturalım
if "Study_Hours_Group" not in df.columns:
    df["Study_Hours_Group"] = pd.cut(
        df["Hours_Studied"],
        bins=[0, 2, 5, 8, 12],
        labels=["0-2", "2-5", "5-8", "8-12"]
    )

labels = list(df["Study_Hours_Group"].unique()) + \
         list(df["Motivation_Level"].unique()) + \
         list(df["Score_Level"].unique())

# Etiket index fonksiyonu
def idx(val):
    return labels.index(val)

source = []
target = []
value = []

# Study Hours → Motivation bağlantıları
for s in df["Study_Hours_Group"].unique():
    for m in df["Motivation_Level"].unique():
        c = len(df[(df["Study_Hours_Group"] == s) & (df["Motivation_Level"] == m)])
        if c > 0:
            source.append(idx(s))
            target.append(idx(m))
            value.append(c)

# Motivation → Score Level bağlantıları
for m in df["Motivation_Level"].unique():
    for sc in df["Score_Level"].unique():
        c = len(df[(df["Motivation_Level"] == m) & (df["Score_Level"] == sc)])
        if c > 0:
            source.append(idx(m))
            target.append(idx(sc))
            value.append(c)

# Sankey çizimi
fig6 = go.Figure(data=[go.Sankey(
    node=dict(label=labels),
    link=dict(source=source, target=target, value=value)
)])

fig6.update_layout(title="Sankey Diagram: Study → Motivation → Score Level")
st.plotly_chart(fig6)
