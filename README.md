# Student Performance Dashboard

## Project Description

This project is an interactive web-based dashboard application built with Streamlit for visualizing and analyzing student performance data. The dashboard provides comprehensive insights into various factors affecting student academic performance through multiple interactive visualizations. 

### Purpose and Objectives

The primary goal of this dashboard is to enable educators, administrators, and researchers to:
- Explore relationships between different variables affecting student performance
- Identify patterns and correlations in student data
- Analyze the impact of factors such as study hours, attendance, teacher quality, parental involvement, and exam scores
- Make data-driven decisions to improve educational outcomes

### Key Features

The application features 9 different types of advanced visualizations:
1. **Box Plot**: Statistical distribution analysis
2. **Treemap**: Hierarchical data visualization
3. **Parallel Coordinates**: Multi-variable relationship analysis
4. **3D Scatter Plot**: Three-dimensional data exploration
5. **Correlation Heatmap**: Variable correlation analysis
6. **Sankey Diagram**: Flow-based relationship visualization
7. **Split Violin Plot**: Distribution comparison by categories
8. **Pie Chart**: Categorical distribution analysis
9. **Marimekko Chart**: Proportional relationship visualization

Each visualization includes interactive filtering capabilities, allowing users to explore the data from different perspectives. The dashboard supports real-time data filtering, outlier detection and removal, and customizable visualization parameters.

### Technical Implementation

The dashboard is built using Python and Streamlit framework, leveraging Plotly for interactive visualizations, Pandas for data manipulation, and NumPy for numerical computations. The application processes CSV data files and provides a user-friendly web interface accessible through any modern web browser.

## Dataset Details

### Dataset Information

- **File Name**: `student_performance.csv`
- **Location**: `data/student_performance.csv`
- **Format**: CSV (Comma-Separated Values)
- **Encoding**: UTF-8
- **Delimiter**: Comma (,)
- **Size**: Contains multiple student records with 20 features
- **Missing Values**: Some features may contain missing values (handled in preprocessing)

### Dataset Features

The dataset includes 20 features that capture various aspects of student performance and environmental factors:

#### Numeric Features

1. **Hours_Studied** (Numeric, Continuous): Number of hours studied per week
   - Range: Typically 0-40 hours
   - Purpose: Measures study time investment

2. **Attendance** (Numeric, Continuous): Attendance rate as a percentage
   - Range: 0-100%
   - Purpose: Measures class attendance consistency

3. **Sleep_Hours** (Numeric, Continuous): Average hours of sleep per night
   - Range: Typically 4-12 hours
   - Purpose: Measures sleep quality and quantity

4. **Previous_Scores** (Numeric, Continuous): Previous academic scores
   - Range: Typically 0-100
   - Purpose: Baseline academic performance indicator

5. **Tutoring_Sessions** (Numeric, Discrete): Number of extra tutoring sessions attended
   - Range: Typically 0-10+ sessions
   - Purpose: Measures additional academic support

6. **Physical_Activity** (Numeric, Continuous): Hours of physical activity per week
   - Range: Typically 0-10+ hours
   - Purpose: Measures physical activity level

7. **Exam_Score** (Numeric, Continuous): Final exam score (target variable)
   - Range: 0-100
   - Purpose: Primary outcome variable for analysis

#### Categorical Features

8. **Parental_Involvement** (Categorical, Ordinal): Level of parental involvement
   - Categories: Low, Medium, High
   - Purpose: Measures family support level

9. **Access_to_Resources** (Categorical, Ordinal): Access to educational resources
   - Categories: Low, Medium, High
   - Purpose: Measures resource availability

10. **Extracurricular_Activities** (Categorical, Binary): Participation in extracurricular activities
    - Categories: Yes, No
    - Purpose: Measures engagement in non-academic activities

11. **Motivation_Level** (Categorical, Ordinal): Student motivation level
    - Categories: Low, Medium, High
    - Purpose: Measures intrinsic motivation

12. **Internet_Access** (Categorical, Binary): Access to internet
    - Categories: Yes, No
    - Purpose: Measures digital resource access

13. **Family_Income** (Categorical, Ordinal): Family income level
    - Categories: Low, Medium, High
    - Purpose: Measures socioeconomic status

14. **Teacher_Quality** (Categorical, Ordinal): Quality of teacher
    - Categories: Low, Medium, High
    - Purpose: Measures teaching quality

15. **School_Type** (Categorical, Nominal): Type of school
    - Categories: Public, Private
    - Purpose: Categorizes school type

