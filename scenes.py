from os import name
from manim import *
import math

class trigonometrics(Scene):
    CONFIG = {
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "num_graph_anchor_points": 3000, #this is the number of points that graph manim
    }

    def construct(self):

        grafico = NumberPlane(
                x_range = [-13, 13, 4],
                x_length = 10,
                y_range = [-1, 1, 1/2],
                y_length = 6
        ).add_coordinates()

        label_sin = grafico.get_axis_labels(x_label = "x", y_label = "sin(x)")
        label_cos = grafico.get_axis_labels(x_label = "x", y_label = "cos(x)")
        label_dif = grafico.get_axis_labels(x_label = "x", y_label = "sin(2x)cos(x)")

        seno = grafico.plot(
                lambda x : math.sin(x),
                x_range = [-4*math.pi, 4*math.pi],
                color = GREEN
        )

        cosseno = grafico.plot(
                lambda x : math.cos(x),
                x_range = [-4*math.pi, 4*math.pi],
                color = GREEN
        )

        diferentona = grafico.plot(
                lambda x : math.sin(2*x)*math.cos(x),
                x_range = [-4*math.pi, 4*math.pi],
                color = GREEN
        )
        

#scene constructor
        self.play(DrawBorderThenFill(grafico), Create(label_sin))
        self.play(Create(seno), run_time = 4)
        self.play(Transform(seno, cosseno), Transform(label_sin, label_cos), run_time = 4)
        self.play(Transform(seno, diferentona), Transform(label_sin, label_dif), run_time = 4)
        self.wait()

class nonperiodic(Scene):
    def construct(self): 
        
        dif = ValueTracker(1)

        grafico2 = NumberPlane(
                x_range = [-10, 10, 1],
                x_length = 10,
                y_range = [-5, 5, 1],
                y_length = 6
        ).add_coordinates()
        
        label_func = grafico2.get_axis_labels(x_label = "x", y_label = "f(x)")
        
        func1 = always_redraw( lambda : grafico2.plot(
                lambda x : (dif.get_value()*10)*math.sin(dif.get_value()*x)*math.cos(x) + x,
                x_range = [-10, 10],
                color = GREEN
        ))

        func2 = always_redraw( lambda : grafico2.plot(
                lambda x :  (x**3 + x**2)*0.2,
                x_range = [-10, 10],
                color = GREEN
        ))

#scene constructor
        self.play(DrawBorderThenFill(grafico2), Create(label_func))
        self.play(Create(func1), run_time = 4)
        self.play(dif.animate.set_value(0.01), run_time = 4)
        self.play(dif.animate.set_value(1), Transform(func1, func2), run_time = 4)
        self.wait()

class texliminating(Scene):
    def construct(self):

        text1 = MathTex("U(f + x) = U(f)")
        text2 = MathTex("+ \ U(x)").next_to(text1, RIGHT)

        self.play(Write(VGroup(text1, text2)), run_time = 3)
        self.play(FadeOut(text2), run_time = 2.5)
        self.wait()

