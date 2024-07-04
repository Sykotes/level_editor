import pygame as pg
import moderngl as mgl

import scripts.globals as globals
from scripts.shaders import ShaderManager
from scripts.level import Level


class Editor:
    def __init__(self) -> None:
        self.screen: pg.Surface = pg.display.set_mode(
            (globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT),
            pg.OPENGL | pg.DOUBLEBUF,
        )
        self.display: pg.Surface = pg.Surface((
            globals.WINDOW_WIDTH,
            globals.WINDOW_HEIGHT,
        ))
        pg.display.set_caption('Level Editor')
        _ = pg.mouse.set_visible(False)
        self.ctx: mgl.Context = mgl.create_context()
        self.shader_manager: ShaderManager = ShaderManager(
            self.ctx, self.display
        )

        self.clock: pg.Clock = pg.Clock()
        self.dt: float = 0.0

        self.running: bool = False

        self.level = Level()
        self._loaded_tiles = False

    def _handle_key_down_event(self, event: pg.Event) -> None:
        if event.key == pg.K_o:
            self.level.import_tiles(self.display)

    def _handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.KEYDOWN:
                self._handle_key_down_event(event)
                self._loaded_tiles = True

    def _render(self) -> None:
        _ = self.display.fill((0, 0, 0))
        _ = pg.draw.rect(
            self.display,
            (0, 255, 255),
            pg.Rect(
                *pg.mouse.get_pos(),
                40.0,
                40.0,
            ),
        )

        if self._loaded_tiles:
            self.level.render(self.display)

        self.shader_manager.tex.write(self.display.get_view('1'))
        self.shader_manager.render_obj.render(mode=mgl.TRIANGLE_STRIP)
        pg.display.flip()

    def run(self) -> None:
        _ = pg.init()

        prev_time: int = 0

        self.running = True
        while self.running:
            now: int = pg.time.get_ticks()
            self.dt = (now - prev_time) / 1000
            prev_time = now

            self._handle_events()
            self._render()

            _ = self.clock.tick(0.0)

        self.shader_manager.tex.release()
        pg.quit()
