from flask_restful import Resource

class ProjectResource :
    def get(self):
        return{
            "hello" : "world"
        }