#version 330 core

uniform sampler2D tex;
uniform float time;

in vec2 uvs;

void main() {
    gl_FragColor = vec4(texture(tex, uvs).rgb, 1.0);
}
