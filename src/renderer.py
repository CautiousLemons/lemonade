
class Renderer:
    def __init__(self):
        pass

    def render(self, config):
        print "info('*** Adding docker containers\\n')"
        # TODO
        for container in config["containers"]:
            output = container["id"] + " = net.addDocker("
            for key, value in container.iteritems():
                output += key + "=\"" + value + "\", "
            output += ")"
            print output

