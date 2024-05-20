from gtts import gTTS

tts = gTTS("안녕하세요. 저는 양희선입니다", lang='ko')
tts.save("mysounds.mp3")
