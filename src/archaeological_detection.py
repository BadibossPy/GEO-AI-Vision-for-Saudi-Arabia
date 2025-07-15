#!/usr/bin/env python3
"""
Archaeological Feature Detection Algorithm
Computer vision pipeline for detecting potential archaeological sites
from satellite imagery.
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import measure
from skimage.feature import canny
from skimage.morphology import disk, opening, closing
from scipy import ndimage
import warnings
warnings.filterwarnings('ignore')


def generate_synthetic_satellite_image(width=512, height=512, seed=42):
    """Generate synthetic satellite imagery with archaeological features."""
    np.random.seed(seed)
    
    # Base terrain
    base_terrain = np.random.normal(0.4, 0.1, (height, width))
    base_terrain = ndimage.gaussian_filter(base_terrain, sigma=20)
    
    # Geological variations
    geological_features = np.random.normal(0, 0.05, (height, width))
    geological_features = ndimage.gaussian_filter(geological_features, sigma=5)
    
    # Archaeological structures
    archaeological_layer = np.zeros((height, width))
    
    structures = [
        (150, 200, 80, 120),
        (300, 150, 60, 90),
        (100, 350, 100, 70),
        (350, 300, 90, 110)
    ]
    
    for x, y, w, h in structures:
        archaeological_layer[y:y+h, x:x+w] += 0.15
        archaeological_layer[y+10:y+h-10, x+10:x+w-10] += 0.1
    
    archaeological_layer = ndimage.gaussian_filter(archaeological_layer, sigma=3)
    
    satellite_image = base_terrain + geological_features + archaeological_layer
    satellite_image = (satellite_image - satellite_image.min()) / (satellite_image.max() - satellite_image.min())
    
    return satellite_image, structures


def detect_archaeological_features(image, threshold_factor=1.2, min_area=500):
    """Feature detection algorithm for archaeological site identification."""
    
    # Gaussian filtering
    smoothed = ndimage.gaussian_filter(image, sigma=1)
    
    # Edge detection
    edges = canny(smoothed, sigma=1, low_threshold=0.1, high_threshold=0.2)
    
    # Morphological operations
    kernel = disk(3)
    edges_cleaned = closing(opening(edges, kernel), kernel)
    
    # Anomaly detection
    mean_intensity = np.mean(smoothed)
    std_intensity = np.std(smoothed)
    threshold = mean_intensity + threshold_factor * std_intensity
    
    anomalies = smoothed > threshold
    
    # Combine features
    combined_features = np.logical_or(edges_cleaned, anomalies)
    
    # Label connected components
    labeled_features = measure.label(combined_features)
    
    # Filter by size
    filtered_features = np.zeros_like(labeled_features)
    
    feature_count = 0
    for region in measure.regionprops(labeled_features):
        if region.area >= min_area:
            feature_count += 1
            filtered_features[labeled_features == region.label] = feature_count
    
    return filtered_features, edges, anomalies, feature_count


def analyze_detected_features(detected_features, satellite_data):
    """Quantitative analysis of detected features."""
    results = []
    
    for region in measure.regionprops(detected_features.astype(int)):
        centroid = region.centroid
        area = region.area
        bbox = region.bbox
        
        aspect_ratio = (bbox[2] - bbox[0]) / (bbox[3] - bbox[1])
        rectangularity = region.area / (region.bbox_area)
        
        feature_mask = detected_features == region.label
        mean_intensity = np.mean(satellite_data[feature_mask])
        
        results.append({
            'Feature_ID': region.label,
            'Centroid_X': centroid[1],
            'Centroid_Y': centroid[0],
            'Area_pixels': area,
            'Aspect_Ratio': aspect_ratio,
            'Rectangularity': rectangularity,
            'Mean_Intensity': mean_intensity,
            'Confidence_Score': rectangularity * mean_intensity * 100
        })
    
    return results


def visualize_results(satellite_data, detected_features, edge_map, anomaly_map, num_features):
    """Visualization of detection results."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    axes[0,0].imshow(satellite_data, cmap='terrain')
    axes[0,0].set_title('Satellite Image')
    
    axes[0,1].imshow(edge_map, cmap='gray')
    axes[0,1].set_title('Edge Detection')
    
    axes[1,0].imshow(anomaly_map, cmap='Reds', alpha=0.7)
    axes[1,0].imshow(satellite_data, cmap='terrain', alpha=0.3)
    axes[1,0].set_title('Anomaly Detection')
    
    axes[1,1].imshow(satellite_data, cmap='terrain', alpha=0.6)
    axes[1,1].imshow(detected_features, cmap='hot', alpha=0.8)
    axes[1,1].set_title(f'Detected Features ({num_features})')
    
    plt.tight_layout()
    plt.show()


def main():
    """Main execution function."""
    print("Archaeological Feature Detection")
    print("=" * 40)
    
    # Generate data
    satellite_data, true_structures = generate_synthetic_satellite_image()
    print(f"Generated {satellite_data.shape} image with {len(true_structures)} features")
    
    # Detect features
    detected_features, edge_map, anomaly_map, num_features = detect_archaeological_features(satellite_data)
    print(f"Detected {num_features} potential features")
    
    # Analyze
    feature_analysis = analyze_detected_features(detected_features, satellite_data)
    
    if feature_analysis:
        avg_confidence = np.mean([f['Confidence_Score'] for f in feature_analysis])
        print(f"Average confidence: {avg_confidence:.1f}%")
    
    # Visualize
    visualize_results(satellite_data, detected_features, edge_map, anomaly_map, num_features)
    
    # Results
    total_pixels = satellite_data.size
    efficiency = (num_features / total_pixels) * 1000000
    
    print(f"\nResults:")
    print(f"Total pixels processed: {total_pixels:,}")
    print(f"Features detected: {num_features}")
    print(f"Efficiency: {efficiency:.1f} features/million pixels")


if __name__ == "__main__":
    main() 