16. **Peer_Influence** (Categorical, Ordinal): Influence of peers
    - Categories: Positive, Neutral, Negative
    - Purpose: Measures peer group impact

17. **Learning_Disabilities** (Categorical, Binary): Presence of learning disabilities
    - Categories: Yes, No
    - Purpose: Identifies special needs

18. **Parental_Education_Level** (Categorical, Ordinal): Education level of parents
    - Categories: High School, College, Postgraduate
    - Purpose: Measures parental education background

19. **Distance_from_Home** (Categorical, Ordinal): Distance from home to school
    - Categories: Near, Moderate, Far
    - Purpose: Measures commute distance

20. **Gender** (Categorical, Nominal): Student gender
    - Categories: Male, Female
    - Purpose: Demographic classification

### Dataset Source 

https://www.kaggle.com/datasets/ayeshaseherr/student-performance

### Data Preprocessing

The dataset undergoes the following preprocessing steps:
- Missing value handling for Distance_from_Home in Marimekko Chart
- Data type conversion for categorical variables
- Outlier detection and removal using IQR method (optional, user-controlled)
- Data aggregation for hierarchical visualizations (Treemap, Sankey)
- Binning operations for continuous variables (Score_Level, Study_Hours_Group)

## Setup Instructions

### Prerequisites

Before installing the project, ensure you have the following software installed:

- **Python 3.7 or higher**: Required for running the application
  - Check version: `python --version` or `python3 --version`
  - Download from: https://www.python.org/downloads/
  
- **pip (Python package manager)**: Usually comes with Python installation
  - Check installation: `pip --version` or `pip3 --version`
  
- **Git (optional)**: For cloning the repository
  - Check installation: `git --version`
  - Download from: https://git-scm.com/downloads

### Installation Steps

#### Step 1: Clone or Download the Project

**Option A: Using Git (Recommended)**
```bash
git clone https://github.com/zeeynepkan/student-performance-dashboard.git
cd student-performance-dashboard

```

**Option B: Manual Download**
1. Download the project as a ZIP file
2. Extract the files to your desired location
3. Navigate to the project directory using terminal/command prompt

#### Step 2: Create a Virtual Environment (Highly Recommended)

Creating a virtual environment helps isolate project dependencies and prevents conflicts with other Python projects.

**Windows:**
```bash
python -m venv venv
```

**Linux/Mac:**
```bash
python3 -m venv venv
```

#### Step 3: Activate the Virtual Environment

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

After activation, you should see `(venv)` prefix in your terminal prompt.

#### Step 4: Install Required Packages

Install all necessary dependencies from the requirements file:

```bash
pip install -r requirements.txt
```

This command will install the following packages with their specific versions:
- **streamlit** (1.51.0): Web application framework for building the dashboard
- **pandas** (2.3.3): Data manipulation and analysis
- **plotly** (6.5.0): Interactive visualizations and charts
- **seaborn** (0.13.2): Statistical data visualization
- **matplotlib** (3.10.7): Additional plotting capabilities
- **altair** (5.5.0): Declarative statistical visualization
- **numpy** (2.3.5): Numerical computations
- **protobuf** (6.33.1): Protocol buffer support

**Installation Time**: The installation process typically takes 2-5 minutes depending on your internet connection and system specifications.

#### Step 5: Verify Dataset File

Before running the application, ensure that the dataset file exists:

1. Check if `data/` directory exists in the project root
2. Verify that `student_performance.csv` is present in the `data/` directory
3. Ensure the file is not corrupted and contains valid CSV data

**Verification Command:**
```bash
# Windows
dir data\student_performance.csv

# Linux/Mac
ls data/student_performance.csv
```

### Running the Application

#### Step 1: Start the Streamlit Server

Make sure you are in the project root directory and your virtual environment is activated, then run:

```bash
streamlit run app.py
```

**Alternative Command:**
```bash
python -m streamlit run app.py
```

#### Step 2: Access the Dashboard

After running the command, Streamlit will:
1. Start a local web server
2. Automatically open your default web browser
3. Navigate to `http://localhost:8501`

If the browser doesn't open automatically:
- Manually navigate to `http://localhost:8501` in your web browser
- Check the terminal for the exact URL (Streamlit may use a different port if 8501 is occupied)

#### Step 3: Using the Dashboard

**Navigation:**
- Use the **sidebar** on the left to filter data by school type and gender
- Scroll down to view all visualizations
- Each visualization has its own interactive controls

