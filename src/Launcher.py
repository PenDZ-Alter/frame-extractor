import argparse
import os
from src.Extractor import FrameExtractor

def check_dir():
  if not os.path.exists('frames'):
    os.makedirs('frames')
  return True

def init_parser() : 
  parser = argparse.ArgumentParser(description="Extract frames from a video.")
  parser.add_argument('--path', '-p', type=str, required=True, help="Path to the video file.")
  parser.add_argument('--frame', '-f', type=int, help="Frame number to extract.")
  parser.add_argument('--min', type=int, help="(Range) Minimum frame number to extract.")
  parser.add_argument('--max', type=int, help="(Range) Maximum frame number to extract.")
  parser.add_argument('--version', '-v', action="version", version="%(prog)s v0.1.0 (Beta version)", help="Print program version and exit")

  args = parser.parse_args()
  
  frame = FrameExtractor(args.path)

  if args.frame is not None:
    frame.extract_single_frame(args.frame)
  elif args.min is not None and args.max is not None:
    frame.extract_frames(args.min, args.max)
  elif (args.min is not None and args.max is None) or (args.min is None and args.max is not None): 
    print("Use both args '--min' and '--max' to specified range frames.")
  else:
    print("No frame or range specified. Extracting all frames from the video.")
    frame.extract_frames()