#ASCII Art
import time
import os
frames = [f"""🟥🟥🟥🟥🟥🟥
🟥        🟥
🟥        🟥
🟥        🟥
🟥🟥🟥🟥🟥🟥
     🟥
     🟥
🟥🟥🟥🟥🟥🟥
     🟥
     🟥
🟥🟥🟥🟥🟥🟥
🟥        🟥
🟥        🟥
🟥        🟥
🟥        🟥
""",f"""🟧🟧🟧🟧🟧🟧
🟧        🟧
🟧        🟧
🟧        🟧
🟧🟧🟧🟧🟧🟧
     🟧
     🟧
🟧🟧🟧🟧🟧🟧
     🟧
     🟧
🟧🟧🟧🟧🟧🟧
🟧        🟧
🟧        🟧
🟧        🟧
🟧        🟧
""",f"""🟨🟨🟨🟨🟨🟨
🟨        🟨
🟨        🟨
🟨        🟨
🟨🟨🟨🟨🟨🟨
     🟨
     🟨
🟨🟨🟨🟨🟨🟨
     🟨
     🟨
🟨🟨🟨🟨🟨🟨
🟨        🟨
🟨        🟨
🟨        🟨
🟨        🟨"""]
for i in frames:
    os.system(("cls" if os.name == "nt" else "clear"))
    print(i)
    time.sleep(1)