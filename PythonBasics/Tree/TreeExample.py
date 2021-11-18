class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, choose):
        if choose == 'both':
            value = self.name + "(" + self.designation + ")"
        elif choose == 'name':
            value = self.name
        else:
            value = self.designation

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(choose)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_management_tree():
    ceo = TreeNode("Nilpul", "CEO")
    cto = TreeNode("Chinmay", "CTO")
    inf_head = TreeNode("Vishwa", "Infrastructure Head")
    cld_mgr = TreeNode("Dhaval", "Cloud Manager")
    app_mgr = TreeNode("Abhijit", "App Manager")
    appl_head = TreeNode("Aamir", "Application Head")
    hr_head = TreeNode("Gels", "HR Head")
    rct_mgr = TreeNode("Peter", "Recruitment Manager")
    pcy_mgr = TreeNode("Waqas", "Policy Manager")

    ceo.add_child(cto)
    ceo.add_child(hr_head)
    cto.add_child(inf_head)
    cto.add_child(appl_head)
    hr_head.add_child(rct_mgr)
    hr_head.add_child(pcy_mgr)
    inf_head.add_child(cld_mgr)
    inf_head.add_child(app_mgr)

    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    root_node.print_tree("designation")  # prints only designation hierarchy
    root_node.print_tree("both")  # prints both (name and designation) hierarchy
