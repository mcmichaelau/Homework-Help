import os

import requests

import re

from bs4 import BeautifulSoup

# replace id with id from question and search for values in response
# can use ,"value":" to search for ids
# sometimes answer is labeled ans1, ans2 etc

id_input = '462b3d3a-805c-4291-82e1-1067863ea231'

#try getting rid of user data and then running through until you get the right answer for multiple choice



# idk = os.getenv('5189843_385h-vFSJPVCUCPGDJMEBBAVRFKCINHBMPFRAF-0e0')

cookies = {
    # 'osano_consentmanager_uuid': '1ea87105-1fe8-4a71-a355-e7d069be5234',
    # 'osano_consentmanager': '3yn2j-hggSvTZ9uhwbc4ZLlzxR1vp3dti1bPgHm964nA2XNSI9u3GwHK5mLOITR1ZYPmur3utf44iB-mDQuGLfE1czf_WesPdCY7ufMkRsiFL7Jqd7wBQHVBctG9vfU5o-5lrQgYegpaZNWiP6Q9taBFT8PoDeDa3yN5Ti0CaJggWnpBLG4Q4HIkG9jgMQ9ExWjEJkcaZtzZAkACQqcvjkXQrd02Mtl49ZfrCW9c3xPADYjkvxOW68Huzbn7BdqRuBuBbdSIIejS61M_HA4mc4amuAc7QgiahL2c7Q==',
    # 'AMCV_1B6E34B85282A0AC0A490D44%40AdobeOrg': '-1124106680%7CMCIDTS%7C19295%7CMCMID%7C11344451058427146173862768382192737247%7CMCAAMLH-1667679158%7C7%7CMCAAMB-1667679158%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1667081558s%7CNONE%7CMCAID%7C3186AF7E192EBE55-60001E55ABF7180D%7CvVersion%7C5.2.0',
    # '_gcl_au': '1.1.1105266584.1667074358',
    # '_ga': 'GA1.2.1607436432.1667074359',
    # 'lastRskxRun': '1667074359723',
    # 'rskxRunCookie': '0',
    # 'rCookie': 'g5qm4624vgatn04lhqym3l9ud14fk',
    # 'rxVisitor': '1667398623339224JGKUU9LCPM0DLERMK6P2MAQJQ0OSA',
    # 'dtCookie': 'v_4_srv_5_sn_1ETIL5HA8J9N2GG2SU3DPS94TG9ES8TF_app-3A182c2fa8506055c5_1_ol_0_perc_100000_mul_1_rcs-3Acss_0',
    # 'dtLatC': '7',
    # 'rxvt': '1667406991163|1667405189848',
    # 'dtPC': f"5{idk}",
    # 'dtSa': 'true%7CC%7C-1%7CHW%2011%7C-%7C1667405199988%7C5189843_385%7Chttps%3A%2F%2Feducation.wiley.com%2Fngonboard%2Findex.html%7C%7C%7C%2FStudentDashboard%7C',
    # 'wpng-user-context': 'eyJvYXV0aF9jb25zdW1lcl9rZXkiOiJXUE5HXzk0MmUwZmZlLTA2ZDgtNDYyZS1hYTk3LWRmY2UzODQ4MWU1ZCIsInVzZXJfaWQiOiI1YWZhOGJlOWY2MzlhZTBkMzcyYjdlNzBhMjBhNDYxMWY1YmQ4NjgzIiwiZXh0ZXJuYWxfdXNlcl9pZCI6IjE4MTk5NTkiLCJyb2xlcyI6IkxlYXJuZXIiLCJjdXN0b21fd2lsZXlfcm9sZSI6IlNUVURFTlQiLCJjb250ZXh0X2lkIjoiNjFmNWQ4Yzk5ZTZjZGQ4Y2Y1NWQ2Mjc3NWI3YWRjYjcwNDdlOTM3OSIsImluc3RpdHV0aW9uX2tleSI6ImY0YjlhZDhlLTQ3MDktMTFlOS05MTI5LTEyOWQ1OTM0MzhkYyIsImN1c3RvbV9jYW52YXNfY291cnNlX2lkIjoiNzg2NzkiLCJjdXN0b21fd2lsZXlfY29udGVudF9tb2RlIjpudWxsLCJyZXNvdXJjZV9saW5rX3RpdGxlIjoiSFcgMDYiLCJjdXN0b21fd2lsZXlfdXNlcl9pbnN0X21hcF9pZCI6IjI2ODU2MzciLCJjdXN0b21fd2lsZXlfdXNlcl9wcm9maWxlX2lkIjoiMjY4NTYzNyIsInVzZXJfcHJvZmlsZV9rZXkiOiJmODYxZDVhMy1hM2M0LTQyMWUtODM4Mi1kM2E4ZjI4OGIxYWQiLCJjdXN0b21fd2lsZXlfZXh0ZXJuYWxfdXNlcl9pZCI6bnVsbCwiY3VzdG9tX3dpbGV5X2NvdXJzZV9pZCI6Ijc4OTc1IiwiY3VzdG9tX3dpbGV5X2V4dGVybmFsX2NvdXJzZV9pZCI6bnVsbCwiY3VzdG9tX3dpbGV5X3Byb2R1Y3RfaWQiOiI0MmQwODY1Ny0yZjQwLTQxYWQtOGUxMC1mYWM0MTM4MjY3OWYiLCJsdGlfbGF1bmNoX2lkIjoiNGMyZTc0ZjEtOTE1Ni00MmE3LTg3OTktYjE2MDVkNzM2MTE1IiwibHRpX2xhdW5jaF91cmwiOiJodHRwczovL2Fzc2Vzc21lbnQuZWR1Y2F0aW9uLndpbGV5LmNvbS93cG5nL2FwaS92MS9sdGkvcHJvZHVjdHMvNDJkMDg2NTctMmY0MC00MWFkLThlMTAtZmFjNDEzODI2NzlmL2Fzc2Vzc21lbnRzL2VmYmIwNDNiLTNlODktNDU3OS05MWUyLTJkM2Y1OTg3ZjlkNyIsImF1dG9fZ3JhZGVfc3luYyI6ZmFsc2UsImN1c3RvbV9hc3Nlc3NtZW50X3BsYXllcl9yZWRlc2lnbl9lbmFibGVkIjp0cnVlLCJjdXN0b21fYXNzZXNzbWVudF9kaXNjb3ZlcnlfcmVkZXNpZ25fZW5hYmxlZCI6dHJ1ZSwiY3VzdG9tX2Fzc2Vzc21lbnRfZGFzaGJvYXJkX2VuYWJsZWQiOmZhbHNlLCJyZWRlc2lnbiI6dHJ1ZSwiY3VzdG9tX2FkYXB0aXZpdHlfZ3JhcGgiOm51bGwsImN1c3RvbV93aWxleV9sbXNfdHlwZSI6IldJTEVZX0NBTlZBUyJ9',
    # 'X-NG-JWT-TOKEN': 'eyJraWQiOiJ3cG5nX2FsaWFzIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJhbWNtaWNoYWVsMUBsaWJlcnR5LmVkdSIsImxtc3JvbGUiOiJTVFVERU5UIiwiaXNzIjoiaHR0cHM6XC9cL2VkdWNhdGlvbi53aWxleS5jb21cL3dwbmdcL2FwaVwvdjFcL3Nzb1wvand0IiwibG1zY29udGV4dGlkIjoiNjFmNWQ4Yzk5ZTZjZGQ4Y2Y1NWQ2Mjc3NWI3YWRjYjcwNDdlOTM3OSIsImxtc3Jlc291cmNlbGlua2lkIjoiNDJlZjY4OWY3OTA4YTU5N2M5NDBkYzYzNTEzZTY2MzI3MDlhNTFiMiIsImx0aWNvbnN1bWVya2V5IjoiMmNjYjUwNGUtZDJiYS00YTNiLTkyNzQtMDZmOTZmM2MzOWYyIiwibG1zdXNlcmlkIjoiNWFmYThiZTlmNjM5YWUwZDM3MmI3ZTcwYTIwYTQ2MTFmNWJkODY4MyIsInVzZXJrZXkiOiJmODYxZDVhMy1hM2M0LTQyMWUtODM4Mi1kM2E4ZjI4OGIxYWQiLCJjb3Vyc2V0eXBlIjoiV0lMRVkiLCJhdWQiOiIiLCJsbXNhc3Nlc3NtZW50aWQiOiJlZmJiMDQzYi0zZTg5LTQ1NzktOTFlMi0yZDNmNTk4N2Y5ZDciLCJleHRlcm5hbGNvdXJzZWtleSI6IjllYWYyZWZmLWYyZDAtNGUwOC1hMzUyLWI1MzgwMmRjNzk2YSIsImFsbV9ndWlkIjoiQUxNLWExZjUzNWYxLWE2NjgtNDE5Yi04YWUzLTA2NjgyNTM4NTY0MSIsImxtc2Fzc2Vzc21lbnRkdWVkYXRlIjoiMjAyMi0xMC0wNlQwMzo1OTo1OVoiLCJzZWN0aW9ua2V5IjoiNjk2NDE0MmEtNTY4MC00MjkyLWFmMTEtODdhYTQzN2M4OTM0IiwiY291cnNla2V5IjoiOWVhZjJlZmYtZjJkMC00ZTA4LWEzNTItYjUzODAyZGM3OTZhIiwiZXhwIjoxNjY4MTY5Nzc4LCJpYXQiOjE2NjgxNDgxNzgsIm5ndXNlcnR5cGUiOiJXSUxFWVVTRVIifQ.YB6q1gdD6ekl9SM5UP-0El8kJzt99lICoH3U0vubEV3fS5DuTzROzjPuhgXTHKxVm9IuSmB_CMJhO_Yp70CoC3FjIsYUA-ZviCJ7iKw92livaZPPpT_SpyNxeR0ILYXYaXOpbX6RuucKrs_ZhXf5snQSNjt0M4vpaG3uskEb3Hui5SJxVqUR3nGAVKLNXJRHay-UAUhKTAP1AnmpJNowJxADE4km1X8IOSpem_BtWbGh3sI18Sq1nj4U4E2bgmF-yxHZ5Y412ykNGLuCGBV81vHtCCM61XTysOGTBJXxiQQHHgpmHuTqPCnI1g3iw-3OmmYu5q5SXBUYnjn3AYL0tA',
    'wpng-api-key': 'b0hSZu8N5nPbCdP57bm2hA==',
    # 'AWSALB': 'QCymQtHPEcU79WHATFL2v2OYLdWYsIfIhRbWrTkqORv/7eJH4EhbM5wFI1uXxKuRVgpKXO/wsxTm2o8CZvxBtekZ3YEn0T7qOEauiF2haS29pamsh51Za8N6XjKt7Vm9kqqjwalmC+Aeo2mXI3j2dLRnuw0Wv5iamoIL86WkE8JEZ1Vd0lbNH4skEOCUlw==',
}

