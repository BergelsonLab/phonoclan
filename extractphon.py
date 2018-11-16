import pyclan as pc
import sys
import csv


def extract_pho(input):
    clan_file = pc.ClanFile(input)
    results = clan_file.get_with_speaker("CHI")

    phos = []
    for x in results:
        next_line = clan_file.line_map[x.index+1]
        i=2
        while (next_line.line[0]=='\t'):
            next_line = clan_file.line_map[x.index+i]
            i += 1
        if not next_line.line.startswith("%pho:"):
            print(next_line.line, next_line.line[1])
            raise Exception("next line wasn't a %pho:  line #{}".format(next_line.index))
        phos.append((x, next_line))

    extracted = []

    for group in phos:

        matches = pc.code_regx.findall(group[0].content)
        print('matches',matches)
        phons = group[1].content.split()
        words = [x for x in matches if x[7] == "CHI"]
        print('words',words)
        if len(words) != len(phons):
            raise Exception("mismatch between # of CHI utts and %pho transcriptions: \n{} vs. {}".format(words,
                                                                                                         group[1]))
        for i, x in enumerate(words):
            extracted.append((x[0], x[3], x[5], x[7], x[9], phons[i], group[0].onset, group[0].offset))

    return extracted


def output_extracted(phos):
    with open("extracted_pho.csv", "wb") as out:
        writer = csv.writer(out)
        writer.writerow(["object", "utt_type", "object_present", "speaker", "hex_id", "phonetic", "onset", "offset"])
        writer.writerows(phos)


if __name__ == "__main__":

    cha_in = sys.argv[1]
    # bl_in = sys.argv[2]
    extracted = extract_pho(cha_in)
    output_extracted(extracted)
