from philh_myftp_biz.pc import Path, relscan
from philh_myftp_biz.terminal import warn

# ===============================================

SRC = Path('D:/Deleted or lost/')

DST = Path('E:/__recovery/Deleted or lost/')

# ===============================================

def get_dst(src:Path, dst:Path) -> None | Path:

    # Loop while the destination path exists
    while dst.exists():

        # If the size is the same
        if src.size() == dst.size():        
            
            # Output None
            return

        # If the size is different
        else:

            # Append a '(1)' to the end of the filename
            dst = dst.sibling(f'{dst.name()} (1).{dst.ext()}')

    # Output the destination path
    return dst

#
for i in relscan(src=SRC, dst=DST):

    src: Path = i['src']
    
    dst: None | Path = get_dst(src=i['src'], dst=i['dst'])

    #
    if dst:

        print()
        print(f'{src=}')
        print(f'{dst=}')
        print()

        #
        try:
            src.copy(dst)
        except OSError as e:
            warn(e)

    #
    else:

        print(src)

# ===============================================