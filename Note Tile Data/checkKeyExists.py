#!/usr/bin/env python3


import json


specific_name = "if-ye-love-me"
voice_type = "Bass"


json_dir_name = '/Users/tchdeveloper1/Documents/Coding Practice/pythonProblems/Note Tile Data/{}/GamePA3-NoteTileData-{}-{}.json'.format(
    specific_name, specific_name, voice_type)

my_dicts = []

with open(json_dir_name, "r") as file:
    data = json.load(file)

    newDictConcept = {"notes": [my_dicts]}

print("Checking if frequency key exists in JSON")
# Wellerman relative pitch.
#relativePitchValue = [100, 3, 5, 6, 8, 10, 11, 13, 15]
#notesInSong = ["X", "C4", "D4", "Eb4", "F4", "G4", "Ab4", "Bb4", "C5"]

scale = [1, 3, 5, 7, 8, 10, 12, 13, 15]
noteValues = ["F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4"]
frequencies = [174.61, 196.0, 220.0, 246.94, 261.63, 293.66, 329.63, 349.23, 392.0]
scales_dict = {3: 'G4', 5: 'A4', 6: 'Bb4', 7: 'G4',
               8: 'A4', 10: 'Bb4', 10: 'Bb4', 10: 'Bb4', 10: 'Bb4'}


def save_json():
    with open(json_dir_name, 'w') as file:
        json.dump(newDictConcept, file)


for info in data["notes"]:
    # print(info)
    # once you know the associated note value to the relative pitch you can likely append them all

    if info["relativePitch"] == scale[0] in info.values():
        info["noteName"] = noteValues[0]
        info["frequency"] = frequencies[0]
        my_dicts.append(info)
        newDictConcept = {"notes": my_dicts}
        save_json()
    if info["relativePitch"] == scale[1] in info.values():
        info["noteName"] = noteValues[1]
        info["frequency"] = frequencies[1]
        my_dicts.append(info)
        newDictConcept = {"notes": my_dicts}
        save_json()
    if info["relativePitch"] == scale[2] in info.values():
        info["noteName"] = noteValues[2]
        info["frequency"] = frequencies[2]
        my_dicts.append(info)
        newDictConcept = {"notes": my_dicts}
        save_json()
    if info["relativePitch"] == scale[3] in info.values():
        info["noteName"] = noteValues[3]
        info["frequency"] = frequencies[3]
        my_dicts.append(info)
        newDictConcept = {"notes": my_dicts}
        save_json()
    if info["relativePitch"] == scale[4] in info.values():
        info["noteName"] = noteValues[4]
        info["frequency"] = frequencies[4]
        my_dicts.append(info)
        newDictConcept = {"notes": my_dicts}
        save_json()
    if info["relativePitch"] == scale[5] in info.values():
        info["noteName"] = noteValues[5]
        info["frequency"] = frequencies[5]
        my_dicts.append(info)
        newDictConcept = {"notes": my_dicts}
        save_json()
    if info["relativePitch"] == scale[6] in info.values():
        info["noteName"] = noteValues[6]
        info["frequency"] = frequencies[6]
        my_dicts.append(info)
        newDictConcept = {"notes": my_dicts}
        save_json()
    if info["relativePitch"] == scale[7] in info.values():
        info["noteName"] = noteValues[7]
        info["frequency"] = frequencies[7]
        my_dicts.append(info)
        newDictConcept = {"notes": my_dicts}
        save_json()
    if info["relativePitch"] == scale[8] in info.values():
        info["noteName"] = noteValues[8]
        info["frequency"] = frequencies[8]
        my_dicts.append(info)
        newDictConcept = {"notes": my_dicts}
        save_json()
    if info["relativePitch"] == 100 in info.values():
        info["noteName"] = "X"
        info["frequency"] = 0.0
        my_dicts.append(info)
        newDictConcept = {"notes": my_dicts}
        save_json()
    else:
        print("Nothing else to attach.")
       


# for pf in noteDetails["notes"]:
    #  print(pf['relativePitch'])
    #  for contato in pf["pessoaFisica"]["contatos"]:
    #      print(contato["valor"])
