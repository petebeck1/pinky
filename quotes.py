#! /usr/bin/env python

import sys
import random
import wikiquotes
import inkyphat

from PIL import Image, ImageDraw, ImageFont


def reflow_quote(quote, width, font):
    words = quote.split(" ")
    reflowed = ''
    line_length = 0

    for i in range(len(words)):
        word = words[i] + " "
        word_length = font.getsize(word)[0]
        line_length += word_length

        if line_length < width:
            reflowed += word
        else:
            line_length = word_length
            reflowed = reflowed[:-1] + " \n" + word

    reflowed = reflowed.rstrip()

    return reflowed


inkyphat.set_colour('red')
w = inkyphat.WIDTH
h = inkyphat.HEIGHT
img = Image.new("P", (w, h))
draw = ImageDraw.Draw(img)

padding = 32
max_width = inkyphat.WIDTH - padding

font_size = 10
quote_font = ImageFont.truetype('/home/pi/TTF/elec.ttf', font_size)

people = [ 
  'Douglas Adams', 
  'Terry Pratchett', 
  'Neil Gaiman', 
  'Arthur Conan Doyle',
  'Raymond Chandler'
]

author = random.choice(people)
found = False
while not found:
    text = wikiquotes.random_quote(author, 'english')
    reflowed = reflow_quote(text, max_width, quote_font)
    if reflowed.count("\n") < 9: found = True
print(reflowed)

y = 0
for line in reflowed.split("\n"):
    line = line + '   '
    (rw, rh) = quote_font.getsize(line)
    x = (w - rw) / 2
    draw.multiline_text((x, y), line, fill=inkyphat.BLACK, font=quote_font)
    y = y + 10
author = '- ' + author + '   '
(aw, ah) = quote_font.getsize(author)
draw.multiline_text((w - aw, y), author, fill=inkyphat.RED, font=quote_font)

inkyphat.set_image(img)
inkyphat.show()

