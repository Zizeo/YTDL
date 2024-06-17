

import os
from pytube import YouTube

_str=""

def complete_func(stream, file_handle):
    global _str
    _str="Download completed\n"
    _str+="File path: " + file_handle+"\n"
    _str+="File size: " + str(os.path.getsize(file_handle) / 1024 / 1024) + " MB"
    print(_str)




def download_video(url, path, only_audio):
    
    yt = YouTube(
        url,
        on_complete_callback=complete_func,
        use_oauth=False,
        allow_oauth_cache=True
    )
    

    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    print(audio_stream)
    
    if only_audio == True:
        audio_stream.download(output_path=path, filename=yt.author+" - "+yt.title+'.opus')
    else:
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=path, filename=yt.author+" - "+yt.title+'.mp4')
        return yt.register_on_complete_callback(complete_func)
    
    return _str