class fourier(Scene):
    def construct(self):
        
        #defining domain and vector field

        domain = MathTex("T: \mathbb{C} \\rightarrow \mathbb{C}")
        self.play(Write(domain), run_time = 2)
        self.play(domain.animate.to_edge(UL), run_time = 2)

        right1 = MathTex("= \int_{-\infty}^{\infty}V(t)e^{-i 2 \pi f t}df").move_to(np.array([1,0,0]))
        left1 = MathTex("U(f)").next_to(right1, LEFT)
        left2 = MathTex("T(V(t))").next_to(right1,LEFT)
        self.play(Write(VGroup(left1, right1)), run_time = 3)
        self.wait(2)
        self.play(Transform(left1, left2))
       
        #first property

        scalar_belongs = MathTex("\\alpha \in \mathbb{C}").move_to(np.array([0,2,0]))
        self.play(Write(scalar_belongs), run_time = 2)
        self.play(scalar_belongs.animate.next_to(domain, DOWN), run_time = 2)
        
        scalar1 = MathTex("\\alpha").next_to(left1, LEFT)
        right2 = MathTex("= \\alpha\int_{-\infty}^{\infty}V(t)e^{-i 2 \pi f t}df").move_to(np.array([1,0,0]))
        self.play(Write(scalar1), Transform(right1, right2), run_time = 2)

        right3 = MathTex("\\alpha\int_{-\infty}^{\infty}V(t)e^{-i 2 \pi f t}df =")
        self.play(FadeOut(VGroup(scalar1, left1)), run_time = 1)
        self.play(Transform(right1, right3))
        self.play(right1.animate.move_to(np.array([-1, 0, 0])), run_time = 2)

        right4 = MathTex("\int_{-\infty}^{\infty}\\alpha V(t)e^{-i 2 \pi f t}df").next_to(right1, RIGHT)
        self.play(Write(right4), run_time = 2)

        right5 = MathTex("\int_{-\infty}^{\infty}\\alpha V(t)e^{-i 2 \pi f t}df =")
        self.play(FadeOut(right1))
        self.play(Transform(right4, right5), run_time = 2)
        self.play(right4.animate.move_to(np.array([-1,0,0])), run_time = 2)

        right6 = MathTex("T(\\alpha V(t))").next_to(right4, RIGHT)
        self.play(Write(right6), run_time = 2)
        self.play(FadeOut(right4), run_time = 1)
        self.play(right6.animate.move_to(np.array([1,0,0])), run_time = 2)
        left3 = MathTex("\\alpha T(V(t)) =").next_to(right6, LEFT)
        self.play(Write(left3), run_time = 2)
        self.wait()
        self.play(VGroup(left3, right6).animate.move_to(np.array([-4.5, 2, 0]))) #put property on top left

        #second property

        tv1 = MathTex("T(V(t_1)) = \int_{-\infty}^{\infty}V(t_1)e^{-i 2 \pi f t}df").move_to(np.array([0,1,0]))
        tv2 = MathTex("T(V(t_2)) = \int_{-\infty}^{\infty}V(t_2)e^{-i 2 \pi f t}df").move_to(np.array([0,-1,0]))
        self.play(Write(tv1), Write(tv2))
        
        tv1ptv2 = MathTex("T(V(t_1)) + T(V(t_2)) = \int_{-\infty}^{\infty}V(t_1)e^{-i 2 \pi f t}df + \int_{-\infty}^{\infty}V(t_2)e^{-i 2 \pi f t}df")
        self.play(tv1.animate.move_to(np.array([0,0,0])), FadeOut(tv1), tv2.animate.move_to(np.array([0,0,0])), Transform(tv2, tv1ptv2), run_time = 2)
        self.play(tv2.animate.move_to([0,-2,0]), run_time = 2)
        self.wait(2)

        tv12First = MathTex("T(V(t_1) + V(t_2)) = \int_{-\infty}^{\infty}(V(t_1) + V(t_2))e^{-i 2 \pi f t}df").move_to(np.array([0,1,0]))
        tv12Second = MathTex("T(V(t_1) + V(t_2)) = \int_{-\infty}^{\infty}V(t_1)e^{-i 2 \pi f t}df + \int_{-\infty}^{\infty}V(t_2)e^{-i 2 \pi f t}df")
        self.play(Write(tv12First), run_time = 2)
        self.wait(1)
        self.play(Transform(tv12First, tv12Second), run_time = 2)
        self.wait(1)
        
        property2 = MathTex("T(V(t_1) + V(t_2)) = T(V(t_1)) + T(V(t_2))")
        self.play(tv12First.animate.move_to(np.array([0,0,0])), Transform(tv12First, property2), FadeOut(tv2), run_time = 2)
        self.wait()
        self.play(tv12First.animate.move_to(np.array([-2.3, 1.2, 0]))) #put property on top left

        #third property

        tnullLeft = MathTex("T(0) =").move_to(np.array([-1, -0.5, 0])) 
        tnullRight = MathTex("\int_{-\infty}^{\infty}0\cdot e^{-i 2 \pi f t}df").next_to(tnullLeft, RIGHT)
        zero = MathTex("0").next_to(tnullLeft, RIGHT)
        self.play(Write(VGroup(tnullLeft, tnullRight)), run_time = 2)
        self.play(Transform(tnullRight, zero), run_time = 3)
        self.play(VGroup(tnullRight, tnullLeft).animate.move_to(np.array([0, -2, 0])), run_time = 2)
        self.play(VGroup(left3, right6).animate.move_to(np.array([0, 0, 0])), tv12First.animate.move_to(np.array([0,-1,0])), run_time = 3)
    
        rect = Rectangle(
                width = 10, 
                height = 3
        ).move_to(np.array([0, -1, 0]))

        self.play(Create(rect), run_time = 3)
        self.wait(5)
