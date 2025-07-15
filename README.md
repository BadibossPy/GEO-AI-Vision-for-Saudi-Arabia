# Archaeological Feature Detection from Satellite Imagery

Computer vision approach for identifying potential archaeological sites in satellite data.

## Overview

This project applies image processing techniques to detect rectangular anomalies in satellite imagery that may indicate buried archaeological structures. The approach combines edge detection, statistical analysis, and morphological operations.

## Implementation

### Core Algorithm
- Gaussian filtering for noise reduction
- Canny edge detection
- Statistical anomaly detection (threshold: μ + 1.2σ)
- Morphological operations (opening/closing)
- Connected component analysis
- Size-based filtering (min 500 pixels)

### Files
- `notebooks/Archaeological_Feature_Detection.ipynb` - Main analysis
- `src/archaeological_detection.py` - Standalone implementation
- `requirements.txt` - Dependencies

## Usage

Install dependencies:
```bash
pip install -r requirements.txt
```

Run analysis:
```bash
jupyter lab notebooks/Archaeological_Feature_Detection.ipynb
```

Or run standalone:
```bash
python src/archaeological_detection.py
```

## Results

The algorithm processes synthetic satellite data and identifies potential archaeological features using computer vision techniques. Results include feature detection, confidence scoring, and visualization.

## Technical Stack

- Python 3.8+
- scikit-image (image processing)
- scikit-learn (clustering)
- numpy/scipy (numerical computing)
- matplotlib (visualization)

## Application

Designed for integration with real satellite data sources (Sentinel-2) and archaeological databases (EAMENA). The modular approach allows for scaling to large geographic areas. 