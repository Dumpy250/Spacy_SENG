# 🧠 spaCy SENG – NLP Text Processing Toolkit

A small, menu-driven Python coursework application using **spaCy** and **textacy** to explore English text processing. It reads the supplied `london.txt` and prints results to the console.

## 📌 Project Overview

The source includes named-entity extraction, noun-token extraction, a narrow statement-extraction example and an experimental replacement routine. Some menu labels overstate the current behavior: **option 4 repeats noun extraction**, and **option 5 is not effective sensitive-data redaction with the supplied model**.

This is an educational demonstration, not a fact-verification or privacy/anonymization tool.

## ⚙️ Features and actual menu behavior

| Option | Menu label | Implemented behavior |
|---|---|---|
| 1 | Extract facts | Uses textacy with hard-coded entity pattern `Dogs` and cue lemma `be`; returns only the first matching fragment, or `None` if none matches. |
| 2 | Extract entities | Prints each recognized entity's text and label from `doc.ents`. |
| 3 | Extract nouns | Returns individual tokens whose `pos_` is `NOUN`; not noun chunks or full noun phrases. |
| 4 | Extract verbs | Currently calls the same noun-extraction method as option 3. |
| 5 | Redact text | Merges recognized entities, checks for a `DOG` entity label and joins token text. See the redaction limitation below. |
| 6 | Quit | Exits the menu loop. |

`verb_extraction.py` does contain a helper that extracts lemmas of `VERB` tokens, but `Main.py` neither imports nor invokes it. Its presence is not evidence that the menu performs verb extraction.

## 🧩 How It Works

### 1. Text input

Every menu operation uses the literal path `london.txt`, relative to the **current working directory**. Run from the repository root, where the supplied file lives; the path is not anchored to the script's location. There is no menu file picker or command-line filename argument.

The modules read text with `Path(text_file).read_text(encoding="utf-8")`. Inputs must actually be UTF-8; explicitly selecting that encoding does not repair files saved in another encoding or prevent all decoding errors.

### 2. NLP processing

The extraction classes load `en_core_web_sm`. Startup constructs multiple helper instances and loads the pipeline before showing the menu, so the model must be installed even before choosing an operation. Each selected operation processes the input again.

The “fact” routine is pattern-based extraction, not a general search for factual statements or a truth check. Its return is inside the loop, so it does not collect every match. Noun filtering uses `NOUN`, not `PROPN`, and does not call spaCy's noun-chunk iterator.

### 3. Output and redaction limits

Results are printed to the console. There is no implemented output-file saving or graphical interface.

**Do not use option 5 to protect sensitive information.** Its replacement condition requires `token.ent_type_ == "DOG"`. The declared `en_core_web_sm` 3.7.1 pipeline has no `DOG` NER label, and this project adds no custom entity component or training for that label. Standard person/organization recognition therefore does not trigger replacement. Joining `token.text` without preserving trailing whitespace can also collapse spacing in the returned text.

These are existing source limitations, not features repaired by setup.

## 📁 Project Structure

```text
Spacy_SENG/
├── Main.py                     # Entry point and menu routes
├── extract_entities.py         # Entity text/label pairs
├── fact_extraction.py          # First Dogs/be fragment only
├── noun_chunk_extraction.py    # NOUN tokens, despite the filename
├── verb_extraction.py          # VERB lemmas; not connected to the menu
├── redact_text.py              # Experimental DOG-label replacement
├── london.txt                  # Supplied UTF-8 input
├── requirements.txt            # Libraries and model package URL
└── README.md
```

## 🧪 Setup Instructions

These instructions are **source-checked and unexecuted**. No dependency resolution, model download, pipeline loading or NLP output is verified by them.

### Requirements and compatibility

- Python **3.11** is the existing README's suggested environment, not an enforced or tested minimum.
- `requirements.txt` lists unpinned `spacy`, `textacy` and `pydantic`, plus a direct URL for **`en_core_web_sm` 3.7.1**.
- That model's [official metadata](https://github.com/explosion/spacy-models/blob/master/meta/en_core_web_sm-3.7.1.json) requires **spaCy `>=3.7.2,<3.8.0`**. It is not a generic match for whichever spaCy release is newest.
- There is no dependency lockfile or `environment.yml`. Exact package resolution and platform compatibility remain unverified; changes to the library/model combination require separate compatibility work.

### 1. Prepare an isolated environment

If using an already installed Conda distribution, the existing manual Python 3.11 approach is:

```sh
conda create -n spacy_seng311 python=3.11
conda activate spacy_seng311
```

This creates a new environment; do not overwrite an unrelated existing environment with that name. Conda is an optional environment manager, not a bundled project requirement or supplied environment manifest.

### 2. Install the declared dependencies and model

From the repository root:

```sh
python -m pip install -r requirements.txt
```

This command downloads and installs packages, including the model archive already named in `requirements.txt`. A separate unversioned `pip install textacy` or `python -m spacy download en_core_web_sm` is not an additional required step; blindly adding those steps can change the intended package/model combination. See spaCy's [pipeline installation and compatibility guidance](https://spacy.io/usage/models).

### 3. Run the menu

Only after preparing a compatible environment, from the directory containing `Main.py` and `london.txt`:

```sh
python Main.py
```

This loads the language pipeline and enables NLP processing. Preserve the capital **M** on case-sensitive systems. Use the numbered menu with the actual behaviors described above. The menu always reads `london.txt`; selecting a different filename requires changing the hard-coded path in the source. Repairing the menu routes also requires code changes.

## ⚠️ Limitations

- English small-pipeline predictions can miss or mislabel entities and parts of speech; no accuracy or redaction-safety guarantee is established.
- Option 4 is miswired, option 5 uses an unsupported entity label, and option 1 is a single-fragment, hard-coded example.
- No robust file/model error recovery, automated test suite or persistent result export is included.
- Tracked cached bytecode is not a compatibility specification or a replacement for reviewing the Python source.
