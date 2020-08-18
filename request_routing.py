# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, route_handler, not_found_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = route_handler
        self.not_found_handler = not_found_handler

    def insert(self, route_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for route in route_list:
            current_node = current_node.insert(route)
            if not current_node.handler:
                current_node.handler = self.not_found_handler

        current_node.handler = handler
                

    def find(self, route_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for route in route_list:
            if route in current_node.children:
                current_node = current_node.children[route]
            else:
                return self.not_found_handler
        
        return current_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, route):
        if route not in self.children:
            self.children[route] = RouteTrieNode()

        return self.children[route]
    

    # The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler, not_found_handler)


    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)

        self.route_trie.insert(path_list, handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)

        return self.route_trie.find(path_list)


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_list = path.split('/')

        if path == '/':
            path_list = path_list[1:]
        if path[-1] == '/':
            path_list = path_list[:-1]

        return path_list

if __name__ == "__main__": 
    # Here are some test cases and expected outputs you can use to test your implementation
    print('Vanilla Test Cases')
    # create the router and add a route
    router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about")) # should print 'about handler'
    print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

    print('\n--Tests--')
    print('Router 1')
    router1 = Router('root','404 page not found')
    router1.add_handler('/1/2/3/4/5/6','6th handler')
    router1.add_handler('/a/b/c/d','d handler')
    router1.add_handler('/a/b','b handler')

    router2 = Router('root', '404 page not found')


    print('Value: {}'.format(router1.lookup('/1/2/3/4/5/6/')))
    print('Expected: {}\n'.format('6th hanlder'))

    print('Value: {}'.format(router1.lookup('/a/b/c/d')))
    print('Expected: {}\n'.format('d hanlder'))

    print('Value: {}'.format(router1.lookup('/a/b/')))
    print('Expected: {}\n'.format('b hanlder'))

    print('Value: {}'.format(router1.lookup('/1/2')))
    print('Expected: {}\n'.format('404 page not found'))

    print('Router 2\n')

    print('Value: {}'.format(router2.lookup('/1/2')))
    print('Expected: {}\n'.format('404 page not found'))

    print('Value: {}'.format(router2.lookup('/')))
    print('Expected: {}'.format('root'))


