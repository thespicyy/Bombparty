import os

# Function to import the dictionary
def importer_fichier_txt(nom_fichier):
    dico = []
    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            dico.append(ligne.strip())
    return dico

# Function to clean the dictionary. Basically removing accents and "-"
def nettoyer_mot(dico):
    dico_cleaned = []
    for mot in dico:
        if "-" not in mot:
            mot_nettoye = mot.lower().replace("ç", "c").replace("à", "a").replace("é", "e").replace("è", "e").replace("ù", "u").replace("â", "a").replace("ê", "e").replace("û", "u").replace("î", "i").replace("ô", "o").replace("ä", "a").replace("ë", "e").replace("ü", "u").replace("ï", "i").replace("ö", "o")
            dico_cleaned.append(mot_nettoye)
    return dico_cleaned

# Get current work directory to find dictionary
pwd = os.getcwd()

# Import and clean the dictionary
dico = importer_fichier_txt(pwd + "\\dico_fr.txt")
dico_cleaned_fr = nettoyer_mot(dico)

# Same but for english version
dico_en = importer_fichier_txt(pwd + "\\dico_en.txt")
dico_cleaned_en = nettoyer_mot(dico_en)





