#!/usr/bin/env python
import time
import sys

FILENAME_TEMPLATE="DI_Logo_D{diameter}mm.kicad_mod"
TEMPLATE="""\
(module DI_Logo_D{diameter}mm (layer F.Cu) (tedit {timestamp:X})
  (tags "DI Logo")
  (fp_text reference "" (at 0 1.9) (layer F.SilkS) hide
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value "" (at 0 -2.025) (layer F.Fab) hide
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_line (start {pos_x} -{pos_y}) (end {pos_x} {pos_y}) (layer F.SilkS) (width {line_width}))
  (fp_line (start {pos_x} 0) (end -{pos_x} -{pos_y}) (layer F.SilkS) (width {line_width}))
  (fp_line (start -{pos_x} -{pos_y}) (end -{pos_x} {pos_y}) (layer F.SilkS) (width {line_width}))
  (fp_line (start -{pos_x} {pos_y}) (end {pos_x} 0) (layer F.SilkS) (width {line_width}))
  (fp_circle (center 0 0) (end {radius} 0) (layer F.SilkS) (width {line_width}))
)
"""


if len(sys.argv) != 2:
    print("usage: generate.py <diameter>")
    exit(1)

diameter = int(sys.argv[1])

dimensions = {
        'diameter': 1,
        'radius': 0.5,
        'pos_x': 0.225,
        'pos_y': 0.4465,
        'line_width': 0.1,
}

for e in dimensions:
    dimensions[e] *= diameter

timestamp=int(time.time())

filename = FILENAME_TEMPLATE.format(**dimensions)
with open(filename, 'w') as outf:
    outf.write(TEMPLATE.format(timestamp=timestamp, **dimensions))
