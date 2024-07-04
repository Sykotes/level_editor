import array

import moderngl as mgl
import pygame as pg


class ShaderManager:
    def __init__(
        self,
        ctx: mgl.Context,
        display: pg.Surface,
    ) -> None:
        self.quad_buffer = ctx.buffer(
            data=array.array(
                "f",
                [
                    -1.0,
                    1.0,
                    0.0,
                    0.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    -1.0,
                    -1.0,
                    0.0,
                    1.0,
                    1.0,
                    -1.0,
                    1.0,
                    1.0,
                ],
            )
        )

        f = open("shaders/shader.vert")
        self.vert_shader = f.read()
        f.close()
        f = open("shaders/shader.frag")
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
    tex: mgl.Texture = ctx.texture(surf.get_size(), 4)
    tex.filter = (mgl.NEAREST, mgl.NEAREST)
    tex.swizzle = "BGRA"
    tex.write(surf.get_view("1"))
    return tex
