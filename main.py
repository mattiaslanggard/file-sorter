import os

source = "C:/Users/matti/Downloads"
image_destination = "C:/Users/matti/Pictures/automoved_pictures"
video_destination = "C:/Users/matti/Videos/automoved_videos"

image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".avif")
video_extensions = (".mp4", ".webm", ".wmv", ".mov")

for file in os.listdir(source):
    name, ext = os.path.splitext(file)
    os.rename(os.path.join(source, file), os.path.join(source, name + ext.lower()))
    if file.endswith(image_extensions):
        src_path = os.path.join(source, file)
        dst_path = os.path.join(image_destination, file)
        os.rename(src_path, dst_path)
    elif file.endswith(video_extensions):
        src_path = os.path.join(source, file)
        dst_path = os.path.join(video_destination, file)
        os.rename(src_path, dst_path)