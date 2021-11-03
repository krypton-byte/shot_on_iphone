from moviepy.editor import concatenate_videoclips, VideoFileClip, AudioFileClip, CompositeAudioClip, concatenate_audioclips
class Iphone:
    def __init__(self, videoClips):
        '''
        :param videoClips: video file

        ex
        ```python
        >>> from shot_on_iphone import Iphone
        >>> meme = Iphone('video.mp4')
        >>> meme.save('meme.mp4')
        ```
        '''
        self.video       = VideoFileClip(videoClips)
        self.constIphone = VideoFileClip("/".join(__file__.split("/")[:-1])+"/iphone.mp4")
        self.audio       = AudioFileClip("/".join(__file__.split("/")[:-1])+"/iphone.mp3")
        assert self.video.duration > 20, "Video Duration > 20 Seconds"
    def __repr__(self):
        return f"<[ Filename : {self.video.filename}, Duration: {self.video.duration} ]>"
    def save(self, OutPut, **kwargs):
        '''
        :param OutPut: output file
        :param **kwargs: write_videofile option

        example
        ```python
        >>> <Iphone Object>.save('meme.mp4')
        ```
        '''
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
