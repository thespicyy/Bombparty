import time
import pyperclip
import copy
import pyautogui
from PIL import ImageGrab
from load_dictionary import dico_cleaned_fr, dico_cleaned_en
from calibration_data import syl_x, syl_y, ws_x, ws_y, pixel_init, language

# Function to display the chosen word
def highlight_substring(full_string, substring):
    start_index = full_string.find(substring)
    if start_index == -1:
        return full_string 
    end_index = start_index + len(substring)

    formatted_string = ('\033[94m' 
                        + full_string[:start_index] 
                        + '\033[31;1m'
                        + full_string[start_index:end_index] 
                        + '\033[0m'  
                        + '\033[94m' 
                        + full_string[end_index:]) 
    return formatted_string

# The dictionary I modify to remove already chosen word
dico_fun_fr = copy.deepcopy(dico_cleaned_fr)
dico_fun_en = copy.deepcopy(dico_cleaned_en)
iter = 0
list_letter = []

# Letters to get a new life
list_letter_jklm = ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v']
letter_out = ['k','w','x','y','z']
list_letter_jklm_en = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y']
letter_out_en = ['x','z']
list_let = []
list_let_out = []

# Calculate the score of word. The higher the score, the more new letters there are in that word
def count(mot, liste):
    count = 0
    for el in mot:
        if el not in liste and el not in letter_out:
            count+=1
    return count

# Function to find the word
def find(dico):
    global dico_fun_fr, dico_fun_en, iter, list_letter, list_letter_jklm, letter_out, list_letter_jklm_en, letter_out_en
    global list_let, list_let_out, syl_x, syl_y, ws_x, ws_y, pixel_init, language
    vie_supp = False
    col = False
    part_word = ""

    # Starting the game depending on the language chosen
    if iter == 0 and language=="fr":
        print("\033[33;1m")
        print("Les règles sont les suivantes :\n")
        print("Séparez votre écran en deux fenêtre, une avec ce script, l'autre avec JKLM\n")
        print('Appuyez sur "entrer" dés que la partie commence\n')
        print("Le programme va lui même écrire le mot sur jklm\n")
        print("Le programme ne réutilise pas les mêmes mots lors d'une même session\n")
        print('Ctrl + c pour arrêter le script quand le curseur pour écrire est revenu sur le script\n')
        print("\033[0m")
        print("\033[1mDébut de la partie ?\033[0m")
        input()
        time.sleep(0.1)
        
    elif iter == 0 and language=="en":
        print("\033[33;1m")
        print("The rules are as follows :\n")
        print("Separate your screen into two windows, one with this script, the other with JKLM\n")
        print('Press "enter" as soon as the game starts\n')
        print("The program will itself write the word on jklm\n")
        print("The program does not reuse the same words during the same session\n")
        print('Ctrl + c to stop the script when the writing cursor returned to the script\n')
        print("\033[0m")
        print("\033[1mStart of the game?\033[0m")
        input()
        time.sleep(0.1)
    
    # Check if it's your turn to answer. You might want to change the coordinates based on your screen
    elif iter!=0:
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
        
        while not col :
            time.sleep(0.1)
            screenshot = ImageGrab.grab()
            pixel_color = screenshot.getpixel((ws_x, ws_y)) # value to eventually change
            if pixel_color == pixel_init:
                col = True  
               
    # Copy the syllable
    time.sleep(0.1) 
    col = False
    pyautogui.moveTo(syl_x, syl_y)
    pyautogui.doubleClick()
    
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)
    
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    
    time.sleep(0.1) 
    
    # Current syllable
    part_word = pyperclip.paste()

    words_found = []
    
    # Search in french dict of english one depending on the language chosen
    if language=="fr":
        dic = dico_fun_fr
        list_let = list_letter_jklm
        list_let_out = letter_out
    elif language=="en":
        dic = dico_fun_en
        list_let = list_letter_jklm_en
        list_let_out = letter_out_en
        
    for mot in dic:
        if part_word.lower() in mot.lower():
            words_found.append((mot,count(mot, list_letter)))
    if len(words_found)==0 and language=="fr":
        print("\033[31;1mAucun mot\033[0m\n")
        return
    elif len(words_found)==0 and language=="en":
        print("\033[31;1mNo word\033[0m\n")
        return
    
    # Find the word with the highest score
    words_found.sort(key=lambda x: x[1], reverse=True)
    
    chosen_word = words_found[0][0]

    for letter in chosen_word:
        if letter not in list_letter and letter not in list_let_out:
            list_letter.append(letter)
    
    if sorted(list_letter) == sorted(list_let):
        list_letter = []
        vie_supp = True
    pyperclip.copy(chosen_word)
    dic.remove(chosen_word)
    
    substring = part_word.lower()
    formatted_string = highlight_substring(chosen_word, substring)
    if language=="fr":
        print("\033[94mMot trouvé : {}\033[0m\n".format(formatted_string))
    elif language=="en":
        print("\033[94mWord found : {}\033[0m\n".format(formatted_string))
    iter +=1
    
    if vie_supp and language=="fr":
        print("\033[92mVie supplémentaire !\033[0m\n")
    elif vie_supp and language=="en":
        print("\033[92mExtra life!\033[0m\n")
    
    time.sleep(0.1) 
    
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    
    time.sleep(0.1)
    
    return words_found[0]

while True:
    word = find(dico_cleaned_fr)