import requests
import re
import os


class Answer:
    def __init__(self, code):
        self.code = code
        self.idk = os.getenv('387655306_829h-vRGOTCNCMHGHFCCFRMHFCQEUHMRNHPUKF-0e0')
        self.cookies = {
            'osano_consentmanager_uuid': '1ea87105-1fe8-4a71-a355-e7d069be5234',
            'osano_consentmanager': '3yn2j-hggSvTZ9uhwbc4ZLlzxR1vp3dti1bPgHm964nA2XNSI9u3GwHK5mLOITR1ZYPmur3utf44iB-mDQuGLfE1czf_WesPdCY7ufMkRsiFL7Jqd7wBQHVBctG9vfU5o-5lrQgYegpaZNWiP6Q9taBFT8PoDeDa3yN5Ti0CaJggWnpBLG4Q4HIkG9jgMQ9ExWjEJkcaZtzZAkACQqcvjkXQrd02Mtl49ZfrCW9c3xPADYjkvxOW68Huzbn7BdqRuBuBbdSIIejS61M_HA4mc4amuAc7QgiahL2c7Q==',
            'AMCV_1B6E34B85282A0AC0A490D44%40AdobeOrg': '-1124106680%7CMCIDTS%7C19295%7CMCMID%7C11344451058427146173862768382192737247%7CMCAAMLH-1667679158%7C7%7CMCAAMB-1667679158%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1667081558s%7CNONE%7CMCAID%7C3186AF7E192EBE55-60001E55ABF7180D%7CvVersion%7C5.2.0',
            '_gcl_au': '1.1.1105266584.1667074358',
            '_ga': 'GA1.2.1607436432.1667074359',
            'lastRskxRun': '1667074359723',
            'rskxRunCookie': '0',
            'rCookie': 'g5qm4624vgatn04lhqym3l9ud14fk',
            'rxVisitor': '1667695850299E93DGQSGVH8GGEK2SEBRAGTRFM5KH4B8',
            'dtCookie': 'v_4_srv_2_sn_2C993841EE47B886EE6F53CC9D179EF7_app-3A182c2fa8506055c5_1_ol_0_perc_100000_mul_1_rcs-3Acss_0',
            'dtLatC': '56',
            'rxvt': '1667789458519|1667787655311',
            'dtSa': 'false%7CC%7C15%7CENGR%20360-001%20Heat%20Transfer%20F021%7Cfetch%7C1667787658512%7C387655306_829%7Chttps%3A%2F%2Feducation.wiley.com%2Fngonboard%2Findex.html%7C%7C%7C%2FStudentDashboard%7C',
            'dtPC': f'2{self.idk}',
            'wpng-user-context': 'eyJvYXV0aF9jb25zdW1lcl9rZXkiOiJXUE5HXzk0MmUwZmZlLTA2ZDgtNDYyZS1hYTk3LWRmY2UzODQ4MWU1ZCIsInVzZXJfaWQiOiI1YWZhOGJlOWY2MzlhZTBkMzcyYjdlNzBhMjBhNDYxMWY1YmQ4NjgzIiwiZXh0ZXJuYWxfdXNlcl9pZCI6IjE4MTk5NTkiLCJyb2xlcyI6IkxlYXJuZXIiLCJjdXN0b21fd2lsZXlfcm9sZSI6IlNUVURFTlQiLCJjb250ZXh0X2lkIjoiNjFmNWQ4Yzk5ZTZjZGQ4Y2Y1NWQ2Mjc3NWI3YWRjYjcwNDdlOTM3OSIsImluc3RpdHV0aW9uX2tleSI6ImY0YjlhZDhlLTQ3MDktMTFlOS05MTI5LTEyOWQ1OTM0MzhkYyIsImN1c3RvbV9jYW52YXNfY291cnNlX2lkIjoiNzg2NzkiLCJjdXN0b21fd2lsZXlfY29udGVudF9tb2RlIjpudWxsLCJyZXNvdXJjZV9saW5rX3RpdGxlIjoiSFcgMTIiLCJjdXN0b21fd2lsZXlfdXNlcl9pbnN0X21hcF9pZCI6IjI2ODU2MzciLCJjdXN0b21fd2lsZXlfdXNlcl9wcm9maWxlX2lkIjoiMjY4NTYzNyIsInVzZXJfcHJvZmlsZV9rZXkiOiJmODYxZDVhMy1hM2M0LTQyMWUtODM4Mi1kM2E4ZjI4OGIxYWQiLCJjdXN0b21fd2lsZXlfZXh0ZXJuYWxfdXNlcl9pZCI6bnVsbCwiY3VzdG9tX3dpbGV5X2NvdXJzZV9pZCI6Ijc4OTc1IiwiY3VzdG9tX3dpbGV5X2V4dGVybmFsX2NvdXJzZV9pZCI6bnVsbCwiY3VzdG9tX3dpbGV5X3Byb2R1Y3RfaWQiOiI0MmQwODY1Ny0yZjQwLTQxYWQtOGUxMC1mYWM0MTM4MjY3OWYiLCJsdGlfbGF1bmNoX2lkIjoiZmExMWNlZTQtMzE3Yy00NjkxLTk4MjktMzdkNGZhMjMxMWM0IiwibHRpX2xhdW5jaF91cmwiOiJodHRwczovL2Fzc2Vzc21lbnQuZWR1Y2F0aW9uLndpbGV5LmNvbS93cG5nL2FwaS92MS9sdGkvcHJvZHVjdHMvNDJkMDg2NTctMmY0MC00MWFkLThlMTAtZmFjNDEzODI2NzlmL2Fzc2Vzc21lbnRzLzRjZDA2MWQyLWYwNjktNGViNy1iYTVhLTMyYjAzYjY3ZWM1YSIsImF1dG9fZ3JhZGVfc3luYyI6ZmFsc2UsImN1c3RvbV9hc3Nlc3NtZW50X3BsYXllcl9yZWRlc2lnbl9lbmFibGVkIjp0cnVlLCJjdXN0b21fYXNzZXNzbWVudF9kaXNjb3ZlcnlfcmVkZXNpZ25fZW5hYmxlZCI6dHJ1ZSwiY3VzdG9tX2Fzc2Vzc21lbnRfZGFzaGJvYXJkX2VuYWJsZWQiOmZhbHNlLCJyZWRlc2lnbiI6dHJ1ZSwiY3VzdG9tX2FkYXB0aXZpdHlfZ3JhcGgiOm51bGwsImN1c3RvbV93aWxleV9sbXNfdHlwZSI6IldJTEVZX0NBTlZBUyJ9',
            'X-NG-JWT-TOKEN': 'eyJraWQiOiJ3cG5nX2FsaWFzIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJhbWNtaWNoYWVsMUBsaWJlcnR5LmVkdSIsImxtc3JvbGUiOiJTVFVERU5UIiwiaXNzIjoiaHR0cHM6XC9cL2VkdWNhdGlvbi53aWxleS5jb21cL3dwbmdcL2FwaVwvdjFcL3Nzb1wvand0IiwibG1zY29udGV4dGlkIjoiNjFmNWQ4Yzk5ZTZjZGQ4Y2Y1NWQ2Mjc3NWI3YWRjYjcwNDdlOTM3OSIsImxtc3Jlc291cmNlbGlua2lkIjoiZjFkM2MxNmIwODNmZjA1MjhlNjcwNDVhMzQ1ZDc3N2VlYjU1N2NhNiIsImx0aWNvbnN1bWVya2V5IjoiMmNjYjUwNGUtZDJiYS00YTNiLTkyNzQtMDZmOTZmM2MzOWYyIiwibG1zdXNlcmlkIjoiNWFmYThiZTlmNjM5YWUwZDM3MmI3ZTcwYTIwYTQ2MTFmNWJkODY4MyIsInVzZXJrZXkiOiJmODYxZDVhMy1hM2M0LTQyMWUtODM4Mi1kM2E4ZjI4OGIxYWQiLCJjb3Vyc2V0eXBlIjoiV0lMRVkiLCJhdWQiOiIiLCJsbXNhc3Nlc3NtZW50aWQiOiI0Y2QwNjFkMi1mMDY5LTRlYjctYmE1YS0zMmIwM2I2N2VjNWEiLCJleHRlcm5hbGNvdXJzZWtleSI6IjllYWYyZWZmLWYyZDAtNGUwOC1hMzUyLWI1MzgwMmRjNzk2YSIsImFsbV9ndWlkIjoiQUxNLWExZjUzNWYxLWE2NjgtNDE5Yi04YWUzLTA2NjgyNTM4NTY0MSIsImxtc2Fzc2Vzc21lbnRkdWVkYXRlIjoiMjAyMi0xMi0wNlQwNDo1OTo1OVoiLCJzZWN0aW9ua2V5IjoiNjk2NDE0MmEtNTY4MC00MjkyLWFmMTEtODdhYTQzN2M4OTM0IiwiY291cnNla2V5IjoiOWVhZjJlZmYtZjJkMC00ZTA4LWEzNTItYjUzODAyZGM3OTZhIiwiZXhwIjoxNjY5NTQ2MDU5LCJpYXQiOjE2Njk1MjQ0NTksIm5ndXNlcnR5cGUiOiJXSUxFWVVTRVIifQ.ec94VpUDzlbHrMdP_qIAffYLie-1flPCLQXV-qrwS-2sUu2u1FPfDym4hSvu5808JTOPQNekPoBu0BXp0p76_dT73bGUzRE7PgqD5Qe-OTnKR2NRGOoz1usc5R-MWokKbfI6eY6r9puAFZxw1Vn3SGdrKvQbmyan7AjiQraSkqOtKttc3hVn1_1WHyzpBYrIoVB7BQ3LjHkTOrODgJPXTyTfwgtZW1HVQagyrXgKYWKqVBZDF84G7qbgBN9jbSVBWxm3S2CfqjP-1usKXhrHxwBJJgNmFBVm6WoWmm3UKDpfyb65RW5vl-Zid56CL3-iPmI74aKDDl1qUs5e-unZrg',
            'wpng-api-key': 'qdKg+9rt5XK5QOBVrJILmQ==',
            'AWSALB': '0VvMQXa3462pM3dH+Sn1hfJFuvv+rx9DZTF27vTcIpwnn7hovu80erdtRm4ehsmB7b3u6b0cGZymxdLrj/Rgs/tiRsT0dnXzFABVYDxBT2EOUu/6aD44txNV7qxIuPTo5w0Y/csCGEDkbR7fypuC/XYmKSkknm0F5KJAguDLjZprbdoZdEYq0usGEoiBUQ==',
        }

        self.headers = {
            'authority': 'was.api.wiley.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            # Requests sorts cookies= alphabetically
            # 'cookie': f'osano_consentmanager_uuid=1ea87105-1fe8-4a71-a355-e7d069be5234; osano_consentmanager=3yn2j-hggSvTZ9uhwbc4ZLlzxR1vp3dti1bPgHm964nA2XNSI9u3GwHK5mLOITR1ZYPmur3utf44iB-mDQuGLfE1czf_WesPdCY7ufMkRsiFL7Jqd7wBQHVBctG9vfU5o-5lrQgYegpaZNWiP6Q9taBFT8PoDeDa3yN5Ti0CaJggWnpBLG4Q4HIkG9jgMQ9ExWjEJkcaZtzZAkACQqcvjkXQrd02Mtl49ZfrCW9c3xPADYjkvxOW68Huzbn7BdqRuBuBbdSIIejS61M_HA4mc4amuAc7QgiahL2c7Q==; AMCV_1B6E34B85282A0AC0A490D44%40AdobeOrg=-1124106680%7CMCIDTS%7C19295%7CMCMID%7C11344451058427146173862768382192737247%7CMCAAMLH-1667679158%7C7%7CMCAAMB-1667679158%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1667081558s%7CNONE%7CMCAID%7C3186AF7E192EBE55-60001E55ABF7180D%7CvVersion%7C5.2.0; _gcl_au=1.1.1105266584.1667074358; _ga=GA1.2.1607436432.1667074359; lastRskxRun=1667074359723; rskxRunCookie=0; rCookie=g5qm4624vgatn04lhqym3l9ud14fk; rxVisitor=1667695850299E93DGQSGVH8GGEK2SEBRAGTRFM5KH4B8; dtCookie=v_4_srv_2_sn_2C993841EE47B886EE6F53CC9D179EF7_app-3A182c2fa8506055c5_1_ol_0_perc_100000_mul_1_rcs-3Acss_0; dtLatC=56; rxvt=1667789458519|1667787655311; dtSa=false%7CC%7C15%7CENGR%20360-001%20Heat%20Transfer%20F021%7Cfetch%7C1667787658512%7C387655306_829%7Chttps%3A%2F%2Feducation.wiley.com%2Fngonboard%2Findex.html%7C%7C%7C%2FStudentDashboard%7C; dtPC=2{387655306_829h-vRGOTCNCMHGHFCCFRMHFCQEUHMRNHPUKF-0e0;} wpng-user-context=eyJvYXV0aF9jb25zdW1lcl9rZXkiOiJXUE5HXzk0MmUwZmZlLTA2ZDgtNDYyZS1hYTk3LWRmY2UzODQ4MWU1ZCIsInVzZXJfaWQiOiI1YWZhOGJlOWY2MzlhZTBkMzcyYjdlNzBhMjBhNDYxMWY1YmQ4NjgzIiwiZXh0ZXJuYWxfdXNlcl9pZCI6IjE4MTk5NTkiLCJyb2xlcyI6IkxlYXJuZXIiLCJjdXN0b21fd2lsZXlfcm9sZSI6IlNUVURFTlQiLCJjb250ZXh0X2lkIjoiNjFmNWQ4Yzk5ZTZjZGQ4Y2Y1NWQ2Mjc3NWI3YWRjYjcwNDdlOTM3OSIsImluc3RpdHV0aW9uX2tleSI6ImY0YjlhZDhlLTQ3MDktMTFlOS05MTI5LTEyOWQ1OTM0MzhkYyIsImN1c3RvbV9jYW52YXNfY291cnNlX2lkIjoiNzg2NzkiLCJjdXN0b21fd2lsZXlfY29udGVudF9tb2RlIjpudWxsLCJyZXNvdXJjZV9saW5rX3RpdGxlIjoiSFcgMTIiLCJjdXN0b21fd2lsZXlfdXNlcl9pbnN0X21hcF9pZCI6IjI2ODU2MzciLCJjdXN0b21fd2lsZXlfdXNlcl9wcm9maWxlX2lkIjoiMjY4NTYzNyIsInVzZXJfcHJvZmlsZV9rZXkiOiJmODYxZDVhMy1hM2M0LTQyMWUtODM4Mi1kM2E4ZjI4OGIxYWQiLCJjdXN0b21fd2lsZXlfZXh0ZXJuYWxfdXNlcl9pZCI6bnVsbCwiY3VzdG9tX3dpbGV5X2NvdXJzZV9pZCI6Ijc4OTc1IiwiY3VzdG9tX3dpbGV5X2V4dGVybmFsX2NvdXJzZV9pZCI6bnVsbCwiY3VzdG9tX3dpbGV5X3Byb2R1Y3RfaWQiOiI0MmQwODY1Ny0yZjQwLTQxYWQtOGUxMC1mYWM0MTM4MjY3OWYiLCJsdGlfbGF1bmNoX2lkIjoiZmExMWNlZTQtMzE3Yy00NjkxLTk4MjktMzdkNGZhMjMxMWM0IiwibHRpX2xhdW5jaF91cmwiOiJodHRwczovL2Fzc2Vzc21lbnQuZWR1Y2F0aW9uLndpbGV5LmNvbS93cG5nL2FwaS92MS9sdGkvcHJvZHVjdHMvNDJkMDg2NTctMmY0MC00MWFkLThlMTAtZmFjNDEzODI2NzlmL2Fzc2Vzc21lbnRzLzRjZDA2MWQyLWYwNjktNGViNy1iYTVhLTMyYjAzYjY3ZWM1YSIsImF1dG9fZ3JhZGVfc3luYyI6ZmFsc2UsImN1c3RvbV9hc3Nlc3NtZW50X3BsYXllcl9yZWRlc2lnbl9lbmFibGVkIjp0cnVlLCJjdXN0b21fYXNzZXNzbWVudF9kaXNjb3ZlcnlfcmVkZXNpZ25fZW5hYmxlZCI6dHJ1ZSwiY3VzdG9tX2Fzc2Vzc21lbnRfZGFzaGJvYXJkX2VuYWJsZWQiOmZhbHNlLCJyZWRlc2lnbiI6dHJ1ZSwiY3VzdG9tX2FkYXB0aXZpdHlfZ3JhcGgiOm51bGwsImN1c3RvbV93aWxleV9sbXNfdHlwZSI6IldJTEVZX0NBTlZBUyJ9; X-NG-JWT-TOKEN=eyJraWQiOiJ3cG5nX2FsaWFzIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJhbWNtaWNoYWVsMUBsaWJlcnR5LmVkdSIsImxtc3JvbGUiOiJTVFVERU5UIiwiaXNzIjoiaHR0cHM6XC9cL2VkdWNhdGlvbi53aWxleS5jb21cL3dwbmdcL2FwaVwvdjFcL3Nzb1wvand0IiwibG1zY29udGV4dGlkIjoiNjFmNWQ4Yzk5ZTZjZGQ4Y2Y1NWQ2Mjc3NWI3YWRjYjcwNDdlOTM3OSIsImxtc3Jlc291cmNlbGlua2lkIjoiZjFkM2MxNmIwODNmZjA1MjhlNjcwNDVhMzQ1ZDc3N2VlYjU1N2NhNiIsImx0aWNvbnN1bWVya2V5IjoiMmNjYjUwNGUtZDJiYS00YTNiLTkyNzQtMDZmOTZmM2MzOWYyIiwibG1zdXNlcmlkIjoiNWFmYThiZTlmNjM5YWUwZDM3MmI3ZTcwYTIwYTQ2MTFmNWJkODY4MyIsInVzZXJrZXkiOiJmODYxZDVhMy1hM2M0LTQyMWUtODM4Mi1kM2E4ZjI4OGIxYWQiLCJjb3Vyc2V0eXBlIjoiV0lMRVkiLCJhdWQiOiIiLCJsbXNhc3Nlc3NtZW50aWQiOiI0Y2QwNjFkMi1mMDY5LTRlYjctYmE1YS0zMmIwM2I2N2VjNWEiLCJleHRlcm5hbGNvdXJzZWtleSI6IjllYWYyZWZmLWYyZDAtNGUwOC1hMzUyLWI1MzgwMmRjNzk2YSIsImFsbV9ndWlkIjoiQUxNLWExZjUzNWYxLWE2NjgtNDE5Yi04YWUzLTA2NjgyNTM4NTY0MSIsImxtc2Fzc2Vzc21lbnRkdWVkYXRlIjoiMjAyMi0xMi0wNlQwNDo1OTo1OVoiLCJzZWN0aW9ua2V5IjoiNjk2NDE0MmEtNTY4MC00MjkyLWFmMTEtODdhYTQzN2M4OTM0IiwiY291cnNla2V5IjoiOWVhZjJlZmYtZjJkMC00ZTA4LWEzNTItYjUzODAyZGM3OTZhIiwiZXhwIjoxNjY5NTQ2MDU5LCJpYXQiOjE2Njk1MjQ0NTksIm5ndXNlcnR5cGUiOiJXSUxFWVVTRVIifQ.ec94VpUDzlbHrMdP_qIAffYLie-1flPCLQXV-qrwS-2sUu2u1FPfDym4hSvu5808JTOPQNekPoBu0BXp0p76_dT73bGUzRE7PgqD5Qe-OTnKR2NRGOoz1usc5R-MWokKbfI6eY6r9puAFZxw1Vn3SGdrKvQbmyan7AjiQraSkqOtKttc3hVn1_1WHyzpBYrIoVB7BQ3LjHkTOrODgJPXTyTfwgtZW1HVQagyrXgKYWKqVBZDF84G7qbgBN9jbSVBWxm3S2CfqjP-1usKXhrHxwBJJgNmFBVm6WoWmm3UKDpfyb65RW5vl-Zid56CL3-iPmI74aKDDl1qUs5e-unZrg; wpng-api-key=qdKg+9rt5XK5QOBVrJILmQ==; AWSALB=0VvMQXa3462pM3dH+Sn1hfJFuvv+rx9DZTF27vTcIpwnn7hovu80erdtRm4ehsmB7b3u6b0cGZymxdLrj/Rgs/tiRsT0dnXzFABVYDxBT2EOUu/6aD44txNV7qxIuPTo5w0Y/csCGEDkbR7fypuC/XYmKSkknm0F5KJAguDLjZprbdoZdEYq0usGEoiBUQ==',
            'origin': 'https://education.wiley.com',
            'referer': 'https://education.wiley.com/',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }

        self.params = {
            'studentMode': 'true',
        }

        self.json_data = {
            'id': self.code,
            'masterQuestionId': 'w384fe828-c02a-4f87-b298-ed2d6a9a588a',
            'masterQuestionVersion': '1',
            'context': {
                'consumer_key': 'WPNG_942e0ffe-06d8-462e-aa97-dfce38481e5d',
                'lis_result_sourcedid': '360415-78679-9823873-1819959-4c1edcec405ea359df9b3b333ce378685d4f3fdc',
                'master_assessment_id': '4cd061d2-f069-4eb7-ba5a-32b03b67ec5a',
                'user_id': '5afa8be9f639ae0d372b7e70a20a4611f5bd8683',
                'roles': [
                    'Learner',
                ],
                'product_id': '42d08657-2f40-41ad-8e10-fac41382679f',
                'question_card_id': '8f4eb928-a66b-4cad-87bd-cfb641989431',
                'context_id': '61f5d8c99e6cdd8cf55d62775b7adcb7047e9379',
                'assessment_id': 'de54cd16b31346079afccd9a2a4d9fe571bc8113911251ed5521134ca3795e92',
                'entry_num': 1,
                'resource_link_id': 'f1d3c16b083ff0528e67045a345d777eeb557ca6',
            },
            'policies': {
                'attemptPolicy': {
                    'maxAttempts': 3,
                    'attemptPenalty': {
                        'attempt': 3,
                        'penalty': 0,
                    },
                },
                'algorithmCalculationMode': 'sameValues',
                'assistancePolicies': [
                    {
                        'assistanceType': 'answer',
                        'availableSinceAttempt': -1,
                        'penalty': 0,
                    },
                    {
                        'assistanceType': 'reference',
                        'availableSinceAttempt': 1,
                        'penalty': 0,
                    },
                    {
                        'assistanceType': 'solution',
                        'availableSinceAttempt': -1,
                        'penalty': 0,
                    },
                ],
                'dueDatePolicy': {
                    'penalties': [],
                    'autoSubmit': True,
                    'rules': {
                        'lateSubmit': 'no',
                        'finish': 'byDueDate',
                        'itemListDetails': 'yes',
                        'itemAccess': 'yes',
                        'itemAssistance': 'all',
                    },
                },
                'feedbackPolicy': 'always',
                'evaluationPolicy': {
                    'numericPolicy': {
                        'defaultTolerance': 2,
                        'enableQuestionLevelTolerance': True,
                        'enableQuestionLevelSignificantDigits': False,
                        'showToleranceInfo': True,
                        'significantDigitsInfo': 'specific',
                        'significantDigitsHelp': 'passive',
                    },
                    'excelEvaluationMode': 'any',
                },
                'hideTitle': False,
                'securityPolicy': {
                    'applicable': False,
                    'password': '',
                },
                'scoreToKeep': 'best',
            },
            'algorithmResult': {
                'id': 'EAT_1480573870321_1_0759442025567383',
                'templateVariables': [
                    {
                        'id': '$L',
                        'value': '3',
                    },
                    {
                        'id': '$Th',
                        'value': '3600',
                    },
                ],
            },
            'score': {
                'type': 'auto',
                'value': 0,
                'rawValue': 0,
                'grade': 'incorrect',
            },
            'submitAll': False,
            'questionCardId': '8f4eb928-a66b-4cad-87bd-cfb641989431',
            'title': 'Problem 12.022',
            'state': 'none',
            'numAttempts': 3,
            'maxAttempts': 3,
            'attemptPenalty': {
                'attempt': 3,
                'penalty': 0,
            },
            'creationDate': '2022-11-25T09:25:58.265Z',
            'modificationDate': '2022-11-27T05:02:22.632Z',
            'timeSpent': 0,
            'itemResults': [
                {
                    'id': 'EAT_1480573870321_1_0759442025567383',
                    'numAttempts': 3,
                    'maxAttempts': 3,
                    'attemptPenalty': {
                        'attempt': 3,
                        'penalty': 0,
                        'used': True,
                    },
                    'score': {
                        'type': 'auto',
                        'value': 0,
                        'rawValue': 0,
                        'grade': 'incorrect',
                    },
                    'feedback': '',
                    'modified': False,
                    'hasSubmit': True,
                    'available': 'yes',
                    'visible': False,
                    'state': 'frozen',
                    'manuallyGraded': False,
                    'sessionStatus': 'final',
                    'datestamp': '2022-11-27T05:02:22.593Z',
                    'responseVariables': [
                        {
                            'id': 'EAT_1480573870321_1_0759442025567383_Numeric_Maple_4',
                            'baseType': 'number',
                            'candidateResponse': {
                                'values': [
                                    '20',
                                ],
                            },
                            'score': 0,
                            'modified': False,
                            'numericPolicies': {
                                'tolerance': '10',
                                'sig': None,
                                'showToleranceInfo': True,
                                'significantDigitsInfo': 'none',
                                'significantDigitsHelp': 'none',
                            },
                            'gradableXLMap': None,
                            'expandPart': False,
                        },
                    ],
                    'availableAssistances': [
                        {
                            'type': 'answer',
                            'penalty': 0,
                            'used': False,
                        },
                        {
                            'type': 'reference',
                            'penalty': 0,
                            'used': False,
                        },
                        {
                            'type': 'solution',
                            'penalty': 0,
                            'used': False,
                        },
                    ],
                },
            ],
            'eventHistory': [
                {
                    'eventId': 'bf19ba5f-1b3f-4279-afcb-5d313e528e47',
                    'number': 3,
                    'date': '2022-11-27T05:02:22.613Z',
                    'availableAssistances': [
                        {
                            'type': 'reference',
                            'penalty': 0,
                            'used': False,
                        },
                    ],
                    'eventType': 'submit',
                    'score': {
                        'type': 'attempt',
                        'value': 0,
                        'grade': 'incorrect',
                        'raw': 0,
                    },
                },
                {
                    'eventId': '27bb7f7a-d687-4785-8532-77157a526677',
                    'number': 2,
                    'date': '2022-11-27T04:52:39.028Z',
                    'availableAssistances': [
                        {
                            'type': 'reference',
                            'penalty': 0,
                            'used': False,
                        },
                    ],
                    'eventType': 'submit',
                    'score': {
                        'type': 'attempt',
                        'value': 0,
                        'grade': 'incorrect',
                        'raw': 0,
                    },
                },
                {
                    'eventId': '1eed1cc5-e28b-4214-9d16-41791fed1c0a',
                    'number': 1,
                    'date': '2022-11-27T04:51:38.105Z',
                    'availableAssistances': [
                        {
                            'type': 'reference',
                            'penalty': 0,
                            'used': False,
                        },
                    ],
                    'eventType': 'submit',
                    'score': {
                        'type': 'attempt',
                        'value': 0,
                        'grade': 'incorrect',
                        'raw': 0,
                    },
                },
            ],
        }

        self.data = {'id': self.code}
        self.key = '","value":"'
        self.answers = []

    def get_answer(self):
        response = requests.post('https://was.api.wiley.com/was/ga/v1/questions/c/items/E/answer', cookies=self.cookies,
                                 json=self.data, headers=self.headers)

        response_string = response.text

        res = [i for i in range(len(response_string)) if response_string.startswith(self.key, i)]

        for index in res:
            value_title_string = response_string[index - 15:index]

            dollar_sign_index_list = [i for i in range(len(value_title_string)) if
                                      value_title_string.startswith('$', i)]

            for dollar_sign_index in dollar_sign_index_list:
                value_title = value_title_string[dollar_sign_index + 1:]

                value = response_string[index + 11:index + 20]
                value_num = re.sub('[^0-9.-]', '', value)

                self.answers.append(f'{value_title}: {value_num}')

        return self.answers




