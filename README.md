# Resume Analyzer 📄

## About the Project

Resume Analyzer is a Python-based web application that helps job seekers analyze their resumes against a job description. It compares the text of both documents and provides a similarity score along with keyword analysis to help users understand how well their resume matches the job requirements.

## Key Features

- **Resume Upload:** Upload a resume in PDF format.
- **Text Extraction:** Extract text from the uploaded resume.
- **Resume Matching:** Compare resume content with a job description.
- **Similarity Score:** Calculate text similarity using TF-IDF and cosine similarity.
- **Keyword Analysis:** Identify words or terms that may be missing from the resume.
- **Interactive Interface:** View results through a Streamlit web application.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| NLTK | Text preprocessing |
| Scikit-learn | TF-IDF and cosine similarity |
| PyPDF2 | PDF text extraction |
| Matplotlib | Data visualization |

## Working Process

1. Upload a resume in PDF format.
2. Enter the relevant job description.
3. Extract and preprocess the text.
4. Convert the text into numerical vectors using TF-IDF.
5. Calculate similarity using cosine similarity.
6. Display the analysis results and potential missing keywords.

## Installation

**Step 1: Clone the repository**

```bash
git clone https://github.com/Meghnagautam/resume_analyzer.git
```

**Step 2: Navigate to the project directory**

```bash
cd resume_analyzer
```

**Step 3: Install the required libraries**

```bash
pip install streamlit matplotlib scikit-learn PyPDF2 nltk
```

**Step 4: Run the application**

```bash
streamlit run app.py
```

Replace `app.py` with your actual Python filename if it is different.

## Learning Outcomes

- Understanding text preprocessing in NLP.
- Working with PDF files in Python.
- Applying TF-IDF for text representation.
- Using cosine similarity for text comparison.
- Building a simple web application using Streamlit.

## Future Scope

- Improve skill extraction from job descriptions.
- Provide more relevant resume improvement suggestions.
- Support additional document formats.
- Enhance the accuracy of keyword analysis.

## Author

**Meghna Gautam**

GitHub: https://github.com/Meghnagautam

---

*This project is intended to assist job seekers with resume analysis. The results are informational and do not guarantee selection for a job.*
