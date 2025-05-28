#!/usr/bin/python
# -*- coding:utf-8 -*-
# Display resolution
# EPD_WIDTH       = 122
# EPD_HEIGHT      = 250

import logging
from driver import epd2in13_V4
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("E-Ink Simple Demo")
    
    # Initalize and Clear screen
    epd = epd2in13_V4.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)
    
    # Display Code Here



    # Clear and Exit
    logging.info("Clear...")
    epd.init()
    epd.Clear(0xFF)
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V4.epdconfig.module_exit(cleanup=True)
    exit()
