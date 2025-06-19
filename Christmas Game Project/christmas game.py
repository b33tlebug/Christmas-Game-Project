from tkinter import Tk, Canvas, Button, HIDDEN, NORMAL
import pygame
from pygame import mixer
import winsound
from itertools import cycle
import time

# the music player, yes i only imported pygame for this im sorry, also mute music var and other sound vars
pygame.mixer.init()
pygame.mixer.music.load("Christmas Game Project/music+sounds/christmas-song.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(1)
musicstopped = 0
soundstopped = 0
button_press = "Christmas Game Project/music+sounds/button_place.wav"
place_sound = "Christmas Game Project/music+sounds/place_sound.wav"
remove_all = "Christmas Game Project/music+sounds/remove_all.wav"
ribbon_place = "Christmas Game Project/music+sounds/ribbon_place.wav"
remove_sound = "Christmas Game Project/music+sounds/remove_sound.wav"
explosion_sound = "Christmas Game Project/music+sounds/explosion_sound.wav"

# configure root and canvas
root = Tk()
root.title('Christmas Tree Decorating Game')
root.resizable(width=False, height=False)
c = Canvas(root, width=500, height=600)
c.configure(bg='pale goldenrod', highlightthickness=0)

# vars used in ornament related functions
r = 15
colours = ['brown4', 'firebrick3', 'red', 'darkorange2', 'tan4', 'gold2', 'goldenrod', 'darkolivegreen3', 'forest green', 'slategray1', 'steelblue2', 'darkorchid1', 'purple', 'palevioletred1', 'antiquewhite1', 'ghost white', 'thistle4', 'gray0']
chosen_deco = 'ball'
current_colour = 0
ornament_colour = colours[current_colour]
two_colour = cycle(['snow2', 'snow3', 'snow4', 'gray10', 'brown1', 'tan1', 'khaki1', 'pale green', 'darkslategray1', 'skyblue1', 'mediumpurple1', 'hotpink1'])
secondary = next(two_colour)
skin_colour = cycle(['#f3d7ce', '#e6bba0', '#d3a87b', '#c6917a', '#906159', '#6b2c18', '#361e16'])
skin = next(skin_colour)
click = 0
button_bg = 'navajowhite3'
active_bg = 'navajowhite4'

# utilities
def previous_colour():
    global ornament_colour, current_colour
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    if current_colour <= 0:
        print('MINIMUM')
    else:
        current_colour = current_colour - 1
        ornament_colour = colours[current_colour]
        c.itemconfig('display', fill=ornament_colour)
        Button.config(ornament_selection2, bg=colours[current_colour + 1])
        if current_colour <= 0:
            Button.config(ornament_selection, bg=colours[current_colour])
        else:
            Button.config(ornament_selection, bg=colours[current_colour - 1])
    c.itemconfig('wire', fill='black')
    c.itemconfig('garland', fill='springgreen4')
    c.itemconfig('wreath', outline='green4')
    c.itemconfig('stripe', fill=secondary)
    c.itemconfig('hollow', fill='')
    c.itemconfig('skin', fill=skin)
    c.itemconfig('pentre', fill='gold')
    c.itemconfig('flame', fill='orange')
def next_colour():
    global ornament_colour, current_colour
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    if current_colour == (len(colours) - 1):
        print('MAXIMUM')
    else:
        current_colour = current_colour + 1
        ornament_colour = colours[current_colour]
        c.itemconfig('display', fill=ornament_colour)
        Button.config(ornament_selection, bg=colours[current_colour - 1])
        if current_colour == (len(colours) - 1):
            Button.config(ornament_selection2, bg=colours[current_colour])
        else:
            Button.config(ornament_selection2, bg=colours[current_colour + 1])
    c.itemconfig('wire', fill='black')
    c.itemconfig('garland', fill='springgreen4')
    c.itemconfig('wreath', outline='green4')
    c.itemconfig('stripe', fill=secondary)
    c.itemconfig('hollow', fill='')
    c.itemconfig('skin', fill=skin)
    c.itemconfig('pentre', fill='gold')
    c.itemconfig('flame', fill='orange')
def upsize():
    global r
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    if r != 25:
        r = r + 1
        c.coords(ornament_display, 455+r, 555+r, 455-r, 555-r)
        c.itemconfig(ribbon_display, width=r)
        c.itemconfig(stripe_display, width=r)
        c.itemconfig(hori_display, width=(r/2))
        c.coords(diamond_display, 455, 555-r, 455+r, 555, 455, 555+r, 455-r, 555)
        c.coords(teardrop_display, 455, 555-r, 455+r, 555 -(r/2), 455, 555+r, 455-r, 555 - (r/2))
        c.coords(square_display, 455-r, 555-r, 455+r, 555-r, 455+r, 555+r, 455-r, 555+r)
        c.coords(egg_display, 455-(r/1.4), 555-r, 455+(r/1.4), 555+r)
        c.coords(star_display, 455, 555-r, 455+(r/3), 555-(r/3), 455+r, 555, 455+(r/3), 555+(r/3), 455, 555+r, 455-(r/3), 555+(r/3), 455-r, 555, 455-(r/3), 555-(r/3))
        c.coords(wreath_display, (455-r)-(r/3), (555-r)-(r/3), (455+r)+(r/3), (555+r)+(r/3))
        c.coords(breath_display, (455-r)-(r/3), (555-r)-(r/3), (455+r)+(r/3), (555+r)+(r/3))
        c.coords(pbase_display, 455-r, 555-r, 455, 555-(r/2), 455+r, 555-r, 455+(r/2), 555, 455+r, 555+r, 455, 555+(r/2), 455-r, 555+r, 455-(r/2), 555)
        c.coords(pcentre_display, 455-(r/5), 555-(r/5), 455+(r/5), 555+(r/5))
        c.coords(candle_display, 455-(r/2), 555-r, 455+(r/2), 555+r)
        c.coords(flame_display, 455, 555-r, 455+(r/2), 555-(r*1.35), 455, 555-(r*2), 455-(r/2), 555-(r*1.35))
    else:
        print('too big')
def downsize():
    global r
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    if r != 5:
        r = r - 1
        c.coords(ornament_display, 455+r, 555+r, 455-r, 555-r)
        c.itemconfig(ribbon_display, width=r)
        c.itemconfig(stripe_display, width=r)
        c.itemconfig(hori_display, width=(r/2))
        c.coords(diamond_display, 455, 555-r, 455+r, 555, 455, 555+r, 455-r, 555)
        c.coords(teardrop_display, 455, 555-r, 455+r, 555 -(r/2), 455, 555+r, 455-r, 555 - (r/2))
        c.coords(square_display, 455-r, 555-r, 455+r, 555-r, 455+r, 555+r, 455-r, 555+r)
        c.coords(egg_display, 455-(r/1.4), 555-r, 455+(r/1.4), 555+r)
        c.coords(star_display, 455, 555-r, 455+(r/3), 555-(r/3), 455+r, 555, 455+(r/3), 555+(r/3), 455, 555+r, 455-(r/3), 555+(r/3), 455-r, 555, 455-(r/3), 555-(r/3))
        c.coords(wreath_display, (455-r)-(r/3), (555-r)-(r/3), (455+r)+(r/3), (555+r)+(r/3))
        c.coords(breath_display, (455-r)-(r/3), (555-r)-(r/3), (455+r)+(r/3), (555+r)+(r/3))
        c.coords(pbase_display, 455-r, 555-r, 455, 555-(r/2), 455+r, 555-r, 455+(r/2), 555, 455+r, 555+r, 455, 555+(r/2), 455-r, 555+r, 455-(r/2), 555)
        c.coords(pcentre_display, 455-(r/5), 555-(r/5), 455+(r/5), 555+(r/5))
        c.coords(candle_display, 455-(r/2), 555-r, 455+(r/2), 555+r)
        c.coords(flame_display, 455, 555-r, 455+(r/2), 555-(r*1.35), 455, 555-(r*2), 455-(r/2), 555-(r*1.35))
    else:
        print('too small')
def next_secondary():
    global secondary
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    secondary = next(two_colour)
    c.itemconfig('stripe', fill=secondary)
    c.itemconfig(star_display, fill=secondary)
    c.itemconfig('berry', outline=secondary)
    Button.config(colour_change, bg=secondary)
def next_tertiary():
    global skin
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    if chosen_deco == 'figure':
        skin = next(skin_colour)
        c.itemconfig('skin', fill=skin)
        Button.config(tertiary_change, bg=skin)


# actual utilities
def stop_music():
    global musicstopped
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    if musicstopped == 1:
        pygame.mixer.music.set_volume(1)
        musicstopped = 0
        Button.config(mute_button, text='Mute Music')
        sound_button.place(x=88, y=560)
    else:
        pygame.mixer.music.set_volume(0)
        musicstopped = 1
        Button.config(mute_button, text='Unmute Music')
        sound_button.place(x=102, y=560)
def stop_sounds():
    global soundstopped, button_press, place_sound, remove_all, remove_sound, ribbon_place
    if soundstopped == 1:
        winsound.PlaySound(button_press, winsound.SND_ASYNC)
        button_press = 'music+sounds/button_place.wav'
        place_sound = 'music+sounds/place_sound.wav'
        remove_all = 'music+sounds/remove_all.wav'
        remove_sound = 'music+sounds/remove_sound.wav'
        ribbon_place = 'music+sounds/ribbon_place.wav'
        soundstopped = 0
        Button.config(sound_button, text='Mute Sounds')
    else:
        button_press = None
        place_sound = None
        remove_all = None
        remove_sound = None
        ribbon_place = None
        soundstopped = 1
        Button.config(sound_button, text='Unmute Sounds')
        
# decoration choice events
def choose_ball():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'ball'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(ornament_display, state=NORMAL)
    colour_change.place_forget()
    size_down.place(x=189, y=405)
    size_up.place(x=259, y=405)
    tertiary_change.place_forget()
def choose_diamond():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'diamond'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(diamond_display, state=NORMAL)
    colour_change.place_forget()
    size_down.place(x=189, y=405)
    size_up.place(x=259, y=405)
    tertiary_change.place_forget()
def choose_teardrop():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'teardrop'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(teardrop_display, state=NORMAL)
    colour_change.place_forget()
    size_down.place(x=189, y=405)
    size_up.place(x=259, y=405)
    tertiary_change.place_forget()
def choose_square():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'square'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(square_display, state=NORMAL)
    colour_change.place_forget()
    size_down.place(x=189, y=405)
    size_up.place(x=259, y=405)
    tertiary_change.place_forget()
def choose_triangle():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'triangle'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(triangle_display, state=NORMAL)
    colour_change.place_forget()
    size_down.place(x=189, y=405)
    size_up.place(x=259, y=405)
    tertiary_change.place_forget()
def choose_ribbon():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'ribbon'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(ribbon_display, state=NORMAL)
    colour_change.place_forget()
    size_down.place(x=189, y=405)
    size_up.place(x=259, y=405)
    tertiary_change.place_forget()
def choose_lights():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'lights'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(wire_display, state=NORMAL)
    c.itemconfig(lights_display, state=NORMAL)
    colour_change.place_forget()
    size_down.place_forget()
    size_up.place_forget()
    tertiary_change.place_forget()
def choose_stripe():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'stripes'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(ribbon_display, state=NORMAL)
    c.itemconfig(stripe_display, state=NORMAL)
    colour_change.place(x=313, y=405)
    size_down.place(x=189, y=405)
    size_up.place(x=259, y=405)
    tertiary_change.place_forget()
def choose_hori():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'hori'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(ribbon_display, state=NORMAL)
    c.itemconfig(hori_display, state=NORMAL)
    colour_change.place(x=313, y=405)
    size_down.place(x=189, y=405)
    size_up.place(x=259, y=405)
    tertiary_change.place_forget()
def choose_egg():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'egg'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(egg_display, state=NORMAL)
    colour_change.place_forget()
    size_down.place(x=189, y=405)
    size_up.place(x=259, y=405)
    tertiary_change.place_forget()
def choose_garland():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'garland'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(garland_display, state=NORMAL)
    c.itemconfig(berry_display, state=NORMAL)
    colour_change.place(x=189, y=405)
    size_down.place_forget()
    size_up.place_forget()
    tertiary_change.place_forget()
def choose_star():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'star'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(star_display, state=NORMAL)
    colour_change.place(x=313, y=405)
    size_down.place(x=189, y=405)
    size_up.place(x=259, y=405)
    tertiary_change.place_forget()
def choose_wreath():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'wreath'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(wreath_display, state=NORMAL)
    c.itemconfig(breath_display, state=NORMAL)
    colour_change.place(x=313, y=405)
    size_down.place(x=189, y=405)
    size_up.place(x=259, y=405)
    tertiary_change.place_forget()
def choose_figure():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'figure'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(fbody_display, state=NORMAL)
    c.itemconfig(fhead_display, state=NORMAL)
    colour_change.place(x=189, y=405)
    tertiary_change.place(x=303, y=405)
    size_down.place_forget()
    size_up.place_forget()
def choose_poinsettia():
    global chosen_deco
    winsound.PlaySound(button_press, winsound.SND_ASYNC)
    chosen_deco = 'poinsettia'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(pbase_display, state=NORMAL)
    c.itemconfig(pcentre_display, state=NORMAL)
    colour_change.place(x=313, y=405)
    size_down.place(x=189, y=405)
    size_up.place(x=259, y=405)
    tertiary_change.place_forget()
def choose_candle():
    global chosen_deco
    winsound.PlaySound(button_press,winsound.SND_ASYNC)
    chosen_deco = 'candle'
    c.itemconfig('display', state=HIDDEN)
    c.itemconfig(candle_display, state=NORMAL)
    c.itemconfig(flame_display, state=NORMAL)
    colour_change.place(x=313, y=405)
    size_down.place(x=189, y=405)
    size_up.place(x=259, y=405)
    tertiary_change.place_forget()

# canvas events
# places ornament, a bunch of elifs for ornament types, last one is CANDLE currently
def place(event):
    winsound.PlaySound(place_sound, winsound.SND_ASYNC)
    if chosen_deco == 'ball':
        x, y = event.x, event.y     #clicked position
        c.create_oval(x - r, y - r, x + r, y + r, fill=ornament_colour, state=NORMAL, tags='ornaments')         #print circle
    elif chosen_deco == 'ribbon':
        global click
        x1 = event.x
        y1 = event.y
        w = event.widget ## Get the canvas object you clicked on
        if click == 0:
            w.cords = (x1,y1)
            click = 1
        else:
            winsound.PlaySound(ribbon_place, winsound.SND_ASYNC)
            c.create_line(w.cords[0], w.cords[1], x1, y1, fill=ornament_colour, width=r, state=NORMAL, tags='ornaments')
            w.cords = (440, 470)
            click = 0
    elif chosen_deco == 'diamond':
        x, y = event.x, event.y     #clicked position
        c.create_polygon(x, y - r, x + r, y, x, y + r, x - r, y, fill=ornament_colour, outline='black', state=NORMAL, tags='ornaments')
    elif chosen_deco == 'teardrop':
        x, y = event.x, event.y     #clicked position
        c.create_polygon(x, y - r, x + r, y - (r/2), x, y + r, x - r, y - (r/2), fill=ornament_colour, outline='black', state=NORMAL, tags='ornaments')
    elif chosen_deco == 'lights':
        x1 = event.x
        y1 = event.y
        w = event.widget ## Get the canvas object you clicked on
        if click == 0:
            w.cordsl = (x1,y1)
            click = 1
        else:
            winsound.PlaySound(ribbon_place, winsound.SND_ASYNC)
            c.create_line(w.cordsl[0], w.cordsl[1], x1, y1, fill='black', width=5, state=NORMAL, tags='wired')
            c.create_line(w.cordsl[0], w.cordsl[1], x1, y1, fill=ornament_colour, width=15, dash=(1, 3), state=NORMAL, tags='light')
            click = 0
    elif chosen_deco == 'square':
        x, y = event.x, event.y
        c.create_polygon(x-r, y-r, x+r, y-r, x+r, y+r, x-r, y+r, fill=ornament_colour, outline='black', state=NORMAL, tags='ornaments')
    elif chosen_deco == 'stripes':                                               
        x1 = event.x
        y1 = event.y
        w = event.widget ## Get the canvas object you clicked on
        if click == 0:
            w.cordsl = (x1,y1)
            click = 1
        else:
            winsound.PlaySound(ribbon_place, winsound.SND_ASYNC)
            c.create_line(w.cordsl[0], w.cordsl[1], x1, y1, fill=ornament_colour, width=r, state=NORMAL, tags='wired')
            c.create_line(w.cordsl[0], w.cordsl[1], x1, y1, fill=secondary, width=r, dash=(1, 3), state=NORMAL, tags='light')
            click = 0
    elif chosen_deco == 'hori':
        x1 = event.x
        y1 = event.y
        w = event.widget ## Get the canvas object you clicked on
        if click == 0:
            w.cordsl = (x1,y1)
            click = 1
        else:
            winsound.PlaySound(ribbon_place, winsound.SND_ASYNC)
            c.create_line(w.cordsl[0], w.cordsl[1], x1, y1, fill=ornament_colour, width=r, state=NORMAL, tags='wired')
            c.create_line(w.cordsl[0], w.cordsl[1], x1, y1, fill=secondary, width=(r/2), state=NORMAL, tags='light')
            click = 0
    elif chosen_deco == 'egg':
        x, y = event.x, event.y     #clicked position
        c.create_oval(x - (r/1.4), y - r, x + (r/1.4), y + r, fill=ornament_colour, state=NORMAL, tags='ornaments')         #print circle
    elif chosen_deco == 'garland':
        x1 = event.x
        y1 = event.y
        w = event.widget ## Get the canvas object you clicked on
        if click == 0:
            w.cordsl = (x1,y1)
            click = 1
        else:
            winsound.PlaySound(ribbon_place, winsound.SND_ASYNC)
            c.create_line(w.cordsl[0], w.cordsl[1], x1, y1, fill='springgreen4', width=5, state=NORMAL, tags='wired')
            c.create_line(w.cordsl[0], w.cordsl[1], x1, y1, fill=secondary, width=15, dash=(1, 3), state=NORMAL, tags='light')
            click = 0
    elif chosen_deco == 'triangle':
        x, y = event.x, event.y
        c.create_polygon(x-r, y-r, x+r, y-r, x, y+r, fill=ornament_colour, outline='black', state=NORMAL, tags='ornaments')
    elif chosen_deco == 'star':
        x, y = event.x, event.y
        c.create_polygon(x, y-r, x+(r/3), y-(r/3), x+r, y, x+(r/3), y+(r/3), x, y+r, x-(r/3), y+(r/3), x-r, y, x-(r/3), y-(r/3), fill=secondary, outline='black', state=NORMAL, tags='ornaments')
    elif chosen_deco == 'wreath':
        x, y = event.x, event.y
        c.create_oval((x-r)-(r/3), (y-r)-(r/3), (x+r)+(r/3), (y+r)+(r/3), width=15, outline='green4', state=NORMAL, tags='wreaths')
        c.create_oval((x-r)-(r/3), (y-r)-(r/3), (x+r)+(r/3), (y+r)+(r/3), width=8, dash=(1,3), outline=secondary, state=NORMAL, tags='wreaths')
    elif chosen_deco == 'figure':
        x, y = event.x, event.y
        c.create_polygon(x, y-15, x+15, y+15, x-15, y+15, fill=secondary, state=NORMAL, tags='figures')
        c.create_oval(x-10, y-30, x+10, y-10, fill=skin, state=NORMAL, tags='figured')
    elif chosen_deco == 'poinsettia':
        x, y = event.x, event.y
        c.create_polygon(x-r, y-r, x, y-(r/2), x+r, y-r, x+(r/2), y, x+r, y+r, x, y+(r/2), x-r, y+r, x-(r/2), y, fill=secondary, state=NORMAL, tags='light')
        c.create_oval(x-(r/5), y-(r/5), x+(r/5), y+(r/5), fill='gold', state=NORMAL, tags='poincentre')
    else:
        x, y = event.x, event.y
        c.create_rectangle(x-(r/2), y-r, x+(r/2), y+r, fill=secondary, state=NORMAL, tags=('candled', 'candles'))
        c.create_polygon(x, y-r, x+(r/2), y-(r*1.35), x, y-(r*2), x-(r/2), y-(r*1.35), fill='orange', state=NORMAL, tags='candles')

# destroys ornament, destroy_both is for stripe types and lights
def destroy(event):
    winsound.PlaySound(remove_sound, winsound.SND_ASYNC)
    c.delete('current')
def destroy_both(event):
    winsound.PlaySound(remove_sound, winsound.SND_ASYNC)
    light_coords = c.bbox('current')
    c.addtag_withtag('delete', 'current')
    c.addtag_enclosed('delete', light_coords[0], light_coords[1], light_coords[2], light_coords[3])
    c.dtag('ornaments', 'delete')
    c.dtag('wreaths', 'delete')
    c.dtag('figures', 'delete')
    c.dtag('figured', 'delete')
    c.delete('delete')
def destroy_wreath(event):
    winsound.PlaySound(remove_sound, winsound.SND_ASYNC)
    wreath_coords = c.bbox('current')
    c.addtag_withtag('delete', 'current')
    c.addtag_enclosed('delete', (wreath_coords[0]-8), (wreath_coords[1]-8), (wreath_coords[2]+8), (wreath_coords[3]+8))
    c.dtag('ornaments', 'delete')
    c.dtag('light', 'delete')
    c.dtag('wired', 'delete')
    c.dtag('figures', 'delete')
    c.dtag('figured', 'delete')
    c.delete('delete')
def destroy_figure(event):
    winsound.PlaySound(remove_sound, winsound.SND_ASYNC)
    figure_coords = c.bbox('current')
    c.addtag_withtag('delete', 'current')
    c.addtag_enclosed('delete', figure_coords[0], (figure_coords[1]-15), figure_coords[2], figure_coords[3])
    c.dtag('ornaments', 'delete')
    c.dtag('light', 'delete')
    c.dtag('wired', 'delete')
    c.dtag('wreaths', 'delete')
    c.dtag('wreaths', 'delete')
    c.dtag('candles', 'delete')
    c.delete('delete')
def destroy_candle(event):
    winsound.PlaySound(remove_sound, winsound.SND_ASYNC)
    figure_coords = c.bbox('current')
    c.addtag_withtag('delete', 'current')
    c.addtag_enclosed('delete', figure_coords[0], (figure_coords[1]-(15+r)), figure_coords[2], figure_coords[3])
    c.dtag('ornaments', 'delete')
    c.dtag('light', 'delete')
    c.dtag('wired', 'delete')
    c.dtag('wreaths', 'delete')
    c.dtag('figures', 'delete')
    c.dtag('figured', 'delete')
    c.delete('delete')
def destroy_all():
    winsound.PlaySound(remove_all, winsound.SND_ASYNC)
    c.delete('ornaments', 'light', 'wired', 'wreaths', 'figures', 'figured', 'poincentre', 'candled', 'candles')
def explosion():
    c.delete('ornaments', 'light', 'wired', 'tree', 'leaves')
    big_red = c.create_oval(70, 30, 430, 400, outline='red', fill='red', state=NORMAL, tags='explosion')
    big_orange = c.create_oval(110, 70, 390, 360, outline='orange', fill='orange', state=NORMAL, tags='explosion')
    big_yellow = c.create_oval(150, 110, 350, 320, outline='yellow', fill='yellow', state=NORMAL, tags='explosion')
    winsound.PlaySound(explosion_sound, winsound.SND_ASYNC)
    c.after(500, explosion_after)
def explosion_after():
    pygame.mixer.music.stop()
    explosion_button.place_forget()
    c.delete('explosion')
    c.create_text(250, 220, font='Georgia', text='what did you think would happen?')

# the tree
first_leaves = c.create_polygon(250, 40, 80, 200, 420, 200, outline='dark green', fill='dark green', tags='leaves')
second_leaves = c.create_polygon(250, 160, 80, 330, 420, 330, outline='dark green', fill='dark green', tags='leaves')
carpet = c.create_oval(140, 365, 360, 390, width=5, outline='firebrick4', fill='firebrick4', tags='tree')
trunk = c.create_rectangle(210, 330, 290, 380, outline='sienna4', fill='sienna4', tags='tree')

# ornament displays, make other displays that are hidden, such as a diamond ornament or like a ribbon or square or something
label_display = c.create_text(455, 510, font='Georgia', text='Selected:')
ornament_display = c.create_oval(440, 540, 470, 570, fill=ornament_colour, outline='black', state=NORMAL, tags='display')
ribbon_display = c.create_line(440, 540, 470, 570, fill=ornament_colour, width=r, state=HIDDEN, tags='display')
stripe_display = c.create_line(440, 540, 470, 570, fill='white', width=r, dash=(1, 3), state=HIDDEN, tags=('display', 'stripe'))
hori_display = c.create_line(440, 540, 470, 570, fill='white', width=(r/2), state=HIDDEN, tags=('display', 'stripe'))
diamond_display = c.create_polygon(455, 540, 470, 555, 455, 570, 440, 555, fill=ornament_colour, outline='black', state=HIDDEN, tags='display')
teardrop_display = c.create_polygon(455, 540, 470, 555 - (r/2), 455, 570, 440, 555 - (r/2), fill=ornament_colour, outline='black', state=HIDDEN, tags='display')
square_display = c.create_polygon(440, 540, 470, 540, 470, 570, 440, 570, fill=ornament_colour, outline='black', state=HIDDEN, tags='display')
triangle_display = c.create_polygon(440, 540, 470, 540, 455, 570, fill=ornament_colour, outline='black', state=HIDDEN, tags='display')
egg_display = c.create_oval(455-(r/1.4), 540, 455+(r/1.4), 570, fill=ornament_colour, outline='black', state=HIDDEN, tags='display')
wire_display = c.create_line(440, 540, 470, 570, fill='black', width=5, state=HIDDEN, tags=('display', 'wire'))
lights_display = c.create_line(440, 540, 470, 570, fill=ornament_colour, width=15, dash=(1, 3), state=HIDDEN, tags='display')
garland_display = c.create_line(440, 540, 470, 570, fill='springgreen4', width=5, state=HIDDEN, tags=('display', 'garland'))
berry_display = c.create_line(440, 540, 470, 570, fill=secondary, width=15, dash=(1, 3), state=HIDDEN, tags=('display', 'stripe'))
star_display = c.create_polygon(455, 540, 455+(r/3), 555-(r/3), 470, 555, 455+(r/3), 555+(r/3), 455, 570, 455-(r/3), 555+(r/3), 440, 555, 455-(r/3), 555-(r/3), fill=secondary, outline='black', state=HIDDEN, tags=('display', 'stripe'))
wreath_display = c.create_oval(435, 535, 475, 575, outline='green4', width=15, state=HIDDEN, tags=('display', 'wreath', 'hollow'))
breath_display = c.create_oval(435, 535, 475, 575, outline=secondary, width=8, dash=(1, 3), state=HIDDEN, tags=('display', 'berry', 'hollow'))
fbody_display = c.create_polygon(455, 540, 470, 570, 440, 570, fill=secondary, state=HIDDEN, tags=('display', 'stripe'))
fhead_display = c.create_oval(445, 525, 465, 545, fill=skin, state=HIDDEN, tags=('display', 'skin'))
pbase_display = c.create_polygon(455-r, 555-r, 455, 555-(r/2), 455+r, 555-r, 455+(r/2), 555, 455+r, 555+r, 455, 555+(r/2), 455-r, 555+r, 455-(r/2), 555, fill=secondary, state=HIDDEN, tags=('display', 'stripe'))
pcentre_display = c.create_oval(455-(r/5), 555-(r/5), 455+(r/5), 555+(r/5), fill='gold', state=HIDDEN, tags=('display', 'pentre'))
candle_display = c.create_rectangle(455-(r/2), 555-r, 455+(r/2), 555+r, fill=secondary, state=HIDDEN, tags=('display', 'stripe'))
flame_display = c.create_polygon(455, 555-r, 455+(r/2), 555-(r*1.35), 455, 555-(r*2), 455-(r/2), 555-(r*1.35), fill='orange', state=HIDDEN, tags=('display', 'flame'))

# menu buttons down here
# colour select buttons and size change buttons
ornament_selection = Button(root, bg=button_bg, activebackground=active_bg, text='Previous Colour', command=previous_colour)
ornament_selection.place(x=10, y=405)
ornament_selection2 = Button(root, bg=button_bg, activebackground=active_bg, text='Next Colour', command=next_colour)
ornament_selection2.place(x=110, y=405)
size_down = Button(root, bg=button_bg, activebackground=active_bg, text='Size Down', command=downsize)
size_down.place(x=189, y=405)
size_up = Button(root, bg=button_bg, activebackground=active_bg, text='Size Up', command=upsize)
size_up.place(x=259, y=405)
colour_change = Button(root, bg=button_bg, activebackground=active_bg, text='Change Secondary', command=next_secondary)
colour_change.place(x=313, y=405)
colour_change.place_forget()
tertiary_change = Button(root, bg=button_bg, activebackground=active_bg, text='Change Tertiary', command=next_tertiary)

# decoration select buttons
# ornaments
deco_ornament = Button(root, bg=button_bg, activebackground=active_bg, text='Bauble', command=choose_ball)
deco_ornament.place(x=10, y=435)
deco_diamond = Button(root, bg=button_bg, activebackground=active_bg, text='Diamond', command=choose_diamond)
deco_diamond.place(x=60, y=435)
deco_teardrop = Button(root, bg=button_bg, activebackground=active_bg, text='Teardrop', command=choose_teardrop)
deco_teardrop.place(x=124, y=435)
deco_square = Button(root, bg=button_bg, activebackground=active_bg, text='Square', command=choose_square)
deco_square.place(x=186, y=435)
deco_egg = Button(root, bg=button_bg, activebackground=active_bg, text='Faberge', command=choose_egg)
deco_egg.place(x=236, y=435)
deco_triangle = Button(root, bg=button_bg, activebackground=active_bg, text='Triangle', command=choose_triangle)
deco_triangle.place(x=293, y=435)
# ribbons and lights, stripe types
deco_ribbon = Button(root, bg=button_bg, activebackground=active_bg, text='Ribbon', command=choose_ribbon)
deco_ribbon.place(x=10, y=465)
deco_striped = Button(root, bg=button_bg, activebackground=active_bg, text='Vertical Stripes', command=choose_stripe)
deco_striped.place(x=62, y=465)
deco_horizontal = Button(root, bg=button_bg, activebackground=active_bg, text='Horizontal Stripes', command=choose_hori)
deco_horizontal.place(x=153, y=465)
deco_lights = Button(root, bg=button_bg, activebackground=active_bg, text='Lights', command=choose_lights)
deco_lights.place(x=260, y=465)
deco_garland = Button(root, bg=button_bg, activebackground=active_bg, text='Garland', command=choose_garland)
deco_garland.place(x=306, y=465)
# tree toppers and misc (wreaths, poinsettias, things with limited colours to choose between (might have their own colour sets))
deco_star = Button(root, bg=button_bg, activebackground=active_bg, text='Star', command=choose_star)
deco_star.place(x=10, y=495)
deco_wreath = Button(root, bg=button_bg, activebackground=active_bg, text='Wreath', command=choose_wreath)
deco_wreath.place(x=44, y=495)
deco_figure = Button(root, bg=button_bg, activebackground=active_bg, text='Figure', command=choose_figure)
deco_figure.place(x=96, y=495)
deco_poinsettia = Button(root, bg=button_bg, activebackground=active_bg, text='Poinsettia', command=choose_poinsettia)
deco_poinsettia.place(x=143, y=495)
deco_candle = Button(root, bg=button_bg, activebackground=active_bg, text='Candle', command=choose_candle)
deco_candle.place(x=209, y=495)

#utility buttons
# destroy all ornaments button?
destroy_button = Button(root, bg='firebrick1', activebackground=active_bg, text='Remove All', command=destroy_all)
destroy_button.place(x=10, y=530)
explosion_button = Button(root, bg='red4', activebackground=active_bg, text='Self Destruct', fg='snow2', command=explosion)
explosion_button.place(x=86, y=530)
# music mute and unmute button & mute sounds buttons
mute_button = Button(root, bg='grey', activebackground=active_bg, text='Mute Music', command=stop_music)
mute_button.place(x=10, y=560)
sound_button = Button(root, bg='grey', activebackground=active_bg, text='Mute Sounds', command=stop_sounds)
sound_button.place(x=88, y=560)

# bind canvas events
c.tag_bind('leaves', '<1>', place)
c.tag_bind('ornaments', '<1>', place)
c.tag_bind('light', '<1>', place)
c.tag_bind('ornaments', '<3>', destroy)
c.tag_bind('light', '<3>', destroy_both)
c.tag_bind('wreaths', '<3>', destroy_wreath)
c.tag_bind('figures', '<3>', destroy_figure)
c.tag_bind('candled', '<3>', destroy_candle)

c.pack()
root.mainloop()
