import os
import shutil

pathLoc1 = "static"
pathLoc2 = "images"
# pathLoc3 = "files"

print(os.path.exists(pathLoc1))
# print(os.path.join(pathLoc1, pathLoc2, pathLoc3))
print(os.listdir("static"))

# shutil.rmtree(os.path.join(pathLoc1, "test_folder"))