# phonoclan

Insert and extract phonetic transcriptions from CLAN files


## dependencies

This package depends on [pyclan](https://github.com/SeedlingsBabylab/pyclan)


## usage

#### insert the %pho's


```
$ python insertphon.py clanfile.cha:
```

This will put a %pho comment tier under every annotated instance where
speaker code is CHI. If there is more than one CHI annotated word on a
single line, there will still only be a single %pho line following it.
You should separate the multiple CHI phonetic transcriptions by a space.

If your input file is 44_17_final.cha, the output will be called
44_17_with_pho.cha.


#### extract %pho annotations:

```
$ python extractphon.py clanfile.cha
```

This will pull out all the phonetic annotations from clanfile.cha and
fill them into a csv file called extracted_pho.csv