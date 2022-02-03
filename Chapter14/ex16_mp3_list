# C:\temp\music 폴더에서 mp3 파일만 목록으로 출력하세요
import os

def get_file_list(dir_path, ext):
    
    files = os.listdir(dir_path)
    # dir_path 내에 모든 파일과 디렉토리 리스트를 린턴한다.
    
    files = list(filter(lambda name : name.endswith(ext), files)) 
    return files

def main():
    DIR_PATH = 'C:/temp/music'
    songs = get_file_list(DIR_PATH, '.mp3')
    
    # 절대 경로로 출력하세요
    # os.path.getsize(파일경로)
    
    for f in songs:
        print(f'{DIR_PATH}/{f}')
        
        print(os.path.join(DIR_PATH, f)) # 경로들을 결합시켜라

main()