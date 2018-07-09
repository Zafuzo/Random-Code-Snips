#Project Name: Play Wav From Web
import requests, pyaudio
import wave
from io import BytesIO


def main():
  #Get Audio From Website
  url = "https://affiliate.radionetworks.com/wp-content/plugins/common-core/af-download.php?file=kin_kan_pgms%2FSPKA10.wav"
  cut = requests.get(url)

  #convert Binary data into wav file
  waveAudio = wave.open(BytesIO(cut.content), 'r')
  
  #Stream Stuff ~ I should update this when I understand exactly what is going on...!!!!!!
  p = pyaudio.PyAudio()
  chunk = 1024
  
  stream = p.open(format=p.get_format_from_width(waveAudio.getsampwidth()),
                    channels=waveAudio.getnchannels(),
                    rate=waveAudio.getframerate(),
                    output=True)

  # read data (based on the chunk size)
  data = waveAudio.readframes(chunk)

  # play stream (looping from beginning of file to the end)
  while data != '':
    # writing to the stream is what *actually* plays the sound.
    stream.write(data)
    data = waveAudio.readframes(chunk)

  # cleanup stuff.
  stream.close()
  p.terminate() 
  
    
#Boiler Plate Default Main
if __name__ == '__main__':
  main()

  