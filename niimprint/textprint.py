import argparse
from niimprint import printerclient
from niimprint import printencoder

from PIL import Image, ImageDraw , ImageDraw2
import time

# import math
# mm_to_px = lambda x: math.ceil(x / 25.4 * 203)
# px_to_mm = lambda x: math.ceil(x / 25.4 * 203)
briosk = "/var/home/bri/Downloads/fonts/dist/briosk-proportional/ttf/briosk-proportional-regular.ttf"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Niimbot printer client")
    parser.add_argument('-a', '--address', required=False, help="MAC address of target device", default="02:09:F8:3E:95:B0")
    parser.add_argument('--no-check', action='store_true', help="Skips image check")
    parser.add_argument('-d', '--density', type=int, default=2, help="Printer density (1~3)")
    parser.add_argument('-t', '--type', type=int, default=1, help="Label type (1~3)")
    parser.add_argument('-n', '--quantity', type=int, default=1, help="Number of copies")
    parser.add_argument('-f', '--foreground', default="white", help="foreground color")
    parser.add_argument('-b', '--background', default="black", help="background color")
    parser.add_argument('--font', default=briosk, help="font")
    parser.add_argument('--size', default=50, type=int, help="font size in pixels")
    parser.add_argument('-x', default=5, type=int, help="x margin")
    parser.add_argument('-y', default=5, type=int, help="y margin")
    parser.add_argument('text', help="Text to print")
    args = parser.parse_args()

    font = ImageDraw2.Font(color=args.foreground, file=args.font, size=args.size)
    img = Image.new(mode="RGB", size=(350,96), color=args.background)
    draw= ImageDraw2.Draw(img)
    draw.text(text=args.text, xy=(args.x,args.y), font=font)
    if img.width / img.height > 1:
        # rotate clockwise 90deg, upper line (left line) prints first.
        img = img.transpose(Image.ROTATE_270)
    else:
        img= img.transpose(Image.ROTATE_90)
    assert args.no_check or (img.width == 96 and img.height < 600)

    printer = printerclient.PrinterClient(args.address)
    printer.set_label_type(args.type)
    printer.set_label_density(args.density)

    printer.start_print()
    printer.allow_print_clear()
    printer.start_page_print()
    printer.set_dimension(img.height, img.width)
    printer.set_quantity(args.quantity)
    for pkt in printencoder.naive_encoder(img):
        printer._send(pkt)
    printer.end_page_print()
    while (a := printer.get_print_status())['page'] != args.quantity:
        # print(a)
        time.sleep(0.1)
    printer.end_print()