**Interactivity Features:**
- **Hover**: Hover over data points to see detailed information
- **Zoom**: Use mouse wheel or zoom controls to zoom in/out on charts
- **Filter**: Use sliders, dropdowns, and checkboxes to filter data
- **Select**: Click on legend items to show/hide data series

**Key Interactions:**
- **Box Plot**: Hover to see individual data points and statistics
- **Parallel Coordinates**: Drag axes to reorder, use outlier removal checkbox
- **3D Scatter Plot**: Rotate, zoom, and pan the 3D view
- **Correlation Heatmap**: Adjust threshold slider to highlight correlations
- **Sankey Diagram**: Use filters to explore different flow paths
- **Pie Chart**: Click on segments to isolate categories

## Project Structure

```
student-performance-dashboard/
│
├── app.py                          # Main Streamlit application file
│                                    # Contains all visualization code and UI logic
│
├── requirements.txt                 # Python package dependencies
│                                    # Lists all required packages with versions
│
├── README.md                        # Project documentation (this file)
│                                    # Complete project documentation and setup guide
│
└── data/
    └── student_performance.csv      # Student performance dataset
                                      # CSV file containing student data with 20 features
```

### File Descriptions

- **app.py**: The main application file containing all Streamlit code, data loading, preprocessing, and visualization implementations. This file is approximately 605 lines and includes all 9 visualization types.

- **requirements.txt**: Text file listing all Python package dependencies with their specific versions. Used by pip to install all required packages.

- **README.md**: Comprehensive documentation file providing project description, setup instructions, dataset details, and team member contributions.

- **data/student_performance.csv**: The dataset file containing student performance records. This file should not be modified unless you want to analyze different data.

## Team Member Contributions

The following section provides a detailed breakdown of each team member's contributions to this project. Each member's specific responsibilities and implemented features are clearly outlined.



#### **[ZEYNEP KAN]**

**Data Management and Initial Visualizations:**
- **Data Preprocessing and Cleaning**: 
  - Performed initial data exploration and analysis
  - Identified data quality issues and missing values
  - Implemented data cleaning procedures
  - Handled data type conversions and categorical variable encoding

- **Dataset Analysis and Feature Exploration**:
  - Conducted exploratory data analysis (EDA)
  - Analyzed feature distributions and relationships
  - Identified key variables for visualization
  - Documented dataset characteristics and statistics

- **Box Plot Visualization Implementation**:
  - Designed and implemented the Box Plot showing Teacher Quality vs Attendance Rate
  - Configured Plotly box plot with proper category ordering (Low, Medium, High)
  - Added hover data functionality showing Hours_Studied, Exam_Score, and Parental_Involvement
  - Implemented color coding based on Teacher Quality levels
  - Created interactive filtering integration with sidebar filters

- **Treemap Visualization Implementation**:
  - Designed hierarchical treemap visualization (School Type → Parental Education → Gender)
  - Implemented data aggregation using groupby operations
  - Configured treemap with proper path hierarchy
  - Set up color scale (Blues) based on Exam_Score values
  - Added hover data for detailed information display

- **Parallel Coordinates Chart Implementation**:
  - Designed multi-variable parallel coordinates visualization
  - Implemented dimension selection (Hours_Studied, Attendance, Sleep_Hours, Previous_Scores, Motivation_Level, Exam_Score)
  - Created categorical to numeric conversion for Motivation_Level
  - Implemented color coding using Exam_Score with diverging color scale (Tealrose)
  - Added interactive range sliders for filtering (Hours Studied, Attendance, Sleep Hours, Motivation Level)

- **Streamlit Application Layout and Sidebar Structure**:
  - Designed the overall application layout and structure
  - Implemented sidebar filtering components
  - Created school type multiselect filter in sidebar
  - Established the main application flow and organization
  - Set up the title and header structure

- **Visualization Design and Layout**:
  - Contributed to overall visualization design principles
  - Ensured consistent styling and layout across visualizations
  - Worked on user interface aesthetics and usability

---

#### **[SUDENUR ŞEKEROĞLU]**

**Advanced Visualizations and Data Analysis:**

- **Sankey Diagram Implementation**:
  - Designed and implemented the Sankey flow diagram showing Study Hours → Motivation → Score relationships
  - Created data binning operations for Score_Level (Low: 0-50, Medium: 50-75, High: 75-100) and Study_Hours_Group (0-2, 2-5, 5-8, 8-12)
  - Implemented node and link generation logic for the flow diagram
  - Created interactive filtering for Motivation Levels and Score Levels using multiselect widgets
  - Implemented link highlighting based on selected filters
  - Added custom hover templates showing study hours, motivation, and score information
  - Configured node styling (padding, thickness, colors) and link colors

