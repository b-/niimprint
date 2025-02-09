# (WIP) Niimbot printer client

## niimprint

    usage: python -m niimprint [-h] -a ADDRESS [--no-check] [-d DENSITY] [-t TYPE] [-n QUANTITY] image

    Niimbot printer client

    positional arguments:
    image                 PIL supported image file

    options:
    -h, --help            show this help message and exit
    -a ADDRESS, --address ADDRESS
                            MAC address of target device
    --no-check            Skips image check
    -d DENSITY, --density DENSITY
                            Printer density (1~3)
    -t TYPE, --type TYPE  Label type (1~3)
    -n QUANTITY, --quantity QUANTITY
                            Number of copies

## niimprint.textprint

    usage: python -m niimprint.textprint [-h] [-a ADDRESS] [--no-check] [-d DENSITY] [-t TYPE]
                        [-n QUANTITY] [-f FOREGROUND] [-b BACKGROUND]
                        [--font FONT] [--size SIZE] [-x X] [-y Y]
                        text

    Niimbot printer client

    positional arguments:
      text                  Text to print

    options:
      -h, --help            show this help message and exit
      -a ADDRESS, --address ADDRESS
                            MAC address of target device
      --no-check            Skips image check
      -d DENSITY, --density DENSITY
                            Printer density (1~3)
      -t TYPE, --type TYPE  Label type (1~3)
      -n QUANTITY, --quantity QUANTITY
                            Number of copies
      -f FOREGROUND, --foreground FOREGROUND
                            foreground color
      -b BACKGROUND, --background BACKGROUND
                            background color
      --font FONT           font
      --size SIZE           font size in pixels
      -x X                  x margin
      -y Y                  y margin
