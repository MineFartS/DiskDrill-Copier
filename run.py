from philh_myftp_biz.pc import Path, relscan
from typing import Literal

# ===============================================

SRC = Path('D:/')

DST = Path('E:/__recovery/')

# ===============================================

R_SRC = SRC.child('Reconstructed')
R_DST = DST.child('Reconstructed')

DL_SRC = SRC.child('Deleted or lost')
DL_DST = DST.child('Deleted or lost')

# ===============================================

queue: list[dict[Literal['src', 'dst'], Path]] = []

# ===============================================

copied_files = list(DL_DST.descendants())

for i in relscan(R_SRC, R_DST):

    # If no previously copied files have the exact same size
    if not any(cf.size()==i['src'].size() for cf in copied_files):

        print(i)
        print()

        queue += [i]

# ===============================================

for i in relscan(DL_SRC, DL_DST):

    print(i)
    print()

    queue += [i]

# ===============================================

for i in queue:

    print(i)
    print(i)

# ===============================================