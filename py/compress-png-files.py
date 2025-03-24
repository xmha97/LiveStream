import os
import glob
from zopflipng import png_optimize
input_folder = "..\\"
output_folder = "..\\png"
os.makedirs(output_folder, exist_ok=True)
png_files = glob.glob(os.path.join(input_folder, "*.png"))
for file_path in png_files:
    with open(file_path, 'rb') as f:
        data = f.read()
    result, code = png_optimize(data)
    if code == 0:
        output_path = os.path.join(output_folder, os.path.basename(file_path))
        with open(output_path, 'wb') as f:
            f.write(result)        
        print(f"Optimized: {file_path} → {output_path}")
    else:
        print(f"Error in processing: {file_path}")
