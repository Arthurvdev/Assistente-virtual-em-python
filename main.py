import speech_recognition as sr 
import pyttsx3
import datetime
import wikipedia
import webbrowser

audio = sr.Recognizer()
maquina = pyttsx3.init()
vozes = maquina.getProperty('voices')
maquina.setProperty('voice', vozes[0].id)



def executa_comando():
    
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            audio.adjust_for_ambient_noise(source)
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'artemis' in comando:
                comando = comando.replace('artemis', '')
                maquina.say(comando)
                maquina.runAndWait()
            

    except:
        print('Microfone não está funcionando corretamente')
    
    return comando



def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
        
    
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        resposta = "claro"
        print(resultado)
        maquina.say(resposta)
        maquina.say(resultado)
        maquina.runAndWait()
        
    
    elif 'abrir google' in comando:
        comando.replace('abrir google', '')
        google = f"https://google.com/"
        resposta = "claro senhor"
        maquina.say(resposta)
        maquina.runAndWait()
        webbrowser.open(google)
        
    
    elif 'pesquisar por' in comando:
        pesquisa = comando.replace('pesquisar por', '')
        google_pesquisa = f"https://www.google.com/search?q={pesquisa}"
        resposta = "claro senhor"
        maquina.say(resposta)
        maquina.runAndWait()
        webbrowser.open(google_pesquisa)
        
    
    elif 'quem é o amor da minha vida' in comando:
        comando.replace('quem é o amor da minha vida', '')
        texto = "A raiane de queiroz sousa é o amor da sua vida "
        texto2 = "Ela é a mulher mais linda do universo"
        texto3 = "O seu sonho é se casar com ela"
        texto4 = "Raiane, vou falar uma curiosidade sobre o arthur. Ele é louco por você e passa horas pensando em ti. Até mesmo quando me programou."
        maquina.say(texto)
        maquina.say(texto2)
        maquina.say(texto3)
        maquina.say(texto4)
        maquina.runAndWait()
        
    

comando_voz_usuario()