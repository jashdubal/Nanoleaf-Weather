from __future__ import annotations

import random
import time
from weather import Weather


import data
from nanoleaf import Nanoleaf, PanelUpdate

nl = Nanoleaf()
nl1 = Nanoleaf()
weath = Weather()

# random hex colors
colors = ["#92ac1d", "#58f982", "#bf6070", "#0eff1f", "#8d2b5d", "#db684c", "#FFFFFF"]
color = "#0000FF"
color1 = "#92ac1d"

class Nums():
    updatesL9 = [
        # Left 9:
        # top
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        # middle
        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),

        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 7, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        #
        PanelUpdate(4, 7, color),
        PanelUpdate(4, 8, color),
        #
        # PanelUpdate(6,5,color),
        # PanelUpdate(6,6,color),
        #
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
        # bottom right
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color)

    ]

    updatesL8 = [
        # Left eight:
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        #
        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),
        #
        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 7, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        #
        PanelUpdate(4, 7, color),
        PanelUpdate(4, 8, color),
        #
        PanelUpdate(6, 5, color),
        PanelUpdate(6, 6, color),
        #
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
        # bottom right
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color)

    ]

    updatesL7 = [
        # Left seven:
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        #
        # PanelUpdate(5,6,color),
        # PanelUpdate(5,7,color),
        # PanelUpdate(5,8,color),
        # PanelUpdate(5,9,color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),
        #
        # PanelUpdate(7,4,color),
        # PanelUpdate(7,5,color),
        # PanelUpdate(7,6,color),
        # PanelUpdate(7,7,color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        #
        # PanelUpdate(4,7,color),
        # PanelUpdate(4,8,color),
        #
        # PanelUpdate(6,5,color),
        # PanelUpdate(6,6,color),
        #
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
        # bottom right
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color)

    ]

    updatesL6 = [
        # Left eight:
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        #
        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),
        #
        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 7, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        #
        PanelUpdate(4, 7, color),
        PanelUpdate(4, 8, color),
        #
        PanelUpdate(6, 5, color),
        PanelUpdate(6, 6, color),
        #
        # PanelUpdate(4,11,color),
        # PanelUpdate(4,12,color),
        # bottom right
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color)

    ]

    updatesL5 = [
        # Left eight:
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        #
        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),
        #
        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 7, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        #
        PanelUpdate(4, 7, color),
        PanelUpdate(4, 8, color),
        #
        # PanelUpdate(6,5,color),
        # PanelUpdate(6,6,color),
        #
        # PanelUpdate(4,11,color),
        # PanelUpdate(4,12,color),
        # bottom right
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color)

    ]

    updatesL4 = [
        # Left eight:
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        # PanelUpdate(3,10,color),
        # PanelUpdate(3,11,color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        #
        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),
        #
        # PanelUpdate(7,4,color),
        # PanelUpdate(7,5,color),
        # PanelUpdate(7,6,color),
        # PanelUpdate(7,7,color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        #
        PanelUpdate(4, 7, color),
        PanelUpdate(4, 8, color),
        #
        # PanelUpdate(6,5,color),
        # PanelUpdate(6,6,color),
        #
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
        # bottom right
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color)

    ]

    updatesR3 = [
        PanelUpdate(4, 13, color1, 10),
        PanelUpdate(4, 14, color1, 10),
        PanelUpdate(4, 15, color1, 10),
        PanelUpdate(4, 16, color1, 10),
        PanelUpdate(4, 17, color1, 10),
        PanelUpdate(4, 18, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        PanelUpdate(6, 12, color1, 10),
        PanelUpdate(6, 13, color1, 10),
        PanelUpdate(6, 14, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        PanelUpdate(8, 10, color1, 10),
        PanelUpdate(8, 11, color1, 10),
        PanelUpdate(8, 12, color1, 10),
        PanelUpdate(8, 13, color1, 10),
        PanelUpdate(8, 14, color1, 10),
        PanelUpdate(6, 16, color1, 10),
        PanelUpdate(8, 9, color1, 10),

        PanelUpdate(4, 13, color1, 10),
        # PanelUpdate(5, 13, color1, 10),
        # PanelUpdate(5, 12, color1, 10),
        PanelUpdate(6, 12, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        PanelUpdate(4, 18, color1, 10),
        PanelUpdate(4, 17, color1, 10),
        PanelUpdate(5, 17, color1, 10),
        PanelUpdate(5, 16, color1, 10),
        PanelUpdate(6, 16, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        # PanelUpdate(7, 11, color1, 10),
        # PanelUpdate(7, 10, color1, 10),
        PanelUpdate(8, 10, color1, 10),
        PanelUpdate(8, 9, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        PanelUpdate(7, 15, color1, 10),
        PanelUpdate(7, 14, color1, 10),
        PanelUpdate(8, 14, color1, 10),
        PanelUpdate(8, 13, color1, 10),
    ]

    updatesL0 = [
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color),
        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 7, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        PanelUpdate(6, 5, color),
        PanelUpdate(6, 6, color),
        PanelUpdate(4, 7, color),
        PanelUpdate(4, 8, color)
    ]

    updatesL1 = [
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(4, 9, color),
        PanelUpdate(4, 10, color),
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(6, 7, color),
        PanelUpdate(6, 8, color),
        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 7, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color)
    ]

    updatesL2 = [
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),
        PanelUpdate(6, 5, color),
        PanelUpdate(6, 7, color),
        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color)
    ]

    updatesL3 = [
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color),
        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color)
    ]
    #######RIGHT#####

    updateR9 = [
        PanelUpdate(4, 13, color1),
        PanelUpdate(5, 13, color1),
        PanelUpdate(5, 12, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(4, 18, color1),
        PanelUpdate(4, 13, color1),
        PanelUpdate(4, 14, color1),
        PanelUpdate(4, 15, color1),
        PanelUpdate(4, 16, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(4, 18, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 13, color1),
        PanelUpdate(6, 14, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(4, 18, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(5, 17, color1),
        PanelUpdate(5, 16, color1),
        PanelUpdate(6, 16, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(7, 15, color1),
        PanelUpdate(7, 14, color1),
        PanelUpdate(8, 14, color1),
        PanelUpdate(8, 13, color1),
    ]

    updateR6 = [PanelUpdate(4, 13, color1),
                PanelUpdate(5, 13, color1),
                PanelUpdate(5, 12, color1),
                PanelUpdate(6, 12, color1),
                PanelUpdate(6, 11, color1),
                PanelUpdate(7, 11, color1),
                PanelUpdate(7, 10, color1),
                PanelUpdate(8, 10, color1),
                PanelUpdate(8, 9, color1),
                PanelUpdate(8, 10, color1),
                PanelUpdate(8, 11, color1),
                PanelUpdate(8, 12, color1),
                PanelUpdate(8, 13, color1),
                PanelUpdate(8, 14, color1),
                PanelUpdate(6, 15, color1),
                PanelUpdate(7, 15, color1),
                PanelUpdate(7, 14, color1),
                PanelUpdate(6, 14, color1),
                PanelUpdate(6, 13, color1),
                ]
    updateR7 = [PanelUpdate(4, 13, color1),
                PanelUpdate(5, 13, color1),
                PanelUpdate(5, 12, color1),
                PanelUpdate(6, 12, color1),
                PanelUpdate(6, 11, color1),
                PanelUpdate(4, 18, color1),
                PanelUpdate(4, 17, color1),
                PanelUpdate(5, 17, color1),
                PanelUpdate(5, 16, color1),
                PanelUpdate(6, 16, color1),
                PanelUpdate(6, 15, color1),
                PanelUpdate(7, 14, color1),
                PanelUpdate(8, 14, color1),
                PanelUpdate(8, 13, color1),
                ]
    updateR8 = [PanelUpdate(4, 13, color1),
                PanelUpdate(4, 14, color1),
                PanelUpdate(4, 15, color1),
                PanelUpdate(4, 16, color1),
                PanelUpdate(4, 17, color1),
                PanelUpdate(4, 18, color1),
                PanelUpdate(6, 11, color1),
                PanelUpdate(6, 12, color1),
                PanelUpdate(6, 13, color1),
                PanelUpdate(6, 14, color1),
                PanelUpdate(6, 15, color1),
                PanelUpdate(8, 10, color1),
                PanelUpdate(8, 11, color1),
                PanelUpdate(8, 12, color1),
                PanelUpdate(8, 13, color1),
                PanelUpdate(8, 14, color1),
                PanelUpdate(6, 16, color1),
                PanelUpdate(8, 9, color1),

                PanelUpdate(4, 13, color1),
                PanelUpdate(5, 13, color1),
                PanelUpdate(5, 12, color1),
                PanelUpdate(6, 12, color1),
                PanelUpdate(6, 11, color1),
                PanelUpdate(4, 18, color1),
                PanelUpdate(4, 17, color1),
                PanelUpdate(5, 17, color1),
                PanelUpdate(5, 16, color1),
                PanelUpdate(6, 16, color1),
                PanelUpdate(6, 15, color1),
                PanelUpdate(6, 11, color1),
                PanelUpdate(7, 11, color1),
                PanelUpdate(7, 10, color1),
                PanelUpdate(8, 10, color1),
                PanelUpdate(8, 9, color1),
                PanelUpdate(6, 15, color1),
                PanelUpdate(7, 15, color1),
                PanelUpdate(7, 14, color1),
                PanelUpdate(8, 14, color1),
                PanelUpdate(8, 13, color1), ]

    updatesR2 = [
        PanelUpdate(4, 13, color1),
        PanelUpdate(4, 14, color1),
        PanelUpdate(4, 15, color1),
        PanelUpdate(4, 16, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(4, 18, color1),

        PanelUpdate(6, 11, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 15, color1),

        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 11, color1),
        PanelUpdate(8, 12, color1),
        PanelUpdate(8, 13, color1),
        PanelUpdate(8, 14, color1),
        PanelUpdate(6, 16, color1),
        PanelUpdate(8, 9, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(4, 18, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(5, 17, color1),
        PanelUpdate(5, 16, color1),
        PanelUpdate(6, 16, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(7, 11, color1),
        PanelUpdate(7, 10, color1),
        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 9, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(8, 14, color1),
        PanelUpdate(8, 13, color1),
    ]

    updatesR0 = [
        PanelUpdate(4, 13, color1),
        PanelUpdate(4, 14, color1),
        PanelUpdate(4, 15, color1),
        PanelUpdate(4, 16, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(4, 18, color1),

        PanelUpdate(6, 11, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 15, color1),

        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 11, color1),
        PanelUpdate(8, 12, color1),
        PanelUpdate(8, 13, color1),
        PanelUpdate(8, 14, color1),
        PanelUpdate(6, 16, color1),
        PanelUpdate(8, 9, color1),

        PanelUpdate(5, 13, color1),
        PanelUpdate(5, 12, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(4, 18, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(5, 17, color1),
        PanelUpdate(5, 16, color1),
        PanelUpdate(6, 16, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(7, 11, color1),
        PanelUpdate(7, 10, color1),
        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 9, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(7, 15, color1),
        PanelUpdate(7, 14, color1),
        PanelUpdate(8, 14, color1),
        PanelUpdate(8, 13, color1),
    ]

    updatesR1 = [
        PanelUpdate(4, 14, color1),
        PanelUpdate(4, 15, color1),
        PanelUpdate(5, 14, color1),
        PanelUpdate(5, 14, color1),
        PanelUpdate(6, 14, color1),
        PanelUpdate(6, 13, color1),
        PanelUpdate(7, 13, color1),
        PanelUpdate(7, 12, color1),
        PanelUpdate(8, 12, color1),
        PanelUpdate(8, 11, color1),
        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 9, color1),
        PanelUpdate(8, 13, color1),
        PanelUpdate(8, 14, color1),

    ]
    updatesR4 = [
        PanelUpdate(4, 13, color1, 10),
        PanelUpdate(4, 14, color1, 10),
        # PanelUpdate(4, 15, color1, 10),
        # PanelUpdate(4, 16, color1, 10),
        PanelUpdate(4, 17, color1, 10),
        PanelUpdate(4, 18, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        PanelUpdate(6, 12, color1, 10),
        PanelUpdate(6, 13, color1, 10),
        PanelUpdate(6, 14, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        # anelUpdate(8, 10, color1, 10),
        # PanelUpdate(8, 11, color1, 10),
        # PanelUpdate(8, 12, color1, 10),
        PanelUpdate(8, 13, color1, 10),
        PanelUpdate(8, 14, color1, 10),
        PanelUpdate(6, 16, color1, 10),
        # PanelUpdate(8, 9, color1, 10),

        PanelUpdate(4, 13, color1, 10),
        PanelUpdate(5, 13, color1, 10),
        PanelUpdate(5, 12, color1, 10),
        PanelUpdate(6, 12, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        PanelUpdate(4, 18, color1, 10),
        PanelUpdate(4, 17, color1, 10),
        PanelUpdate(5, 17, color1, 10),
        PanelUpdate(5, 16, color1, 10),
        PanelUpdate(6, 16, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        # PanelUpdate(7, 11, color1, 10),
        # PanelUpdate(7, 10, color1, 10),
        PanelUpdate(8, 10, color1, 10),
        PanelUpdate(8, 9, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        PanelUpdate(7, 15, color1, 10),
        PanelUpdate(7, 14, color1, 10),
        PanelUpdate(8, 14, color1, 10),
        PanelUpdate(8, 13, color1, 10),
    ]

    updatesR5 = [
        PanelUpdate(4, 13, color1, 10),
        PanelUpdate(4, 14, color1, 10),
        PanelUpdate(4, 15, color1, 10),
        PanelUpdate(4, 16, color1, 10),
        PanelUpdate(4, 17, color1, 10),
        PanelUpdate(4, 18, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        PanelUpdate(6, 12, color1, 10),
        PanelUpdate(6, 13, color1, 10),
        PanelUpdate(6, 14, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        PanelUpdate(8, 10, color1, 10),
        PanelUpdate(8, 11, color1, 10),
        PanelUpdate(8, 12, color1, 10),
        PanelUpdate(8, 13, color1, 10),
        PanelUpdate(8, 14, color1, 10),
        PanelUpdate(6, 16, color1, 10),
        PanelUpdate(8, 9, color1, 10),

        PanelUpdate(5, 13, color1, 10),
        PanelUpdate(5, 12, color1, 10),
        PanelUpdate(6, 12, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        PanelUpdate(4, 18, color1, 10),
        PanelUpdate(4, 17, color1, 10),
        # PanelUpdate(5, 17, color1, 10),
        # PanelUpdate(5, 16, color1, 10),
        PanelUpdate(6, 16, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        # PanelUpdate(7, 11, color1, 10),
        # PanelUpdate(7, 10, color1, 10),
        PanelUpdate(8, 10, color1, 10),
        PanelUpdate(8, 9, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        PanelUpdate(7, 15, color1, 10),
        PanelUpdate(7, 14, color1, 10),
        PanelUpdate(8, 14, color1, 10),
        PanelUpdate(8, 13, color1, 10),
    ]

foo  = Nums()

# # here
# 
# updates = [
#     PanelUpdate(row, col, random.choice(colors), 10) for row, col in data.panel_positions[0],
#     PanelUpdate(row, col, random.choice(colors), 10) for row, col in data.panel_positions[1],
#     PanelUpdate(row, col, random.choice(colors), 10) for row, col in data.panel_positions[2],
#     PanelUpdate(row, col, random.choice(colors), 10) for row, col in data.panel_positions[3],
#     PanelUpdate(row, col, random.choice(colors), 10) for row, col in data.panel_positions[4],
#     PanelUpdate(row, col, random.choice(colors), 10) for row, col in data.panel_positions[5],
#     PanelUpdate(row, col, random.choice(colors), 10) for row, col in data.panel_positions[6],
#     PanelUpdate(row, col, random.choice(colors), 10) for row, col in data.panel_positions[7],
#     PanelUpdate(row, col, random.choice(colors), 10) for row, col in data.panel_positions[8],
# ]
# 
# for update in updates:
#     nl.update(update)
# time.sleep(1)
# 
# # here

def fill(nl, color_fill):
    for i in range(10):
        updates = [PanelUpdate(row, col, color_fill, 10) for row, col in data.panel_positions[i]]
        nl.update(updates)





while True:
    the_updates = []
    first_digit = 2
    if(weath.dark_mode):
        fill_color = "#000080"
    else:
        fill_color = "#87CEEB"


    fill(nl, fill_color)

    time.sleep(5)

    if(first_digit == 2):
        the_updates = foo.updatesL2
    else:
        the_updates = foo.updatesL8
        
    nl.update(the_updates)
    # nl1 = update(foo.updateR8)
    time.sleep(5)




# updates1 = [PanelUpdate(row, col, random.choice(colors), 10) for row, col in data.panel_positions[8]]

