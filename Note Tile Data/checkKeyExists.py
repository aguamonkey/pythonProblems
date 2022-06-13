#!/usr/bin/env python3


import json

specific_name = "wellerman"
voice_type = "Soprano"
json_dir_name = '/Users/tchdeveloper1/Documents/Coding Practice/pythonProblems/Note Tile Data/{}/GamePA3-NoteTileData-{}-{}.json'.format(specific_name, specific_name, voice_type)

my_dicts = []

with open(json_dir_name, "r") as file:
    data = json.load(file)


    newDictConcept = {"notes" : [my_dicts]}

print("Checking if frequency key exists in JSON")
#Wellerman relative pitch.
relativePitchValue = [100, 3, 5, 6, 8, 10, 11, 13, 15]
notesInSong = ["X", "C4", "D4", "Eb4", "F4", "G4", "Ab4", "Bb4", "C5"]

def save_json():
  with open(json_dir_name, 'w') as file:
                json.dump(newDictConcept, file)

for info in data["notes"]:
       # print(info)
        #once you know the associated note value to the relative pitch you can likely append them all
    
          if 100 in info.values():
            info["noteName"]= "X"
            my_dicts.append(info)
            newDictConcept = {"notes" : my_dicts}
            save_json()
            
          if 3 in info.values():
            info["noteName"]= "C4"
            my_dicts.append(info)
            newDictConcept = {"notes" : my_dicts}
            save_json()
          if 5 in info.values():
            info["noteName"]= "D4"
            my_dicts.append(info)
            newDictConcept = {"notes" : my_dicts}
            save_json()
          if 6 in info.values():
            info["noteName"]= "Eb4"
            my_dicts.append(info)
            newDictConcept = {"notes" : my_dicts}
            save_json()
          if 8 in info.values():
            info["noteName"]= "F4"
            my_dicts.append(info)
            newDictConcept = {"notes" : my_dicts}
            save_json()
          if 10 in info.values():
            info["noteName"]= "G4"
            my_dicts.append(info)
            newDictConcept = {"notes" : my_dicts}
            save_json()
          if 11 in info.values():
            info["noteName"]= "Ab4"
            my_dicts.append(info)
            newDictConcept = {"notes" : my_dicts}
            save_json()
          if 13 in info.values():
            info["noteName"]= "Bb4"
            my_dicts.append(info)
            newDictConcept = {"notes" : my_dicts}
            save_json()
          if 15 in info.values():
            info["noteName"]= "C5"
            my_dicts.append(info)
            newDictConcept = {"notes" : my_dicts}
            save_json()
          else:
            print("Nothing else to attach.")
                

#for pf in noteDetails["notes"]:
  #  print(pf['relativePitch'])
  #  for contato in pf["pessoaFisica"]["contatos"]:
  #      print(contato["valor"])  
