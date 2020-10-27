import pygame
import speech_recognition as sr

class music:
    def __init__(self):
        self.filename1= 'music/Dawn.mp3'
        self.filename2= 'music/Tomorrow.mp3'
        self.initMixer()
        self.r = sr.Recognizer()
        self.playmusic(self.filename1)
    def playmusic(self,soundfile):
        pygame.init()
        pygame.mixer.init()
        self.clock= pygame.time.Clock()
        pygame.mixer.music.load(soundfile)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): # 파일이 재생되고 있는동안 True
            print("Playing... - func => playingmusic")
            self.clock.tick(1000) # 초당 1000프레임이상이 안되게 제한
            with sr.Microphone() as source:
                self.r.adjust_for_ambient_noise(source)
                print("명령")
                self.audio_text = self.r.listen(source)
                try :
                    print("다 들었음")
                    r2=self.r.recognize_google(self.audio_text,language='ko-KR')
                    print(r2)
                    if '멈춰' in r2:
                        pygame.mixer.music.stop()
                        #stopmusic()
                    
                except KeyboardInterrupt:
                    self.stopmusic()
                    print("\nPlay stopped by user")

                except:
                    print("진행중")
         
 
    def stopmusic(self): # 재생 정지
        """stop currently playing music"""
        pygame.mixer.music.stop()
    
    def getmixerargs(self):
        pygame.mixer.init()
        freq, size, chan= pygame.mixer.get_init()
        return freq, size, chan
    
    
    def initMixer(self):
        BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
        FREQ, SIZE, CHAN= self.getmixerargs()
        pygame.mixer.init(FREQ, SIZE, CHAN,BUFFER)
    
 
'''You definitely need test mp3 file (a.mp3 in example) in a directory, say under 'C:\\Temp'
   * To play wav format file instead of mp3,
      1) replace a.mp3 file with it, say 'a.wav'
      2) In try except clause below replace "playmusic()" with "playsound()"
     
'''
if __name__ == "__main__":
               
    music=music()
    pass
    

