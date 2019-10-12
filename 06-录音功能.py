import pyaudio
import wave
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RECORD_SECONDS = 10  # 录音时间
RATE = 16000
WAVE_OUTPUT_FILENAME = 'OUTPU.wav'

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
              channels = CHANNELS,
              rate = RATE,
              input = True,
              frames_per_buffer = CHUNK)
print('录音中……')
frames = []
for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
print('录音结束！')
frames.append(data)
stream.stop_stream()
stream.close()
p.terminate()
f = wave.open(WAVE_OUTPUT_FILENAME,'wb')
f.setnchannels(CHANNELS)
f.setsampwidth(p.get_sample_size(FORMAT))
f.setframerate(RATE)
f.writeframes(b''.join(frames))
f.close()
