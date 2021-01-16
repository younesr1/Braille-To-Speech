#!/usr/bin/python3
import os
def cropImage(input_path, output_path = ""):
    if not output_path:
        output_path = input_path
    os.system(f"convert {input_path} -trim {output_path}")
    