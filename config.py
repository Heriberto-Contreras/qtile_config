# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess


mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"],"Return",lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"), # fullscreen
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "space", lazy.spawn("rofi -show drun")),
    # Volume control key binds
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([mod],
        "equal",
        lazy.spawn("amixer -c 2 sset Master 1+ unmute"),
        lazy.spawn("amixer -c 1 sset Master 2+ unmute")
        ),
    Key([mod],
        "minus",
        lazy.spawn("amixer -c 2 sset Master 1- unmute"),
        lazy.spawn("amixer -c 1 sset Master 1- unmute")
        ),
    #Key([mod], "equal", lazy.spawn("amixer -c 1 sset Master 1+ unmute")),
    #Key([mod], "minus", lazy.spawn("amixer -c 1 sset Master 1- unmute")),
    # Screen Brightness control key binds
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 5"))
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
colors = [
    ["#002b36", "#002b36"], # background 0
    ["#839496", "#839496"], # grey 1
    ["#073642", "#073642"], # different shade of backgroud color 2
    ["#dc322f", "#dc322f"], # Red 3
    ["#859900", "#859900"], # Green 4
    ["#b58900", "#b58900"], # Yellow 5
    ["#268bd2", "#268bd2"], # Blue 6
    ["#d33682", "#d33682"], # Magenta 7
    ["#2aa198", "#2aa198"], # Cyan 8
    ["#FFFFFF", "#FFFFFF"], # White 9
    ["#000000", "#000000"], # Black 10
    ["#6c71c4", "#6c71c4"], # Violet 11
    ["#cb4b16", "#cb4b16"]  # Orange 12
]
widget_defaults = dict(
    font="jetbrainsmono",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    foreground = colors[2],
                    background = colors[0]
                ),
                widget.GroupBox(
                    fontsize = 18,
                    margin_y = 4,
                    margin_x = 0,
                    padding_y =10,
                    padding_x = 10,
                    borderwidth = 1,
                    active = colors[9],
                    inactive = colors[10],
                    rounded = False,
                    highlight_method = "block",
                    this_current_screen_border = colors[12],
                    this_screen_border = colors[6],
                    other_current_screen_border = colors[12],
                    other_screen_border = colors[6],
                    foreground = colors[2],
                    background = colors[0],
                ),
                widget.WindowName(
                    background = colors[0],
                    foreground = colors[9],
                    fontsize = 18
                ),
                widget.TextBox(
                    background = colors[0],
                    foreground = colors[3],
                    fontsize = 60,
                    text = "◀",
                    padding = 0,
                ),
                widget.CheckUpdates(
                    distro = "Arch",
                    background = colors[3],
                    foreground = colors[10],
                    display_format = "Updates: {updates}",
                    no_update_string = "No Updates",
                    fontsize = 18
                ),
                widget.TextBox(
                    background = colors[3],
                    foreground = colors[7],
                    fontsize = 60,
                    text = "◀",
                    padding = 0,
                ),
                widget.TextBox(
                    background = colors[7],
                    foreground = colors[9],
                    fontsize = 18,
                    text = "🔈"
                ),
                widget.GenPollText(
                    update_interval=0.1,
                    func = lambda: subprocess.check_output("/home/Heriberto/.local/bin/volumeOne").decode("utf-8"),
                    background = colors[7],
                    fontsize = 18,
                ),
                widget.GenPollText(
                    update_interval=0.1,
                    func = lambda: subprocess.check_output("/home/Heriberto/.local/bin/volumeTwo").decode("utf-8"),
                    background = colors[7],
                    fontsize = 18,
                ),
                widget.TextBox(
                    background = colors[7],
                    foreground = colors[5],
                    fontsize = 60,
                    text = "◀",
                    padding = 0,
                ),
                widget.Systray(
                    background = colors[5],
                    fontsize = 18
                ),
                widget.TextBox(
                    background = colors[5],
                    foreground = colors[8],
                    fontsize = 60,
                    text = "◀",
                    padding = 0,
                ),
                widget.Clock(
                    format="%a %m-%d-%Y %I:%m %p",
                    fontsize = 18,
                    background = colors[8],
                    foreground = colors[10]
                ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
wmname = "LG3D"

