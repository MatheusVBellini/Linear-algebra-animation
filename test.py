from os import name
from manim import *

class geometryTest(Scene):
    def construct(self):
        
        #
        # Object description
        sq = Square(
                side_length = 5.0,
                stroke_color = WHITE,
                fill_color = BLACK,
                fill_opacity = 1.0
        )

        zap = Circle(
                radius = 3.0,
                stroke_color = WHITE,
                stroke_width = 23.0,
                fill_color = GREEN,
                fill_opacity = 1.0
        )
        
        retangulo = Rectangle(
                stroke_color = WHITE,
                fill_color = WHITE,
                fill_opacity = 1.0,
                width = 1.0,
                height = 3.0
        )

        phone1 = Circle(
                radius = 0.5,
                stroke_color = WHITE,
                fill_color = WHITE,
                fill_opacity = 1.0
        ).to_corner(LEFT)

        phone2 = Circle(
                radius = 0.5,
                stroke_color = WHITE,
                fill_color = WHITE,
                fill_opacity = 1.0
        ).to_corner(RIGHT)

        #
        # Arrow generation with updater
        arrow1 = always_redraw(
                lambda : Line(
                    start = phone1.get_center(),
                    end = retangulo.get_top(),
                    color = YELLOW,
        ).add_tip())

        #
        # Scene rendering
        self.play(
                Create(sq), 
                run_time=2
        )
        self.play(
                Transform(sq, zap),
                Create(retangulo),
                Create(VGroup(phone1, phone2)),
                Create(arrow1),
                run_time=3
        )
        self.play(
                retangulo.animate.rotate(0.4),
                phone1.animate.move_to(np.array([-0.15,1.05,0])),
                phone2.animate.move_to(np.array([0.70,-0.85,0]))
        )
        self.wait()

class textTest(Scene):
    def construct(self):

        #
        # Screen elements
        matheq = MathTex("/alpha x^2")

        box = SurroundingRectangle(
                matheq,
                color = DARK_BLUE,
                buff = 0.5
        )

        nome = Tex("ZAP 3000").next_to(box, DOWN, buff = 0.25)

        #
        # Scene render
        self.play(Create(VGroup(matheq, box, nome)))
        self.wait()

class valueTrackerTest(Scene):
    def construct(self):
        
        k = ValueTracker(0)

        num = always_redraw(lambda : DecimalNumber().set_value(k.get_value()))

        self.play(Create(num))
        self.play(k.animate.set_value(10), run_time = 3, rate_func = smooth)
        self.wait()

class graphingTest(Scene):
    def construct(self):
        
        grafico = NumberPlane(
                x_range = [-4, 4, 2],
                x_length = 7,
                y_range = [0, 16, 4],
                y_length = 5
        ).add_coordinates()

        label = grafico.get_axis_labels(x_label = "x", y_label = "f(x)")

        parabola = grafico.plot(
                lambda x : x**2, 
                x_range = [-4, 4],
                color = GREEN
        )
        
        dif = ValueTracker(1)

        area = always_redraw(lambda : grafico.get_riemann_rectangles(
                graph = parabola,
                x_range = [-4, 4],
                dx = dif.get_value(),
                stroke_width = 0.1,
                stroke_color = WHITE       
        ))

        #value = always_redraw( 
        #                lambda : DecimalNumber().set_value(dif.get_value()),
        #        ).next_to(grafico, DOWN, buff=0.25)
        

        self.play(DrawBorderThenFill(grafico), Create(label))
        self.play(Create(parabola), FadeIn(area), run_time = 5)
        self.play(dif.animate.set_value(0.01),rate_func = linear, run_time = 7)
        self.wait()

class inverseMatrixTest(Scene):
    def construct(self):

        mat = Matrix([["a", "b", "c"],["d", "e", "f"],["g", "h", "i"]], 
                left_bracket = "(",
                right_bracket = ")"
        )


        bigmat = Matrix([["a", "b", "c", "|", 1, 0, 0],["d", "e", "f", "|", 0, 1, 0],["g", "h", "i", "|", 0, 0, 1]], 
                left_bracket = "(",
                right_bracket = ")"
        )

        #names = MathTex(r"A",r"I_3",r"A^(-1)")
        #names[0].next_to(bigmat, UR, buff=0.25)
        #names[1].next_to(bigmat, UR, buff=0.25)
        #names[2].next_to(bigmat, UR, buff=0.25)

        self.play(
                Create(mat),
        )
        self.play(
                FadeOut(mat),
                FadeIn(bigmat)
        )
        self.wait()
