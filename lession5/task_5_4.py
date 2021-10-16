from google_trans_new import google_translator
translator = google_translator()
my_file = open("m_file4.txt", "r")
new_file = open("new_file.txt", "w")
while 1:
    line = my_file.readline()
    if line == '':
        break
    translate_text = translator.translate(line, lang_tgt='en')
    new_file.writelines(translate_text+"\n")
my_file.close()
new_file.close()
