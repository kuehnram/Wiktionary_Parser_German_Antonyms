# German_Antonyms
This repository offers a Python Dictionary of German words and their antonyms from the German Wiktionary.
It was built based on the dump of 2021-11-21 17:50:44.

For more information, please refer to Ramona Kühn, Jelena Mitrović, and Michael Granitzer. "Hidden in Plain Sight: Resources and Methods for Detecting German Antitheses in Telegram". (2022, unpublished).


To load the Dictionary and to work with, you can use following code:
```
# load antonym dictionary
with open("AntonymDict.txt", mode="r", encoding="utf-8") as f:
    antonym_file = f.read()
antonym_dict = ast.literal_eval(antonym_file)

```
