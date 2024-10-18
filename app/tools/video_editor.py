import sys
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips

def video_editor(video_files: list[str], audio_files: list[str], output_filename: str):
    """
    This function takes a list of video files, resizes and crops them to fit YouTube Shorts dimensions,
    then concatenates them. It also concatenates the audio files sequentially and combines them into
    the final video output without overlapping audio.

    :param video_files: A list of paths to video files.
    :param audio_files: A list of paths to audio files (mp3).
    :param output_filename: The path to the output video file.
    :return: The path to the output video file.
    """

    clips = []
    for video in video_files:
        try:
            clip = VideoFileClip(video)

            target_width = 1080
            target_height = 1920

            clip_width, clip_height = clip.size
            width_ratio = target_width / clip_width
            height_ratio = target_height / clip_height
            scaling_factor = max(width_ratio, height_ratio)

            clip_resized = clip.resize(height=int(clip.h * scaling_factor))

            clip_cropped = clip_resized.crop(
                x_center=clip_resized.w / 2,
                y_center=clip_resized.h / 2,
                width=target_width,
                height=target_height
            )

            clips.append(clip_cropped)
        except Exception as e:
            print(f"Error processing {video}: {e}")
            continue

    if not clips:
        print("No valid video clips were processed.")
        sys.exit(1)

    final_clip = concatenate_videoclips(clips, method='compose')

    if audio_files:
        audio_clips = []
        for audio_file in audio_files:
            try:
                audio = AudioFileClip(audio_file)
                audio_clips.append(audio)
            except Exception as e:
                print(f"Error processing audio {audio_file}: {e}")
                continue

        if audio_clips:
            final_audio = concatenate_audioclips(audio_clips)
            final_clip = final_clip.set_audio(final_audio)

    final_clip.write_videofile(
        output_filename,
        fps=30,
        codec='libx264',
        audio_codec='aac',
        preset='medium',
        threads=4
    )

    return output_filename
