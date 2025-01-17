import moderngl as mgl
import pygame as pg

import scripts.globals as globals
from scripts.level import Level
from scripts.shaders import ShaderManager


class Editor:
    def __init__(self) -> None:
        # create two surfaces for rendering two the screen with flip
        self.screen: pg.Surface = pg.display.set_mode(
            (globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT),
            pg.OPENGL | pg.DOUBLEBUF,
        )
        self.display: pg.Surface = pg.Surface(
            (
                globals.WINDOW_WIDTH,
                globals.WINDOW_HEIGHT,
            )
        )
        pg.display.set_caption("Level Editor")
        _ = pg.mouse.set_visible(False)

        self.ctx: mgl.Context = mgl.create_context()
        self.shader_manager: ShaderManager = ShaderManager(self.ctx, self.display)

        self.clock: pg.Clock = pg.Clock()
        self.delta_time: float = 0.0

        self.scroll_offset: pg.Vector2 = pg.Vector2(30.0, 50.0)

        self.placing_tile = False

        self.running: bool = False

        self.level = Level(tilesize=16)
        self._loaded_tiles = False

    def _handle_key_down_event(self) -> None:
        pressed = pg.key.get_pressed()
        just_pressed = pg.key.get_just_pressed()
        just_released = pg.key.get_just_released()

        _ = just_released

        if just_pressed[pg.K_o]:
            self.level.import_tiles(self.display)
            self._loaded_tiles = True

        self.scroll_offset.x += (
            self.delta_time * 100 * (pressed[pg.K_a] - pressed[pg.K_d])
        )
        self.scroll_offset.y += (
            self.delta_time * 100 * (pressed[pg.K_w] - pressed[pg.K_s])
        )

    def _handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

        self._handle_key_down_event()

    def _render(self) -> None:
        _ = self.display.fill((0, 0, 0))

        if self._loaded_tiles:
            self.level.render(self.display, offset=self.scroll_offset)

        _ = pg.draw.rect(
            self.display,
            (0, 255, 255),
            pg.Rect(
                *pg.mouse.get_pos(),
                40.0,
                40.0,
            ),
        )

        self.shader_manager.tex.write(self.display.get_view("1"))
        self.shader_manager.render_obj.render(mode=mgl.TRIANGLE_STRIP)
        pg.display.flip()

    def run(self) -> None:
        """main program loop"""
        _ = pg.init()

        self.running = True
        while self.running:
            mouse_pos: tuple[int, int] = pg.mouse.get_pos()
            new_tile_pos: tuple[int, int] = (
                int((mouse_pos[0] + self.scroll_offset.x) // self.level.tilesize),
                int((mouse_pos[1] + self.scroll_offset.y) // self.level.tilesize),
            )
            _ = new_tile_pos

            self._handle_events()
            self._render()

            self.delta_time = self.clock.tick(0.0)
            self.delta_time = self.delta_time / 1000

        self.shader_manager.tex.release()
        pg.quit()
