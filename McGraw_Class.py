import requests


class McGrawAnswer:
    def __init__(self, url):
        self.key = 'question-group/'
        self.url = url

    def get_answers(self):

        bopr_key_start = [i for i in range(len(self.url)) if self.url.startswith(self.key, i)][0]

        print(bopr_key_start)

        bopr_key = self.url[bopr_key_start + 15:]

        print(bopr_key)

        bopr_response = requests.get(f'https://ezto.mheducation.com/api/caa/item/render/{bopr_key}')

        print(bopr_response.json())

        boprid = bopr_response.json()['items'][0]['boprid']

        response = requests.get(f'https://ezto.mheducation.com/api/caa/item/render/{boprid}')

        num_answers = response.json()['items'][0]['qinfo']['answers']

        num_answers_list = []
        i = 1
        for answer in num_answers:
            try:
                num_answers_list.append(f"Numeric answer {i}: {num_answers[answer]['correctAnswer']}")
                i = i + 1
            except:
                pass

        return response


