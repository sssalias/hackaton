rus_to_morz = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..',
               'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
               'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
               'Ш': '----', 'Щ': '--.-', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'}
eng_to_morz = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
               'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
               'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
               'Y': '-.--', 'Z': '--..'}
num_to_morz = {'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
               '7': '--...', '8': '---..', '9': '----.'}
morz_to_rus, morz_to_eng, morz_to_num = {}, {}, {}

for i, j in rus_to_morz.items():
    morz_to_rus[j] = i
for i, j in eng_to_morz.items():
    morz_to_eng[j] = i
for i, j in num_to_morz.items():
    morz_to_num[j] = i


class Morz:
    def __init__(self, text=None, morz=None):
        if text is not None:
            self.text = [i.split() for i in text.upper().split('\n')]
        if morz is not None:
            self.morz = [[j.split() for j in i] for i in morz]

    def code_to_morse(self, language='Multi'):  # функция на кодировку
        final_word = []
        if language == 'English':
            try:
                for i in range(len(self.text)):
                    final_word.append([])
                    for j in self.text[i]:
                        word = ''
                        for k in j:
                            if k.isdigit():
                                word += num_to_morz[k] + ' '
                            else:
                                word += eng_to_morz[k] + ' '
                        final_word[i].append(word[:-1])
                return final_word
            except KeyError:
                return 'ERROR'
        if language == 'Russian':
            try:
                for i in range(len(self.text)):
                    final_word.append([])
                    for j in self.text[i]:
                        word = ''
                        for k in j:
                            if k.isdigit():
                                word += num_to_morz[k] + ' '
                            else:
                                word += rus_to_morz[k] + ' '
                        final_word[i].append(word[:-1])
                return final_word
            except KeyError:
                return 'ERROR'
        if language == 'Multi':
            try:
                for i in range(len(self.text)):
                    final_word.append([])
                    for j in self.text[i]:
                        word = ''
                        for k in j:
                            if k.isdigit():
                                word += num_to_morz[k] + ' '
                            elif k in rus_to_morz.keys():
                                word += rus_to_morz[k] + ' '
                            else:
                                word += eng_to_morz[k] + ' '
                        final_word[i].append(word[:-1])
                return final_word
            except KeyError:
                return 'ERROR'

    def decode_to_morse(self, language='Multi', priority='English'):  # функция на декодировку
        final_word = []
        if language == 'English':
            try:
                for i in range(len(self.morz)):
                    final_word.append([])
                    for j in self.morz[i]:
                        word = ''
                        for k in j:
                            if k in morz_to_num.keys():
                                word += morz_to_num[k]
                            else:
                                word += morz_to_eng[k]
                        final_word[i].append(word)
                result = ' '.join([''.join(j).lower() for i in final_word for j in i])
                return result
            except KeyError:
                return 'ERROR'
        if language == 'Russian':
            try:
                for i in range(len(self.morz)):
                    final_word.append([])
                    for j in self.morz[i]:
                        word = ''
                        for k in j:
                            if k in morz_to_num.keys():
                                word += morz_to_num[k]
                            else:
                                word += morz_to_rus[k]
                        final_word[i].append(word)
                result = ' '.join([''.join(j).lower() for i in final_word for j in i])
                return result
            except KeyError:
                return 'ERROR'
        if language == 'Multi' and priority == 'English':
            try:
                for i in range(len(self.morz)):
                    final_word.append([])
                    for j in self.morz[i]:
                        word = ''
                        for k in j:
                            if k in morz_to_num.keys():
                                word += morz_to_num[k]
                            elif k in morz_to_eng.keys():
                                word += morz_to_eng[k]
                            else:
                                word += morz_to_rus[k]
                        final_word[i].append(word)
                result = ' '.join([''.join(j).lower() for i in final_word for j in i])
                return result
            except KeyError:
                return 'ERROR'
        if language == 'Multi' and priority == 'Russian':
            try:
                for i in range(len(self.morz)):
                    final_word.append([])
                    for j in self.morz[i]:
                        word = ''
                        for k in j:
                            if k in morz_to_num.keys():
                                word += morz_to_num[k]
                            elif k in morz_to_rus.keys():
                                word += morz_to_rus[k]
                            else:
                                word += morz_to_eng[k]
                        final_word[i].append(word)
                result = ' '.join([''.join(j).lower() for i in final_word for j in i])
                return result
            except KeyError:
                return 'ERROR'
