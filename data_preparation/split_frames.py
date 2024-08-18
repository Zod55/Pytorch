import shutil 
from pathlib import Path 
import glob,os
from time import sleep
def installed(binary:str):
  return shutil.which(binary) is not None

def cutframes(path:Path,destination_path):
   import subprocess
   paths_for_video =  glob.glob(f"{path}/*")
   
   for path  in paths_for_video:
     if os.path.isfile(path):
       path = Path(path)
       print(f"creating dir for {path.stem}")
       path_to_dir = destination_path / path.stem
       path_to_dir.mkdir(exist_ok=True)
       command = ['ffmpeg','-i',path,'-vf','select=not(mod(n\\,1))','-vsync','vfr',(f"{path_to_dir}/frame_%04d.png")]
       result = subprocess.run(command,capture_output=True,text=True)
       print(result.stdout)
       print(result.stderr)
       print("taking a nap")
       sleep(3)

   print("Done!")


def python_frames(paths:Path,
destination_path:Path):
   import cv2
   paths_for_video =  glob.glob(f"{paths}/*")
   for path  in paths_for_video:
     if os.path.isfile(path):
       path = Path(path)
       path_to_dir = destination_path / path.stem
       if not path_to_dir.is_dir():
         print(f"creating dir for {path.stem}")
         path_to_dir.mkdir(exist_ok=True,parents=True)
       
       
       
       cap = cv2.VideoCapture(path)
       frame_num = 0
       while cap.isOpened():
          ret,frame = cap.read()
          if not ret:
              break
          frame_path = path_to_dir /  f"{path.stem}_{frame_num}.jpg"
          cv2.imwrite(frame_path,frame)
          frame_num += 1
       cap.release()
       cv2.destroyAllWindows()
       print("you could watch the frames in your destination path")
    








path = Path(input("videos path:"))
dest_path =  Path(input("destantion path:"))
binary = "ffmpeg"
if not installed(binary):
  print(f"found {binary} using it to cut the frames")
  cutframes(path,dest_path)
else:
  print(f"Didn't found the binary:{binary} using opencv to cut the frames")
  python_frames(path,dest_path)




