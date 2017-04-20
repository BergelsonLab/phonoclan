import pyclan as pc
import sys
import os


def insert_pho(input):
    clan_file = pc.ClanFile(input)

    out = os.path.basename(input)[:5]+"_with_pho.cha"
    results = clan_file.get_with_speaker("CHI")

    inserted_lines = []

    for x in results:
        if x.index not in inserted_lines:
            inserted_lines.append(x.index)
            line = pc.ClanLine(index=x.index + 1, line="%pho:\t\n")
            clan_file.insert_line(line, x.index + 1)
    clan_file.write_to_cha(out)


if __name__ == "__main__":

    in_file = sys.argv[1]

    insert_pho(in_file)
