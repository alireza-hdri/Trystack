from crypt import methods
import imp
from Trystack.Trystack import apiv1 as api
from .project import ProjectResource
api.add_resource (
    ProjectResource ,
    "/project" ,
    methods=["GET" , "POST"],
    endpoint="projects"
)