from moviepy.editor import concatenate_videoclips, VideoFileClip, AudioFileClip, CompositeAudioClip, concatenate_audioclips
import os, requests
class Convert:
    def __init__(self, videoClips):
        self.video       = VideoFileClip(videoClips)
        self.constIphone = VideoFileClip("/".join(__file__.split("/")[:-1])+"/iphone.mp4")
        self.audio       = AudioFileClip("/".join(__file__.split("/")[:-1])+"/iphone.mp3")
    def __repr__(self):
        return f"<[ Filename : {self.video.filename}, Duration: {self.video.duration} ]>"
    def Merge(self, OutPut, **kwargs):
        merged   = concatenate_videoclips([self.video, self.constIphone.resize(self.video.size)])
        mixaudio = CompositeAudioClip([
                                        self.audio.subclip(0, audio1:=(self.audio.duration-self.constIphone.duration)+1), 
                                        self.video.audio.subclip(audio2:=self.video.duration-audio1)
                                    ])
        if self.video.duration-audio1 < 0:
            self.audio       = AudioFileClip("/".join(__file__.split("/")[:-1])+"/iphone.mp3").subclip(audio1-self.video.duration)
            mixaudio = CompositeAudioClip([
                                        self.audio.subclip(0, audio1:=(self.audio.duration-self.constIphone.duration)+1), 
                                        self.video.audio.subclip(audio2:=self.video.duration-audio1)
                                    ])
        merged.audio=concatenate_audioclips([
                        self.video.audio.subclip(0, audio2), 
                        mixaudio, 
                        self.audio.subclip(audio1)
                    ])
        merged.write_videofile(OutPut, **kwargs)
for i_ in list({"iphone.mp4", "iphone.mp3"} - set(os.listdir("/".join(__file__.split("/")[:-1])))):
    open("/".join(__file__.split("/")[:-1])+"/"+i_,"wb").write(requests.get(f"https://github.com/krypton-byte/shot_on_iphone/raw/master/{i_}").content)