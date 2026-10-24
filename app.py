import streamlit as st
import matplotlib.pyplot as plt 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag


nltk.download('punkt_tab',quiet=True)
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# page setup
st.set_page_config(page_title="Resume Analyzer", page_icon=":clipboard:", layout="wide")
st.markdown("""
Upload your resume and job description to analyze how well your resume matches the job requirements.  
""")

with st.sidebar:
    st.header("About")
    st.info("""
         This tool helps you:
         - Measures how well your resume matches a job description.
         - Identify important job keywords
         - Improve your resume based on missing terms 
    """)

    st.header("How to use")
    st.write("""
             1. Upload your resume.
             2. Upload the job description.
             3. Click **Analyze Match** to see the results.
             4. Review Score and Suggestions.

             3. Identify important job keywords and improve your resume based on missing terms.
        """)

    # helper function

def extract_text_from_pdf(uploaded_file):
     try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
     except Exception as e:
         st.error(f"Error reading PDF file: {e}")
         return ""


def clean_text(text):
    # Remove special charcters and digits and convert to lower case
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '',text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word= word_tokenize(text)
    filtered_words = [w for w in word if not w in stop_words]
    return ' '.join(filtered_words)

def calculate_similarity(resume_text, job_description):
    resume_processed = remove_stopwords(clean_text(resume_text)) 
    job_processed = remove_stopwords(clean_text(job_description))
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_processed, job_processed])
    score = cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:2])[0][0]*100
    return round(score,2),resume_processed, job_processed
  

def extract_keywords(text, num_keywords=10):
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return filtered_tokens


# main app
def main():
    uploaded_file=st.file_uploader("upload your resumre",type=['pdf'])
    job_description = st.text_area(" Paste the job description here")
    
    if st.button("Analyze Match"):
        if not uploaded_file:
            st.warning("Please upload your resume")
        if not job_description:
            st.warning("Please paste the job description")
            return
            
        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            if not resume_text:
                st.error("failed to extract text from the uploaded file. Plesae try another pdf")
                return 
            
            # calculate similarity score
            score, resume_processed, job_processed = calculate_similarity(resume_text, job_description)

            st.subheader("Match Score")
            st.metric("Match Score", f"{score:.2f}%")

            
            resume_words = set(resume_processed.lower().split())

            job_tokens = word_tokenize(job_description.lower())
            tagged_words = pos_tag(job_tokens)

             # Extract meaningful words from job description
            job_keywords = {
    word for word, tag in tagged_words
    if tag in ("NN", "NNS", "NNP", "NNPS")
    and word.isalpha()
    and word not in stopwords.words("english")
}

            missing_keywords = job_keywords - resume_words

            st.subheader("Missing Skills / Keywords")
            st.write(", ".join(sorted(missing_keywords)))


           # gauge chart
            fig,ax= plt.subplots(figsize=(10,0.2))
            colors = ['red' , 'orange' , 'green']
            color_index = min(int(score // 33 ),2)
            ax.barh([0],[score],color=colors[color_index])
            ax.set_xlim(0,100)
            ax.set_xlabel(" Match percentage")
            ax.set_yticks([])
            ax.set_title(" Resume Job Match")
            st.pyplot(fig)

            if score <40 :
                st.warning(" Your resume has a low match with the job description")

            elif score <70:
                st.info(" Your resume has a moderate match with the job description")

            else:
                st.success(" Your resume has a good match with the job description")

    

if __name__ == "__main__":
    main()