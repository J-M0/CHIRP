"""Main entrypoint for CHIRP."""

# Standard Python Libraries
from multiprocessing import freeze_support
import os
import sys
import time
from typing import NoReturn

# cisagov Libraries
from chirp import run
from chirp.common import CONSOLE, ERROR, OUTPUT_DIR, save_log


def main() -> NoReturn:
    try:
        freeze_support()
        run.run()
        time.sleep(2)
        CONSOLE(
            f"[green][+][/green] DONE! Your results can be found in {os.path.abspath(OUTPUT_DIR)}. Press any key to exit."
        )
        input()
        save_log()
        sys.exit(0)
    except KeyboardInterrupt:
        ERROR("Received an escape sequence. Goodbye.")
        save_log()
        sys.exit(0)


if __name__ == "__main__":
    main()
