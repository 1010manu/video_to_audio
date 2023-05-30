import moviepy
import moviepy.editor
video=moviepy.editor.VideoFileClip('ep1.mp4')
audio=video.audio
audio.write_audiofile('new.mp3')
