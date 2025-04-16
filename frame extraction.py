import subprocess
import os

# Function to extract frames from the video
def extract_frames(video_path, output_folder, frame_rate=25, resolution="1920x1080"):
    """
    Extract frames from a video at a specified frame rate and save as PNG files.
    
    Args:
    video_path (str): Path to the input video file.
    output_folder (str): Folder where the PNG frames will be saved.
    frame_rate (int): Frame rate in frames per second (fps).
    resolution (str): Resolution of the extracted frames (default is "1920x1080").
    
    Returns:
    None
    """
    
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Construct FFmpeg command
    command = [
        "ffmpeg",
        "-i", video_path,                      # Input video file
        "-vf", f"fps={frame_rate},scale={resolution}", # Apply frame rate and resolution scaling
        os.path.join(output_folder, "%04d.png")   # Save frames as PNG with numbered filenames
    ]
    
    # Run FFmpeg command
    try:
        subprocess.run(command, check=True)
        print(f"Frames extracted and saved to {output_folder}")
    except subprocess.CalledProcessError as e:
        print(f"Error extracting frames: {e}")

# Example usage
video_path = "video_name.mp4"  # Replace with your video file path
output_folder = "extracted_frames"     # Folder where frames will be saved

# Extract frames from the video
extract_frames(video_path, output_folder)
