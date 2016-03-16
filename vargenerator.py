class Generator:
    def __init__(self):
        self.countstack = 0
        self.countdata = 0
        self.count = 0

    def gen_stack_var(self):
        self.countstack += 1
        return "s" + str(self.countstack)

    def gen_data_var(self):
        self.countdata += 1
        return "Id_" + str(self.countdata)

    def gen_data_var(self, position):
        self.countdata = max(position + 1, self.countdata)
        return "Id_" + str(position)

    def gen_data_size(self):
        return "Id_size"

    def gen_mem_var(self, address):
        return "mem_" + str(address)

    def get_arbitrary_var(self):
        self.count += 1
        return "some_var_" + str(self.count)