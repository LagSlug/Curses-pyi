from typing import NamedTuple, Tuple, Optional, Any, Union, Callable
from io import IOBase

"""
Note:
Whenever x or y arguments to a function or a method are optional, they default to the current cursor location.
Whenever attr is optional, it defaults to A_NORMAL.
"""

class error(Exception): ...
"""Exception raised when a curses library function returns an error."""


# Functions
def baudrate() -> int:
 """Returns the output speed of the terminal in bits per second."""

def beep() -> None:
 """Emit a short attention sound."""

def can_change_color() -> bool:
 """Returns True or False depending on whether colors can be changed."""

def cbreak() -> None:
 """Enter cbreak mode, turning off normal tty line buffering."""

def color_content(color_number: int) -> tuple:
 """Returns the intensity of the RGB components in the color."""

def color_pair(pair_number: int) -> int:
 """Returns the attribute value for a specified color pair."""

def curs_set(visibility: int) -> int:
 """Sets the cursor state to invisible, normal, or very visible."""

def def_prog_mode() -> None:
 """Save the current terminal mode as the 'program' mode."""

def def_shell_mode() -> None:
 """Save the current terminal mode as the 'shell' mode."""

def delay_output(ms: int) -> None:
 """Insert a pause in output for a specified number of milliseconds."""

def doupdate() -> None:
 """Update the physical screen to match the virtual screen."""

def echo() -> None:
 """Enter echo mode, echoing each character input to the screen."""

def endwin() -> None:
 """De-initialize the library and return terminal to normal status."""

def erasechar() -> bytes:
 """Return the user's current erase character."""

def filter() -> None:
 """Must be called before initscr(). Confines cursor and screen updates to the current line."""

def flash() -> None:
 """Flashes the screen to reverse-video and then back."""

def flushinp() -> None:
 """Flushes all input buffers, discarding any typeahead that has not yet been processed."""

def getmouse() -> tuple:
 """Retrieves a queued mouse event after getch() returns KEY_MOUSE."""

def getsyx() -> tuple:
 """Returns the current coordinates of the virtual screen cursor."""

def getwin(file) -> '_CursesWindow':
 """Reads window data from a file and returns a new window object."""

def has_colors() -> bool:
 """Returns True if the terminal can display colors."""

def has_extended_color_support() -> bool:
 """Returns True if the module supports extended colors."""

def has_ic() -> bool:
 """Returns True if the terminal has insert- and delete-character capabilities."""

def has_il() -> bool:
 """Returns True if the terminal has insert- and delete-line capabilities."""

def has_key(ch: int) -> bool:
 """Returns True if the current terminal type recognizes a key with the given value."""

def halfdelay(tenths: int) -> None:
 """Sets half-delay mode, raising an exception if no input is received within 'tenths' tenths of a second."""

def init_color(color_number: int, r: int, g: int, b: int) -> None:
 """Change the definition of a color."""

def init_pair(pair_number: int, fg: int, bg: int) -> None:
 """Change the definition of a color-pair."""

def initscr() -> '_CursesWindow':
 """Initialize the library and return a window object for the whole screen."""

def is_term_resized(nlines: int, ncols: int) -> bool:
 """Check if resize_term() would modify the window structure."""

def isendwin() -> bool:
 """Check if endwin() has been called."""

def keyname(k: int) -> bytes:
 """Return the name of the key numbered k."""

def killchar() -> bytes:
 """Return the user's current line kill character."""

def longname() -> bytes:
 """Return the terminfo long name field for the current terminal."""

def meta(flag: bool) -> None:
 """Allow 8-bit characters to be input if flag is True, otherwise allow only 7-bit chars."""

def mouseinterval(interval: int) -> int:
 """Set the maximum time for mouse click recognition."""

def mousemask(mousemask: int) -> Tuple[int, int]:
 """Set the mouse events to be reported."""

def napms(ms: int) -> None:
 """Sleep for a specified number of milliseconds."""

def newpad(nlines: int, ncols: int) -> '_CursesWindow':
 """Create and return a new pad data structure."""

def newwin(nlines: int, ncols: int, begin_y: int, begin_x: int) -> '_CursesWindow':
 """Return a new window with specified dimensions and position."""

def nl() -> None:
 """Enter newline mode."""