# headers = {
#     'authority': 'was.api.wiley.com',
#     'accept': 'application/json, text/javascript, */*; q=0.01',
#     'accept-language': 'en-US,en;q=0.9',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': f"osano_consentmanager_uuid=1ea87105-1fe8-4a71-a355-e7d069be5234; osano_consentmanager=3yn2j-hggSvTZ9uhwbc4ZLlzxR1vp3dti1bPgHm964nA2XNSI9u3GwHK5mLOITR1ZYPmur3utf44iB-mDQuGLfE1czf_WesPdCY7ufMkRsiFL7Jqd7wBQHVBctG9vfU5o-5lrQgYegpaZNWiP6Q9taBFT8PoDeDa3yN5Ti0CaJggWnpBLG4Q4HIkG9jgMQ9ExWjEJkcaZtzZAkACQqcvjkXQrd02Mtl49ZfrCW9c3xPADYjkvxOW68Huzbn7BdqRuBuBbdSIIejS61M_HA4mc4amuAc7QgiahL2c7Q==; AMCV_1B6E34B85282A0AC0A490D44%40AdobeOrg=-1124106680%7CMCIDTS%7C19295%7CMCMID%7C11344451058427146173862768382192737247%7CMCAAMLH-1667679158%7C7%7CMCAAMB-1667679158%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1667081558s%7CNONE%7CMCAID%7C3186AF7E192EBE55-60001E55ABF7180D%7CvVersion%7C5.2.0; _gcl_au=1.1.1105266584.1667074358; _ga=GA1.2.1607436432.1667074359; lastRskxRun=1667074359723; rskxRunCookie=0; rCookie=g5qm4624vgatn04lhqym3l9ud14fk; rxVisitor=1667398623339224JGKUU9LCPM0DLERMK6P2MAQJQ0OSA; dtCookie=v_4_srv_5_sn_1ETIL5HA8J9N2GG2SU3DPS94TG9ES8TF_app-3A182c2fa8506055c5_1_ol_0_perc_100000_mul_1_rcs-3Acss_0; dtLatC=7; rxvt=1667406991163|1667405189848; dtPC=5{5189843_385h-vFSJPVCUCPGDJMEBBAVRFKCINHBMPFRAF-0e0;} dtSa=true%7CC%7C-1%7CHW%2011%7C-%7C1667405199988%7C5189843_385%7Chttps%3A%2F%2Feducation.wiley.com%2Fngonboard%2Findex.html%7C%7C%7C%2FStudentDashboard%7C; wpng-user-context=eyJvYXV0aF9jb25zdW1lcl9rZXkiOiJXUE5HXzk0MmUwZmZlLTA2ZDgtNDYyZS1hYTk3LWRmY2UzODQ4MWU1ZCIsInVzZXJfaWQiOiI1YWZhOGJlOWY2MzlhZTBkMzcyYjdlNzBhMjBhNDYxMWY1YmQ4NjgzIiwiZXh0ZXJuYWxfdXNlcl9pZCI6IjE4MTk5NTkiLCJyb2xlcyI6IkxlYXJuZXIiLCJjdXN0b21fd2lsZXlfcm9sZSI6IlNUVURFTlQiLCJjb250ZXh0X2lkIjoiNjFmNWQ4Yzk5ZTZjZGQ4Y2Y1NWQ2Mjc3NWI3YWRjYjcwNDdlOTM3OSIsImluc3RpdHV0aW9uX2tleSI6ImY0YjlhZDhlLTQ3MDktMTFlOS05MTI5LTEyOWQ1OTM0MzhkYyIsImN1c3RvbV9jYW52YXNfY291cnNlX2lkIjoiNzg2NzkiLCJjdXN0b21fd2lsZXlfY29udGVudF9tb2RlIjpudWxsLCJyZXNvdXJjZV9saW5rX3RpdGxlIjoiSFcgMDYiLCJjdXN0b21fd2lsZXlfdXNlcl9pbnN0X21hcF9pZCI6IjI2ODU2MzciLCJjdXN0b21fd2lsZXlfdXNlcl9wcm9maWxlX2lkIjoiMjY4NTYzNyIsInVzZXJfcHJvZmlsZV9rZXkiOiJmODYxZDVhMy1hM2M0LTQyMWUtODM4Mi1kM2E4ZjI4OGIxYWQiLCJjdXN0b21fd2lsZXlfZXh0ZXJuYWxfdXNlcl9pZCI6bnVsbCwiY3VzdG9tX3dpbGV5X2NvdXJzZV9pZCI6Ijc4OTc1IiwiY3VzdG9tX3dpbGV5X2V4dGVybmFsX2NvdXJzZV9pZCI6bnVsbCwiY3VzdG9tX3dpbGV5X3Byb2R1Y3RfaWQiOiI0MmQwODY1Ny0yZjQwLTQxYWQtOGUxMC1mYWM0MTM4MjY3OWYiLCJsdGlfbGF1bmNoX2lkIjoiNGMyZTc0ZjEtOTE1Ni00MmE3LTg3OTktYjE2MDVkNzM2MTE1IiwibHRpX2xhdW5jaF91cmwiOiJodHRwczovL2Fzc2Vzc21lbnQuZWR1Y2F0aW9uLndpbGV5LmNvbS93cG5nL2FwaS92MS9sdGkvcHJvZHVjdHMvNDJkMDg2NTctMmY0MC00MWFkLThlMTAtZmFjNDEzODI2NzlmL2Fzc2Vzc21lbnRzL2VmYmIwNDNiLTNlODktNDU3OS05MWUyLTJkM2Y1OTg3ZjlkNyIsImF1dG9fZ3JhZGVfc3luYyI6ZmFsc2UsImN1c3RvbV9hc3Nlc3NtZW50X3BsYXllcl9yZWRlc2lnbl9lbmFibGVkIjp0cnVlLCJjdXN0b21fYXNzZXNzbWVudF9kaXNjb3ZlcnlfcmVkZXNpZ25fZW5hYmxlZCI6dHJ1ZSwiY3VzdG9tX2Fzc2Vzc21lbnRfZGFzaGJvYXJkX2VuYWJsZWQiOmZhbHNlLCJyZWRlc2lnbiI6dHJ1ZSwiY3VzdG9tX2FkYXB0aXZpdHlfZ3JhcGgiOm51bGwsImN1c3RvbV93aWxleV9sbXNfdHlwZSI6IldJTEVZX0NBTlZBUyJ9; X-NG-JWT-TOKEN=eyJraWQiOiJ3cG5nX2FsaWFzIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJhbWNtaWNoYWVsMUBsaWJlcnR5LmVkdSIsImxtc3JvbGUiOiJTVFVERU5UIiwiaXNzIjoiaHR0cHM6XC9cL2VkdWNhdGlvbi53aWxleS5jb21cL3dwbmdcL2FwaVwvdjFcL3Nzb1wvand0IiwibG1zY29udGV4dGlkIjoiNjFmNWQ4Yzk5ZTZjZGQ4Y2Y1NWQ2Mjc3NWI3YWRjYjcwNDdlOTM3OSIsImxtc3Jlc291cmNlbGlua2lkIjoiNDJlZjY4OWY3OTA4YTU5N2M5NDBkYzYzNTEzZTY2MzI3MDlhNTFiMiIsImx0aWNvbnN1bWVya2V5IjoiMmNjYjUwNGUtZDJiYS00YTNiLTkyNzQtMDZmOTZmM2MzOWYyIiwibG1zdXNlcmlkIjoiNWFmYThiZTlmNjM5YWUwZDM3MmI3ZTcwYTIwYTQ2MTFmNWJkODY4MyIsInVzZXJrZXkiOiJmODYxZDVhMy1hM2M0LTQyMWUtODM4Mi1kM2E4ZjI4OGIxYWQiLCJjb3Vyc2V0eXBlIjoiV0lMRVkiLCJhdWQiOiIiLCJsbXNhc3Nlc3NtZW50aWQiOiJlZmJiMDQzYi0zZTg5LTQ1NzktOTFlMi0yZDNmNTk4N2Y5ZDciLCJleHRlcm5hbGNvdXJzZWtleSI6IjllYWYyZWZmLWYyZDAtNGUwOC1hMzUyLWI1MzgwMmRjNzk2YSIsImFsbV9ndWlkIjoiQUxNLWExZjUzNWYxLWE2NjgtNDE5Yi04YWUzLTA2NjgyNTM4NTY0MSIsImxtc2Fzc2Vzc21lbnRkdWVkYXRlIjoiMjAyMi0xMC0wNlQwMzo1OTo1OVoiLCJzZWN0aW9ua2V5IjoiNjk2NDE0MmEtNTY4MC00MjkyLWFmMTEtODdhYTQzN2M4OTM0IiwiY291cnNla2V5IjoiOWVhZjJlZmYtZjJkMC00ZTA4LWEzNTItYjUzODAyZGM3OTZhIiwiZXhwIjoxNjY4MTY5Nzc4LCJpYXQiOjE2NjgxNDgxNzgsIm5ndXNlcnR5cGUiOiJXSUxFWVVTRVIifQ.YB6q1gdD6ekl9SM5UP-0El8kJzt99lICoH3U0vubEV3fS5DuTzROzjPuhgXTHKxVm9IuSmB_CMJhO_Yp70CoC3FjIsYUA-ZviCJ7iKw92livaZPPpT_SpyNxeR0ILYXYaXOpbX6RuucKrs_ZhXf5snQSNjt0M4vpaG3uskEb3Hui5SJxVqUR3nGAVKLNXJRHay-UAUhKTAP1AnmpJNowJxADE4km1X8IOSpem_BtWbGh3sI18Sq1nj4U4E2bgmF-yxHZ5Y412ykNGLuCGBV81vHtCCM61XTysOGTBJXxiQQHHgpmHuTqPCnI1g3iw-3OmmYu5q5SXBUYnjn3AYL0tA; wpng-api-key=b0hSZu8N5nPbCdP57bm2hA==; AWSALB=QCymQtHPEcU79WHATFL2v2OYLdWYsIfIhRbWrTkqORv/7eJH4EhbM5wFI1uXxKuRVgpKXO/wsxTm2o8CZvxBtekZ3YEn0T7qOEauiF2haS29pamsh51Za8N6XjKt7Vm9kqqjwalmC+Aeo2mXI3j2dLRnuw0Wv5iamoIL86WkE8JEZ1Vd0lbNH4skEOCUlw==",
#     'origin': 'https://education.wiley.com',
#     'referer': 'https://education.wiley.com/',
#     'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
# }