- **3D Scatter Plot Implementation**:
  - Designed three-dimensional scatter plot showing relationship between Hours_Studied, Previous_Scores, and Exam_Score
  - Implemented data cleaning by removing rows with missing values in required columns
  - Created interactive range sliders for all three dimensions (Hours Studied, Previous Scores, Exam Score)
  - Implemented dynamic color coding with selectbox allowing choice between Exam_Score, Gender, and Motivation_Level
  - Created color mapping for categorical variables (Gender: blue/pink, Motivation_Level: red/yellow/green)
  - Added size encoding based on Hours_Studied
  - Configured 3D scene with proper axis labels and titles
  - Implemented hover data showing Gender and Motivation_Level

- **Correlation Heatmap Graph Implementation**:
  - Designed correlation matrix heatmap visualization
  - Implemented dynamic column selection using multiselect widget
  - Created correlation calculation using pandas corr() method
  - Implemented threshold-based highlighting using slider (0.0 to 1.0)
  - Added rectangular shapes to highlight correlations above threshold
  - Configured diverging color scale (RdBu) for positive (blue) and negative (red) correlations
  - Set proper z-axis limits (-1 to 1) for correlation values
  - Created custom hover templates showing variable pairs and correlation values
  - Added validation to ensure at least two columns are selected

- **Outlier Detection and Removal Functionality (IQR Method)**:
  - Implemented Interquartile Range (IQR) method for outlier detection
  - Created `remove_outliers_iqr()` function that processes multiple numeric columns
  - Calculated Q1 (25th percentile), Q3 (75th percentile), and IQR for each column
  - Implemented outlier removal using bounds: lower = Q1 - 1.5*IQR, upper = Q3 + 1.5*IQR
  - Integrated outlier removal checkbox in Parallel Coordinates visualization
  - Applied outlier removal to columns: Hours_Studied, Attendance, Sleep_Hours, Previous_Scores, Exam_Score
  - Ensured proper data type checking before applying IQR method

- **Interactive Filtering Implementation**:
  - Implemented range slider filters for Parallel Coordinates (Hours Studied, Attendance, Sleep Hours, Motivation Level)
  - Created filter application logic combining multiple conditions
  - Implemented multiselect filters for Sankey Diagram (Motivation Levels, Score Levels)
  - Added gender-based filtering for Pie Chart in sidebar
  - Ensured filters work correctly with filtered_df from sidebar
  - Implemented proper data filtering chains maintaining data consistency

- **Visualization Design and Layout**:
  - Contributed to overall visualization design and styling
  - Ensured interactive elements are user-friendly and intuitive
  - Worked on color schemes and visual aesthetics

- **README.md Documentation**:
  - Completed comprehensive README.md documentation
  - Documented all project features and setup instructions
  - Created detailed dataset description
  - Wrote troubleshooting section
  - Documented team member contributions

---

#### **[SONGÜL MEŞALE]**

**Statistical Visualizations and User Interface:**

- **Split Violin Plot Implementation**:
  - Designed split violin plot for gender-based comparison of Exam Score vs Motivation Level
  - Implemented separate violin plots for each motivation level (Low, Medium, High)
  - Created gender-split visualization with Female on negative side (left, pink) and Male on positive side (right, blue)
  - Implemented data filtering by motivation level and gender
  - Configured violin plot styling (opacity, width, line colors, fill colors)
  - Set up proper layout with violingap=0 and violinmode="overlay"
  - Added legend showing motivation level and gender combinations
  - Configured axis titles and chart title

- **Pie Chart Implementation**:
  - Designed pie chart for Peer Influence Distribution
  - Implemented data aggregation using value_counts() to count peer influence categories
  - Created color mapping: Negative (red), Neutral (yellow), Positive (green)
  - Integrated sidebar gender filter for pie chart data
  - Implemented data filtering by selected genders using multiselect widget
  - Configured Plotly pie chart with proper labels and values
  - Added percentage display and hover information
  - Set up fallback color (lightgray) for unexpected categories

