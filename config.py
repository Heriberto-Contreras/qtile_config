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
import json


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
    Key([mod, "control"], "equal", lazy.spawn("/home/heriberto/.local/bin/raiseBrightness")),
    Key([mod, "control"], "minus", lazy.spawn("/home/heriberto/.local/bin/lowerBrightness")),
    # Volume control key binds
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

# Getting pywal colors
# color0 = background and color15 = foreground
wal_colors_path = '/home/heriberto/.cache/wal/colors.json'
with open(wal_colors_path, 'r') as file:
    data = json.load(file)
    colors = data['colors'] # this is a colors dictonary 0-15

widget_defaults = dict(
    font="jetbrainsmono",
    fontsize=18,
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    margin_y = 4,
                    margin_x = 0,
                    padding_y =10,
                    padding_x = 10,
                    borderwidth = 1,
                    active = colors['color14'],
                    inactive = colors['color0'],
                    rounded = False,
                    highlight_method = "block",
                    this_current_screen_border = colors['color1'],
                    this_screen_border = colors['color4'],
                    foreground = colors['color15'],
                    background = colors['color0'],
                ),
                widget.WindowName(
                    background = colors['color2'],
                    foreground = colors['color0'],
                ),
                widget.CPU(
                    background = colors['color2'],
                    foreground = colors['color0'],
                    format = 'CPU: {load_percent}%'
                ),
                widget.Sep(
                    background = colors['color2'],
                    foreground = colors['color0'],
                ),
                widget.Memory(
                    background = colors['color2'],
                    foreground = colors['color0'],
                    format = 'RAM: {MemPercent:.1f}' '%'
                ),
                widget.Systray(
                    background = colors['color2'],
                    foreground = colors['color0'],
                ),
                widget.Sep(
                    background = colors['color2'],
                    foreground = colors['color0'],
                ),
                widget.Battery(
                    background = colors['color2'],
                    foreground = colors['color0'],                   
                    format = '🔋{percent:2.0%}'
                ),
                widget.Sep(
                    background = colors['color2'],
                    foreground = colors['color0'],
                ),
                widget.GenPollText(
                    background = colors['color2'],
                    foreground = colors['color0'],
                    update_interval = 0.1,
                    func = lambda: subprocess.check_output("/home/heriberto/.local/bin/getVolume").decode("utf-8"),
                    fmt = '🔊' '{}'
                ),
                widget.Sep(
                    background = colors['color2'],
                    foreground = colors['color0'],
                ),
                widget.GenPollText(
                    background = colors['color2'],
                    foreground = colors['color0'],
                    update_interval = 0.1,
                    func = lambda: subprocess.check_output("/home/heriberto/.local/bin/getBrightness").decode("utf-8"),
                    fmt = '🔆' '{}'
                ),
                widget.Sep(
                    background = colors['color2'],
                    foreground = colors['color0'],
                ),
                widget.Clock(
                    background = colors['color2'],
                    foreground = colors['color0'],
                    format="%Y-%m-%d %a %I:%M %p"
                )
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



