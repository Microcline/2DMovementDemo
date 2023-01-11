"""
Author: 
Date:   
"""
import tcod as libtcod
from input_handlers import handle_keys
from entity import Entity
from render_functions import render_all, clear_all
from map_objects.game_map import GameMap

def main():
    # Screen vars
    screen_width = 80
    screen_height = 50
    map_width = 80 
    map_height = 45 #comment

    # Console vars
    con = libtcod.console_new(screen_width, screen_height)
    game_map = GameMap(map_width, map_height)
    game_map.make_map()

    colors = {'dark_wall': libtcod.Color(0, 0, 100),
              'dark_ground': libtcod.Color(50, 50, 150)
    }

    # Entity instantiation and dictionary tracking
    player  = Entity(1, 1, '@', libtcod.white)
    npc     = Entity(10, 10, '@', libtcod.yellow)
    entities = [player, npc]

    # What does this do?
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, 'Little Red Wagon Autofighter', False)

    # key + mouse support
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # Game loop
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        render_all(con, entities, game_map, screen_width, screen_height, colors)
        libtcod.console_flush()
        #libtcod.console_put_char(con, player.x, player.y, ' ', libtcod.BKGND_NONE)
        clear_all(con, entities)
        
        # Gather keypress
        action = handle_keys(key)
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')  

        if move:
            deltaX, deltaY = move
            if not game_map.is_blocked(player.x + deltaX, player.y + deltaY):
                player.move(deltaX, deltaY)
        if exit:
            return True
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        # Exit the console
        if key.vk == libtcod.KEY_ESCAPE:
            return True
    # End game loop



if __name__ == '__main__':
    main()  # comment for change