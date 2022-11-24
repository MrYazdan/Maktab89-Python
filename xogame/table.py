class Table:
    table_map = {k: '-' for k in range(1, 10)}

    def table(self):
        return """
|\t{}\t|\t{}\t|\t{}\t|
|\t{}\t|\t{}\t|\t{}\t|
|\t{}\t|\t{}\t|\t{}\t|
        """.format(*self.table_map.values())

    def set(self, cell, sign):
        self.table_map[cell] = sign


# table = Table()
#
# table.set(5, 'x')
# table.set(6, 'o')
#
# print(table.table())
