# Wiktionary Parser to Extract German Antonyms
This repository offers a Python Dictionary of German words and their antonyms from the German Wiktionary.
It was built based on the Wiktionary dump of 2021-11-21 17:50:44.
If used, please cite

```
@inproceedings{kuehn2023hidden,
  title={Hidden in Plain Sight: Can German Wiktionary and Wordnets Facilitate the Detection of Antithesis?},
  author={K{\"u}hn, Ramona and Mitrovic, Jelena and Granitzer, Michael},
  booktitle={12th International Global Wordnet Conference},
  year={2023}
}
```


## Applications and Usage
This antonym resource can be used to find antonyms or for antithesis detection in the German language.
The keys are the actual word, the values are its antonyms.
There are two versions of the AntonymDict: one is case sensitive (AntonymDictCaseSensitiv.txt, based on dump from 01.03.2023), and one is completely lowercase (AntonymDict.txt), which was used in the paper mentioned above.

To load the Dictionary and to work with, you can use following code:
```
import ast

# load antonym dictionary
with open("AntonymDict.txt", mode="r", encoding="utf-8") as f:
    antonym_file = f.read()
antonym_dict = ast.literal_eval(antonym_file)

```

## Wiktionary Parser
It is based on regular expressions to extract the antonyms ("Gegenwörter"). It only selects antonyms in the German language. It can be extended to also extract synonyms, idiomatic expressions, etc.

## Acknowledgement
The project on which this report is based was funded by the German Federal Ministry of Education and Research (BMBF) under the funding code 01IS20049. The authors are responsible for the content of this publication.

<img src="https://github.com/user-attachments/assets/5e1ca975-704b-417b-958a-9fbfb6a893d8" width="400" height="300">
