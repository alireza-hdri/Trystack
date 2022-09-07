from Trystack.controller.apiv1 import ProjectController
from flask_restful import Resource

class ProjectResource :
    def get(self , project_id=None):
        """
        GET / project --> Project List.
        GET /project/<Project_id> --> Not Allowed.
        """
        if project_id is None :
            return ProjectController.get_projects()
        else:
            return ProjectController.get_projects(project_id)
    def post(self):
        """
        POST /projecta --> Create a new project.
        POST /project/<Project_id> --> Not Allowed.
        """
        return ProjectController.create_projects()
    def patch(self,project_id):
        """
        PATCH /projects --> Not Allowed.
        PATCH /project/<Project_id> --> Update projects.
        """
        return ProjectController.update_projects(project_id)
    def delete(self, project_id):
        """
        DELETE /projects --> Not Allowed.
        DELETE /project/<Project_id> --> Delete projects.
        """
        return ProjectController.delete_projects(project_id)