def nocbreak() -> None:
 """Leave cbreak mode."""

def noecho() -> None:
 """Leave echo mode."""

def nonl() -> None:
 """Leave newline mode."""

def noqiflush() -> None:
 """Disable normal flush of input and output queues for certain characters."""

def noraw() -> None:
 """Leave raw mode."""

def pair_content(pair_number: int) -> Tuple[int, int]:
 """Return a tuple containing the colors for the requested color pair."""

def pair_number(attr: int) -> int:
 """Return the number of the color-pair set by the attribute value attr."""

def putp(str: str) -> None:
 """Emit the value of a specified terminfo capability for the current terminal."""

def qiflush(flag: Optional[bool] = True) -> None:
 """Control the flushing of input and output queues based on control characters."""

def raw() -> None:
 """Enter raw mode, turning off line buffering and special key processing."""

def reset_prog_mode() -> None:
 """Restore the terminal to 'program' mode."""

def reset_shell_mode() -> None:
 """Restore the terminal to 'shell' mode."""

def resetty() -> None:
 """Restore the state of the terminal modes to the last saved state."""

def resize_term(nlines: int, ncols: int) -> None:
 """Backend function for resizing the terminal."""

def resizeterm(nlines: int, ncols: int) -> None:
 """Resize the standard and current windows to the specified dimensions."""

def savetty() -> None:
 """Save the current state of the terminal modes."""

def get_escdelay() -> int:
 """Retrieve the value set by set_escdelay()."""

def set_escdelay(ms: int) -> None:
 """Set the number of milliseconds to wait after reading an escape character."""

def get_tabsize() -> int:
 """Retrieve the value set by set_tabsize()."""

def set_tabsize(size: int) -> None:
 """Set the number of columns used when converting a tab character to spaces."""

def setsyx(y: int, x: int) -> None:
 """Set the virtual screen cursor to y, x."""

def setupterm(term: Optional[str] = None, fd: int = -1) -> None:
 """Initialize the terminal with optional terminal name and file descriptor."""

def start_color() -> None:
 """Initialize color functionality."""

def termattrs() -> int:
 """Return a logical OR of all video attributes supported by the terminal."""

def termname() -> bytes:
 """Return the value of the environment variable TERM."""

def tigetflag(capname: str) -> int:
 """Return the value of the Boolean capability corresponding to capname."""

def tigetnum(capname: str) -> int:
 """Return the value of the numeric capability corresponding to capname."""

def tigetstr(capname: str) -> Optional[bytes]:
 """Return the value of the string capability corresponding to capname."""

def tparm(str: bytes, *args: Any) -> bytes:
 """Instantiate a parameterized string with the supplied parameters."""

def typeahead(fd: int) -> None:
 """Specify file descriptor for typeahead checking."""

def unctrl(ch: int) -> bytes:
 """Return a printable representation of the character ch."""

def ungetch(ch: int) -> None:
 """Push ch so the next getch() will return it."""

def update_lines_cols() -> None:
 """Update the LINES and COLS module variables."""

def unget_wch(ch: int) -> None:
 """Push ch so the next get_wch() will return it."""

def ungetmouse(id: int, x: int, y: int, z: int, bstate: int) -> None:
 """Push a KEY_MOUSE event onto the input queue."""

def use_env(flag: bool) -> None:
 """Override environment variables for lines and columns."""

def use_default_colors() -> None:
 """Allow use of default values for colors."""

def wrapper(func: Callable, /, *args: Any, **kwargs: Any) -> None:
 """Initialize curses and call another callable object, func."""



