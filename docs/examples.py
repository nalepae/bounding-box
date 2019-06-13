#!/usr/bin/env python

from __future__ import print_function
import cv2
from bounding_box import bounding_box as bb
import os

def show_and_save(title, image, path):
    cv2.imwrite(path, image)
    cv2.imshow(title, image)
    print("Press 'Enter' to display the next picture...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    in_path = os.path.join("docs", "images", "winton.jpg")
    out_path = os.path.join("docs", "images", "winton_bb.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    bb.add_bounding_box(image, 281, 12, 744, 431, "Winton", "maroon")
    bb.add_bounding_box(image, 166, 149, 500, 297, "Trumpet", "yellow")
    show_and_save("Winton MARSALIS", image, out_path)

    in_path = os.path.join("docs", "images", "khatia.jpg")
    out_path = os.path.join("docs", "images", "khatia_bb.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    bb.add_bounding_box(image, 280, 24, 802, 593, "Khatia", "maroon")
    bb.add_bounding_box(image, 687, 1, 1448, 648, "Piano", "gray")
    bb.add_bounding_box(image, 888, 492, 1190, 536, "Text")
    show_and_save("Khatia BUNIATISHVILI", image, out_path)

    in_path = os.path.join("docs", "images", "clarifloue.jpg")
    out_path = os.path.join("docs", "images", "clarifloue_bb.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    bb.add_bounding_box(image, 69, 86, 470, 136, label="Headache designer")
    bb.add_bounding_box(image, 136, 196, 406, 234, "Text")
    bb.add_bounding_box(image, 67, 351, 471, 400, "Headache designer")
    bb.add_bounding_box(image, 130, 456, 390, 494, "Text")
    show_and_save("Clarinet", image, out_path)

    in_path = os.path.join("docs", "images", "nao-romeo-pepper.jpg")
    out_path = os.path.join("docs", "images", "nao-romeo-pepper_bb.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    bb.add_bounding_box(image, 155, 152, 244, 297, "Nao")
    bb.add_bounding_box(image, 260, 6, 423, 416, "Romeo")
    bb.add_bounding_box(image, 421, 76, 547, 402, "Pepper")
    show_and_save("Robots", image, out_path)

    in_path = os.path.join("docs", "images", "ski-paraglider.jpg")
    out_path = os.path.join("docs", "images", "ski-paraglider_bb.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    bb.add_bounding_box(image, 0, 128, 645, 589, "Paraglider", "orange")
    bb.add_bounding_box(image, 689, 442, 818, 566, "Skier", "gray")
    show_and_save("Ski and paraglider", image, out_path)

    in_path = os.path.join("docs", "images", "paragliders.jpg")
    out_path = os.path.join("docs", "images", "paragliders_bb.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    bb.add_bounding_box(image, 90, 228, 318, 428, "Paraglider")
    bb.add_bounding_box(image, 521, 110, 656, 415, "Paraglider")
    show_and_save("Pretty Bounding Box", image, out_path)

    in_path = os.path.join("docs", "images", "selfie.jpg")
    out_path = os.path.join("docs", "images", "selfie_bb.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    bb.add_bounding_box(image, 5, 7, 150, 169, "Female", "fuchsia")
    bb.add_bounding_box(image, 116, 7, 193, 113, "Male", "blue")
    bb.add_bounding_box(image, 189, 7, 291, 124, "Female", "fuchsia")
    bb.add_bounding_box(image, 288, 25, 355, 114, "Male", "blue")
    bb.add_bounding_box(image, 367, 0, 448, 92, "Male", "blue")
    bb.add_bounding_box(image, 435, 29, 506, 104, "Female", "fuchsia")
    bb.add_bounding_box(image, 497, 3, 597, 111, "Female", "fuchsia")
    bb.add_bounding_box(image, 110, 133, 213, 245, "Female", "fuchsia")
    bb.add_bounding_box(image, 176, 120, 293, 289, "Female", "fuchsia")
    bb.add_bounding_box(image, 314, 115, 470, 357, "Male", "blue")
    bb.add_bounding_box(image, 468, 72, 577, 226, "Male", "blue")
    show_and_save("The Selfie", image, out_path)

    in_path = os.path.join("docs", "images", "pobb.jpg")
    out_path = os.path.join("docs", "images", "pobb_bb.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    bb.add_bounding_box(image, 76, 62, 155, 271, "Female", "fuchsia")
    bb.add_bounding_box(image, 157, 44, 288, 274, "Male", "blue")
    bb.add_bounding_box(image, 224, 64, 317, 274, "Male", "blue")
    bb.add_bounding_box(image, 290, 48, 383, 277, "Male", "blue")
    bb.add_bounding_box(image, 350, 42, 458, 276, "Female", "fuchsia")
    bb.add_bounding_box(image, 416, 17, 510, 279, "Male", "blue")
    bb.add_bounding_box(image, 482, 55, 573, 278, "Female", "fuchsia")
    bb.add_bounding_box(image, 547, 63, 615, 277, "Female", "fuchsia")
    bb.add_bounding_box(image, 608, 49, 704, 275, "Female", "fuchsia")
    bb.add_bounding_box(image, 672, 34, 767, 274, "Male", "blue")
    bb.add_bounding_box(image, 725, 62, 813, 273, "Female", "fuchsia")
    bb.add_bounding_box(image, 786, 38, 887, 267, "Male", "blue")
    bb.add_bounding_box(image, 864, 51, 959, 266, "Male", "blue")
    show_and_save("POBB", image, out_path)

if __name__ == "__main__":
    main()
