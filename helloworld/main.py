def hello_world(request): 


    request_args = request.args  # this will return a dictionary


    '''
       If the dictionary returned is not empty, its going to look for key `name`
    '''
    if request_args and 'name' in request_args:
        name = request_args['name']
    else: 
        name = 'World'

    return f"Hello {name}"

