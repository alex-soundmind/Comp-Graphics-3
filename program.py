import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import math


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.column1 = tk.Frame(self)
        self.column1.pack(side="left")
        self.column2 = tk.Frame(self)
        self.column2.pack(side="left")

        self.segment1_label = tk.Label(self.column1)
        self.segment1_label["text"] = "Отрезок 1 (x1 y1 x2 y2):"
        self.segment1_label.pack(side="top")
        self.segment1_entry = tk.Entry(self.column1)
        self.segment1_entry.insert(0, "50 30 200 40")
        self.segment1_entry.pack(side="top")
        self.segment2_label = tk.Label(self.column1)
        self.segment2_label["text"] = "Отрезок 2 (x1 y1 x2 y2):"
        self.segment2_label.pack(side="top")
        self.segment2_entry = tk.Entry(self.column1)
        self.segment2_entry.insert(0, "100 80 300 40")
        self.segment2_entry.pack(side="top")

        self.segment3_label = tk.Label(self.column1)
        self.segment3_label["text"] = "Отрезок 3 (x1 y1 x2 y2):"
        self.segment3_label.pack(side="top")
        self.segment3_entry = tk.Entry(self.column1)
        self.segment3_entry.insert(0, "120 120 400 140")
        self.segment3_entry.pack(side="top")

        self.cube_position_label = tk.Label(self.column1)
        self.cube_position_label["text"] = "Координаты положения куба (x y z):"
        self.cube_position_label.pack(side="top")
        self.cube_position_entry = tk.Entry(self.column1)
        self.cube_position_entry.insert(0, "200 200 200")
        self.cube_position_entry.pack(side="top")

        self.cube_side_length_label = tk.Label(self.column1)
        self.cube_side_length_label["text"] = "Длина стороны куба:"
        self.cube_side_length_label.pack(side="top")
        self.cube_side_length_entry = tk.Entry(self.column1)
        self.cube_side_length_entry.insert(0, "50")
        self.cube_side_length_entry.pack(side="top")

        self.scale_label = tk.Label(self.column1)
        self.scale_label["text"] = "Масштабирование (kx ky):"
        self.scale_label.pack(side="top")
        self.scale_entry = tk.Entry(self.column1)
        self.scale_entry.insert(0, "1.3 1.8")
        self.scale_entry.pack(side="top")

        self.translate_label = tk.Label(self.column1)
        self.translate_label["text"] = "Перенос (tx ty):"
        self.translate_label.pack(side="top")
        self.translate_entry = tk.Entry(self.column1)
        self.translate_entry.insert(0, "100 -100")
        self.translate_entry.pack(side="top")

        self.rotate_label = tk.Label(self.column1)
        self.rotate_label["text"] = "Угол поворота (градусы):"
        self.rotate_label.pack(side="top")
        self.rotate_entry = tk.Entry(self.column1)
        self.rotate_entry.insert(0, "45")
        self.rotate_entry.pack(side="top")

        self.image_label = tk.Label(self)
        self.image_label.pack(side="top")

        self.update_image()

    def update_image(self):
        try:
            segment1 = list(map(int, self.segment1_entry.get().split()))
            segment2 = list(map(int, self.segment2_entry.get().split()))
            segment3 = list(map(int, self.segment3_entry.get().split()))
            scale = list(map(float, self.scale_entry.get().split()))
            translate = list(map(float, self.translate_entry.get().split()))
            rotate = float(self.rotate_entry.get())

            image = Image.new("RGB", (800, 600), (255, 255, 255))
            draw = ImageDraw.Draw(image)

            cube_position = list(map(int, self.cube_position_entry.get().split()))
            cube_side_length = int(self.cube_side_length_entry.get())

            cube_points = [
                (cube_position[0] - cube_side_length, cube_position[1] - cube_side_length),
                (cube_position[0] + cube_side_length, cube_position[1] - cube_side_length),
                (cube_position[0] + cube_side_length, cube_position[1] + cube_side_length),
                (cube_position[0] - cube_side_length, cube_position[1] + cube_side_length),
                (cube_position[0] - cube_side_length, cube_position[1] - cube_side_length)
            ]

            draw.polygon(cube_points, fill=(0, 0, 0))

            draw.line([tuple(segment1[:2]), tuple(segment1[2:])], fill=(0, 0, 0))
            draw.line([tuple(segment2[:2]), tuple(segment2[2:])], fill=(0, 0, 0))
            draw.line([tuple(segment3[:2]), tuple(segment3[2:])], fill=(0, 0, 0))

            scaled_segment1 = [(x*scale[0] + translate[0], y*scale[1] + translate[1]) for x, y in [segment1[:2], segment1[2:]]]
            scaled_segment2 = [(x*scale[0] + translate[0], y*scale[1] + translate[1]) for x, y in [segment2[:2], segment2[2:]]]
            scaled_segment3 = [(x*scale[0] + translate[0], y*scale[1] + translate[1]) for x, y in [segment3[:2], segment3[2:]]]

            rotated_segment1 = [(x*math.cos(math.radians(rotate)) - y*math.sin(math.radians(rotate)), x*math.sin(math.radians(rotate)) + y*math.cos(math.radians(rotate))) for x, y in scaled_segment1]
            rotated_segment2 = [(x*math.cos(math.radians(rotate)) - y*math.sin(math.radians(rotate)), x*math.sin(math.radians(rotate)) + y*math.cos(math.radians(rotate))) for x, y in scaled_segment2]
            rotated_segment3 = [(x*math.cos(math.radians(rotate)) - y*math.sin(math.radians(rotate)), x*math.sin(math.radians(rotate)) + y*math.cos(math.radians(rotate))) for x, y in scaled_segment3]

            draw.line([tuple(rotated_segment1[0]), tuple(rotated_segment1[1])], fill=(255, 0, 0))
            draw.line([tuple(rotated_segment2[0]), tuple(rotated_segment2[1])], fill=(255, 0, 0))
            draw.line([tuple(rotated_segment3[0]), tuple(rotated_segment3[1])], fill=(255, 0, 0))

            scale = list(map(float, self.scale_entry.get().split()))
            translate = list(map(float, self.translate_entry.get().split()))

            rotated_cube_points = [
                (cube_position[0] + (x - cube_position[0]) * math.cos(math.radians(rotate)) - (y - cube_position[1]) * math.sin(math.radians(rotate)),
                cube_position[1] + (x - cube_position[0]) * math.sin(math.radians(rotate)) + (y - cube_position[1]) * math.cos(math.radians(rotate)))
                for x, y in cube_points
            ]

            scaled_cube_points = [(x * scale[0] + translate[0], y * scale[1] + translate[1]) for x, y in rotated_cube_points]

            draw.polygon(scaled_cube_points, fill=(255, 0, 0))

            image_tk = ImageTk.PhotoImage(image)
            self.image_label.config(image=image_tk)
            self.image_label.image = image_tk
        except:
            pass

        self.after(1000, self.update_image)

import math

root = tk.Tk()
app = Application(master=root)
app.mainloop()
