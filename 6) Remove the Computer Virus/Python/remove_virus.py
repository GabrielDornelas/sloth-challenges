def remove_virus(pc_files_str):
    files_list = pc_files_str.split(': ')[1].split(', ')
    cleaned_list = []

    for file in files_list:
        if 'antivirus' in file or 'notvirus' in file:
            cleaned_list.append(file)
        elif 'virus' not in file and 'malware' not in file:
            cleaned_list.append(file)

    answer = 'PC Files: Empty'
    if len(cleaned_list) > 0:
        answer = 'PC Files: ' + ', '.join(cleaned_list)
        
    return answer

if __name__ == '__main__':
    print(remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg"))
    print(remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe"))
    print(remove_virus("PC Files: notvirus.exe, funnycat.gif"))
    print(remove_virus("PC Files: virus.exe, lethalmalware.exe, dangerousvirus.bat"))
