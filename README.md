# phonoclan

Insert and extract phonetic transcriptions from CLAN files



## usage

#### insert the %pho's


```
$ python insertphon.py clanfile.cha:
```

This will put a %pho comment tier under every annotated instance where
speaker code is CHI. If there is more than one CHI annotated word on a
single line, there will still only be a single %pho line following it.
You should separate the multiple CHI phonetic transcriptions by a space.


#### extract %pho annotations:

```
$ python extractphon.py clanfile.cha
```

This will pull out all the phonetic annotations from clanfile.cha and
fill them into a csv file called extracted_pho.csv