# Window
class _CursesWindow:
    def addch(self, ch: str, attr: int = None) -> None: ...
    def addch(self, y: int, x: int, ch: str, attr: int = None) -> None:
        """Paint character ch at (y, x) with attributes attr, overwriting any character previously painted at that location."""

    def addnstr(self, str: str, n: int, attr: int = None) -> None: ...
    def addnstr(self, y: int, x: int, str: str, n: int, attr: int = None) -> None: 
        """Paint at most n characters of the character string str at (y, x) with attributes attr, overwriting anything previously on the display."""

    def addstr(self, str: str, attr: int = None) -> None: ...
    def addstr(self, y: int, x: int, str: str, attr: int = None) -> None: 
        """Paint the character string str at (y, x) with attributes attr, overwriting anything previously on the display."""

    def attroff(self, attr: int) -> None:
        """Remove attribute attr from the 'background' set applied to all writes to the current window."""

    def attron(self, attr: int) -> None:
        """Add attribute attr from the 'background' set applied to all writes to the current window."""

    def attrset(self, attr: int) -> None:
        """Set the 'background' set of attributes to attr. This set is initially 0 (no attributes)."""

    def bkgd(self, ch: str, attr: int = None) -> None:
        """Set the background property of the window to the character ch, with attributes attr."""

    def bkgdset(self, ch: str, attr: int = None) -> None:
        """Set the window's background. A window's background consists of a character and any combination of attributes."""

    def border(self, ls: int = 0, rs: int = 0, ts: int = 0, bs: int = 0, tl: int = 0, tr: int = 0, bl: int = 0, br: int = 0) -> None:
        """Draw a border around the edges of the window."""

    def box(self, vertch: int, horch: int) -> None:
        """Similar to border(), but both ls and rs are vertch and both ts and bs are horch."""

    def chgat(self, attr: int) -> None: ...
    def chgat(self, num: int, attr: int) -> None: ...
    def chgat(self, y: int, x: int, attr: int) -> None: ...
    def chgat(self, y: int, x: int, num: int, attr: int) -> None:
        """Set the attributes of num characters at the current cursor position, or at position (y, x) if supplied."""

    def clear(self) -> None:
        """Like erase(), but also cause the whole window to be repainted upon next call to refresh()."""

    def clearok(self, flag: bool) -> None:
        """If flag is True, the next call to refresh() will clear the window completely."""

    def clrtobot(self) -> None:
        """Erase from cursor to the end of the window."""

    def clrtoeol(self) -> None:
        """Erase from cursor to the end of the line."""

    def cursyncup(self) -> None:
        """Update the current cursor position of all the ancestors of the window to reflect the current cursor position of the window."""

    def delch(self, y: int = None, x: int = None) -> None:
        """Delete any character at (y, x)."""

    def deleteln(self) -> None:
        """Delete the line under the cursor. All following lines are moved up by one line."""

    def derwin(self, begin_y: int, begin_x: int) -> '_CursesWindow': ...
    def derwin(self, nlines: int, ncols: int, begin_y: int, begin_x: int) -> '_CursesWindow':
        """Return a window object for the derived window."""

    def echochar(self, ch: str, attr: int = None) -> None:
        """Add character ch with attribute attr, and immediately call refresh() on the window."""

    def enclose(self, y: int, x: int) -> bool:
        """Test whether the given pair of screen-relative character-cell coordinates are enclosed by the given window."""

    encoding: str
    """Encoding used to encode method arguments. By default, current locale encoding is used."""

    def erase(self) -> None:
        """Clear the window."""

    def getbegyx(self) -> Tuple[int, int]:
        """Return a tuple (y, x) of co-ordinates of upper-left corner."""

    def getbkgd(self) -> Tuple[str, int]:
        """Return the given window's current background character/attribute pair."""

    def getch(self, y: int = None, x: int = None) -> int:
        """Get a character. In no-delay mode, return -1 if there is no input."""

    def get_wch(self, y: int = None, x: int = None) -> Union[str, int]:
        """Get a wide character. In no-delay mode, raise an exception if there is no input."""

    def getkey(self, y: int = None, x: int = None) -> str:
        """Get a character, returning a string instead of an integer. In no-delay mode, raise an exception if there is no input."""

    def getmaxyx(self) -> Tuple[int, int]:
        """Return a tuple (y, x) of the height and width of the window."""

    def getparyx(self) -> Tuple[int, int]:
        """Return the beginning coordinates of this window relative to its parent window."""

    def getstr(self, n: int = None) -> bytes: ...
    def getstr(self, y: int, x: int) -> bytes: ...
    def getstr(self, y: int, x: int, n: int) -> bytes: 
        """Read a bytes object from the user, with primitive line editing capacity."""

    def getyx(self) -> Tuple[int, int]:
        """Return a tuple (y, x) of current cursor position relative to the window's upper-left corner."""

    def hline(self, ch: str, n: int) -> None: ...
    def hline(self, y: int, x: int, ch: str, n: int) -> None:
        """Display a horizontal line starting at (y, x) with length n consisting of the character ch."""

    def idcok(self, flag: bool) -> None:
        """If flag is False, curses no longer considers using the hardware insert/delete character feature."""

    def idlok(self, flag: bool) -> None:
        """If flag is True, curses will try and use hardware line editing facilities."""

    def immedok(self, flag: bool) -> None:
        """If flag is True, any change in the window image automatically causes the window to be refreshed."""

    def inch(self, y: int = None, x: int = None) -> int:
        """Return the character at the given position in the window."""

    def insch(self, ch: str, attr: int = None) -> None: ...
    def insch(self, y: int, x: int, ch: str, attr: int = None) -> None: 
        """Paint character ch at (y, x) with attributes attr, moving the line from position x right by one character."""

    def insdelln(self, nlines: int) -> None:
        """Insert nlines lines into the specified window above the current line."""

    def insertln(self) -> None:
        """Insert a blank line under the cursor."""

    def insnstr(self, str: str, n: int, attr: int = None) -> None: ...
    def insnstr(self, y: int, x: int, str: str, n: int, attr: int = None) -> None:
        """Insert a character string before the character under the cursor, up to n characters."""

    def insstr(self, str: str, attr: int = None) -> None: ...
    def insstr(self, y: int, x: int, str: str, attr: int = None) -> None: 
        """Insert a character string before the character under the cursor."""

    def instr(self, n: int = None) -> bytes: ...
    def instr(self, y: int, x: int, n: int = None) -> bytes: 
        """Return a bytes object of characters, extracted from the window starting at the current cursor position."""

    def is_linetouched(self, line: int) -> bool:
        """Return True if the specified line was modified since the last call to refresh()."""

    def is_wintouched(self) -> bool:
        """Return True if the specified window was modified since the last call to refresh()."""

    def keypad(self, flag: bool) -> None:
        """If flag is True, escape sequences generated by some keys will be interpreted by curses."""

    def leaveok(self, flag: bool) -> None:
        """If flag is True, cursor is left where it is on update, instead of being at 'cursor position'."""

    def move(self, new_y: int, new_x: int) -> None:
        """Move cursor to (new_y, new_x)."""

    def mvderwin(self, y: int, x: int) -> None:
        """Move the window inside its parent window."""

    def mvwin(self, new_y: int, new_x: int) -> None:
        """Move the window so its upper-left corner is at (new_y, new_x)."""

    def nodelay(self, flag: bool) -> None:
        """If flag is True, getch() will be non-blocking."""

    def notimeout(self, flag: bool) -> None:
        """If flag is True, escape sequences will not be timed out."""

    def noutrefresh(self) -> None:
        """Mark for refresh but wait. To update the physical screen, call doupdate()."""

    def overlay(self, destwin: '_CursesWindow', sminrow: int = None, smincol: int = None, dminrow: int = None, dmincol: int = None, dmaxrow: int = None, dmaxcol: int = None) -> None:
        """Overlay the window on top of destwin. Only the overlapping region is copied."""

    def overwrite(self, destwin: '_CursesWindow', sminrow: int = None, smincol: int = None, dminrow: int = None, dmincol: int = None, dmaxrow: int = None, dmaxcol: int = None) -> None:
        """Overwrite the window on top of destwin. Only the overlapping region is copied. This copy is destructive."""

    def putwin(self, file: 'IOBase') -> None:
        """Write all data associated with the window into the provided file object."""

    def redrawln(self, beg: int, num: int) -> None:
        """Indicate that the num screen lines, starting at line beg, are corrupted and should be completely redrawn."""

    def redrawwin(self) -> None:
        """Touch the entire window, causing it to be completely redrawn on the next refresh() call."""

    def refresh(self, pminrow: int = None, pmincol: int = None, sminrow: int = None, smincol: int = None, smaxrow: int = None, smaxcol: int = None) -> None:
        """Update the display immediately. The 6 optional arguments can only be specified when the window is a pad."""

    def resize(self, nlines: int, ncols: int) -> None:
        """Reallocate storage for a curses window to adjust its dimensions."""

    def scroll(self, lines: int = 1) -> None:
        """Scroll the screen or scrolling region upward by lines lines."""

    def scrollok(self, flag: bool) -> None:
        """Control what happens when the cursor of a window is moved off the edge of the window or scrolling region."""

    def setscrreg(self, top: int, bottom: int) -> None:
        """Set the scrolling region from line top to line bottom."""

    def standend(self) -> None:
        """Turn off the standout attribute. May turn off all attributes on some terminals."""

    def standout(self) -> None:
        """Turn on attribute A_STANDOUT."""

    def subpad(self, begin_y: int, begin_x: int, nlines: int = None, ncols: int = None) -> '_CursesWindow':
        """Return a sub-window with specified upper-left corner and dimensions."""

    def subwin(self, begin_y: int, begin_x: int, nlines: int = None, ncols: int = None) -> '_CursesWindow':
        """Return a sub-window with specified upper-left corner and dimensions. Extends to lower right corner by default."""

    def syncdown(self) -> None:
        """Touch each location in the window that has been touched in any of its ancestor windows."""

    def syncok(self, flag: bool) -> None:
        """If flag is True, syncup() is called automatically whenever there is a change in the window."""

    def syncup(self) -> None:
        """Touch all locations in ancestors of the window that have been changed in the window."""

    def timeout(self, delay: int) -> None:
        """Set blocking or non-blocking read behavior for the window."""

    def touchline(self, start: int, count: int, changed: bool = None) -> None:
        """Pretend count lines have been changed, starting with line start. Optionally mark as changed or unchanged."""

    def touchwin(self) -> None:
        """Pretend the whole window has been changed for drawing optimizations."""

    def untouchwin(self) -> None:
        """Mark all lines in the window as unchanged since the last call to refresh()."""

    def vline(self, ch: str, n: int, attr: int = None, y: int = None, x: int = None) -> None:
        """Display a vertical line starting at (y, x) with length n consisting of the character ch."""

