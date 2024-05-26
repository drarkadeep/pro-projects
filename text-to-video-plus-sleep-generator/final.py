# we'll use moviepy for the video and gTTS for the audio
from moviepy.editor import *
from gtts import gTTS
import os

def text_to_video(para):
    # aim is to break up a paragraph into words and convert each into a clip with the word and the audio and compile them together
    video_list = []
    texts = para.split(" ")
    for text in texts:
        tts = gTTS(text=text, lang='en')
        tts.save("audio.mp3")

        # create the textclip with the word at the center and attach the audio
        text_clip = TextClip(text, size=(700,500), fontsize=70, color='white')
        text_clip = text_clip.set_duration(AudioFileClip("audio.mp3").duration)
        final_clip = text_clip.set_audio(AudioFileClip("audio.mp3"))
        final_clip.write_videofile("video.mp4", fps=1)

        # i'm pretty sure there's a better way to do it, but i'm saving the temp video clip and reloading it for concatenation later
        video_list.append(VideoFileClip("video.mp4"))

        # remove the tempfiles
        os.remove("audio.mp3")
        os.remove("video.mp4")

    # simply concatenate the clips
    compiled_video = concatenate_videoclips(video_list) 
    compiled_video.write_videofile("output.mp4")

    # # use the following lines of code if you wanna generate an alvin and the chipmunks style of video 
    # new_video = VideoFileClip("output.mp4")
    # speed_video = new_video.fx(vfx.speedx, 2.0)
    # speed_video.write_videofile("output.mp4", fps=24)

# this is what you can play with when don't want to play with the code itself! 
para = "I made a text to video generator so bad that it makes you wanna fall asleep. The monotonous drone, coupled with a barrage of technical terms, washes over you, slowly coaxing your eyelids shut. Alternatively, the dimly lit minimalist background and the relentless wall of words conspire to lull you into a drowsy complacency. A slumber like a lumber, if you will. Goodnight, little one!"
text_to_video(para)
