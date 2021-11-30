from os import name
from manim import *
import math

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
        
        def matrixUpdate(values1,values2,vector1,vector2):
            vector1[0].set_value(values1[0]),
            vector1[1].set_value(values1[1]),
            vector1[2].set_value(values1[2]),
            vector1[3].set_value(values1[3]),
            vector1[4].set_value(values1[4]),
            vector1[5].set_value(values1[5]),
            vector1[6].set_value(values1[6]),
            vector1[7].set_value(values1[7]),
            vector1[8].set_value(values1[8]),
            vector2[0].set_value(values2[0]),
            vector2[1].set_value(values2[1]),
            vector2[2].set_value(values2[2]),
            vector2[3].set_value(values2[3]),
            vector2[4].set_value(values2[4]),
            vector2[5].set_value(values2[5]),
            vector2[6].set_value(values2[6]),
            vector2[7].set_value(values2[7]),
            vector2[8].set_value(values2[8]),

            return vector1,vector2

        mat = Matrix([["a", "b", "c"],["d", "e", "f"],["g", "h", "i"]], 
                left_bracket = "(",
                right_bracket = ")"
        )   

        x = [ValueTracker(1), ValueTracker(1), ValueTracker(1), ValueTracker(1), ValueTracker(1), ValueTracker(1),ValueTracker(1), ValueTracker(1), ValueTracker(1)] 
        y = [ValueTracker(1), ValueTracker(0), ValueTracker(0), ValueTracker(0), ValueTracker(1), ValueTracker(0),ValueTracker(0), ValueTracker(0), ValueTracker(1)] 

        bigmat = always_redraw(lambda : Matrix([[x[0].get_value(), x[1].get_value(), x[2].get_value(), "|", y[0].get_value(), y[1].get_value(), y[2].get_value()],[x[3].get_value(), x[4].get_value(), x[5].get_value(), "|", y[3].get_value(), y[4].get_value(), y[5].get_value()],[x[6].get_value(), x[7].get_value(), x[8].get_value(), "|", y[6].get_value(), y[7].get_value(), y[8].get_value()]], 
                left_bracket = "(",
                right_bracket = ")"
        ))

        names = MathTex(r"A",r"I_3",r"A^(-1)")
        names[0].move_to(np.array([-2.2, 1.8, 0]))
        names[1].move_to(np.array([2.2, 1.8, 0]))
        names[2].next_to(bigmat, UR, buff=0.25)

        self.play(
                Create(mat)
        )
        self.wait(2)
        self.play(
                Transform(mat,bigmat),
                FadeIn(VGroup(names[0],names[1]))
        )
        self.play(
                x,y = matrixUpdate([2,2,2,2,2,2,2,2,2],[2,0,1,2,0,1,2,0,1],x,y)
        )
        self.wait()

class Tangent(Scene):
    CONFIG = {
        "y_max" : 10,
        "y_min" : -10,
        "x_max" : 5,
        "x_min" : -5,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : BLUE, 
        "num_graph_anchor_points": 3000, #this is the number of points that graph manim
        "graph_origin" : ORIGIN,
    }
    def construct(self):
        self.setup_axes()
        graph_1 = self.get_graph(lambda x : math.tan(x), 
                                    color = RED,
                                    x_min = 0, # Domain 1
                                    x_max = math.pi/2 - 0.1
                                    )
        graph_2 =self.get_graph(lambda x : 1/x,
                                    color = GREEN,
                                    x_min = math.pi/2 + 0.1, # Domain 2
                                    x_max = math.pi
                                    )
        self.play(
            ShowCreation(graph_1),
            run_time = 1
        )
        self.play(
            ShowCreation(graph_2),
            run_time = 1
        )
        self.wait()
