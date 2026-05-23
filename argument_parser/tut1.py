import argparse



parser = argparse.ArgumentParser()

parser.add_argument("--name", type=str)

#can also set default value
parser.add_argument("--epochs", type=int, default=10)

args = parser.parse_args()

print("Hello", args.name)


"""
    CLI Command 
    (100_days_of_Python_course) PS D:\All other stuffs\All other stuffs\100_days_of_Python_course\argument_parser> python .\tut1.py --name Babar

    passing string argument through CLI . WOW 

    anther very usefull command is  
    python tut1.py --help
     
"""
TARGET_FPS = 10

    # ── Extraction parameters ────────────────────────────────
parser.add_argument(
    "--fps",
    type=float,
    default=TARGET_FPS,
    metavar="N",
    help=(
        f"Uniform baseline FPS — how many frames per second to always keep.\n"
        f"Default: {TARGET_FPS}"
    ),
)