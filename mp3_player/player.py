import os
import sys
from pygame import mixer
import eyed3
from file_util import get_file_list

DIR_PATH = 'C:/temp/music' # 음악 파일 디렉토리
song_list = []                           # 재생 목록 
song = None                              # 현재 재생중인 파일
current_index = -1                       # 현재 재생 파일의 인덱스

# 메뉴
# 목록 재생 정지 이전 다음 종료

def init():
    global song_list
    mixer.init()
    song_list = get_file_list(DIR_PATH, '.mp3')
    
    print(song_list)
    
def print_list():
    for ix, song in enumerate(song_list):
        print(f'{ix}] {song}')
    
    print()
    
def play():
    # 선곡: 2
    global current_index, song
    current_index = int(input('선곡: '))
    
    # 이전에 재생중이면 먼저 정지
    if song:
        song.stop()
    
    song_path = os.path.join(DIR_PATH, song_list[current_index])
    song = mixer.Sound(song_path)
    song.play()



def print_tag(file_path):
    s = eyed3.load(file_path)
    if (s.tag.artist and s.tag.album and s.tag.title ) == 0: 
        
        print (f'가수:  {s.tag.artist}')
        print (f'앨범:  {s.tag.album}')
        print (f'곡명:  {s.tag.title}')
    else:
        print(file_path)



def play_music(index):
    global song
    
    song_path = os.path.join(DIR_PATH, song_list[index])
    print_tag(song_path)
    print(f'곡명: {song_list[index]}')
    song = mixer.Sound(song_path)
    song.play()   

def stop():
    global song
    if song:
        song.stop()
    song = None

# 다음 곡 재생
def play_prev():
    global song, current_index
    
    current_index -= 1
    if current_index == -1:
        current_index = len(song_list)-1
    if song:
        song.stop()
    play_music(current_index)

def play_next():
    global song, current_index
    current_index += 1
    
    if current_index == len(song_list) :
        current_index= 0
    # current_index = (current_index + 1) % len(song_list)
    if song:
        song.stop()
    play_music(current_index)

def exit():
   sys.exit(0)

def print_menu():
    print("-"*40)
    print("목록 재생 정지 이전 다음 종료")
    print("-"*40) 

def main():
    init()
    while True :
        print_menu()
        select = input('선택> ')
        
        if select == '목록':
            print_list()
        elif select == '재생':
            play()
        elif select == '정지':
            stop()
        elif select == '이전':
            play_prev()
        elif select == '다음':
            play_next()
        elif select == '종료':
            exit() 
main()