# Constants
## Curses

ERR: int
"""Some curses routines that return an integer, such as getch(), return ERR upon failure."""

OK: int
"""Some curses routines that return an integer, such as napms(), return OK upon success."""

version: bytes
"""A bytes object representing the current version of the module."""

__version__: bytes
"""A bytes object representing the current version of the module."""

class ncurses_version(NamedTuple):
    """A named tuple containing the three components of the ncurses library version."""
    
    major: int
    minor: int
    patch: int

COLORS: int
"""The maximum number of colors the terminal can support. Defined only after the call to start_color()."""

COLOR_PAIRS: int
"""The maximum number of color pairs the terminal can support. Defined only after the call to start_color()."""

COLS: int
"""The width of the screen, i.e., the number of columns. Defined only after the call to initscr()."""

LINES: int
"""The height of the screen, i.e., the number of lines. Defined only after the call to initscr()."""

## Attributes
A_ALTCHARSET: int
"""Alternate character set mode"""

A_BLINK: int
"""Blink mode"""

A_BOLD: int
"""Bold mode"""

A_DIM: int
"""Dim mode"""

A_INVIS: int
"""Invisible or blank mode"""

A_ITALIC: int
"""Italic mode"""

A_NORMAL: int
"""Normal attribute"""

A_PROTECT: int
"""Protected mode"""

