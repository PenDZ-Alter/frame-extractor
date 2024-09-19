import argparse
import os
from src.Extractor import FrameExtractor

def check_dir():
  if not os.path.exists('frames'):
    os.makedirs('frames')
  return True

def init_parser() : 
  parser = argparse.ArgumentParser(description="Extract frames from a video.")
  parser.add_argument('--path', type=str, required=True, help="Path to the video file.")
  parser.add_argument('--frame', type=int, help="Frame number to extract.")
  parser.add_argument('--min', type=int, help="Minimum frame number to extract.")
  parser.add_argument('--max', type=int, help="Maximum frame number to extract.")

  args = parser.parse_args()
  
  frame = FrameExtractor(args.path)

  if args.frame is not None:
    frame.extract_single_frame(args.frame)
  elif args.min is not None and args.max is not None:
    frame.extract_frames(args.min, args.max)
  else:
    print("No frame or range specified. Extracting all frames from the video.")
    frame.extract_frames()