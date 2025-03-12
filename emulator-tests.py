import sys
import os

import emu.emulator
sys.path.append(os.getcwd())
import emu
em=emu.emulator.Emulator()
print(em.isReady)   
print(em.version)
print(em.users)
print(em.chkUser("user2","5678"))
print(em.chkUser("user2","1234"))
print(em.chkUser("user3","3456"))


