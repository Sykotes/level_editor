import moderngl as mgl
import numpy as np
import pygame as pg


class ShaderManager:
    """Handles loading and compiling the fragment and vertex shaders
    Maps pg surfaces to a texture for use in surfaces"""

    def __init__(
        self,
        ctx: mgl.Context,
        display: pg.Surface,
    ) -> None:

        # a matrix to map corners of pygame surfaces to a opengl texture
        mat = np.asarray(
            [
                (-1.0, 1.0, 0.0, 0.0),
                (1.0, 1.0, 1.0, 0.0),
                (-1.0, -1.0, 0.0, 1.0),
                (1.0, -1.0, 1.0, 1.0),
            ],
            dtype="f4",
        )

        self.quad_buffer = ctx.buffer(mat.tobytes())

        f = open("./level_editor/shaders/shader.vert")
        self.vert_shader = f.read()
        f.close()
        f = open("./level_editor/shaders/shader.frag")
        self.frag_shader = f.read()
        f.close()

        self.program = ctx.program(
            vertex_shader=self.vert_shader,
            fragment_shader=self.frag_shader,
        )

        self.render_obj = ctx.vertex_array(
            self.program,
            [
                (
                    self.quad_buffer,
                    "2f 2f",
                    "vert",
                    "texcoord",
                )
            ],
        )

        self.tex = surf_to_texture(ctx, display)
        self.tex.use(0)

        self.program["tex"] = 0


def surf_to_texture(
    ctx: mgl.Context,
    surf: pg.Surface,
) -> mgl.Texture:
    # Components are the color channels (Red, Green, Blue and Alpha)
    number_of_components: int = 4
    tex: mgl.Texture = ctx.texture(surf.get_size(), number_of_components)
    tex.filter = (mgl.NEAREST, mgl.NEAREST)
    tex.swizzle = "BGRA"
    tex.write(surf.get_view("1"))
    return tex
