from directory_functions import scan_directory
from Image import Image as ImgClass

def test_task(img_path):
    img = ImgClass(img_path)
    img.show_faces()
    img.release()
    return img.get_img_data()

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    scan_directory(folder, task=test_task)