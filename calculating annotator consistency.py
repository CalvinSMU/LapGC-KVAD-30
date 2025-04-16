import numpy as np
import SimpleITK as sitk
from scipy.spatial.distance import directed_hausdorff
import math
import argparse

def calculate_dice(mask1, mask2):
    """Calculate Dice coefficient between two binary masks"""
    intersection = np.logical_and(mask1, mask2)
    dice = (2.0 * intersection.sum()) / (mask1.sum() + mask2.sum())
    return dice

def calculate_hd(mask1, mask2, spacing=None):
    """Calculate 95% Hausdorff Distance between two binary masks"""
    # Get coordinates of foreground pixels
    points1 = np.argwhere(mask1 > 0)
    points2 = np.argwhere(mask2 > 0)
    
    # Adjust coordinates if pixel spacing is provided
    if spacing is not None:
        points1 = points1 * spacing
        points2 = points2 * spacing
    
    # Calculate bidirectional Hausdorff distance
    if len(points1) == 0 or len(points2) == 0:
        return float('nan'), float('nan')
    
    hd1 = directed_hausdorff(points1, points2)[0]
    hd2 = directed_hausdorff(points2, points1)[0]
    hd = max(hd1, hd2)
    
    # Calculate 95% HD
    if len(points1) > 0 and len(points2) > 0:
        # Calculate distances between all point pairs
        distances = []
        for p1 in points1:
            min_dist = min(np.linalg.norm(p1 - p2) for p2 in points2)
            distances.append(min_dist)
        for p2 in points2:
            min_dist = min(np.linalg.norm(p2 - p1) for p1 in points1)
            distances.append(min_dist)
        
        # Get 95th percentile
        distances_sorted = np.sort(distances)
        hd95 = np.percentile(distances_sorted, 95)
    else:
        hd95 = float('nan')
    
    return hd, hd95

def calculate_diagonal_length(mask, spacing=None):
    """Calculate the diagonal length of the image"""
    if spacing is None:
        spacing = [1.0, 1.0, 1.0] if mask.ndim == 3 else [1.0, 1.0]
    
    shape = mask.shape
    # Calculate diagonal length only for 2D plane (x, y dimensions)
    diagonal = math.sqrt((shape[0]*spacing[0])**2 + 
                         (shape[1]*spacing[1])**2)
    
    return diagonal

def main(mask1_path, mask2_path):
    # Read images
    mask1_sitk = sitk.ReadImage(mask1_path)
    mask2_sitk = sitk.ReadImage(mask2_path)
    
    # Convert to numpy arrays
    mask1 = sitk.GetArrayFromImage(mask1_sitk)
    mask2 = sitk.GetArrayFromImage(mask2_sitk)
    
    # Get pixel spacing (for 3D images)
    spacing = mask1_sitk.GetSpacing()
    
    # Binarize masks (ensure values are 0 and 1)
    mask1 = (mask1 > 0).astype(np.uint8)
    mask2 = (mask2 > 0).astype(np.uint8)
    
    # Calculate Dice coefficient
    dice = calculate_dice(mask1, mask2)
    
    # Calculate Hausdorff distances
    hd, hd95 = calculate_hd(mask1, mask2, spacing)
    
    # Calculate diagonal length
    diagonal = calculate_diagonal_length(mask1, spacing)
    
    # Calculate normalized 95% HD
    hd95_norm = hd95 / diagonal if not np.isnan(hd95) else float('nan')
    
    # Print results
    print(f"Mask1: {mask1_path}")
    print(f"Mask2: {mask2_path}")
    print(f"Dice Coefficient: {dice:.8f}")
    print(f"95% Hausdorff Distance: {hd95:.8f}")
    print(f"Diagonal Length: {diagonal:.8f}")
    print(f"Normalized 95% HD (95% HD / Diagonal): {hd95_norm:.8f}")
    
    return dice, hd95, hd95_norm

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate Dice coefficient and 95% HDnorm between two masks.')
    parser.add_argument('mask1', type=str, help='Path to the first mask image')
    parser.add_argument('mask2', type=str, help='Path to the second mask image')
    
    args = parser.parse_args()
    
    main(args.mask1, args.mask2)