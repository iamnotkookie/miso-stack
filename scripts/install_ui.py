"""Keyboard picker for terminal installs, with a plain-terminal fallback."""
import os


HOST_LABELS = {"codex": "Codex", "claude": "Claude Code", "grok": "Grok Build", "opencode": "OpenCode"}


def plain_picker(detected):
    print("\nMisoStack · Choose your coding agents\n")
    print("  1. All detected harnesses (Recommended): " + ", ".join(detected))
    for number, host in enumerate(detected, 2):
        print(f"  {number}. {HOST_LABELS[host]}")
    print("  0. Cancel")
    while True:
        answer = input("Choose [1], or enter names/numbers separated by spaces: ").strip().lower()
        if answer in ("", "1", "all"):
            return detected
        if answer in ("0", "q", "quit", "cancel"):
            return []
        choices = {str(number): host for number, host in enumerate(detected, 2)}
        selected = [choices.get(token, token) for token in answer.replace(",", " ").split()]
        if selected and all(host in detected for host in selected):
            return list(dict.fromkeys(selected))
        print("Choose listed harnesses, 1 for all, or 0 to cancel.")


def choose(detected):
    if os.environ.get("TERM", "dumb") == "dumb":
        return plain_picker(detected)
    try:
        import curses
    except ImportError:
        return plain_picker(detected)
    try:
        return curses.wrapper(lambda screen: keyboard_picker(screen, curses, detected))
    except curses.error:
        print("Terminal controls unavailable. Use the numbered choices below.")
        return plain_picker(detected)


def read_key(screen, curses):
    key = screen.getch()
    if key != 27:
        return key
    # Accept both normal cursor sequences and xterm application sequences.
    screen.timeout(40)
    prefix = screen.getch()
    suffix = screen.getch() if prefix in (ord("["), ord("O")) else -1
    screen.timeout(100)
    return {ord("A"): curses.KEY_UP, ord("B"): curses.KEY_DOWN}.get(suffix, 27)


def draw(screen, curses, detected, selected, focus, message, accent):
    rows, columns = screen.getmaxyx()
    screen.erase()
    left = max(2, (columns - 68) // 2)
    width = columns - left * 2

    def line(y, text, style=0):
        if y < rows - 1 and width > 0:
            screen.addnstr(y, left, text, width, style)

    if rows < 18 or columns < 44:
        line(1, "MisoStack", curses.A_BOLD)
        line(3, "Enlarge terminal to 44 x 18.")
        line(5, "Esc Cancel")
    else:
        line(1, "MisoStack", curses.A_BOLD | accent)
        line(2, "Set up your coding agents", curses.A_DIM)
        line(4, "Where should we install?", curses.A_BOLD)
        all_mark = "x" if len(selected) == len(detected) else "-" if selected else " "
        options = [(None, f"[{all_mark}] All detected   Recommended")]
        for host, label in HOST_LABELS.items():
            mark = "x" if host in selected else " "
            options.append((host, f"[{mark}] {label}" if host in detected else f" -  {label}  (not found)"))
        for index, (host, label) in enumerate(options):
            active = host == focus
            enabled = host is None or host in detected
            style = curses.A_REVERSE | curses.A_BOLD if active else 0 if enabled else curses.A_DIM
            line(5 + index, (("> " if active else "  ") + label).ljust(width), style)
        line(11, message or f"{len(selected)} of {len(detected)} available agents selected", accent)
        line(12, "Codex / Claude: plugins. Others: shared skills.", curses.A_DIM)
        line(14, "↑/↓ Move   Space Toggle   Enter Install", curses.A_BOLD)
        line(15, "Esc Cancel", curses.A_DIM)
    # npm's progress indicator writes to the current line. Leave it an empty row.
    screen.move(rows - 2, 0)
    screen.redrawwin()
    screen.refresh()


def keyboard_picker(screen, curses, detected):
    screen.keypad(True)
    screen.timeout(100)
    curses.set_escdelay(40)
    accent = 0
    if curses.has_colors() and "NO_COLOR" not in os.environ:
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_CYAN, -1)
        accent = curses.color_pair(1)
    choices = [None, *detected]
    selected = set(detected)
    position = 0
    message = ""
    while True:
        draw(screen, curses, detected, selected, choices[position], message, accent)
        key = read_key(screen, curses)
        if key in (27, ord("q"), ord("0")):
            return []
        if screen.getmaxyx()[0] < 18 or screen.getmaxyx()[1] < 44:
            continue
        if key in (curses.KEY_UP, ord("k")):
            position = (position - 1) % len(choices)
        elif key in (curses.KEY_DOWN, ord("j"), 9):
            position = (position + 1) % len(choices)
        elif key == ord(" "):
            host = choices[position]
            if host is None:
                selected = set() if len(selected) == len(detected) else set(detected)
            else:
                selected = selected ^ {host}
            message = ""
        elif key in (10, 13, curses.KEY_ENTER):
            if selected:
                return [host for host in detected if host in selected]
            message = "Select at least one agent, or Esc to cancel."
