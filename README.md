# SONA Archive Index

A comprehensive Python tool to fetch, index, and analyze State of the Nation (SONA) addresses from the Internet Archive. This project creates a searchable database of speeches with advanced analytics and visualizations.

## Features

- **Web Scraper**: Automatically fetches SONA data from Internet Archive
- **Searchable Index**: SQLite database for fast keyword and speaker searches
- **Data Analysis**: Extract insights including word frequency, sentiment analysis, and timeline trends
- **Visualizations**: Generate word clouds, timeline charts, speaker statistics, and frequency graphs
- **Command-line Search**: Easy-to-use search interface

## Installation

```bash
git clone https://github.com/Misotek25/sona-archive-index.git
cd sona-archive-index
pip install -r requirements.txt
```

## Usage

### 1. Fetch and Index SONA Data

```bash
python scraper.py
python indexer.py
```

### 2. Search the Index

```bash
python search.py "education"
python search.py --speaker "Nelson Mandela"
python search.py --year 2020
```

### 3. Generate Visualizations

```bash
python visualizer.py
```

This will generate:
- `word_cloud.png` - Most common words across all speeches
- `timeline_chart.png` - Speech count and average length over years
- `speaker_statistics.png` - Top speakers and their contributions
- `sentiment_analysis.png` - Sentiment trends over time
- `frequency_distribution.png` - Word frequency analysis

## Project Structure

```
sona-archive-index/
├── scraper.py           # Fetch SONA data from Internet Archive
├── indexer.py           # Create and manage SQLite index
├── analyzer.py          # Analyze speeches and extract insights
├── visualizer.py        # Generate charts and visualizations
├── search.py            # Command-line search interface
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── .gitignore           # Git ignore rules
├── data/                # Generated data and visualizations
│   ├── sona.db          # SQLite database
│   ├── visualizations/  # Generated images
│   └── raw/             # Raw fetched data
└── LICENSE              # MIT License
```

## Data Source

Data is fetched from: https://archive.org/details/sona-archive-summary

## Analysis Metrics

The project provides:

1. **Word Frequency**: Most common words, trends over time
2. **Sentiment Analysis**: Speech tone and emotional content
3. **Speaker Statistics**: Speech count, average length, activity timeline
4. **Temporal Analysis**: Changes in topics and language over decades
5. **Speech Metrics**: Length, complexity, keyword extraction

## Requirements

- Python 3.8+
- Internet connection (for fetching data)
- See `requirements.txt` for dependencies

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Misotek25

## Disclaimer

This project is for educational and research purposes. All data is sourced from the Internet Archive's public collection.