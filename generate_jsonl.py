import json
import os


if __name__ == '__main__':
    result = list()
    for filename in os.listdir('premises/'):
        with open('premises/%s' % filename, 'r', encoding='utf-8') as infile:
            premise = infile.read()
        new_filename = filename.replace('premise', 'script')
        with open('scripts/%s' % new_filename, 'r', encoding='utf-8') as infile:
            script = infile.read()
        info = {'prompt': premise + '\n\nSCRIPT: ', 'completion': ' ' + script}
        result.append(info)
    with open('scripts.jsonl', 'w') as outfile:
        for i in result:
            json.dump(i, outfile)
            outfile.write('\n')