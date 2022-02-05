from pygame import mixer
def main():
    song_path='c:/temp/music/After_You.mp3'
    song_path2='c:/temp/music/Burkinelectric.mp3'

    mixer.init()
    song = mixer.Sound(song_path) # 믹서 모듈안의 정의된 Sound 클래스의 인스턴스를 생성
    song.play()
    input("정리하려면 엔터")
    song.stop()

    song = mixer.Sound(song_path2)
    song.play()
    input("정리하려면 엔터")
    song.stop()

main()
