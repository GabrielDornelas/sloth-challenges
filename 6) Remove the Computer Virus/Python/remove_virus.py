def remove_virus(pc_files_str: list[str]) -> str:
    '''Finds the viruses strings in pc_files_str and removes them.
    Bad files will contain "virus" or "malware", but "antivirus" and "notvirus" will not be viruses.

    Args:
        pc_files_str: The input list of strings with PC Files: + each file in the PC.

    Returns:
        list[str]: List with PC Files: Empty" if there are no files left on the computer or PC Files: + safe files.
    '''
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
    func = remove_virus
    inputs = [
        "PC Files: spotifysetup.exe, virus.exe, dog.jpg",
        "PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe",
        "PC Files: notvirus.exe, funnycat.gif",
        "PC Files: virus.exe, lethalmalware.exe, dangerousvirus.bat"
    ]
    for item in inputs:
        print(f"{item}: {func(item)}")
