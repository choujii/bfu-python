from moviepy.video.io.VideoFileClip import VideoFileClip
import sys

def extract_video_segment(input_file, start_time, end_time, output_file):
    # Загружаем видеофайл
    with VideoFileClip(input_file) as video:
        # Извлекаем нужный фрагмент
        video_segment = video.subclip(start_time, end_time)
        # Сохраняем извлеченный фрагмент
        video_segment.write_videofile(output_file, codec='libx264')

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Использование: python lvov_m_lab4_1.py <входной файл> <время начала> <время окончания> <выходной файл>")
        sys.exit(1)

    input_file = sys.argv[1]
    start_time = float(sys.argv[2])  # Время начала в секундах
    end_time = float(sys.argv[3])      # Время окончания в секундах
    output_file = sys.argv[4]

    extract_video_segment(input_file, start_time, end_time, output_file)



