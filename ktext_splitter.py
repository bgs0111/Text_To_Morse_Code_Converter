CHOSUNG_LIST = ('ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
JUNGSUNG_LIST = ('ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                 'ㅣ')
JONGSUNG_LIST = (' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
DOUBLE_LIST = {
    'ㄲ': ['ㄱ', 'ㄱ'], 'ㄸ': ['ㄷ', 'ㄷ'], 'ㅃ': ['ㅂ', 'ㅂ'], 'ㅆ': ['ㅅ', 'ㅅ'], 'ㅉ': ['ㅈ', 'ㅈ'], 'ㄳ': ['ㄱ', 'ㅅ'],
    'ㄵ': ['ㄴ', 'ㅈ'], 'ㄶ': ['ㄴ', 'ㅎ'], 'ㄺ': ['ㄹ', 'ㄱ'], 'ㄻ': ['ㄹ', 'ㅁ'], 'ㄼ': ['ㄹ', 'ㅂ'], 'ㄽ': ['ㄹ', 'ㅅ'],
    'ㄾ': ['ㄹ', 'ㅌ'], 'ㄿ': ['ㄹ', 'ㅍ'], 'ㅀ': ['ㄹ', 'ㅎ'], 'ㅄ': ['ㅂ', 'ㅅ'], 'ㅒ': ['ㅑ', 'ㅣ'], 'ㅖ': ['ㅕ', 'ㅣ'],
    'ㅘ': ['ㅗ', 'ㅏ'], 'ㅙ': ['ㅗ', 'ㅐ'], 'ㅚ': ['ㅗ', 'ㅣ'], 'ㅝ': ['ㅜ', 'ㅓ'], 'ㅞ': ['ㅜ', 'ㅔ'], 'ㅟ': ['ㅜ', 'ㅣ'],
    'ㅢ': ['ㅡ', 'ㅣ']
}

def decompose_korean(character):
    kchar_list = []
    ch1 = (ord(character) - ord('가')) // 588
    ch2 = ((ord(character) - ord('가')) - (588 * ch1)) // 28
    ch3 = (ord(character) - ord('가')) - (588 * ch1) - 28 * ch2
    if CHOSUNG_LIST[ch1] not in DOUBLE_LIST:
        kchar_list.append(CHOSUNG_LIST[ch1])
    else:
        temp_list = DOUBLE_LIST[CHOSUNG_LIST[ch1]]
        for letter in temp_list:
            kchar_list.append(letter)
        temp_list.clear()

    if JUNGSUNG_LIST[ch2] not in DOUBLE_LIST:
        kchar_list.append(JUNGSUNG_LIST[ch2])
    else:
        temp_list = DOUBLE_LIST[JUNGSUNG_LIST[ch2]]
        for letter in temp_list:
            kchar_list.append(letter)
        temp_list.clear()

    if JONGSUNG_LIST[ch3] not in DOUBLE_LIST:
        kchar_list.append(JONGSUNG_LIST[ch3])
    else:
        temp_list = DOUBLE_LIST[JONGSUNG_LIST[ch3]]
        for letter in temp_list:
            kchar_list.append(letter)
        temp_list.clear()

    if ' ' in kchar_list:
        kchar_list.remove(' ')

    return kchar_list