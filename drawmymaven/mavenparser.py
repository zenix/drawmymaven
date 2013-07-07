import string
import subprocess
import os
import shlex

from xml.etree import cElementTree


class MavenTreeParser():
    base_path = '/Users/a121865/sw/git/omaelisa/omaelisa/'
    maven_command = 'mvn -o org.apache.maven.plugins:maven-dependency-plugin:2.6:tree -DoutputFile=tree.txt'
    maven_search_text = 'Wrote dependency tree to: '
    search_len = len(maven_search_text)
    root_dependency = ''
    dependency = '+-'
    sibling_node_dependency = '\-'
    dependency_field_separator = ':'
    depth = '|'
    markers = [dependency, sibling_node_dependency, depth]

    def parse_dependency_entries(self):
        entries = self.get_dependency_tree_entries()
        for entry in entries:
            self.handle_maven_dependencies(entry);

    def handle_maven_dependencies(self, path):
        file = open(path, 'r')
        for line in file.readlines():
            """parser_markets = [marker for marker in self.markers if marker in line]"""
            if self.dependency in line:
                print("dependency")

            if self.sibling_node_dependency in line:
                print("Sibling node")

            if self.depth in line:
                print("depth")


    def get_dependency_tree_entries(self):
        current_dir = os.getcwd()
        os.chdir(self.base_path)
        maven_command_split = shlex.split(self.maven_command)
        output, error = subprocess.Popen(maven_command_split, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        os.chdir(current_dir)
        return self.get_dependency_tree_files(output)

    def get_dependency_tree_files(self, output):
        return [self.get_path(line.strip()) for line in output.split('\n') if self.maven_search_text in line]

    def get_path(self, line):
        position = line.index(self.maven_search_text) + self.search_len
        return line[position:len(line)]


class MavenXMLParser():
    base_path = '/Users/a121865/sw/git/omaelisa/omaelisa/'

    def parse(self):
        return cElementTree.parse(self.base_path + 'pom.xml').getroot()

    def get_namespace(self, root):
        return string.split(root.tag[1:], '}', 1)[0]

    def get_element_findall(self, element, name):
        return element.findall('.//{' + self.get_namespace(element) + '}' + name)

    def get_element_find(self, element, name):
        return element.find('./{' + self.get_namespace(element) + '}' + name)

    def handle_dependencies(self, root):
        return [self.handle_dependency(dependency) for dependency in self.get_element_findall(root, 'dependency')]

    def handle_dependency(self, dependency):
        groupId = self.get_element_find(dependency, 'groupId').text
        artifactId = self.get_element_find(dependency, 'artifactId').text
        version = self.get_element_find(dependency, 'version').text
        return groupId, artifactId, version
