<div align="center">

# 🛡️ AI-Driven Phishing Email Detection Using NLP

### An End-to-End Machine Learning & Natural Language Processing System for Intelligent Spam and Phishing Message Detection

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![NLTK](https://img.shields.io/badge/NLTK-NLP-154F3C?style=for-the-badge)](https://www.nltk.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**NLP • Machine Learning • Feature Engineering • Cybersecurity • Streamlit**

</div>

---

## 📌 Overview

**AI-Driven Phishing Email Detection Using NLP** is an end-to-end Natural Language Processing and Machine Learning project designed to classify incoming text messages as **legitimate (Ham)** or **spam/phishing-like content**.

The project implements a complete machine learning workflow, starting from raw data collection and exploratory analysis to NLP preprocessing, TF-IDF vectorization, metadata feature engineering, multi-model training, performance evaluation, prediction, and interactive deployment using Streamlit.

Six machine learning algorithms were trained and compared, with the **Neural Network (MLPClassifier)** achieving the best overall performance with an accuracy of approximately **99.03%**.

> **Note:** The current version is trained on an SMS Spam Collection dataset. Therefore, the deployed classifier primarily performs spam/ham text classification. Extending the system with dedicated phishing email datasets, email headers, sender domains, and URL intelligence is planned for future versions.

---

## 🎯 Project Objective

The primary objective of this project is to develop an intelligent text classification pipeline capable of identifying potentially malicious or unsolicited messages using NLP and Machine Learning.

The project focuses on:

- Cleaning and preprocessing raw textual data
- Understanding patterns in legitimate and spam messages
- Converting textual information into numerical representations
- Engineering additional structural metadata features
- Training and comparing multiple classification algorithms
- Evaluating models using multiple performance metrics
- Building a reusable prediction pipeline
- Deploying the final model through an interactive Streamlit interface

---

## ✨ Key Features

- 🧹 Complete NLP text preprocessing pipeline
- 🔤 Tokenization and stopword removal
- 🧠 WordNet lemmatization
- 📊 Exploratory Data Analysis
- ☁️ Spam and Ham word-cloud analysis
- 🔢 TF-IDF feature extraction
- 🧩 Unigram and Bigram representations
- 🔍 Metadata feature engineering
- 🤖 Six Machine Learning models
- 📈 Model performance comparison
- 🎯 Automated best-model selection
- 🧪 Confusion Matrix and Classification Report
- 💾 Model serialization using Joblib
- 🔮 Real-time message prediction
- 📊 Prediction confidence score
- 🌐 Interactive Streamlit web application

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| NLP | NLTK, Regex |
| Feature Engineering | TF-IDF, SciPy |
| Machine Learning | Scikit-learn |
| Visualization | Matplotlib, WordCloud |
| Model Persistence | Joblib |
| Web Application | Streamlit |
| Development | Jupyter Notebook |
| Version Control | Git & GitHub |

---

## 🔄 Machine Learning Pipeline

```text
                    ┌─────────────────────┐
                    │     Raw Dataset     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Data Collection   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Understanding  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │        EDA          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Text Preprocessing │
                    └──────────┬──────────┘
                               │
                               ▼
                ┌─────────────────────────────┐
                │       Feature Engineering   │
                │                             │
                │  TF-IDF + Metadata Features │
                └──────────────┬──────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Model Training   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Model Evaluation   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Prediction Pipeline │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Streamlit Web App   │
                    └─────────────────────┘
```

---

## 🧹 NLP Preprocessing Pipeline

Raw messages undergo a structured preprocessing pipeline before feature extraction:

```text
Raw Message
    │
    ▼
Convert to Lowercase
    │
    ▼
Remove HTML Tags
    │
    ▼
Remove URLs
    │
    ▼
Remove Email Addresses
    │
    ▼
Remove Numbers
    │
    ▼
Remove Punctuation
    │
    ▼
Tokenization
    │
    ▼
Stopword Removal
    │
    ▼
Lemmatization
    │
    ▼
Cleaned Text
```

This standardized representation is subsequently transformed into numerical features for machine learning.

---

## 🧩 Feature Engineering

The system combines textual information with additional metadata features.

### TF-IDF Features

The TF-IDF vectorizer uses:

```python
TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2)
)
```

This captures both:

- Unigrams
- Bigrams

### Metadata Features

Five additional structural features are extracted from each message:

| Feature | Description |
|---|---|
| Message Length | Total number of characters |
| URL Count | Number of URL indicators |
| Digit Count | Number of numerical characters |
| Exclamation Count | Number of `!` characters |
| Uppercase Count | Number of uppercase characters |

The final feature representation combines:

```text
TF-IDF Features
       +
Metadata Features
       │
       ▼
Combined Feature Matrix
```

---

## 🤖 Machine Learning Models

Six classification algorithms were trained and evaluated:

1. Neural Network (MLPClassifier)
2. Random Forest
3. Logistic Regression
4. Support Vector Machine
5. Decision Tree
6. Multinomial Naive Bayes

---

## 🏆 Model Performance

| Rank | Model | Accuracy | Precision | Recall | F1 Score |
|---:|---|---:|---:|---:|---:|
| 🥇 1 | **Neural Network** | **99.03%** | **99.19%** | **93.13%** | **96.06%** |
| 🥈 2 | Random Forest | 98.84% | 99.17% | 91.60% | 95.24% |
| 🥉 3 | Logistic Regression | 97.97% | 95.08% | 88.55% | 91.70% |
| 4 | Support Vector Machine | 97.77% | 92.19% | 90.08% | 91.12% |
| 5 | Decision Tree | 96.81% | 84.03% | 92.37% | 88.00% |
| 6 | Naive Bayes | 94.97% | 75.16% | 90.08% | 81.94% |

### 🏅 Best Performing Model

```text
Model       : Neural Network (MLPClassifier)
Accuracy    : 99.03%
Precision   : 99.19%
Recall      : 93.13%
F1 Score    : 96.06%
```

The Neural Network achieved the highest overall accuracy and F1 score and was selected as the final model.

---

## 📊 Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

Using multiple evaluation metrics is particularly important because the dataset contains an imbalanced distribution between legitimate and spam messages.

---

## 🔮 Prediction Pipeline

For a new message, the application follows the same processing pipeline used during model training:

```text
User Message
     │
     ▼
NLP Preprocessing
     │
     ├───────────────┐
     ▼               ▼
TF-IDF Features   Metadata Features
     │               │
     └───────┬───────┘
             ▼
     Combined Features
             │
             ▼
      Neural Network
             │
             ▼
     Spam / Legitimate
             │
             ▼
      Confidence Score
```

Maintaining the same feature engineering pipeline during training and inference ensures consistent model input.

---

## 🌐 Streamlit Web Application

The project includes an interactive Streamlit application that allows users to enter a message and receive an instant prediction.

### Application Features

- Message input area
- Real-time ML prediction
- Spam detection alert
- Legitimate message confirmation
- Prediction confidence score
- Clean interactive interface

Run the application locally using:

```bash
python -m streamlit run app.py
```

---

## 📁 Project Structure

```text
AI-Driven-Phishing-Email-Detection-Using-NLP/
│
├── dataset/
│   ├── raw/
│   │   └── spam.csv
│   │
│   └── processed/
│       ├── base_dataset.csv
│       ├── understanding_dataset.csv
│       ├── eda_dataset.csv
│       ├── preprocessed_dataset.csv
│       └── final_dataset.csv
│
├── notebooks/
│   ├── 01_Project_Setup.ipynb
│   ├── 02_Data_Collection.ipynb
│   ├── 03_Data_Understanding.ipynb
│   ├── 04_Exploratory_Data_Analysis.ipynb
│   ├── 05_Text_Preprocessing.ipynb
│   ├── 06_Feature_Engineering.ipynb
│   ├── 07_Model_Training.ipynb
│   ├── 08_Model_Evaluation.ipynb
│   ├── 09_Email_Prediction.ipynb
│   └── 10_Streamlit_Deployment.ipynb
│
├── models/
│   ├── phishing_detector.pkl
│   ├── tfidf_vectorizer.pkl
│   ├── X_train.pkl
│   ├── X_test.pkl
│   ├── y_train.pkl
│   └── y_test.pkl
│
├── reports/
│   ├── model_comparison.csv
│   └── model_evaluation.txt
│
├── images/
│
├── presentation/
│
├── app.py
├── requirements.txt
├── LICENSE
├── .gitignore
└── README.md
```

---

## 📚 Notebook Development Progress

| Day | Notebook | Status |
|---:|---|:---:|
| 01 | Project Setup | ✅ |
| 02 | Data Collection | ✅ |
| 03 | Data Understanding | ✅ |
| 04 | Exploratory Data Analysis | ✅ |
| 05 | Text Preprocessing | ✅ |
| 06 | Feature Engineering | ✅ |
| 07 | Model Training | ✅ |
| 08 | Model Evaluation | ✅ |
| 09 | Email Prediction | ✅ |
| 10 | Streamlit Deployment | ✅ |

> **Project Status: Version 1.0 Completed**

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

### 2. Navigate to the Project

```bash
cd AI-Driven-Phishing-Email-Detection-Using-NLP
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python -m streamlit run app.py
```

---

## 🚀 Future Improvements

The current project establishes a strong baseline for NLP-based message classification.

Future versions can include:

- 📧 Dedicated phishing email datasets
- 📨 `.eml` file upload and parsing
- 🌐 Sender domain analysis
- 🔗 URL reputation and structural analysis
- 🧠 BERT / DistilBERT / RoBERTa models
- 🔍 Explainable AI using SHAP or LIME
- ⚡ FastAPI REST API
- 🐳 Docker containerization
- 🔄 CI/CD using GitHub Actions
- ☁️ Cloud deployment
- 📡 Real-time phishing intelligence APIs
- 🛡️ Advanced email header analysis

---

## ⚠️ Limitations

This project is intended for educational and research purposes.

The current model is trained primarily on SMS spam/ham data. As a result, it should be considered a **spam and phishing-like message classifier**, rather than a production-grade phishing email security system.

A real-world phishing detection platform should additionally analyze:

- Sender reputation
- Email headers
- Domain age and reputation
- URL characteristics
- HTML structure
- Attachments
- Authentication mechanisms such as SPF, DKIM, and DMARC

---

## 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

## 👨‍💻 Author

**Abhiney Kumar**

B.Tech — Electronics & Communication Engineering  
Dr. B. R. Ambedkar National Institute of Technology, Jalandhar

Interests:

- Embedded Systems
- Embedded Firmware Development
- Machine Learning
- Artificial Intelligence
- Natural Language Processing

---

<div align="center">

### ⭐ If you find this project useful, consider giving the repository a star.

**Built with Python, NLP, Machine Learning & Streamlit**

</div>