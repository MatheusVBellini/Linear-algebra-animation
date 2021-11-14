from manim import *

class GenSquare(Scene):
    def construct(self):

        sq = Square(
                side_length=5.0,
                stroke_color=WHITE,
                fill_color=BLACK,
                fill_opacity=1.0
        )

        zap = Circle(
                radius = 3.0,
                stroke_color=WHITE,
                stroke_width=23.0,
                fill_color=GREEN,
                fill_opacity=1.0
        )
        
        retangulo = Rectangle(
                stroke_color=WHITE,
                fill_color=WHITE,
                fill_opacity=1.0,
                width=1.0,
                height=3.0
        )

        phone1 = Circle(
                radius = 0.5,
                stroke_color=WHITE,
                fill_color=WHITE,
                fill_opacity=1.0
        ).to_corner(LEFT)

        phone2 = Circle(
                radius = 0.5,
                stroke_color=WHITE,
                fill_color=WHITE,
                fill_opacity=1.0
        ).to_corner(RIGHT)

        self.play(
                Create(sq), 
                run_time=2
        )
        self.play(
                Transform(sq, zap), 
                Create(retangulo), 
                Create(phone1),
                Create(phone2),  
                run_time=3
        )
        self.play(
                retangulo.animate.rotate(0.4),
                phone1.animate.move_to(np.array([-0.15,1.05,0])),
                phone2.animate.move_to(np.array([0.70,-0.85,0]))
        )
        self.wait()
