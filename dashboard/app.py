import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import KaplanMeierFitter
import streamlit as st

st.set_page_config(page_title="TCGA Immune Dashboard", layout="wide")
st.title("🧬 TCGA Immune Biomarker Dashboard")

# Sidebar - Upload Files
st.sidebar.header("Upload Your Data")
expr_file = st.sidebar.file_uploader("Upload gene expression file (CSV)", type="csv")
subtype_file = st.sidebar.file_uploader("Upload immune subtype file (CSV)", type="csv")
clinical_file = st.sidebar.file_uploader("Upload clinical file (CSV)", type="csv")

if expr_file and subtype_file and clinical_file:
    expr_df = pd.read_csv(expr_file, index_col=0)
    subtypes = pd.read_csv(subtype_file)
    clinical = pd.read_csv(clinical_file, index_col=0)

    # Merge all data
    expr_df = expr_df.join(subtypes.set_index("SampleID"), on="sampleId")
    expr_df['patientId'] = expr_df.index.str.replace('-Tumor', '', regex=False).str.slice(0, 12)
    expr_df = expr_df.join(clinical, on='patientId')
    expr_df = expr_df.dropna(subset=['ImmuneSubtype', 'OS_Time', 'OS_Status'])

    gene_choice = st.sidebar.selectbox("Select gene to visualize", expr_df.columns[:-4])

    st.subheader(f"Gene Expression of {gene_choice} by Immune Subtype")
    fig, ax = plt.subplots()
    sns.boxplot(data=expr_df, x="ImmuneSubtype", y=gene_choice, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader("Survival Analysis")
    median_expr = expr_df[gene_choice].median()
    high = expr_df[expr_df[gene_choice] > median_expr]
    low = expr_df[expr_df[gene_choice] <= median_expr]

    kmf = KaplanMeierFitter()
    fig2, ax2 = plt.subplots()
    kmf.fit(high['OS_Time'], high['OS_Status'], label=f"High {gene_choice}")
    kmf.plot(ax=ax2)
    kmf.fit(low['OS_Time'], low['OS_Status'], label=f"Low {gene_choice}")
    kmf.plot(ax=ax2)
    plt.title(f"Survival by {gene_choice} Expression")
    st.pyplot(fig2)

else:
    st.info("Upload expression, subtype, and clinical CSV files to begin.")
