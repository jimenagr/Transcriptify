# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
from moviepy.editor import VideoFileClip

# create a speech recognition object
r = sr.Recognizer()

def transcribe_audio(path):
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        text = r.recognize_google(audio_listened)
    return text


def get_large_audio_transcription_on_silence(path):
    sound = AudioSegment.from_file(path)  
    chunks = split_on_silence(sound,
        min_silence_len = 500,
        silence_thresh = sound.dBFS-14,
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        try:
            text = transcribe_audio(chunk_filename)
        except sr.UnknownValueError as e:
            pass
        else:
            text = f"{text.capitalize()}. "
            whole_text += text
    return whole_text

def mp3(archivo):
    print(archivo)
    sound = AudioSegment.from_mp3(archivo)
    output_filename = archivo.replace(".mp3", ".wav")
    sound.export(output_filename, format="wav")
    
    path = output_filename
    result = get_large_audio_transcription_on_silence(path)
    print(result)
    return result

def mp4(archivo):
    video_clip = VideoFileClip(archivo)
    audio_clip = video_clip.audio
    output_filename = archivo.replace(".mp4", ".wav")
    audio_clip.write_audiofile(output_filename, codec="pcm_s16le")
    audio_clip.close()
    video_clip.close()

    path = output_filename
    result = get_large_audio_transcription_on_silence(path)
    print(result)
    return result

#resultado = mp3("audio.mp3")
# resultado = mp4("tu_archivo.mp4")
#print(resultado)
