# import ast

# node = ast.Expression(ast.BinOp(ast.Str("xy"), ast.Mult(), ast.Num(3)))

# fixed = ast.fix_missing_locations(node)

# codeobj = compile(fixed, "<string>", "eval")

# print(eval(codeobj))


import ast
import astpretty

# source = "6 + 8"
# node = ast.parse(source, mode="eval")

# print(eval(compile(node, "<string>", mode="eval")))

# print(ast.dump(node))

# print(astpretty.pprint(node))


import ast


class MyVisitor(ast.NodeVisitor):
    def visit_Str(self, node):
        print('Found string "%s"' % node.s)
        self.generic_visit(node)


class MyTransformer(ast.NodeTransformer):
    def visit_Str(self, node):
        return ast.Str("str: " + node.s)


# source = 'x=10;y=20;z=eval("x + y", {"x": x, "y": y});a=eval("10+z")'

source = """\n
x=10\n
y=20\n
z=eval("x + y", {"x": x, "y": y})\n
a=eval("10+z")\n
"""

node = ast.parse(source)

MyTransformer().visit(node)
MyVisitor().visit(node)

# astpretty.pprint(node)
print(ast.dump(node, indent=4))


print(ast.dump(ast.parse(source, mode="eval"), indent=4))
