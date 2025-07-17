# A Proposed Framework for AI-Assisted Archaeological Survey

## 1. Problem Statement

Traditional archaeological surveys rely on manual interpretation of aerial imagery or ground-level inspection, which are costly and do not scale effectively across large, remote, or inaccessible regions. While photogrammetry excels at documenting known sites, a scalable methodology for the *ab initio* discovery of unknown sites is a significant operational challenge. This document outlines a computational framework to accelerate this process using a phased application of computer vision and machine learning.

## 2. Proposed Technical Framework

We propose a four-phase, iterative approach that begins with simple, validated techniques and progressively incorporates more complex deep learning models as data is acquired and annotated.

### Phase 1: Foundational Heuristic Model (Current Implementation)

The initial phase, implemented in this repository, uses a heuristic model based on established computer vision algorithms to detect potential subsurface structures in single-band raster imagery.

*   **Methodology**:
    1.  **Preprocessing**: Apply a Gaussian filter to reduce high-frequency noise.
    2.  **Feature Engineering**: Combine two distinct signals:
        *   **Edge Detection**: A Canny edge detector identifies sharp linear gradients.
        *   **Anomaly Detection**: A statistical threshold (`μ + n*σ`) identifies pixels with intensities that are statistical outliers relative to the local terrain.
    3.  **Candidate Selection**: Merge the edge and anomaly masks and use connected-component analysis to group pixels. Filter these components by a minimum area to produce a final set of candidate regions.
*   **Current Status**: This model has been validated on synthetic data to confirm its ability to detect rectangular features against a noisy background.

### Phase 2: Validation on Real-World Data

The next critical step is to benchmark the Phase 1 model against real-world data.
*   **Data Sources**: Utilize open-source satellite imagery (e.g., Sentinel-2, Landsat) or high-resolution drone imagery over areas with known, documented archaeological sites (e.g., from the EAMENA database).
*   **Objective**: Quantify the model's precision and recall. This step is crucial for establishing a performance baseline and identifying the model's limitations (e.g., sensitivity to terrain type, feature morphology).

### Phase 3: Transition to a Supervised Deep Learning Model

Based on the findings from Phase 2, transition to a supervised deep learning approach for semantic segmentation.

*   **Model Architecture**: A U-Net or similar encoder-decoder architecture is a strong candidate, as it is well-suited for pixel-level classification tasks in geospatial imagery.
*   **Training Data**: The annotated data from Phase 2 will serve as the initial training set. This dataset will be augmented using standard techniques (rotation, scaling, noise injection) to improve model robustness.
*   **Objective**: Develop a model that can generalize across different types of terrain and archaeological features, moving beyond the simple rectangular heuristics of the initial model.

### Phase 4: Scalable Deployment and Iteration

The final phase focuses on operationalizing the trained model for large-area surveys.
*   **Packaging**: Containerize the model and its dependencies (e.g., using Docker) for portability.
*   **Deployment**: Deploy the container on a cloud platform (e.g., AWS, Azure) to enable parallel processing of large imagery datasets.
*   **Human-in-the-Loop**: The output of the model is not a final answer but a "heatmap" of potential sites. This output must be reviewed by human experts in a GIS environment (e.g., QGIS), who provide feedback that can be used to further refine the model in a continuous learning loop.

## 3. Conclusion

This framework provides a pragmatic, phased pathway for developing a robust, AI-assisted archaeological survey tool. By starting with a simple, explainable model and incrementally building towards a more sophisticated deep learning solution, we can manage technical risk while ensuring that each phase delivers tangible, verifiable progress. The current repository represents the successful completion of Phase 1. 