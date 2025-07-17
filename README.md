# GeoArch: Archaeological Anomaly Detection

A proof-of-concept for detecting potential archaeological anomalies (e.g., buried structures) in raster imagery using statistical and computer vision techniques. This project demonstrates a foundational workflow for identifying rectangular patterns that differ from the surrounding terrain.

For a detailed overview of the proposed framework and its application, see [**A Proposed Framework for AI-Assisted Archaeological Survey**](./ARTICLE.md).

---

### Core Methodology

The detection pipeline operates on single-band grayscale images and uses a multi-step process:
1.  **Noise Reduction**: A Gaussian filter smooths the image.
2.  **Edge & Anomaly Detection**: The algorithm combines a Canny edge detector with a statistical anomaly finder that flags pixels deviating significantly from the image's mean intensity.
3.  **Component Analysis**: Detected pixels are grouped into components, which are then filtered by size to remove noise and isolate objects of interest.

### Example Output

The following shows the pipeline applied to a synthetic image with four buried structures.

| Input Grayscale Image | Detected Edges | Identified Anomalies | Final Detected Features |
| :---: | :---: | :---: | :---: |
| `[IMAGE_PLACEHOLDER_1]` | `[IMAGE_PLACEHOLDER_2]` | `[IMAGE_PLACEHOLDER_3]` | `[IMAGE_PLACEHOLDER_4]` |
*Note: Replace placeholders with actual output images.*

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run on a synthetic image and show plot
python -m geo_arch.cli --show
```

To analyze your own grayscale image (e.g., a GeoTIFF):
```bash
python -m geo_arch.cli path/to/your/image.tif
```

### Project Roadmap

This repository is the first step in a larger vision. The planned development path is:
- [x] **Phase 1: Core Algorithm**: Develop and validate the fundamental detection logic on synthetic data.
- [ ] **Phase 2: Real-World Data Validation**: Test the algorithm on open-source satellite or drone imagery of known archaeological sites.
- [ ] **Phase 3: Deep Learning Model**: Implement a U-Net or similar semantic segmentation model for improved accuracy and generalization.
- [ ] **Phase 4: Scalable Deployment**: Package the tool for large-scale analysis on cloud infrastructure. 