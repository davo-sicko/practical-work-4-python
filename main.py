from PIL import Image
import os, time, multiprocessing, sys

# Обработка одного изображения
def process(path):
    img = Image.open(path)
    img = img.rotate(-90, expand=True)
    img = img.resize((800, 600), Image.LANCZOS)
    img = img.convert("L")
    name = os.path.basename(path)
    img.save(f"processed/out_{name}")

if __name__ == '__main__':
    os.makedirs("processed", exist_ok=True)

    files = [f"img/{f}" for f in os.listdir("img")
             if f.lower().endswith((".jpg", ".jpeg"))]

    if not files:
        sys.exit("Похоже в папке нету ни одной фотографии с jpg форматом")

    mode = sys.argv[1] if len(sys.argv) > 1 else "seq"
    start = time.time()

    if mode == "par":
        with multiprocessing.Pool() as pool:
            pool.map(process, files)
        print(f" Параллельно: {time.time() - start} сек")
        print(f" Файлов: {len(files)}")
    else:
        for f in files:
            process(f)
        print(f"Последовательно: {time.time() - start}")
        print(f"Файлов: {len(files)}")