import gtts
import google.cloud.texttospeech as tts

class TalkToSpeech():
    def __init__(self, json):
        self.gcloud = tts.TextToSpeechClient.from_service_account_json(json)
        self.gtts_prefix = {
            'afrikaans':'af',   'arabic':'ar',      'bulgarian':'bg', 
            'bengali':'bn',     'bosnian':'bs',     'catalan':'ca', 
            'czech':'cs',       'welsh':'cy',       'danish':'da', 
            'germany':'de',     'greek':'el',       'english':'en',
            'esperanto':'eo',   'spanish':'es',      'estonian':'et',
            'finnish':'fi',     'french':'fr',      'gujarati':'gu',
            'hindi':'hi',       'croatian':'hr',    'hungarian':'hu',
            'armenian':'hy',    'indonesian':'id',  'icelandic':'is',
            'italian':'it',     'hebrew':'iw',      'japanese':'ja',
            'javanese':'jw',    'khmer':'km',       'kannada':'kn',
            'korean':'ko',      'latin':'la',       'latvian':'lv',
            'macedonian':'mk',  'malayalam':'ml',   'marathi':'mr',
            'malay':'ms',       'myanmar':'my',     'nepali':'ne',
            'dutch':'nl',       'norwegian':'no',   'polish':'pl',
            'portuguese':'pt',  'romanian':'ro',    'russian':'ru',
            'sinhala':'si',     'slovak':'sk',      'albanian':'sq',
            'serbian':'sr',     'sundanese':'su',   'swedish':'sv',
            'swahili':'sw',     'tamil':'ta',       'telugu':'te',
            'thai':'th',        'filipino':'tl',    'turkish':'tr',
            'ukrainian':'uk',   'vietnamese':'vi',  'chinese':'zh',
        }

        self.wavenet_prefix = {
            "ar_female" :{"language_code":"ar-XA", "name": "ar-XA-Wavenet-A"},
            "ar_male"   :{"language_code":"ar-XA", "name": "ar-XA-Wavenet-B"},

            "bn_female" :{"language_code":"bn-IN", "name": "bn-IN-Wavenet-A"},
            "bn_male"   :{"language_code":"bn-IN", "name": "bn-IN-Wavenet-B"},

            "da_female" :{"language_code":"da-DK", "name": "da-DK-Wavenet-A"},
            "da_male"   :{"language_code":"da-DK", "name": "da-DK-Wavenet-C"},

            "nl_female" :{"language_code":"nl-NL", "name": "nl-NL-Wavenet-A"},
            "nl_male"   :{"language_code":"nl-NL", "name": "nl-NL-Wavenet-A"},

            "en-AU_female" :{"language_code":"en-AU", "name": "en-AU-Wavenet-A"},
            "en-AU_male"   :{"language_code":"en-AU", "name": "en-AU-Wavenet-B"},

            "en-IN_female" :{"language_code":"en-IN", "name": "en-IN-Wavenet-A"},
            "en-IN_male"   :{"language_code":"en-IN", "name": "en-IN-Wavenet-B"},

            "en-IN_female" :{"language_code":"en-IN", "name": "en-IN-Wavenet-A"},
            "en-IN_male"   :{"language_code":"en-IN", "name": "en-IN-Wavenet-B"},

            "uk_female" :{"language_code":"en-GB", "name": "en-GB-Wavenet-A"},
            "uk_male"   :{"language_code":"en-GB", "name": "en-GB-Wavenet-B"},

            "us_female" :{"language_code":"en-US", "name": "en-US-Wavenet-G"},
            "us_male"   :{"language_code":"en-US", "name": "en-US-Wavenet-B"},

            "ph_female" :{"language_code":"fil-PH", "name": "fil-PH-Wavenet-A"},
            "ph_male"   :{"language_code":"fil-PH", "name": "fil-PH-Wavenet-C"},

            "fr_female" :{"language_code":"fr-FR", "name": "fr-FR-Wavenet-A"},
            "fr_male"   :{"language_code":"fr-FR", "name": "fr-FR-Wavenet-B"},
            
            "de_female" :{"language_code":"de-DE", "name": "de-DE-Wavenet-A"},
            "de_male"   :{"language_code":"de-DE", "name": "de-DE-Wavenet-A"},
            
            "gu_female" :{"language_code":"gu-IN", "name": "gu-IN-Wavenet-A"},
            "gu_male"   :{"language_code":"gu-IN", "name": "gu-IN-Wavenet-B"},

            "hi_female" :{"language_code":"hi-IN", "name": "hi-IN-Wavenet-A"},
            "hi_male"   :{"language_code":"hi-IN", "name": "hi-IN-Wavenet-B"},
            
            "id_female" :{"language_code":"id-ID", "name": "id-ID-Wavenet-A"},
            "id_male"   :{"language_code":"id-ID", "name": "id-ID-Wavenet-B"},

            "it_female" :{"language_code":"it-IT", "name": "it-IT-Wavenet-A"},
            "it_male"   :{"language_code":"it-IT", "name": "it-IT-Wavenet-B"},

            "jp_female" :{"language_code":"ja-JP", "name": "ja-JP-Wavenet-A"},
            "jp_male"   :{"language_code":"ja-JP", "name": "ja-JP-Wavenet-C"},
            
            "kn_female" :{"language_code":"kn-IN", "name": "kn-IN-Wavenet-A"},
            "kn_male"   :{"language_code":"kn-IN", "name": "kn-IN-Wavenet-B"},

            "ko_female" :{"language_code":"ko-KR", "name": "ko-KR-Wavenet-A"},
            "ko_male"   :{"language_code":"ko-KR", "name": "ko-KR-Wavenet-C"},

            "ms_female" :{"language_code":"ms-MY", "name": "ms-MY-Wavenet-A"},
            "ms_male"   :{"language_code":"ms-MY", "name": "ms-MY-Wavenet-B"},

            "ml_female" :{"language_code":"ml-IN", "name": "ml-IN-Wavenet-A"},
            "ml_male"   :{"language_code":"ml-IN", "name": "ml-IN-Wavenet-A"},
            
            "cmn-CN_female" :{"language_code":"cmn-CN", "name": "cmn-CN-Wavenet-A"},
            "cmn-CN_male"   :{"language_code":"cmn-CN", "name": "cmn-CN-Wavenet-B"},

            "cmn-TW_female" :{"language_code":"cmn-TW", "name": "cmn-TW-Wavenet-A"},
            "cmn-TW_male"   :{"language_code":"cmn-TW", "name": "cmn-TW-Wavenet-B"},
            
            "no_female" :{"language_code":"nb-NO", "name": "nb-NO-Wavenet-A"},
            "no_male"   :{"language_code":"nb-NO", "name": "nb-NO-Wavenet-B"},

            "pl_female" :{"language_code":"pl-PL", "name": "pl-PL-Wavenet-A"},
            "pl_male"   :{"language_code":"pl-PL", "name": "pl-PL-Wavenet-B"},

            "pt_female" :{"language_code":"pt-PT", "name": "pt-PT-Wavenet-A"},
            "pt_male"   :{"language_code":"pt-PT", "name": "pt-PT-Wavenet-B"},
            
            "pa_female" :{"language_code":"pa-IN", "name": "pa-IN-Wavenet-A"},
            "pa_male"   :{"language_code":"pa-IN", "name": "pa-IN-Wavenet-B"},
            
            "ru_female" :{"language_code":"ru-RU", "name": "ru-RU-Wavenet-A"},
            "ru_male"   :{"language_code":"ru-RU", "name": "ru-RU-Wavenet-B"},

            "es_female" :{"language_code":"es-ES", "name": "es-ES-Wavenet-C"},
            "es_male"   :{"language_code":"es-ES", "name": "es-ES-Wavenet-B"}, 

            "sv_female" :{"language_code":"sv-SE", "name": "sv-SE-Wavenet-A"},
            "sv_male"   :{"language_code":"sv-SE", "name": "sv-SE-Wavenet-B"},

            "ta_female" :{"language_code":"ta-IN", "name": "ta-IN-Wavenet-A"},
            "ta_male"   :{"language_code":"ta-IN", "name": "ta-IN-Wavenet-B"},

            "tr_female" :{"language_code":"tr-TR", "name": "tr-TR-Wavenet-A"},
            "tr_male"   :{"language_code":"tr-TR", "name": "tr-TR-Wavenet-A"},

            "vi_female" :{"language_code":"vi-VN", "name": "vi-VN-Wavenet-A"},
            "vi_male"   :{"language_code":"vi-VN", "name": "vi-VN-Wavenet-A"},
        }

    def is_gtts_prefix(self, param):
        if param in self.gtts_prefix: return True
        else: return False

    def is_wavenet_prefix(self, param):
        if param in self.wavenet_prefix: return True
        else: return False

    def get_gtts(self, param):
        return self.gtts_prefix[param]

    def get_wavenet(self, param):
        return self.wavenet_prefix[param]


    def decode(self, _tts):
        try:
            for idx, decoded in enumerate(_tts):
                return(decoded)
        except: raise


    def gtts(self, text, lang):
        words = iter(text.split())
        lines, current = [], next(words)
        for word in words:
            if len(current) + 1 + len(word) > 100:
                lines.append(current)
                current = word
            else:
                current += " " + word
        lines.append(current)

        _tts = b''
        for line in lines:
            _tts = _tts + self.decode(gtts.gTTS(text=line, tld='com', lang=lang).stream())

        return _tts


    def api(self, text, language_code, name):
        text_input = tts.SynthesisInput(text=text)
        voice_params = tts.VoiceSelectionParams(
            name = name,
            language_code = language_code,
        )
        audio_config = tts.AudioConfig(
            audio_encoding=tts.AudioEncoding.LINEAR16,
        )
        response = self.gcloud.synthesize_speech(input=text_input,
                                                 voice=voice_params,
                                                 audio_config=audio_config)
        return response.audio_content


    def text_to_speech(self, text, param=None):
        try:
            if param is not None:
                if self.is_wavenet_prefix(param):
                    return(self.api(text, **self.get_wavenet(param)))
                elif self.is_gtts_prefix(param):
                    return(self.gtts(text, self.get_gtts(param)))
            else:
                return(self.gtts(text, "en"))
        except: raise


    def save(self, tts, file):        
        with open(file, "wb") as out:
            out.write(tts)
