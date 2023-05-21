import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")



import BingPython as ai
import asyncio

if __name__ == "__main__":
    # Cookies
    # You can get with Cookie Editor
    # - Enter to https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx
    # - Open cookie editor
    # - Write your cookie
    # OR
    # - Export your cookies as Netscape
    # - Write your cookies inside of cookies.txt
    #     try:
    #         import cookielib
    #     except:
    #         import http.cookiejar
    #         cookielib = http.cookiejar
    # cookies = cookielib.MozillaCookieJar('cookies.txt')
    # cookies.load()
    cookies = {
        'MUID': '',
        'BCP': '',
        'MUIDB': '',
        'USRLOC': '',
        'SRCHD': 'AF=hpcodx',
        'MMCASM': '',
        '_UR': '',
        'ANON': '',
        'NAP': '',
        'ABDEF': '',
        'PPLState': '1',
        'KievRPSSecAuth': '',
        '_U': '',
        'SUID': '',
        '_EDGE_S': '',
        'WLS': '',
        '_HPVN': '',
        '_SS': '',
        '_clck': '',
        'SRCHUSR': '',
        '_RwBf': '',
        'SRCHHPGUSR': '',
        'ipv6': '',
    }

    ask = text
    command = ai.BingPython.sendcom_sydney(ai.BingPython.CreateSession(cookies), ask)
    x =(asyncio.get_event_loop().run_until_complete(command))

    from gtts import gTTS
    import os

    # Text to be converted to speech
    text = x

    # Create a gTTS object
    tts = gTTS(text=text, lang='en')

    # Save the audio file
    tts.save('output.mp3')

    # Play the audio file
    os.system('../../output.mp3')


