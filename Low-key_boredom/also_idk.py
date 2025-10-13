#ASCII Art
import time
import os
frames = [f"""(O-O)
 -|-
 /\\""",f"""(O-O)
 -|-__
 /""", f"""  (O-O)
 __-|-
     \\""", f"""  (O-O)
   -|-
    /\\"""]

for i in frames:
    os.system("cls" if os.name == "nt" else "clear")
    print(i)
    time.sleep(.5)