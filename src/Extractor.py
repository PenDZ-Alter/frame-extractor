import cv2
from tqdm import tqdm

class FrameExtractor : 
  def __init__(self, video_path) :
    self.video_path = video_path
    self.min_frame = None
    self.max_frame = None
    self.frame_number = None

  def extract_frames(self, min_frame=None, max_frame=None):
    self.min_frame = min_frame
    self.max_frame = max_frame
    video = cv2.VideoCapture(self.video_path)

    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    if self.min_frame is None and self.max_frame is None:
      self.min_frame = 0
      self.max_frame = total_frames - 1

    if self.min_frame < 0 or self.max_frame > total_frames or self.min_frame >= self.max_frame:
      print(f"Invalid frame range. Video has {total_frames} frames.")
      return

    pbar = tqdm(total = self.max_frame - self.min_frame + 1, desc="Extracting frames ...", unit="frame")

    frame_count = 0
    extracted_frames = 0
    while True:
      success, frame = video.read()

      if not success:
        break

      if self.min_frame <= frame_count <= self.max_frame:
        cv2.imwrite(f"frames/frame_{frame_count}.jpg", frame)
        extracted_frames += 1
        pbar.update(1)

      frame_count += 1

      if frame_count > self.max_frame:
        break

    pbar.close()
    video.release()
    print(f"Extracted {extracted_frames} frames from frame {self.min_frame} to {self.max_frame}.")

  def extract_single_frame(self, frame_number):
    self.frame_number = frame_number
    video = cv2.VideoCapture(self.video_path)

    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    if self.frame_number < 0 or self.frame_number >= total_frames:
      print(f"Invalid frame number. Video has {total_frames} frames.")
      return

    video.set(cv2.CAP_PROP_POS_FRAMES, self.frame_number)

    success, frame = video.read()

    if success:
      cv2.imwrite(f"frames/frame_{self.frame_number}.jpg", frame)
      print(f"Extracted and saved frame {self.frame_number} as frame_{self.frame_number}.jpg")
    else:
      print(f"Could not extract frame {self.frame_number}.")

    video.release()