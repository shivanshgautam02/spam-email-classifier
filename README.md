# Spam Detection Web App

## Overview
This project is designed to classify emails as spam or not spam using machine learning models. It utilizes the SpamAssassin Public Corpus dataset, which must be downloaded and placed inside the `data/` folder. The web application is built using Streamlit, providing an easy-to-use interface for spam detection.

## Setup Instructions

1. **Download the Dataset:**
   - Download the SpamAssassin dataset from [SpamAssassin Public Corpus](https://spamassassin.apache.org/old/publiccorpus/).
   - Place the downloaded files inside the `data/` folder.
   - Extract the emails using the provided scripts (`extract_from_bz2.py` or `extracting_all.py`).

2. **Extracting Data:**
   - `extract_from_bz2.py`: Extracts specific `.tar.bz2` files.
   - `extracting_all.py`: Extracts all `.tar.bz2` files inside the `data/` folder.

3. **Train the Spam Classification Model:**
   - Three Jupyter notebooks are available for training:
     - `notebook.ipynb` (Naïve Bayes model, `spam_classifier.pkl`)
     - `notebook2.ipynb` (Logistic Regression, `spam_classifier_logistic.pkl`)
     - `notebook3.ipynb` (Logistic Regression with improved text preprocessing, `spam_classifier_logistic.pkl`)
   - Currently, **`notebook3.ipynb` is recommended** for better results.

4. **Run the Web App:**
   - The Streamlit web app now uses `spam_classifier_logistic.pkl` (Logistic Regression model).
   - Ensure `spam_classifier_logistic.pkl` is in the project directory.
   - Run the Streamlit app:
     ```bash
     streamlit run app.py
     ```

## Project Structure
```
/project-root
│── data/
│   ├── 20021010_easy_ham.tar.bz2
│   ├── 20030228_spam.tar.bz2
│   ├── extracted_emails/
│── notebooks/
│   ├── notebook.ipynb
│   ├── notebook2.ipynb
│   ├── notebook3.ipynb
│── src/
│   ├── app.py  # Streamlit web app
│   ├── extract_from_bz2.py  # Extracts specific files
│   ├── extracting_all.py  # Extracts all files
│── spam_classifier.pkl  # Naïve Bayes model (legacy)
│── spam_classifier_logistic.pkl  # Recommended model
```

## Dependencies
Ensure you have the following dependencies installed:
```bash
pip install -r requirements.txt
```
The `requirements.txt` file includes essential libraries like:
- `streamlit`
- `matplotlib`
- `pandas`
- `scikit-learn`

## Conclusion
This project provides an efficient spam detection system using machine learning. With multiple models available, the Logistic Regression model (`notebook3.ipynb`) is the most effective. The Streamlit web app offers a user-friendly interface for spam classification.

