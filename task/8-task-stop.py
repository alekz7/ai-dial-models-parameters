from task.app.main import run

# TODO:
#  Try `stop` parameter.
#  `stop` (str or list[str]): Tells the AI to stop generating text when it encounters specific words or phrases.
#  Like setting custom "end of response" triggers.
#       Default: None
#  User massage: Explain the key components of a Large Language Model architecture

run(
    deployment_name='gemini-2.5-pro',
    print_request=False, # Switch to False if you do not want to see the request in console
    print_only_content=True, # Switch to True if you want to see only content from response
    stop=["**Embedding Layer**", "**Transformer Blocks**", "**Training**", "language", "Language"]
)

# With `stop` parameter we can stop content generation. It can be used for some policies/guardrails. For instance,
# we are the company with the name `Pear` and we don't want that anybody will see in results that our competitor `Apple`
# is cool (stop: ["Apple is cool", "Apple top"]).
# The `finish_reason` will be set as `stop`. So, the users won't know what is the real reason why LLM has stopped generation.