A_REVERSE: int
"""Reverse background and foreground colors"""

A_STANDOUT: int
"""Standout mode"""

A_UNDERLINE: int
"""Underline mode"""

A_HORIZONTAL: int
"""Horizontal highlight"""

A_LEFT: int
"""Left highlight"""

A_LOW: int
"""Low highlight"""

A_RIGHT: int
"""Right highlight"""

A_TOP: int
"""Top highlight"""

A_VERTICAL: int
"""Vertical highlight"""

## Bit-mask
A_ATTRIBUTES: int
"""Bit-mask to extract attributes"""

A_CHARTEXT: int
"""Bit-mask to extract a character"""

A_COLOR: int
"""Bit-mask to extract color-pair field information"""


## Keys
KEY_MIN: int
"""Minimum key value"""

KEY_BREAK: int
"""Break key (unreliable)"""

KEY_DOWN: int
"""Down-arrow"""

KEY_UP: int
"""Up-arrow"""

KEY_LEFT: int
"""Left-arrow"""

KEY_RIGHT: int
"""Right-arrow"""

KEY_HOME: int
"""Home key (upward+left arrow)"""

KEY_BACKSPACE: int
"""Backspace (unreliable)"""

KEY_F0: int
"""Function keys. Up to 64 function keys are supported."""

