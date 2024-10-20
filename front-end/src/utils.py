import json
import os
import urllib.request


def get_response(prompt):

    data = {
        "messages": [
            {"role": "system", "content": "You are helpful assistant."},
            {"role": "assistant", "content": prompt},
        ],
        "model": "mistral",
        # "max_tokens": 500,
        # "temperature": 0.8,
        # "top_p": 0.1,
        # "best_of": 1,
        # "presence_penalty": 0,
        # "use_beam_search": False,
        # "ignore_eos": False,
        # "skip_special_tokens": False,
        # "logprobs": False,
        # "top_logprobs": None,
    }

    body = str.encode(json.dumps(data))

    url = "http://localhost:11434/api/chat"
    # Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
    # api_key = os.getenv("lemma_apikey")
    # if not api_key:
    #     raise Exception("A key should be provided to invoke the endpoint")

    headers = {
        "Content-Type": "application/json",
        # "Authorization": ("Bearer " + api_key),
    }

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", "ignore"))

    final_string = ""
    for text in result.decode("utf-8").split("done_reason")[0].split("\n"):
        try:
            final_string += json.loads(text)["message"]["content"]
        except:
            pass

    return final_string
