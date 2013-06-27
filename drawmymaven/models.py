from neo4django.db import models


class Dependency(models.NodeModel):
    groupId = models.StringProperty()
    artifactId = models.StringProperty()
    version = models.StringProperty()
    dependencies = models.Relationship('self', rel_type='dependencies')

    def __unicode__(self):
        return self.groupId + " " + self.artifactId + " " + self.version