from manimlib import *


# https://3b1b.github.io/manim/
# manimgl main.py IntegrationByParts
# manimgl main.py IntegrationByParts -w --prerun -r="2560x1440" --video_dir="./export" --file_name="name" --uhd


class IntegrationByParts(Scene):
    def construct(self):

        # self.embed(True)

        # Step 1: Product Rule
        self.write_product_rule_1()
        # Step 2: Integration
        self.integrate_both_sides_2()
        # Step 3: U-substitution
        self.substitute_u_3()
        # Step 4: V-substitution
        self.substitute_v_4()
        # Step 5: Rearrenging
        self.rearrenge_eqation_5()

        # Adjust zoom speed
        self.play(self.camera.frame.animate.scale(3).move_to(self.eq4), run_time=2)

    def write_product_rule_1(self):
        # Point 1
        self.point_1 = Tex("1)")
        self.point_1.to_corner(LEFT + UP)
        self.play(Write(self.point_1))

        # Equation
        self.eq1 = Tex(r"\frac{d}{dx} \left[ f(x) g(x) \right] = f(x) g'(x) + f'(x) g(x)")
        self.eq1.next_to(self.point_1, RIGHT, DEFAULT_BUFF_RATIO)
        self.eq1.set_color(GREEN_C)
        self.eq1.set_color_by_tex("=", WHITE)
        self.eq1.set_color_by_tex("+", WHITE)
        self.play(Write(self.eq1))
        self.wait()

    def integrate_both_sides_2(self):
        # Point 2
        self.point_2 = Tex("2)")
        self.point_2.next_to(self.eq1, DOWN, LARGE_BUFF).to_edge()
        self.play(Write(self.point_2))

        # Equation 2
        self.eq2 = Tex(r"\int \left[ \frac{d}{dx} \left[f(x)g(x)\right] \right]dx = \int \left[ f(x)g'(x) + f'(x)g(x) \right]dx")
        self.eq2.next_to(self.point_2, RIGHT, buff=DEFAULT_BUFF_RATIO)
        self.play(Write(self.eq2))
        self.wait()
        self.play(
            FadeToColor(self.eq2.get_part_by_tex(r"\frac{d}{dx} \left[f(x)g(x)\right]"), GREEN_C),
            FadeToColor(self.eq2.get_part_by_tex(r"f(x)g'(x) + f'(x)g(x)"), GREEN_C),
        )
        self.wait()

        # Fundamental theorem of calculus (highlight cancel-terms)
        # part 1
        self.integral_part1 = self.eq2.get_parts_by_tex(r"\int \left[")[0]
        self.integral_part2 = self.eq2.get_parts_by_tex(r"\right]dx")[0]
        self.play(
            FadeToColor(self.integral_part1, RED),
            FadeToColor(self.integral_part2, RED),
        )
        self.wait()

        # part 2
        serivative_part1 = self.eq2.get_part_by_tex(r"\frac{d}{dx} \left[")
        serivative_part2 = self.eq2.get_parts_by_tex(r"\right]")[0]
        self.play(
            FadeToColor(serivative_part1, RED),
            FadeToColor(serivative_part2, RED),
        )
        self.wait()

        # Distribute integral
        integral = self.eq2.get_parts_by_tex(r"\int")[-1]
        quantity_part_1 = self.eq2.get_part_by_tex("f(x)g'(x)")
        quantity_part_2 = self.eq2.get_part_by_tex("f'(x)g(x)")
        integral_arrow_1 = Arrow(integral.get_top(), quantity_part_1.get_top(), SMALL_BUFF, path_arc=-50 * DEGREES).set_opacity(0.5)
        integral_arrow_2 = Arrow(integral.get_top(), quantity_part_2.get_top(), SMALL_BUFF, path_arc=-50 * DEGREES).set_opacity(0.5)
        self.play(GrowArrow(integral_arrow_1))
        self.play(GrowArrow(integral_arrow_2))
        self.wait()

        # Equation 3 (rewriting simplified equation)
        self.eq3 = Tex(r"f(x)g(x) = \int \left[ f(x)g'(x) \right]dx + \int \left[ f'(x)g(x) \right]dx")
        self.eq3.next_to(self.eq2, DOWN, buff=SMALL_BUFF)
        self.eq3.align_to(self.eq2.get_part_by_tex(r"\int"), LEFT)
        self.eq3.set_color_by_tex_to_color_map(
            {
                "f(x)g(x)": GREEN_C,
                "f(x)g'(x)": GREEN_C,
                "f'(x)g(x)": GREEN_C,
            }
        )
        self.play(TransformFromCopy(self.eq2.copy(), self.eq3), **{"run_time": 1})
        self.wait()

    def substitute_u_3(self):
        # Point 3
        self.point_3 = Tex("3)")
        self.point_3.next_to(self.eq3, DOWN, LARGE_BUFF).to_edge()
        self.play(Write(self.point_3))

        # U-substitution
        u = Tex(r"let \,u = f(x)")
        u.next_to(self.point_3, RIGHT, buff=DEFAULT_BUFF_RATIO)
        self.play(Write(u))
        self.wait()

        du = Tex(r"du = f'(x)dx")
        du.next_to(u, RIGHT, buff=DEFAULT_BUFF_RATIO)
        self.play(Write(du))
        self.wait(2)

        # Copying eq3
        self.eq3_copy = self.eq3.copy()
        self.eq3_copy.next_to(u, DOWN, DEFAULT_BUFF_RATIO)
        self.eq3_copy.align_to(u.get_part_by_tex("let"), LEFT)
        self.play(TransformFromCopy(self.eq3.copy(), self.eq3_copy), **{"run_time": 1})
        self.wait()

        # U-highlighting
        u_letter = u.get_part_by_tex("u")
        self.play(FadeToColor(u_letter, BLUE_D))

        f_x_u = u.get_part_by_tex("f(x)")
        self.play(FadeToColor(f_x_u, BLUE_D))

        f_x_eq3 = self.eq3_copy.get_parts_by_tex(r"f(x)")
        u_arrows = VGroup(*[Arrow(f_x_u.get_center(), fx.get_center(), DEFAULT_BUFF_RATIO).set_color(BLUE_D).set_opacity(0.5) for fx in f_x_eq3])
        self.play(LaggedStartMap(GrowArrow, u_arrows))
        self.play(FadeToColor(f_x_eq3, BLUE_D))

        # Du-highlighting
        du_letters = du.get_part_by_tex("du")
        self.play(FadeToColor(du_letters, BLUE_D))

        f_prime_x_dx_du = du.get_part_by_tex("f'(x)dx")
        self.play(FadeToColor(f_prime_x_dx_du, BLUE_D))

        f_prime_eq3_copy = self.eq3_copy.get_part_by_tex("f'(x)")
        last_dx_eq3_copy = self.eq3_copy.get_parts_by_tex("dx")[-1]
        du_arrows = VGroup(
            Arrow(du.get_part_by_tex("f'(x)").get_bottom(), f_prime_eq3_copy.get_top(), 0.25).set_color(BLUE_D).set_opacity(0.5),
            Arrow(du.get_part_by_tex("dx").get_bottom(), last_dx_eq3_copy.get_top(), 0.25).set_color(BLUE_D).set_opacity(0.5),
        )
        self.play(LaggedStartMap(GrowArrow, du_arrows))
        self.play(
            FadeToColor(f_prime_eq3_copy, BLUE_D),
            FadeToColor(last_dx_eq3_copy, BLUE_D),
        )
        self.wait()

        # Equation 4
        self.eq4 = Tex(r"u*g(x) = \int u*g'(x)dx + \int g(x)*du")
        self.eq4.next_to(self.eq3_copy, DOWN, DEFAULT_BUFF_RATIO)
        self.eq4.align_to(self.eq3_copy.get_part_by_tex("f(x)"), LEFT)
        self.eq4.set_color_by_tex_to_color_map(
            {
                "u": BLUE_D,
                "du": BLUE_D,
                "g(x)": GREEN_C,
                "g'(x)": GREEN_C,
            }
        )

        # Shift the camera down by 2 units over 4 seconds
        camera_shift = ApplyMethod(self.camera.frame.shift, 5 * DOWN, run_time=3)

        self.play(
            camera_shift,
            TransformFromCopy(self.eq3_copy.copy(), self.eq4, run_time=1.5),
        )

        self.wait()

    def substitute_v_4(self):
        # Point 4
        self.point_4 = Tex("4)")
        self.point_4.next_to(self.eq4, DOWN, LARGE_BUFF).to_edge()
        self.play(Write(self.point_4))

        # V-substitution
        v = Tex(r"let \,v = g(x)")
        v.next_to(self.point_4, RIGHT, buff=DEFAULT_BUFF_RATIO)
        self.play(Write(v))
        self.wait()

        dv = Tex(r"dv = g'(x)dx")
        dv.next_to(v, RIGHT, buff=DEFAULT_BUFF_RATIO)
        self.play(Write(dv))
        self.wait()

        # Substituting
        self.eq4_copy = self.eq4.copy()
        self.eq4_copy.next_to(v, DOWN, DEFAULT_BUFF_RATIO).to_edge()
        self.eq4_copy.align_to(v.get_part_by_tex("let"), LEFT)
        self.play(TransformFromCopy(self.eq4.copy(), self.eq4_copy), **{"run_time": 1})
        self.wait()

        # V-Highlightning
        v_letter = v.get_part_by_tex("v")
        self.play(FadeToColor(v_letter, TEAL_C))

        g_x_v = v.get_part_by_tex("g(x)")
        self.play(FadeToColor(g_x_v, TEAL_C))

        g_x_eq4_copy = self.eq4_copy.get_parts_by_tex(r"g(x)")
        v_arrows = VGroup(*[Arrow(g_x_v.get_bottom(), fx.get_top(), 0.2).set_color(TEAL_D).set_opacity(0.5) for fx in g_x_eq4_copy])
        self.play(LaggedStartMap(GrowArrow, v_arrows))
        self.play(FadeToColor(g_x_eq4_copy, TEAL_D))

        # DV-Highlightning
        dv_letters = dv.get_part_by_tex("dv")
        self.play(FadeToColor(dv_letters, TEAL_C))

        g_prime_x_dx_dv = dv.get_part_by_tex("g'(x)dx")
        self.play(FadeToColor(g_prime_x_dx_dv, TEAL_C))

        g_prime_eq4_copy = self.eq4_copy.get_part_by_tex("g'(x)")
        last_dx_eq4_copy = self.eq4_copy.get_part_by_tex("dx")
        dv_arrows = VGroup(
            Arrow(dv.get_part_by_tex("g'(x)").get_bottom(), g_prime_eq4_copy.get_top(), 0.1).set_color(TEAL_C).set_opacity(0.5),
            Arrow(dv.get_part_by_tex("dx").get_bottom(), last_dx_eq4_copy.get_top(), 0.1).set_color(TEAL_C).set_opacity(0.5),
        )
        self.play(LaggedStartMap(GrowArrow, dv_arrows))
        self.play(
            FadeToColor(g_prime_eq4_copy, TEAL_C),
            FadeToColor(last_dx_eq4_copy, TEAL_C),
        )
        self.wait()

        # Equation 5
        self.eq5 = Tex(r"u*v = \int u*dv + \int v*du")
        self.eq5.next_to(self.eq4_copy, DOWN, DEFAULT_BUFF_RATIO)
        self.eq5.align_to(self.eq4_copy.get_part_by_tex("u"), LEFT)
        self.eq5.set_color_by_tex_to_color_map(
            {
                "u": BLUE_D,
                "du": BLUE_D,
                "v": TEAL_C,
                "dv": TEAL_C,
            }
        )
        # Shift the camera down by 2 units over 4 seconds
        camera_shift = ApplyMethod(self.camera.frame.shift, 4.5 * DOWN, run_time=3)
        self.play(
            camera_shift,
            TransformFromCopy(self.eq4_copy.copy(), self.eq5, run_time=1.5),
        )
        self.wait()

    def rearrenge_eqation_5(self):
        # Point 1
        self.point_5 = Tex("5)")
        self.point_5.next_to(self.eq5, DOWN, LARGE_BUFF).to_edge()
        self.play(Write(self.point_5))

        # Equation
        self.eq5_copy = self.eq5.copy()
        self.eq5_copy.next_to(self.point_5, RIGHT, DEFAULT_BUFF_RATIO)
        self.play(Write(self.eq5_copy))
        self.wait()

        self.rearrenging_factor = Tex(r"\big| - \int v*du")
        self.rearrenging_factor.next_to(self.eq5_copy, RIGHT, DEFAULT_BUFF_RATIO)
        self.play(Write(self.rearrenging_factor))
        self.wait()

        self.eq6 = Tex(r"u*v - \int v*du = \int u*dv + \int v*du - \int v*du")
        self.eq6.set_color_by_tex_to_color_map(
            {
                "u": BLUE_D,
                "du": BLUE_D,
                "v": TEAL_C,
                "dv": TEAL_C,
            }
        )

        du_part = self.eq6.get_parts_by_tex("du")
        du_part[0].set_color(WHITE)
        du_part[-1].set_color(WHITE)

        v_part = self.eq6.get_parts_by_tex("v")
        v_part[1].set_color(WHITE)
        v_part[-1].set_color(WHITE)

        self.eq6.next_to(self.point_5, RIGHT, DEFAULT_BUFF_RATIO)
        self.play(FadeOut(self.rearrenging_factor))
        self.play(TransformMatchingTex(self.eq5_copy, self.eq6))

        # Highlighting cancel terms
        self.play(FadeToColor(self.eq6.get_part_by_tex(r"+ \int v*du"), RED), FadeToColor(self.eq6.get_parts_by_tex(r"- \int v*du")[-1], RED))
        self.wait()

        # Equation 7
        self.eq7 = Tex(r"u*v - \int v*du = \int u*dv")
        self.eq7.set_color_by_tex_to_color_map(
            {
                "u": BLUE_D,
                "du": BLUE_D,
                "v": TEAL_C,
                "dv": TEAL_C,
            }
        )
        self.eq7.next_to(self.eq6, DOWN, DEFAULT_BUFF_RATIO)
        self.eq7.align_to(self.eq6, LEFT)

        # Shift the camera down by 2 units over 4 seconds
        camera_shift = ApplyMethod(self.camera.frame.shift, 3.5 * DOWN, run_time=3)

        self.play(
            camera_shift,
            TransformFromCopy(self.eq6.copy(), self.eq7, run_time=1.5),
        )
        self.wait()

        self.eq7_no_mult = Tex(r"uv - \int vdu = \int udv")
        self.eq7_no_mult.set_color_by_tex_to_color_map(
            {
                "u": BLUE_D,
                "du": BLUE_D,
                "v": TEAL_C,
                "dv": TEAL_C,
            }
        )
        self.eq7_no_mult.next_to(self.eq7, RIGHT, DEFAULT_BUFF_RATIO)
        self.eq7_no_mult.align_to(self.eq6, LEFT)
        self.play(TransformMatchingTex(self.eq7, self.eq7_no_mult))
        self.wait()

        self.eq8 = Tex(r"\int udv = uv - \int vdu")
        self.eq8.set_color_by_tex_to_color_map(
            {
                "u": BLUE_D,
                "du": BLUE_D,
                "v": TEAL_C,
                "dv": TEAL_C,
            }
        )
        self.play(self.eq7_no_mult.animate.shift(1.5 * DOWN + 2.5 * RIGHT), run_time=2)
        self.eq8.next_to(self.eq7_no_mult, RIGHT, DEFAULT_BUFF_RATIO)
        self.eq8.align_to(self.eq7_no_mult, LEFT)
        self.play(TransformMatchingTex(self.eq7_no_mult, self.eq8, path_arc=180 * DEGREES), **{"run_time": 4})

        self.rect = SurroundingRectangle(self.eq8, DEFAULT_BUFF_RATIO, GREEN_C)
        self.play(Write(self.rect), **{"run_time": 3})

