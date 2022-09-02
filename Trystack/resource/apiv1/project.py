from Trystack.controller.apiv1 import ProjectController
from flask_restful import Resource

class ProjectResource :
    def get(self , project_id=None):
        if project_id is None :
            return ProjectController.get_projects()
        else:
            return ProjectController.get_projects(project_id)
    def post(self):
        return ProjectController.create_projects()
    def patch(self,project_id):
        return ProjectController.update_projects(project_id)
    def delete(self, project_id):
        return ProjectController.delete_projects(project_id)