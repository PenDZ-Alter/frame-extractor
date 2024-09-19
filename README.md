# frame-extractor
A simple video frame extractor using Python and OpenCV

## Usage
Install the requirements first
  ```bash
  pip install -r requirements.txt
  ```
<br>

If you want to extract all frames, you can use this command : 
  ```bash
  python main.py --path "/path/to/file_video"
  ```
<br>

If you want to extract single frame, you can use this command : 
  ```bash
  python main.py --path "/path/to/file_video" --frame n
  ```
n is the number of frame. <br>

If you want to extract frame in range, you can use this command :
  ```bash
  python main.py --path "/path/to/file_video" --min n --max m
  ```
n is the number start frame and m is the number of the end frame<br>

All files are extracted in `frames` folder