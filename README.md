# CVSS Score Prediction from CVE Descriptions

This project aims to predict the severity of vulnerabilities, measured by the CVSS v3 base score, based on their descriptions using machine learning. The dataset is sourced from the National Vulnerability Database (NVD) and includes CVEs from 2002 to 2024.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- Install dependencies from `requirements.txt` by running:

```bash
pip install -r requirements.txt
```

Dependencies include:

- `scikit-learn`
- `pandas`
- `matplotlib`
- `seaborn`
- `wordcloud`
- `numpy`

## Running the Python Script

To run the Python script for data preprocessing, feature extraction, and model training, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/davidhwilliams/CSCA-5622-ML-I-Final/tree/main/data.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd CSCA-5622-ML-I-Final
   ```

3. Run the Python script:

   ```python
   python CveDataMirror.py
   ```

### Alternate Data Collection

- [NVD JSON Data Feeds](https://nvd.nist.gov/vuln/data-feeds)

## Running the Jupyter Notebook

To interactively explore the data and train models, you can use the provided Jupyter notebook. Follow these steps:

1. Start Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

2. Open the notebook from the notebooks/ directory:

   ```
   final.ipynb
   ```

This notebook includes:

- Exploratory Data Analysis (EDA) on CVE descriptions.
- Feature extraction using TF-IDF.
- Training and evaluating a Random Forest Regressor.
- Hyperparameter tuning using GridSearchCV.
- Model performance visualization.

### Results

- Mean Squared Error (MSE): Measures the average squared difference between actual and predicted CVSS v3 base scores.
- R-squared: Indicates how well the model explains the variance in the CVSS scores.
- Feature Importance: Identifies the most predictive terms in the CVE descriptions.

## Future Improvements

- Use GPU-based training to reduce computation time.
- Add more data, especially for low and high-severity vulnerabilities.
- Experiment with different models such as gradient boosting or neural networks.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
