# 🧠 spaCy SENG – NLP Text Processing Toolkit

A Python-based Natural Language Processing (NLP) application built with **spaCy** and **textacy**.  
This project provides a menu-driven interface for extracting linguistic information from text files, including facts, named entities, noun phrases, verbs, and redacted text.

The project was originally built for coursework and later cleaned up to follow better **software engineering and environment management practices**.

---

## 📌 Project Overview

The application allows users to analyze a text file (`london.txt`) using multiple NLP techniques:

- Fact extraction from semi-structured statements
- Named entity recognition (NER)
- Noun phrase (chunk) extraction
- Verb extraction
- Text redaction

All processing is powered by **spaCy’s `en_core_web_sm` model**, with additional functionality provided by **textacy**.

---

## ⚙️ Features

- Menu-driven CLI interface
- Modular extraction classes (single responsibility)
- UTF-8–safe file handling (Windows compatible)
- Conda-based environment isolation
- Extensible architecture for adding new NLP tasks

---

## 🧩 How It Works

### 1. Text Input
The application reads from a local text file: london.txt


The file must be located in the **project root directory**.

---

### 2. NLP Processing
Depending on user choice, the application performs:

| Option | Function |
|------|---------|
| 1 | Extract factual statements |
| 2 | Extract named entities |
| 3 | Extract noun phrases |
| 4 | Extract verbs |
| 5 | Redact sensitive text |
| 6 | Exit program |

Each operation is implemented in its own module for clarity and maintainability.

---

### 3. Output
Results are printed directly to the console in a readable format.

---

## 📁 Project Structure

```
Spacy_SENG/
├── Main.py                     # Entry point / menu controller
├── extract_entities.py         # Named entity extraction
├── fact_extraction.py          # Fact extraction using textacy
├── noun_chunk_extraction.py    # Noun phrase extraction
├── verb_extraction.py          # Verb extraction
├── redact_text.py              # Text redaction logic
├── london.txt                  # Sample input text
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```



---

## 🧪 Setup Instructions (Windows / Conda)

### ✅ Prerequisites
- Miniconda or Anaconda installed
- Python **3.11** (recommended)

---

### 1. Create a dedicated Conda environment

```
conda create -n spacy_seng311 python=3.11 -y
conda activate spacy_seng311
```
2. Install dependencies
```
pip install -r requirements.txt
pip install textacy
```

3. Install spaCy language model
```
python -m spacy download en_core_web_sm
```

4. Run the application
```
python Main.py
```
📝 Notes on Text Encoding (Windows)

All text files are read using UTF-8 encoding to ensure compatibility with Unicode characters.

Example implementation:
```
Path(text_file).read_text(encoding="utf-8")
```
This avoids common Windows UnicodeDecodeError issues.

⚠️ Limitations

- Designed for educational use

- Assumes English-language input

- Uses spaCy’s small model (en_core_web_sm)

- Console output only (no GUI)
