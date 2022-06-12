#!/usr/bin/env python3


import json

specific_name = "wellerman"
json_dir_name = '/Users/tchdeveloper1/Documents/Coding Practice/pythonProblems/Note Tile Data/{}/GamePA3-NoteTileData-{}-Alto.json'.format(specific_name, specific_name)

my_dicts = []

with open(json_dir_name, "r") as file:
    data = json.load(file)


    newDictConcept = {"notes" : [my_dicts]}

print("Checking if frequency key exists in JSON")

relativePitchValue = [100, 3, 5, 6, 8, 10, 11, 13, 15]

for info in data["notes"]:
       # print(info)
        #once you know the associated note value to the relative pitch you can likely append them all
         value = 100

         if value in info.values():
            print("Key exist in JSON data")
            print(f"Yes, Value: '{value}' exists in dictionary")
            print(info)

    
            info["noteName"]= "X"
         #   print(info)
            arrayMy = [info]
            arrayMy.append(info)
          #  print(arrayMy)

            my_dicts.append(info)
            newDictConcept = {"notes" : my_dicts}
            print(my_dicts)
            with open(json_dir_name, 'w') as file:
                json.dump(newDictConcept, file)
    #         varTest = ""
        #    print(noteDetails["notes"], "marks is: ", noteDetails["notes"])
         else:
            arrayMy = [info]
            arrayMy.append(info)
          #  print(arrayMy)
            info["noteName"]= "A"
            my_dicts.append(info)
            newDictConcept = {"notes" : my_dicts}
            print(my_dicts)
            with open(json_dir_name, 'w') as file:
                json.dump(newDictConcept, file)
                print("Key doesn't exist in JSON data")

#for pf in noteDetails["notes"]:
  #  print(pf['relativePitch'])
  #  for contato in pf["pessoaFisica"]["contatos"]:
  #      print(contato["valor"])  
