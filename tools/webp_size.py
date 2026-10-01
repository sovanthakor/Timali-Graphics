"""Reads dimensions straight from WebP headers (no Pillow needed)."""
import os, struct, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "assets", "img", "portfolio")


def webp_size(path):
    with open(path, "rb") as f:
        d = f.read(64)
    if d[:4] != b"RIFF" or d[8:12] != b"WEBP":
        return None
    fourcc = d[12:16]
    if fourcc == b"VP8 ":
        # 3-byte frame tag, 3-byte sync 0x9D 0x01 0x2A, then 16-bit w/h (14 bits used)
        w, h = struct.unpack("<HH", d[26:30])
        return w & 0x3FFF, h & 0x3FFF
    if fourcc == b"VP8L":
        b = d[21:26]
        bits = int.from_bytes(b, "little")
        w = (bits & 0x3FFF) + 1
        h = ((bits >> 14) & 0x3FFF) + 1
        return w, h
    if fourcc == b"VP8X":
        w = int.from_bytes(d[24:27], "little") + 1
        h = int.from_bytes(d[27:30], "little") + 1
        return w, h
    return None


for p in sorted(glob.glob(os.path.join(D, "*.webp"))):
    s = webp_size(p)
    name = os.path.basename(p)
    if s:
        w, h = s
        ratio = w / h
        tag = "4:3" if abs(ratio - 4/3) < 0.03 else ("16:9" if abs(ratio - 16/9) < 0.03 else ("1:1" if abs(ratio-1) < 0.03 else "other"))
        print(f"{name:<28} {w}x{h}   ratio {ratio:.2f}  ({tag})")
    else:
        print(f"{name:<28} could not parse")
