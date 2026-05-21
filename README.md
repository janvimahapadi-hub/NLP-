# NLP Class Assignment – Task 1 and Task 2

## Overview

This assignment demonstrates basic Natural Language Processing (NLP) concepts using Python and different NLP libraries. The practical work includes dependency parsing, named entity recognition (NER), document similarity using TF-IDF, and a simple job recommendation system.

The assignment helps in understanding how text data can be processed, analyzed, and compared using NLP techniques.



## Technologies and Libraries Used

- Python
- spaCy
- NLTK
- pandas
- scikit-learn
- IPython Display

Install required libraries:

```bash
pip install spacy nltk pandas scikit-learn
python -m spacy download en_core_web_sm
```

---

# Task 1: Dependency Parsing, Named Entity Recognition, and Document Similarity

## Objective

The purpose of this task is to understand sentence structure, identify important entities from text, and compare document similarity.

### Part A: Dependency Parsing

Sentence used:

```text
I saw the man with a telescope.
```

Tasks performed:

- Loaded spaCy English model
- Parsed sentence structure
- Identified ROOT word
- Displayed dependency relationships
- Visualized output using displacy
- Analyzed sentence ambiguity

Expected learning:

- Understand grammatical relationships
- Learn how words depend on each other
- Observe multiple meanings of a sentence


### Part B: Named Entity Recognition (NER)

NER was used to detect:

- Organizations
- Person names
- Dates
- Locations

Examples of labels:

- ORG
- PERSON
- GPE
- DATE

Expected learning:

- Identify important information from text automatically
- Understand entity classification

---

### Part C: TF-IDF and Cosine Similarity

Documents used:

1. AI is transforming healthcare
2. Machine learning improves healthcare
3. Football is a popular sport

Tasks performed:

- Created TF-IDF vectors
- Generated vocabulary
- Calculated cosine similarity
- Compared document similarity scores

Expected learning:

- Understand document comparison
- Learn importance of TF-IDF



# Task 2: Job Recommendation System using NLP

## Objective

The aim of this task is to build a simple job recommendation system that suggests jobs based on user skills.



## Dataset

Sample job roles used:

- Data Science Intern
- Frontend Developer
- Cybersecurity Analyst
- Machine Learning Engineer
- AI Research Intern

Each job contains:

- Job title
- Job description

---

## Steps Performed

### Step 1: Text Preprocessing

Preprocessing operations:

- Convert text to lowercase
- Remove punctuation
- Remove stop words
- Perform lemmatization

Purpose:

- Clean the text data
- Remove unnecessary words
- Improve model performance



### Step 2: Feature Extraction using TF-IDF

TF-IDF was used to convert job descriptions into numerical vectors.

Purpose:

- Assign importance to important words
- Represent text in numerical format

---

### Step 3: User Query Processing

Example query:

```text
python machine learning data analysis
```

The query was preprocessed using the same steps applied to job descriptions.


### Step 4: Similarity Calculation

Cosine similarity was used to compare:

- User skills
- Job descriptions

Purpose:

- Find matching jobs
- Rank recommendations

---

### Step 5: Display Top Results

The system displays:

- Job title
- Job description
- Similarity score

## Results

Task 1:

- Dependency parsing successfully showed sentence structure.
- NER detected important entities.
- TF-IDF similarity identified related documents.

Task 2:

- The recommendation system successfully matched user skills with suitable jobs.
- Data Science and AI-related jobs showed higher similarity scores.


## Conclusion

This assignment helped in understanding fundamental NLP concepts and their practical applications. It demonstrated how NLP techniques can be used for sentence analysis, entity detection, document similarity, and recommendation systems.
