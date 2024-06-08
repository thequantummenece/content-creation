from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

class AudioVideoMerger:
    def __init__(self, video_path, audio_path, output_path):
        self.video_path = video_path
        self.audio_path = audio_path
        self.output_path = output_path

    def concatenate_videos(self, num_repeats):
        # Load video clip
        video_clip = VideoFileClip(self.video_path)

        # Concatenate videos
        concatenated_clip = concatenate_videoclips([video_clip] * num_repeats)

        # Write the result to a file
        concatenated_clip.write_videofile(self.output_path, codec='libx264', audio_codec='aac')

    def get_video_duration(self):
        video_clip = VideoFileClip(self.video_path)
        video_duration = video_clip.duration
        return video_duration

    def trim_video(self, start_time, end_time):
        video_clip = VideoFileClip(self.output_path)
        trimmed_clip = video_clip.subclip(start_time, end_time)
        trimmed_clip.write_videofile(self.output_path, codec='libx264', audio_codec='aac')

    def get_audio_duration(self):
        audio_clip = AudioFileClip(self.audio_path)
        audio_duration = audio_clip.duration
        return audio_duration

    def merge_audio_video(self):
        # Load video and audio clips
        video_clip = VideoFileClip(self.video_path)
        audio_clip = AudioFileClip(self.audio_path)

        # Set video clip with the audio
        video_clip = video_clip.set_audio(audio_clip)

        # Write the result to a file
        video_clip.write_videofile(self.output_path, codec='libx264', audio_codec='aac')

# if __name__ == "__main__":
#     # Paths to your video, audio, and output files
#     video_file_path = "inputvideo/samplefile.mp4"
#     audio_file_path = "audiofiles/sample.mp3"
#     output_file_path = "outputvideo/samplefile_output.mp4"
#
#     # Create an instance of the AudioVideoMerger class
#     merger = AudioVideoMerger(video_file_path, audio_file_path, output_file_path)
#
#     # Merge audio and video
#     merger.merge_audio_video()
#
#     # Get the duration of the audio
#     audio_duration = merger.get_audio_duration()
#     video_duration = merger.get_video_duration()
#
#     # Determine the number of times to repeat the video
#     num_repeats = int(audio_duration / video_duration) + 1
#
#     # Concatenate videos
#     merger.concatenate_videos(num_repeats)
#
#     # Trim video to the duration of the audio (up to 60 seconds)
#     merger.trim_video(0, min(audio_duration, 60))
