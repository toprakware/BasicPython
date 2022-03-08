#@toprakware

class EqSolver:

    @staticmethod
    def solvelin(eq: str, _dict=False, _tuple=False): #ax + c

        import re
        eq = re.sub(r"\s+", "", str(eq), flags=re.UNICODE).replace("X", "x")

        #finding (a)
        index, a = 0, ""
        try:
            if eq[0] == "+" or eq[0] == "-":
                while eq[index] != "x":
                    a += eq[index]
                    index += 1
                try:
                    int(a)
                except ValueError:
                    a = eq[0] + "1"
            else:
                while eq[index] != "x":
                    a += eq[index]
                    index += 1
                try:
                    int(a)
                    a = "+" + a
                except ValueError:
                    a = "+1"
        #if equation has no "x"
        except IndexError:
            return [eq]

        #finding (c)
        index, c = 1, ""
        while eq[-index] != "+" and eq[-index] != "-":
            if eq[-index] == "x":
                c = "0"
                break
            c += eq[-index]
            index += 1
        c = eq[-index] + c[::-1] if c != "0" else c

        #solving the equation
        if int(a) == 0:
            print("a cannot be zero")
            return [None]

        x = -int(c) / int(a)

        if _dict:
            return [{"x": x}]
        if _tuple:
            return [(x)]
        else:
            print([x])

    @staticmethod
    def solvequad(eq: str, _dict=False, _tuple=False): #ax^2 + bx + c

        import re
        eq = re.sub(r"\s+", "", str(eq), flags=re.UNICODE).replace("X", "x")

        #finding (a)
        index, a, a2 = 0, "", ""
        try:
            if eq[0] == "+" or eq[0] == "-":
                while eq[index] != "x":
                    a += eq[index]
                    index += 1
                a2 = a
                try:
                    int(a)
                except ValueError:
                    a = eq[0] + "1"
            else:
                while eq[index] != "x":
                    a += eq[index]
                    index += 1
                a2 = a
                try:
                    int(a)
                    a = "+" + a
                except ValueError:
                    a = "+1"
        #if equation has no "x"
        except IndexError:
            return [eq]

        #finding (b)
        index = len(a) + 2 if len(a) - len(a2) == 1 else len(a) + 1 if len(a) - len(a2) == 2 else len(a) + 3
        b = ""
        try:
            while eq[index] != "x":
                b += eq[index]
                index += 1
            try:
                int(b)
            except ValueError:
                b += "1"
        except IndexError:
            b = "0"

        #finding (c)
        index, c = 1, ""
        while eq[-index] != "+" and eq[-index] != "-":
            if eq[-index] == "x":
                c = "0"
                break
            c += eq[-index]
            index += 1
        c = eq[-index] + c[::-1] if c != "0" else c

        #solving the equation
        try:
            if int(a) == 0:
                print("a cannot be zero")
                return [None]

            from math import sqrt
            x1 = (-int(b) + sqrt(int(b) ** 2 - 4 * int(a) * int(c))) / (2 * int(a))
            x2 = (-int(b) - sqrt(int(b) ** 2 - 4 * int(a) * int(c))) / (2 * int(a))

        except ValueError:
            print("this equation has no real solutions")
            return [None]

        if _dict:
            return [{"x1": x1, "x2": x2}]
        if _tuple:
            return [(x1, x2)]
        else:
            print([x1, x2])


solver = EqSolver()

eq = "x^2 + 4x + 4" # (x^2 + 4x + 4 = 0)

solver.solvequad(eq)
