import cv2

def play_video_with_info(video_path): #Воспроизведение видео и отображение параметров: имя файла, fps, ширина,высота
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Ошибка: Не удалось открыть видеофайл.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    video_name = video_path.split('/')[-1]  

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Достигнут конец видео.")
            break

        text = (f"File: {video_name}, FPS: {fps:.2f}, "
                f"Width: {int(width)}, Height: {int(height)}")
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = "input_video.mp4"
    play_video_with_info(video_path)