KEY_Fn: int
"""Value of function key n"""

KEY_DL: int
"""Delete line"""

KEY_IL: int
"""Insert line"""

KEY_DC: int
"""Delete character"""

KEY_IC: int
"""Insert char or enter insert mode"""

KEY_EIC: int
"""Exit insert char mode"""

KEY_CLEAR: int
"""Clear screen"""

KEY_EOS: int
"""Clear to end of screen"""

KEY_EOL: int
"""Clear to end of line"""

KEY_SF: int
"""Scroll 1 line forward"""

KEY_SR: int
"""Scroll 1 line backward (reverse)"""

KEY_NPAGE: int
"""Next page"""

KEY_PPAGE: int
"""Previous page"""

KEY_STAB: int
"""Set tab"""

KEY_CTAB: int
"""Clear tab"""

KEY_CATAB: int
"""Clear all tabs"""

KEY_ENTER: int
"""Enter or send (unreliable)"""

KEY_SRESET: int
"""Soft (partial) reset (unreliable)"""

KEY_RESET: int
"""Reset or hard reset (unreliable)"""

KEY_PRINT: int
"""Print"""

KEY_LL: int
"""Home down or bottom (lower left)"""

KEY_A1: int
"""Upper left of keypad"""

KEY_A3: int
"""Upper right of keypad"""

KEY_B2: int
"""Center of keypad"""

KEY_C1: int
"""Lower left of keypad"""

KEY_C3: int
"""Lower right of keypad"""

KEY_BTAB: int
"""Back tab"""

KEY_BEG: int
"""Beg (beginning)"""

KEY_CANCEL: int
"""Cancel"""

KEY_CLOSE: int
"""Close"""

KEY_COMMAND: int
"""Cmd (command)"""

KEY_COPY: int
"""Copy"""

KEY_CREATE: int
"""Create"""

KEY_END: int
"""End"""

KEY_EXIT: int
"""Exit"""

KEY_FIND: int
"""Find"""

KEY_HELP: int
"""Help"""

KEY_MARK: int
"""Mark"""

KEY_MESSAGE: int
"""Message"""

KEY_MOVE: int
"""Move"""

KEY_NEXT: int
"""Next"""

KEY_OPEN: int
"""Open"""

KEY_OPTIONS: int
"""Options"""

KEY_PREVIOUS: int
"""Prev (previous)"""

KEY_REDO: int
"""Redo"""

KEY_REFERENCE: int
"""Ref (reference)"""

KEY_REFRESH: int
"""Refresh"""

KEY_REPLACE: int
"""Replace"""

KEY_RESTART: int
"""Restart"""

KEY_RESUME: int
"""Resume"""

KEY_SAVE: int
"""Save"""

KEY_SBEG: int
"""Shifted Beg (beginning)"""

KEY_SCANCEL: int
"""Shifted Cancel"""

KEY_SCOMMAND: int
"""Shifted Command"""

KEY_SCOPY: int
"""Shifted Copy"""

KEY_SCREATE: int
"""Shifted Create"""

KEY_SDC: int
"""Shifted Delete char"""

KEY_SDL: int
"""Shifted Delete line"""

KEY_SELECT: int
"""Select"""

KEY_SEND: int
"""Shifted End"""

KEY_SEOL: int
"""Shifted Clear line"""

KEY_SEXIT: int
"""Shifted Exit"""

KEY_SFIND: int
"""Shifted Find"""

KEY_SHELP: int
"""Shifted Help"""

KEY_SHOME: int
"""Shifted Home"""

KEY_SIC: int
"""Shifted Input"""

KEY_SLEFT: int
"""Shifted Left arrow"""

KEY_SMESSAGE: int
"""Shifted Message"""

KEY_SMOVE: int
"""Shifted Move"""

KEY_SNEXT: int
"""Shifted Next"""

KEY_SOPTIONS: int
"""Shifted Options"""

KEY_SPREVIOUS: int
"""Shifted Prev"""

KEY_SPRINT: int
"""Shifted Print"""