- **Marimekko Chart Implementation**:
  - Designed complex Marimekko (Mosaic) chart showing Distance from Home vs Extra Tutoring Sessions
  - Implemented data cleaning by removing NaN values from Distance_from_Home column
  - Created session categorization function grouping 0-3 sessions individually and 4+ as a group
  - Calculated X-axis proportions (distance category shares) and cumulative positions
  - Implemented conditional percentages (Y-axis heights) using crosstab and row percentage calculations
  - Created stacked bar traces with proportional widths based on distance category shares
  - Implemented color mapping for session categories (Purple, Orange-Red, Gold, Cyan, Green)
  - Added text labels showing conditional percentages inside bars
  - Configured custom hover templates showing distance category, share percentage, sessions, and conditional percentage
  - Set up proper X-axis with category labels and share percentages
  - Configured Y-axis with 0-100% range and percentage suffix
  - Implemented proper stacking order for session categories

- **Streamlit Application Layout and Sidebar Structure**:
  - Contributed to overall application layout design
  - Worked on sidebar structure and organization
  - Implemented gender filter in sidebar for Pie Chart
  - Ensured consistent UI elements across the application

- **Report Preparation**:
  - Prepared project report documentation
  - Organized project findings and analysis results
  - Documented visualization insights and interpretations

- **User Interface Development**:
  - Contributed to user interface design and development
  - Ensured user-friendly interaction elements
  - Worked on visual consistency and aesthetics
  - Implemented responsive design considerations

---

### Summary of Contributions by Task Type

**Data Preprocessing:**
- ZEYNEP KAN: Initial data cleaning, exploration, and preprocessing

**Visualization Implementation:**
- ZEYNEP KAN: Box Plot, Treemap, Parallel Coordinates
- SUDENUR ŞEKEROĞLU: Sankey Diagram, 3D Scatter Plot, Correlation Heatmap
- SONGÜL MEŞALE: Split Violin Plot, Pie Chart, Marimekko Chart

**Interactive Features:**
- ZEYNEP KAN: Parallel Coordinates range sliders, sidebar school type filter
- SUDENUR ŞEKEROĞLU: Outlier removal functionality, Sankey filters, 3D scatter filters, correlation threshold slider
- SONGÜL MEŞALE: Pie chart gender filter

**Application Structure:**
- ZEYNEP KAN: Initial application layout and sidebar structure


**Documentation:**
- SUDENUR ŞEKEROĞLU: Complete README.md documentation
- SONGÜL MEŞALE: Report preparation

## Visualizations

The dashboard includes the following 9 comprehensive visualizations, each designed to provide unique insights into student performance data:

### 1. Box Plot: Teacher Quality vs Attendance Rate
- **Purpose**: Analyze the distribution of attendance rates across different teacher quality levels
- **Features**: Color-coded by teacher quality, shows all data points, hover information
- **Implementation**: ZEYNEP KAN

### 2. Treemap: School Type → Parental Education → Gender
- **Purpose**: Visualize hierarchical relationships and average exam scores
- **Features**: Three-level hierarchy, color intensity based on exam scores
- **Implementation**: ZEYNEP KAN

### 3. Parallel Coordinates: Multi-variable Analysis
- **Purpose**: Explore relationships between multiple variables simultaneously
- **Features**: Outlier removal option, interactive range filters, color-coded by exam score
- **Implementation**: ZEYNEP KAN 

### 4. 3D Scatter Plot: Study Hours - Previous Scores - Exam Score
- **Purpose**: Three-dimensional analysis of key performance factors
- **Features**: Dynamic color coding, size encoding, interactive 3D rotation, range filters
- **Implementation**: SUDENUR ŞEKEROĞLU

### 5. Correlation Heatmap: Variable Relationships
- **Purpose**: Identify correlations between numerical variables
- **Features**: Customizable column selection, threshold-based highlighting, diverging color scale
- **Implementation**: SUDENUR ŞEKEROĞLU

### 6. Sankey Diagram: Study Hours → Motivation → Score
- **Purpose**: Visualize flow relationships between study patterns, motivation, and outcomes
- **Features**: Interactive filtering, link highlighting, custom hover information
- **Implementation**: SUDENUR ŞEKEROĞLU

### 7. Split Violin Plot: Exam Score vs Motivation Level (Gender Comparison)
- **Purpose**: Compare exam score distributions by motivation level, split by gender
- **Features**: Side-by-side gender comparison, motivation level grouping
- **Implementation**: SONGÜL MEŞALE

### 8. Pie Chart: Peer Influence Distribution
- **Purpose**: Show distribution of peer influence categories
- **Features**: Gender-based filtering, color-coded categories
- **Implementation**: SONGÜL MEŞALE

### 9. Marimekko Chart: Distance vs Extra Tutoring Sessions
- **Purpose**: Analyze proportional relationships between distance and tutoring sessions
- **Features**: Proportional bar widths, conditional percentages, session categorization
- **Implementation**: SONGÜL MEŞALE
