# Pan-Cancer Immune Biomarker Discovery

This project analyzes TCGA gene expression and survival data using the cBioPortal API to identify immune biomarkers associated with patient outcomes.

## Project Structure

```
.
├── notebooks/
│   └── immune_biomarker_tcga_with_survival.ipynb  # Main analysis notebook
├── requirements.txt                               # Python dependencies
└── README.md                                      # This file
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Open the Jupyter notebook:
```bash
jupyter notebook notebooks/immune_biomarker_tcga_with_survival.ipynb
```

2. Run the cells in sequence to:
   - Connect to cBioPortal API
   - Download TCGA BRCA sample data
   - Analyze gene expression
   - Perform survival analysis

## Dependencies

- Python 3.8+
- pandas
- matplotlib
- seaborn
- lifelines
- scikit-learn
- requests

## License

MIT License