KEY_SREDO: int
"""Shifted Redo"""

KEY_SREPLACE: int
"""Shifted Replace"""

KEY_SRIGHT: int
"""Shifted Right arrow"""

KEY_SRSUME: int
"""Shifted Resume"""

KEY_SSAVE: int
"""Shifted Save"""

KEY_SSUSPEND: int
"""Shifted Suspend"""

KEY_SUNDO: int
"""Shifted Undo"""

KEY_SUSPEND: int
"""Suspend"""

KEY_UNDO: int
"""Undo"""

KEY_MOUSE: int
"""Mouse event has occurred"""

KEY_RESIZE: int
"""Terminal resize event"""

KEY_MAX: int
"""Maximum key value"""


## ACS Code
ACS_BBSS: int
"""alternate name for upper right corner"""

ACS_BLOCK: int
"""solid square block"""

ACS_BOARD: int
"""board of squares"""

ACS_BSBS: int
"""alternate name for horizontal line"""

ACS_BSSB: int
"""alternate name for upper left corner"""

ACS_BSSS: int
"""alternate name for top tee"""

ACS_BTEE: int
"""bottom tee"""

ACS_BULLET: int
"""bullet"""

ACS_CKBOARD: int
"""checker board (stipple)"""

ACS_DARROW: int
"""arrow pointing down"""

ACS_DEGREE: int
"""degree symbol"""

ACS_DIAMOND: int
"""diamond"""

ACS_GEQUAL: int
"""greater-than-or-equal-to"""

ACS_HLINE: int
"""horizontal line"""

ACS_LANTERN: int
"""lantern symbol"""

ACS_LARROW: int
"""left arrow"""

ACS_LEQUAL: int
"""less-than-or-equal-to"""

ACS_LLCORNER: int
"""lower left-hand corner"""

ACS_LRCORNER: int
"""lower right-hand corner"""

ACS_LTEE: int
"""left tee"""

ACS_NEQUAL: int
"""not-equal sign"""

ACS_PI: int
"""letter pi"""

ACS_PLMINUS: int
"""plus-or-minus sign"""

ACS_PLUS: int
"""big plus sign"""

ACS_RARROW: int
"""right arrow"""

ACS_RTEE: int
"""right tee"""

ACS_S1: int
"""scan line 1"""

ACS_S3: int
"""scan line 3"""

ACS_S7: int
"""scan line 7"""

ACS_S9: int
"""scan line 9"""

ACS_SBBS: int
"""alternate name for lower right corner"""

ACS_SBSB: int
"""alternate name for vertical line"""

ACS_SBSS: int
"""alternate name for right tee"""

ACS_SSBB: int
"""alternate name for lower left corner"""

ACS_SSBS: int
"""alternate name for bottom tee"""

ACS_SSSB: int
"""alternate name for left tee"""

ACS_SSSS: int
"""alternate name for crossover or big plus"""

ACS_STERLING: int
"""pound sterling"""

ACS_TTEE: int
"""top tee"""

ACS_UARROW: int
"""up arrow"""

ACS_ULCORNER: int
"""upper left corner"""

ACS_URCORNER: int
"""upper right corner"""

ACS_VLINE: int
"""vertical line"""


## Mouse button
BUTTONn_PRESSED: int
"""Mouse button n pressed"""

BUTTONn_RELEASED: int
"""Mouse button n released"""

BUTTONn_CLICKED: int
"""Mouse button n clicked"""

BUTTONn_DOUBLE_CLICKED: int
"""Mouse button n double clicked"""

BUTTONn_TRIPLE_CLICKED: int
"""Mouse button n triple clicked"""

BUTTON_SHIFT: int
"""Shift was down during button state change"""

BUTTON_CTRL: int
"""Control was down during button state change"""

BUTTON_ALT: int
"""Control was down during button state change"""


## Colors
COLOR_BLACK: int
"""Black"""

COLOR_BLUE: int
"""Blue"""

COLOR_CYAN: int
"""Cyan (light greenish blue)"""

COLOR_GREEN: int
"""Green"""

COLOR_MAGENTA: int
"""Magenta (purplish red)"""

COLOR_RED: int
"""Red"""

COLOR_WHITE: int
"""White"""

COLOR_YELLOW: int
"""Yellow"""
