class ProjectParameters:
    def __init__(self):
        self.default_student_code = 'searchAgents.py, search.py'
        self.test_classes = 'searchTestClasses.py'
        self.project_name = 'Project 1: Search'
        self.bonus_picture = False
if __name__ == "__main__":
    project_params = ProjectParameters()
    print("Default Student Code Files:", project_params.default_student_code)
    print("Test Classes File:", project_params.test_classes)
    print("Project Name:", project_params.project_name)
    print("Bonus Picture:", project_params.bonus_picture)