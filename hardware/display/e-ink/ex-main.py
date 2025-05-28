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
    
    epd = epd2in13_V4.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)

    # Fonts ('Font.ttf'), size)
    fira24 = ImageFont.truetype('fonts/FiraCode.ttf', 24)
    plex24 = ImageFont.truetype('fonts/IBMPlex.ttf', 24)
    
    # 1. Initialize Display
    epd.init()
    
    # 2. Create an image and draw image
    image=Image.new('1', (epd.height, epd.width), 255) # 255: clear the frame
    draw=ImageDraw.Draw(image)
    draw.rectangle((0,0,122,250),fill=255)
    
    # Issue PIL drawing commands and commands
    # that will be sent to the display.
    
    logging.info("Text Display")
    
    #draw.text(y,x),'text',font=font.ttf, fill=0)
    draw.text((0,0), 'Boo! Fira 2025', font=fira24, fill=0)
    draw.text((0,50), 'Hoo! Plex 2025', font=plex24, fill=0)
    
    # 3. Send buffered data to the screen.
    epd.display(epd.getbuffer(image))
    # End of simple display code.
    #
    # Pause the screen for a bit. 
    time.sleep(20)
    
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
