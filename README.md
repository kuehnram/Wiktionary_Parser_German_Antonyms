# German Antonyms
This repository offers a Python Dictionary of German words and their antonyms from the German Wiktionary.
It was built based on the dump of 2021-11-21 17:50:44.


# Applications and References
This antonym resource can be used for antithesis detection in the German language.
For more information, please see:

**Ramona Kühn, Jelena Mitrović, and Michael Granitzer. "Hidden in Plain Sight: Resources and Methods for Detecting German Antitheses in Telegram". (2022, unpublished).**

# Usage
To load the Dictionary and to work with, you can use following code:
```
# load antonym dictionary
with open("AntonymDict.txt", mode="r", encoding="utf-8") as f:
    antonym_file = f.read()
antonym_dict = ast.literal_eval(antonym_file)

```

# Wiktionary Parser
Please go to https://github.com/kuehnram/Antithesis_Detection/tree/main/WiktionaryParser to download the parser that created this antonym resource.
