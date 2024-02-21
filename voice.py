import google.cloud.texttospeech as tts


def list_voices(language_code=None):
    client = tts.TextToSpeechClient()
    response = client.list_voices(language_code=language_code)
    voices = sorted(response.voices, key=lambda voice: voice.name)

    print(f" Voices: {len(voices)} ".center(60, "-"))
    for voice in voices:
        languages = ", ".join(voice.language_codes)
        name = voice.name
        gender = tts.SsmlVoiceGender(voice.ssml_gender).name
        rate = voice.natural_sample_rate_hertz
        print(f"{languages:<8} | {name:<24} | {gender:<8} | {rate:,} Hz")

def text_to_wav(voice_name: str, text: str):
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )

    filename = f"{voice_name}.wav"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')
    return filename


# text = audioToText(1)
# text_to_wav("es-ES-Neural2-C", translate_text("es", amp_transcipt_hardcoded)['translatedText'])

amp_transcipt_hardcoded = "Amp is used for the management of your BJSS corporate CV which is used by resourcing team to send to potential clients before you start a new project so should be updated regularly to login. You'll be sent a link from your local operations team. You will need your bgss username and password if you have any issues logging in please contact your local admin team. You'll be home page where you can access your profile your profile should contain all relevant for employers as well as clients. You've worked for it bjss and should be updated as you move engagements. Also allows you to add your skills and expertise including qualifications which are vital for account managers when searching for people with particular skills clicking on your profile will display all your information as well as subsections your experience skills and qualifications and expertise you can change your basic profile details by clicking edit the experience section displays all your previous. As well as any clients with him. You've worked with a bjss ordered by start date in this section you will have the option to edit delete or add an entry. Please read the guidelines to ensure you are conforming with the bjss corporate standards for profile the skill section allows you to add amend or delete skills from your profile click add and use the search box to find the skill you require and using the guidelines on the side select the appropriate level for your skill All You Need Is Not you can click create scale to add your own the qualifications and expertise section lists your primary expertise and any relevant qualifications you can add a new qualification by using the add new option. If you need any further information, please refer to the amp user guide on keplr if you are having any issues, please escalate them to your local operations team."
