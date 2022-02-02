files1 = [
    "figure1.jpg",
    "song1.mp3",
    "song2.MP3",
    "video1.Mp4",
    "figure2.jpg",
    "video.mp4"
]

files2 = [
    "figxure1.jpg",
    "song1xx.mp3",
    "sonxxg2.MP3",
    "videxo1.mp4",
    "fixxgure2.jpg",
    "videxo.mp4"
]
# 문제 : files 리스트에서 jpg 파일만 출력하세요

def printBYExt(files, n):
    print(n + "files")
    for file in files :
        # file = file.lower()
        # 알파벳을 소문자로 읽어라
        if file.lower().endswith('.' + n):
            print(file)
    print('-' * 20)

def main():
    printBYExt(files1, 'mp4')
    printBYExt(files1, 'jpg')
    printBYExt(files2, 'mp4')
    printBYExt(files2, 'jpg')
    
main()