# BERT Abstract: NLP Pipeline and Vocabulary Analysis

[![CI](https://github.com/Aboudlal/nlp-06-nlp-pipeline-custom/actions/workflows/ci-python-zensical.yml/badge.svg)](https://github.com/Aboudlal/nlp-06-nlp-pipeline-custom/actions/workflows/ci-python-zensical.yml)
[![Documentation](https://img.shields.io/badge/docs-site-blue)](https://aboudlal.github.io/nlp-06-nlp-pipeline-custom/)
[![Python](https://img.shields.io/badge/python-3.14%2B-blue)](pyproject.toml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Extract, clean, analyze, and visualize an academic abstract using a reproducible EVTAL pipeline.

**Author:** Abdellah Boudlal
**Date:** 2026-11
**Course:** Web Mining and Applied NLP — Module 6

## Project Overview

This project analyzes the abstract of the BERT research paper
using an Extract, Validate, Transform, Analyze, Load (EVTAL) pipeline.

Building on my Module 5 project, it retrieves the paper's arXiv
page, validates its HTML structure, extracts metadata, processes
the abstract, and generates vocabulary statistics and visualizations.

The main analytical question is:

**How does stopword removal affect token frequencies and vocabulary
measurements in the BERT abstract?**

The project analyzes the text of the paper's abstract.
It uses spaCy for text processing; it does not run the BERT model.

Adapted from
[Denise Case's example project](https://github.com/denisecase/nlp-06-nlp-pipeline).

## Data

The custom pipeline retrieves:

[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)

Authors: Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova.

The pipeline extracts:

- Title and authors.
- Abstract text.
- Subject information.
- Submission information.
- arXiv identifier.

The analysis covers one abstract, containing 141
whitespace-separated words, rather than the full paper.

## Methods and Tools

| Stage | Purpose | Tools |
| --- | --- | --- |
| Extract | Retrieve HTML and save the source document | Requests |
| Validate | Check expected HTML elements | BeautifulSoup |
| Transform | Extract metadata, clean text, and calculate features | BeautifulSoup, spaCy, Pandas |
| Analyze | Count token frequencies and generate visuals | Counter, Matplotlib, WordCloud |
| Load | Export the structured results | Pandas, CSV |

The project uses spaCy's `en_core_web_sm` English model for
tokenization and identifying stopwords, punctuation, and whitespace.

The analysis calculates:

- Raw abstract word count.
- Processed token count.
- Unique token count.
- Type-token ratio.
- Token frequencies.
- Author count.

**TTR = unique token count / total token count**

Part-of-speech tagging and named entity recognition are available
in the spaCy model but are not used in this analysis.

## Setup

Install Git and uv, then run these commands from your Repos folder:

```powershell
git clone https://github.com/Aboudlal/nlp-06-nlp-pipeline-custom.git
cd nlp-06-nlp-pipeline-custom
uv python install
uv sync --frozen
```

Runtime dependencies are declared in `pyproject.toml`:

- datafun-toolkit
- requests
- beautifulsoup4
- lxml
- pandas
- matplotlib
- wordcloud
- spacy
- en-core-web-sm

For additional setup instructions, see the
[Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/).

## Run the Project

Run commands from the repository root.

### Custom BERT Pipeline

```powershell
uv run python -m nlp.pipeline_web_html_custom
```

The current custom transformation retains stopwords.

### Original Example Pipeline

```powershell
uv run python -m nlp.pipeline_web_html
```

The original example analyzes *Agents of Chaos*.

Successful execution ends with:

```text
Pipeline executed successfully!
```

The custom pipeline uses separate BERT HTML and CSV filenames.
Both pipelines use `case_top_tokens.png` and `case_wordcloud.png`
for their generated charts, so these images are replaced on each run.

Named copies in `docs/images/` preserve the comparison visuals.

## Technical Experiment: Top 20 vs. Top 15

Before analyzing BERT, I made a small technical modification using
the original *Agents of Chaos* example.

### Modification and Reason

I copied the original pipeline into `pipeline_web_html_custom.py`
and added `top_n=15` to the analysis call:

```python
run_analyze(
    df=df,
    LOG=LOG,
    top_n=15,
)
```

I chose this change to make the chart more focused by displaying
fewer tokens.

### Prediction

The chart and logged frequency list would show 15 tokens instead
of 20. Token counts and TTR would remain unchanged because the
extraction and cleaning steps were unchanged.

### Observed Result

The modified pipeline completed successfully and displayed
the top 15 tokens.

Both example runs produced:

| Measurement | Original: Top 20 | Modified: Top 15 |
| --- | --- | --- |
| Processed tokens | 130 | 130 |
| Unique tokens | 118 | 118 |
| Type-token ratio | 0.9077 | 0.9077 |

### What I Learned

The display limit changes how much vocabulary is shown without
changing the underlying text statistics. A shorter chart also
omits some lower-ranked terms.

## Custom Application: BERT Stopword Comparison

I adapted the pipeline to the paper selected for my Module 5
project and investigated one preprocessing decision.

### Custom Files

- `config_abdellah.py` defines the BERT source and output paths.
- `pipeline_web_html_custom.py` runs the custom workflow.
- `stage03_transform_abdellah.py` retains stopwords during cleaning.

The original processing files remain available as examples.

### Prediction

Retaining stopwords would increase the token count and introduce
common grammatical words into the most frequent tokens.

The effect on TTR would be measured from the output.

### Preprocessing Change

The original transformation removes stopwords, punctuation,
and whitespace tokens:

```python
if not (token.is_stop or token.is_punct or token.is_space)
```

The custom transformation retains stopwords:

```python
if not (token.is_punct or token.is_space)
```

The source document and other processing steps stayed the same.

### Reproduce Both Settings

In `pipeline_web_html_custom.py`, use the following import for
the stopword-removed analysis:

```python
from nlp.stage03_transform import run_transform
```

Use the following import for the retained-stopword analysis:

```python
from nlp.stage03_transform_abdellah import run_transform
```

Select only one of these imports, save the file, and run:

```powershell
uv run python -m nlp.pipeline_web_html_custom
```

The two settings overwrite the same main BERT CSV and chart paths.
Separate snapshots preserve the recorded comparison.

## Results

### Vocabulary Measurements

| Measurement | Stopwords Removed | Stopwords Retained |
| --- | --- | --- |
| Raw abstract word count | 141 | 141 |
| Processed tokens | 106 | 151 |
| Unique tokens | 78 | 103 |
| Type-token ratio | 0.7358 | 0.6821 |
| Authors | 4 | 4 |

Removing stopwords excluded 45 token occurrences and 25 distinct
token types.

Retaining stopwords increased both total and unique token counts,
but total tokens increased proportionally more. TTR therefore
decreased from 0.7358 to 0.6821.

The raw word count uses whitespace splitting, while the processed
count follows spaCy tokenization. These are different measurements:
one whitespace-separated expression can produce multiple tokens.

### Stopwords Removed

The most frequent tokens were “language,” “absolute,” and
“improvement,” each appearing four times.

![BERT top 15 tokens with stopwords removed](docs/images/bert_top15.png)

### Stopwords Retained

The most frequent token became “to,” appearing six times.
“And” and “the” each appeared four times.

![BERT top 15 tokens with stopwords retained](docs/images/bert_top15_with_stopwords.png)

### Word Cloud

![BERT word cloud with stopwords removed](docs/images/bert_wordcloud.png)

The word cloud provides a visual overview. The frequency charts
and tables provide the exact comparisons.

## Interpretation and Limitations

Removing stopwords made the frequency chart more focused on
topic-related vocabulary. “Language” and “bert” reflect the subject,
while “absolute,” “improvement,” and “point” reflect the abstract's
discussion of evaluation results.

Retaining stopwords preserves more grammatical information,
but common words occupy more positions in the top-15 chart.

The higher TTR after filtering reflects the preprocessing choice.
It does not establish that the text became better or more informative.

Limitations include:

- Only one abstract is analyzed.
- TTR depends on text length, tokenization, and preprocessing.
- Frequencies do not explain sentence context or verify research claims.
- Lowercasing removes capitalization information.
- Stopword removal can discard meaningful words.
- Punctuation removal can break meaningful expressions.
- No lemmatization is applied, so “model” and “models” remain separate.
- WordCloud applies additional default processing when generating
  an image from text, including its own stopword filtering.

The bar charts, CSV metrics, and logged counts are the primary
evidence for the preprocessing comparison.

See the [full project report](https://aboudlal.github.io/nlp-06-nlp-pipeline-custom/)
for additional explanation.

## Project Structure

| File or Directory | Purpose |
| --- | --- |
| `src/nlp/pipeline_web_html.py` | Original example pipeline |
| `src/nlp/pipeline_web_html_custom.py` | Custom BERT pipeline with top-15 analysis |
| `src/nlp/config.py` | Original example configuration |
| `src/nlp/config_abdellah.py` | BERT source and output configuration |
| `src/nlp/stage01_extract.py` | HTML retrieval |
| `src/nlp/stage02_validate.py` | HTML structure validation |
| `src/nlp/stage03_transform.py` | Original transformation with stopword removal |
| `src/nlp/stage03_transform_abdellah.py` | Custom transformation retaining stopwords |
| `src/nlp/stage04_analyze.py` | Frequency analysis and visualization |
| `src/nlp/stage05_load.py` | CSV export |
| `data/` | Source HTML and processed results |
| `docs/index.md` | Custom project report |
| `docs/images/` | Saved comparison visuals |
| `tests/` | Automated tests |
| `pyproject.toml` | Dependencies and project configuration |
| `.github/workflows/` | Automated checks and documentation deployment |

## Saved Outputs

| Path | Content |
| --- | --- |
| `data/raw/abdellah_bert_raw.html` | Retrieved BERT HTML |
| `data/processed/abdellah_bert.csv` | Most recent custom run |
| `data/processed/abdellah_bert_without_stopwords.csv` | Snapshot with stopwords removed |
| `data/processed/abdellah_bert_with_stopwords.csv` | Snapshot with stopwords retained |
| `docs/images/bert_top15.png` | Chart with stopwords removed |
| `docs/images/bert_top15_with_stopwords.png` | Chart with stopwords retained |
| `docs/images/bert_wordcloud.png` | Word cloud from the stopword-removed run |
| `docs/images/bert_wordcloud_with_stopwords.png` | Word cloud generated during the retained-stopword run |

The word-cloud images may filter stopwords independently of the
pipeline, so they should not be treated as exact token comparisons.

## Verification

Both BERT preprocessing runs completed successfully.
The validation logs confirmed the expected HTML elements were present.

The documentation build also completed with:

```text
No issues found
```

The initial automated test run reported:

- One test passed.
- 82.46% total coverage.
- The required minimum coverage of 20% was satisfied.

These test figures describe the initial example before the custom
files were added. They are not a coverage measurement of the final
custom implementation.

To run the current tests:

```powershell
uv run python -m pytest
```

## Development Checks

### Install and Run Git Hooks

```powershell
uvx prek install --force
uvx prek update --freeze --cooldown-days 7
git add -A
uvx prek run --all-files
```

If hooks modify files, review the changes and repeat:

```powershell
git add -A
uvx prek run --all-files
```

### Check Code and Build Documentation

```powershell
uv run ruff check .
uv run ruff format --check .
uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Commit and Push

```powershell
git add -A
git commit -m "Describe what changed and why"
git push
```

## Possible Extensions

- Add a configuration option for stopword removal.
- Save each preprocessing setting to separate paths automatically.
- Generate word clouds directly from measured token frequencies.
- Investigate lemmatization and hyphenated expressions.
- Compare multiple abstracts while accounting for differences in length.

## Documentation and Automation

The project documentation is built with Zensical and published
through GitHub Pages.

- [Hosted Documentation](https://aboudlal.github.io/nlp-06-nlp-pipeline-custom/)
- [Report Source](docs/index.md)
- [GitHub Actions](https://github.com/Aboudlal/nlp-06-nlp-pipeline-custom/actions)
- [Commit History](https://github.com/Aboudlal/nlp-06-nlp-pipeline-custom/commits/main/)

## Credits and Resources

- [Original Example by Denise Case](https://github.com/denisecase/nlp-06-nlp-pipeline)
- [BERT Paper and Abstract](https://arxiv.org/abs/1810.04805)
- [Original Experiment Data: Agents of Chaos](https://arxiv.org/abs/2602.20021)
- [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
- [NLP Evolution](docs/nlp-evolution.md)
- [Citation](CITATION.cff)

## License

This project is distributed under the [MIT License](LICENSE).
