from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

run(
    deployment_name='gemini-2.5-pro',
    #print_request=False, # Switch to False if you do not want to see the request in console
    #print_only_content=True, # Switch to True if you want to see only content from response
    temperature=2.0,
)