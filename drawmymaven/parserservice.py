from drawmymaven.mavenparser import MavenXMLParser
from drawmymaven.models import Dependency

class GraphModelFactory():
    def create_models(self):
        dependencies = self.get_dependencies()
        for dependency in dependencies:
            dependency_model = Dependency.objects.create(groupId=dependency[0], artifactId=dependency[1], version=dependency[2])
            dependency_model.save()

    def get_dependencies(self):
        parser = MavenParser()
        return parser.handle_dependencies(parser.parse())