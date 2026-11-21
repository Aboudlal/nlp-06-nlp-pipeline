# Author: Abdellah Boudlal
# Date: 2026-11

"""Configuration for the custom BERT web text analysis pipeline.

Source: https://arxiv.org/abs/1810.04805

Defines the source URL, HTTP headers, and output paths for
the Extract, Validate, Transform, Analyze, Load (EVTAL) pipeline.
"""

from pathlib import Path

# ============================================================
# SOURCE CONFIGURATION
# ============================================================

PAGE_URL: str = "https://arxiv.org/abs/1810.04805"

HTTP_REQUEST_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (educational-use; web-mining-course)"
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

RAW_HTML_PATH: Path = RAW_PATH / "abdellah_bert_raw.html"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "abdellah_bert.csv"
