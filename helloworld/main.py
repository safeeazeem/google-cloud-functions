def hello_world(request): 


    request_args = request.args  # this will return a dictionary

    # Passing values for json
    # We set Silent=True, so that if we dont pass any json to this, we will set this variable to None
    request_json = request.get_json(silent = True)


    '''
       If the dictionary returned is not empty, its going to look for key `name`
    '''
    if request_args and 'name' in request_args and 'lastname' in request_args:
        name = request_args['name']
        lastname = request_args['lastname']
    elif request_json and 'name' in request_json and 'lastname' in request_json: 
        name = request_json['name']
        lastname = request_json['lastname'] 
    else: 
        name = 'World'
        lastname = ''

    return f"Hello {name} {lastname}"

