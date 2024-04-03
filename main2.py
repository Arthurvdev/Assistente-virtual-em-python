import speech_recognition as sr 
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit

maquina = pyttsx3.init()
vozes = maquina.getProperty('voices')
maquina.setProperty('voice', vozes[0].id)
maquina.setProperty("rate",220)

def falar(audio):
    maquina.say(audio)
    maquina.runAndWait()
    
def microfone():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        print("Reconhecendo...")
        comando = r.recognize_google(audio, language='pt-BR')
        print(comando)
        
    except Exception as e:
        print(e)
        
        return "None"
    
    return comando

def abrir_google():
        google = f"https://google.com/"
        falar("claro parça")
        webbrowser.open(google)

def tempo():
    Tempo = datetime.datetime.now().strftime("%I:%M")
    falar("agora são")
    falar(Tempo)

def tocar(musica):  
      pywhatkit.playonyt(musica)
        
def boas_vindas():
    falar("Olá arthur. Seja bem vindo")
    falar("como posso lhe ajudar?")


     
if __name__ == "__main__":
    boas_vindas()    
    
    while True:
        print("escutando...")
        comando = microfone().lower()
    
        if 'artemis' in comando and 'olá' in comando:
            falar("Olá")
            
        elif 'oi' in comando and 'artemis' in comando:
            falar("Olá, tudo bem?")
        
        elif 'e você' in comando:
            falar("Que bom, fico feliz. Eu estou ótima")
        
        elif 'como você está' in comando and 'artemis' in comando:
            falar("Estou bem, obrigada")
        
        elif 'quem é o amor da minha vida' in comando and 'artemis' in comando:
            falar("A raiane de queiroz sousa é o amor da sua vida. Ela é a mulher mais linda do universo. O seu sonho é se casar com ela. Raiane, vou falar uma curiosidade sobre o arthur. Ele é louco por você e passa horas pensando em ti. Até mesmo quando me programou.  ")
        
        elif 'hora' in comando and 'artemis' in comando:
            tempo()
            
        elif 'abrir google' in comando and 'artemis' in comando:
            abrir_google()
        
        elif 'artemis' in comando and 'tocar' in comando:
            musica = comando.replace('artemis' and 'tocar', '')
            tocar(musica)
        
        elif 'artemis' in comando and 'ferrar' in comando:
            falar("vai se ferrar você seu desgraçado")
        
       
            
            

