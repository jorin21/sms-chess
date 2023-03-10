from PIL import Image, ImageDraw, ImageFont

def gen_board(board):
# board = '''\
# ┌───┬───┬───┬───┬───┬───┬───┬───┐
# │ . │ # │ . │ # │ . │ # │ . │ # │
# ├───┼───┼───┼───┼───┼───┼───┼───┤
# │ # │ . │ # │ . │ # │ . │ # │ . │
# ├───┼───┼───┼───┼───┼───┼───┼───┤
# │ . │ # │ . │ # │ . │ # │ . │ # │
# ├───┼───┼───┼───┼───┼───┼───┼───┤
# │ # │ . │ # │ . │ # │ . │ # │ . │
# ├───┼───┼───┼───┼───┼───┼───┼───┤
# │ . │ # │ . │ # │ . │ # │ . │ # │
# ├───┼───┼───┼───┼───┼───┼───┼───┤
# │ # │ . │ # │ . │ # │ . │ # │ . │
# ├───┼───┼───┼───┼───┼───┼───┼───┤
# │ . │ # │ . │ # │ . │ # │ . │ # │
# ├───┼───┼───┼───┼───┼───┼───┼───┤
# │ # │ . │ # │ . │ # │ . │ # │ . │
# └───┴───┴───┴───┴───┴───┴───┴───┘'''

    img = Image.new("RGBA",(680,600),color=(30,30,30,0))

    fnt = ImageFont.truetype("DejavuSansMono-5m7L.ttf", 30)

    draw = ImageDraw.Draw(img)

    draw.multiline_text((20,0),board,font=fnt,fill=(0,0,0))


    # img.show()
    img.save('board.png', "PNG")


def gen_take(taken):
    img = Image.new("RGBA",(680,165),color=(30,30,30,0))

    fnt = ImageFont.truetype("DejavuSansMono-5m7L.ttf", 30)

    draw = ImageDraw.Draw(img)

    draw.multiline_text((20,0),taken,font=fnt,fill=(0,0,0))

    img.save('taken.png', "PNG")