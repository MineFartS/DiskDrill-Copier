from philh_myftp_biz.pc import Path, relscan
from typing import Literal

# ===============================================

SRC = Path('D:/Deleted or lost')

DST = Path('E:/__recovery/Deleted or lost')

# ===============================================

queue: list[dict[Literal['src', 'dst'], Path]] = []

# ===============================================

def get_dst(src:Path, dst:Path):

    while dst.exists():

        if src.size() == dst.size():
            
            return

        dst = dst.sibling(f'{dst.name()} (1).{dst.ext()}')

    return dst

for i in relscan(SRC, DST):

    src = i['src']
    
    dst = get_dst(i['src'], i['dst'])

    print()
    print(f'COPY={dst != None}')
    print(f'{src=}')
    print(f'{dst=}')

    if dst:

        input('paused ...')
        pass
        #src.copy(dst)

# ===============================================