import pygame as pg
import moderngl as mgl

import scripts.globals as globals
from scripts.shaders import ShaderManager


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
        pg.mouse.set_visible(False)
        self.ctx: mgl.Context = mgl.create_context()
        self.shader_manager: ShaderManager = ShaderManager(
            self.ctx, self.display
        )

        self.clock: pg.Clock = pg.Clock()
        self.dt: float = 0.0

        self.running: bool = False

    def handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def render(self) -> None:
        self.display.fill((0, 0, 0))
        pg.draw.rect(
            self.display,
            (0, 255, 255),
            pg.Rect(
                *pg.mouse.get_pos(),
                40.0,
                40.0,
            ),
        )

        self.shader_manager.tex.write(self.display.get_view('1'))
        self.shader_manager.render_obj.render(mode=mgl.TRIANGLE_STRIP)
        pg.display.flip()

    def run(self) -> None:
        pg.init()

        prev_time: int = 0

        self.running = True
        while self.running:
            now: int = pg.time.get_ticks()
            self.dt = (now - prev_time) / 1000
            prev_time = now

            self.handle_events()
            self.render()

            self.clock.tick(0.0)

        self.shader_manager.tex.release()
        pg.quit()
