
labelled_phrases_list = [
    ["Kutheni umntwana wam engalali?", "lala", "xho"],
    ["Ndingambhalisa njani umntwana wam?", "bhala", "xho"],
    ["Impawu zokuba ndizokubeleka?", "zokubeleka", "xho"],
    ["Ndazi njani ukuba ndizokubeleka phambi kwexesha?", "phambi", "xho"],
    ["Ndine pre-eclampsia?", "pre-eclampsia", "xho"],
    ["Lide kangakanani ixesha lokubeleka?", "ixesha", "xho"],
    ["Ndinesifo sasekuseni?", "morning_sickness", "xho"],
    ["Ndine UTI ngelixa ndikhulelwe", "uti", "xho"],
    ["I high-blood pressure ngelixa ukhulelwe", "high-blood", "xho"],
    ["Ndinesifo sokwasulelana ngesondo", "std", "xho"],
    ["Ndiyagula ngelixa ndikhulelwe", "ndiyagula", "xho"],
    ["Umntwana wam uyagula", "uyagula", "xho"],
    ["Ndineentlungu, ndingaya njani ekliniki?", "ekliniki", "xho"],
    ["Ndinemilenze edumbileyo", "dumbileyo", "xho"],
    ["Yintoni endimele ndondle ngayo umntwana wam?", "ndondle", "xho"],
    ["Ndiyopha ngexesha lokukhulelwa", "opha", "xho"],
    ["Ndinocinezelelo lwengqondo", "depressed", "xho"],
    ["Ndingasifumana njani isibonelelo somntwana wam?", "isibonelelo", "xho"],
    ["Ingaba umntwana wam uzobane HIV?", "hiv", "xho"],
    ["Ndingancancisa ndine HIV?", "hiv_cancisa", "xho"],
    ["Umntwana wam unorhawuzelelo owenziwa yi-nappy", "nappy_rash", "xho"],
    ["Umntwana wam akatyi", "akatyi", "xho"],
    ["Ndingabelana ngesondo xa ndikhulelwe?", "ngesondo", "xho"],
    ["Ndingayenza i-C-Section?", "c-section", "xho"],
    ["Ndingayenza uqhaqho?", "c-section", "xho"],
]
def print_labelled_phrases(phrases):
    for phrase in phrases:
        text, label, lang_code = phrase
        print(f"Phrase: {text}\nLabel: {label}\nLanguage Code: {lang_code}\n")
print_labelled_phrases(labelled_phrases_list)