import os
from os import walk, listdir, system
from os.path import join, isfile

def find_in_file(content, starting):
    return [c for c in content if c.startswith(starting)]

folder_to_search = './'
folders_with_file = []
for path, directories, files in walk(folder_to_search):
    if files:  # Find folders not empty
        folders_with_file.append(path)

with open('transcripts.txt', 'r') as inp:
    content = inp.readlines()

folders_with_file.remove('./')
folders_with_file.remove('./.ipynb_checkpoints')


for folder in folders_with_file:
    print(folder)
    #first_level = folder.split('/')[1]
    #second_level = folder.split('/')[2]
    #folder_path = join(folder, file_name)
    #single_file = find_in_file(content, '{}-{}'.format(first_level, second_level))
    all_files = [f for f in listdir(folder) if isfile(join(folder,f))]
    all_files = [f for f in all_files if f.endswith('flac')]
    for f in all_files:
        info_audio = f.replace('.flac', '').split('_')
        track_name = '{}_{}_{}'.format(info_audio[0], info_audio[1], info_audio[2])
        single_file = find_in_file(content, track_name)
        file_name = '{}_{}_{}.txt'.format(info_audio[0], info_audio[1], info_audio[2])
        with open(join(folder, file_name), 'w') as out:
            if len(single_file) != 1:
                print('Stranoooo {}'.format(file_name))
                print(single_file)
            else:
                out.write(single_file[0].replace(track_name, '').lstrip())