params = {
    'studentMode': 'true',
}

json_data = {
    'id': id_input,
    # 'masterQuestionId': 'w74c71a1a-ec37-4928-9ff5-8fc50ccce34e',
    # 'masterQuestionVersion': '1',
    # 'context': {
        # 'consumer_key': 'WPNG_942e0ffe-06d8-462e-aa97-dfce38481e5d',
        # 'lis_result_sourcedid': '360415-78679-9823186-1819959-4dc7813f4c34937ffcdabb4be78af34a1dabb5d7',
        # 'master_assessment_id': 'efbb043b-3e89-4579-91e2-2d3f5987f9d7',
        # 'user_id': '5afa8be9f639ae0d372b7e70a20a4611f5bd8683',
        # 'roles': [
        #     'Learner',
        # ],
        # 'product_id': '42d08657-2f40-41ad-8e10-fac41382679f',
        # 'question_card_id': 'fcc05fdf-11d1-413e-a31a-2e38f7b9f44e',
        # 'context_id': '61f5d8c99e6cdd8cf55d62775b7adcb7047e9379',
        # 'assessment_id': '38d0369a8e581bcf1bec78ab08c3baa180eec54cddef64f915c754b0d0b8434f',
        # 'entry_num': 1,
        # 'resource_link_id': '42ef689f7908a597c940dc63513e6632709a51b2',
    # },
    # 'policies': {
        # 'attemptPolicy': {
        #     # 'maxAttempts': 3,
        #     'attemptPenalty': {
        #         'attempt': 3,
        #         'penalty': 0,
        #     },
        # },
        # 'algorithmCalculationMode': 'sameValues',
        # 'assistancePolicies': [
            # {
            #     'assistanceType': 'answer',
            #     'availableSinceAttempt': -1,
            #     'penalty': 0,
            # },
        #     {
        #         'assistanceType': 'reference',
        #         'availableSinceAttempt': 1,
        #         'penalty': 0,
        #     },
        #     {
        #         'assistanceType': 'solution',
        #         'availableSinceAttempt': -1,
        #         'penalty': 0,
        #     },
        # ],
        # 'dueDatePolicy': {
            # 'penalties': [],
            # 'autoSubmit': True,
            # 'rules': {
            #     'lateSubmit': 'no',
            #     'finish': 'byDueDate',
            #     'itemListDetails': 'yes',
            #     'itemAccess': 'yes',
            #     'itemAssistance': 'all',
            # },
        # },
        # 'feedbackPolicy': 'always',
        # 'evaluationPolicy': {
            # 'numericPolicy': {
            #     'defaultTolerance': 2,
            #     'enableQuestionLevelTolerance': True,
            #     'enableQuestionLevelSignificantDigits': False,
            #     'showToleranceInfo': True,
            #     'significantDigitsInfo': 'specific',
            #     'significantDigitsHelp': 'passive',
            # },
        #     'excelEvaluationMode': 'any',
        # },
        # 'hideTitle': False,
        # 'securityPolicy': {
        #     'applicable': False,
        #     'password': '',
        # },
    #     'scoreToKeep': 'best',
    # },
    # 'algorithmResult': {
    #     'id': 'EAT_1474210019582_1_0640614364404777',
    #     'templateVariables': [
            # {
            #     'id': '$ro',
            #     'value': '7800',
            # },
            # {
            #     'id': '$h',
            #     'value': '20',
            # },
            # {
            #     'id': '$k',
            #     'value': '40',
            # },
            # {
            #     'id': '$T_inf',
            #     'value': '325',
            # },
            # {
            #     'id': '$d_sec',
            #     'value': '12',
            # },
            # {
            #     'id': '$T',
            #     'value': '440',
            # },
            # {
            #     'id': '$Ti',
            #     'value': '1100',
            # },
            # {
            #     'id': '$c',
            #     'value': '600',
            # },
        # ],
    # },
    # 'score': None,
    # 'submitAll': False,
    # 'questionCardId': 'fcc05fdf-11d1-413e-a31a-2e38f7b9f44e',
    # 'title': 'Problem 5.007',
    # 'state': 'none',
    # 'numAttempts': 0,
    # 'maxAttempts': 3,
    # 'attemptPenalty': {
    #     'attempt': 3,
    #     'penalty': 0,
    # },
    # 'creationDate': '2022-11-11T06:29:47.909Z',
    # 'timeSpent': 0,
    # 'itemResults': [
    #     {
    #         'id': 'EAT_1474210019582_1_0640614364404777',
    #         'numAttempts': 0,
    #         'maxAttempts': 3,
    #         'attemptPenalty': {
    #             'attempt': 3,
    #             'penalty': 0,
    #             'used': False,
    #         },
    #         'score': None,
    #         'feedback': None,
    #         'modified': False,
    #         'hasSubmit': True,
    #         'available': 'yes',
    #         'visible': False,
    #         'state': 'frozen',
    #         'manuallyGraded': False,
    #         'sessionStatus': 'final',
    #         'datestamp': '2022-11-11T06:29:47.881Z',
    #         'responseVariables': [
    #             {
    #                 'id': 'EAT_1474210019582_1_0640614364404777_te_n_14',
    #                 'baseType': 'number',
    #                 'candidateResponse': {
    #                     'values': [
    #                         '',
    #                     ],
    #                 },
    #                 'score': 0,
    #                 'modified': False,
    #                 'numericPolicies': {
    #                     'tolerance': '2',
    #                     'sig': None,
    #                     'showToleranceInfo': True,
    #                     'significantDigitsInfo': 'none',
    #                     'significantDigitsHelp': 'none',
    #                 },
    #                 'gradableXLMap': None,
    #                 'expandPart': False,
    #             },
    #         ],
    #         'availableAssistances': [
    #             {
    #                 'type': 'answer',
    #                 'penalty': 0,
    #                 'used': False,
    #             },
    #             {
    #                 'type': 'reference',
    #                 'penalty': 0,
    #                 'used': False,
    #             },
    #             {
    #                 'type': 'solution',
    #                 'penalty': 0,
    #                 'used': False,
    #             },
    #         ],
    #     },
    # ],
    # 'eventHistory': [],
}

response = requests.post('https://was.api.wiley.com/was/ga/v1/questions/c/items/E/answer',  cookies=cookies, json=json_data)

print(response.url)
key = '","value":"'

response_string = response.text

print(response_string)

res = [i for i in range(len(response_string)) if response_string.startswith(key, i)]

for index in res:
    value_title_string = response_string[index-15:index]

    dollar_sign_index_list = [i for i in range(len(value_title_string)) if value_title_string.startswith('$', i)]

    for dollar_sign_index in dollar_sign_index_list:
        value_title = value_title_string[dollar_sign_index+1:]

        value = response_string[index+11:index+20]
        value_num = re.sub('[^0-9.-]','', value)
        print(f'{value_title} = {value_num}')