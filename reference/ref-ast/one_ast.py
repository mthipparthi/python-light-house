import ast


class IntegerWrapper(ast.NodeTransformer):
    """Wraps all integers in a call to Integer()"""

    def visit_Num(self, node):
        if isinstance(node.n, int):
            return ast.Call(
                func=ast.Name(id="Integer", ctx=ast.Load()), args=[node], keywords=[]
            )
        return node


# tree = ast.parse("print('hello world')")

# print(tree)
# breakpoint()

tree = ast.parse("1/3")
tree = IntegerWrapper().visit(tree)
# Add lineno & col_offset to the nodes we created
ast.fix_missing_locations(tree)
breakpoint()


source = "items = [1,2,3,45]; field1 = sum(items); field2 = sum(items)*2"
tree = ast.parse(source)





