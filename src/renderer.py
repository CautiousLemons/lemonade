
class Renderer:
    def __init__(self):
        print("Instantiating Renderer class")
        pass

    def render(self, config):
        print "nfo('*** Adding docker containers\\n')"
        # TODO
        for container in config["containers"]:
            output = container["id"] + " = net.addDocker("
            for key, value in container.iteritems():
                output += key + "=\"" + value + "\", "
            output += ")"
            print output

