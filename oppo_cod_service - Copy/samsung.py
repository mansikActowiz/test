# import requests
import pandas as pd
import json
from curl_cffi import requests
cookies = {
    'recent_list': '[{"familyCode":"539175","modelCode":"SM-A566EZGZ","tellsomeYn":"N","updated":"2025-08-15 09:23:18"},{"familyCode":"539188","modelCode":"SM-A366ELVK","tellsomeYn":"N","updated":"2025-08-15 10:39:22"}]',
    'deliveryPincode': '682042',
    'country_region': 'CA-ON',
    's_fpid': '3df65fcd-0b41-4c45-8cb6-cdd5afdd4739',
    'country_codes': 'in',
    'device_type': 'pc',
    '__COM_SPEED': 'H',
    'cookie_country': 'in',
    'home_pnz': 'Mobile',
    'ak_bmsc': 'B298B4A8ABD7861471BB42ABD05554FB~000000000000000000000000000000~YAAQt/Q3FyzhNquYAQAA+d8KrRzGyiSsTtu6cdYlYC0UxX3xqspbKi7kQeIjy89jX1ot6+YWwba+smFVl7GX80yLEePhMY0lENG3xNGT+TVEcsSbDgDLXqKm9rbh1RW7f7S96QRFx0Sej7tzgh4xZPuSo5SYhV0aF/e2msZx1qR4L7HjKtwCDoEckIE1sZlmwH7/WCvRaiIRumSOjSCU+GwngA7wfrd9KiWXdmqEy12/ITPGiM852RqGHKzxhIWZf4KFbnTZy2X7HAxcZAkghzTsUg63rW7+y5OnhmIhoeG2lSzVXaQYvdQmQUKFtWfbbEMkBPr3TMpRImTOCqgwef88NXfV+jwtsIZo8HJI1aPVMgTOugH8s5hTjN2s6/irrDyQT2XSeSox2Krm',
    'bm_sz': 'F3C920C6A7CF44E0C4C97BC2893A075B~YAAQt/Q3Fy3hNquYAQAA+d8KrRwRlrYgyqmFzH4+8liwgAlE31syv7p2jmDi5szW5bG493TQsqACds9OnLideJXfDZqFgpHrOevyVjbmbTIVbfox7eQTKEb7BAARA2ENqof19OcWZ6Eh6hnMAb+4QAEBaVoMp1I60dWFoN2utQxNqMgM7kpM/lFPQkibvrzI7vSlUik2JZ+T7KB1trG1UWKN9HkZuvAI1lkagfWbjU4jc4tsPCi/5qLcKgXF8w+ZB8o/hk8TfGSuc87ejOVOWL1DcBVLNp6TisI1MfuSriv3Y7/J+kjhTVOsJdsmI3bj2e1UNBCPiO5EJvTlQt9z9Mk9A0jtRSGSTrsnaRf2U20lrBrQJg==~3360051~3355461',
    'cmapi_cookie_privacy': 'permit%201%2C2%2C3%2C4',
    'notice_gdpr_prefs': '0%2C1%2C2%2C3::implied%2Ceu',
    'directCallFlAA': 'undefined',
    'AMCVS_80163DBE5A3CC3DC0A495EC2%40AdobeOrg': '1',
    'AMCV_80163DBE5A3CC3DC0A495EC2%40AdobeOrg': '179643557%7CMCIDTS%7C20316%7CMCMID%7C40647209780920150572609104903293249546%7CMCAAMLH-1755854600%7C12%7CMCAAMB-1755854600%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1755257000s%7CNONE%7CvVersion%7C5.5.0',
    'kndctr_80163DBE5A3CC3DC0A495EC2_AdobeOrg_identity': 'CiY0MDY0NzIwOTc4MDkyMDE1MDU3MjYwOTEwNDkwMzI5MzI0OTU0NlIRCJDKq%2DiKMxgBKgRJTkQxMAOgAZTKq%2DiKM7ABAPABkMqr6Ioz',
    'BVBRANDID': '22dd61bc-9825-47f3-af0d-36a8d336008a',
    '_gcl_gs': '2.1.k1$i1755249796$u180406437',
    '_ga': 'GA1.1.837507620.1755249802',
    '_ba_exist': 'true',
    'FPGCLAW': '2.1.kCjwKCAjwtfvEBhAmEiwA-DsKjjhL4FjjOpAmVKnbh7zmGjSktvNKt4vtbTqQ8RK-lkp4ra-Gj8ouXxoC2fcQAvD_BwE$i1755249832',
    'FPGCLGS': '2.1.k1$i1755249825$u180406437',
    'FPAU': '1.2.2125246221.1755249832',
    'kampyle_userid': '2420-a76e-4979-1b46-2501-408c-4845-92b7',
    '_fbp': 'fb.1.1755249804920.505874056674959550',
    '_gcl_au': '1.1.1430124959.1755249805',
    '_scid': 'Fn8dkzbznNvc1NloTMFWFjCE2RPgO2pG',
    '_ScCbts': '%5B%5D',
    '_clck': '1tzrrot%7C2%7Cfyh%7C0%7C2053',
    'spr-chat-token-60b09fbd4a12a35df6a54193_app_943747': '',
    'mfKey': 'xjpegm.1755249807708',
    '_sctr': '1%7C1755196200000',
    '_gcl_aw': 'GCL.1755249820.CjwKCAjwtfvEBhAmEiwA-DsKjjhL4FjjOpAmVKnbh7zmGjSktvNKt4vtbTqQ8RK-lkp4ra-Gj8ouXxoC2fcQAvD_BwE',
    'cookiesaccepted-countries': 'in',
    'cookiesaccepted': 'true',
    '_abck': 'ADCAFB8E522F21641B755D6E0859A1B4~-1~YAAQ7xzFF+nknqSYAQAAyqcOrQ42lg8N2j8jsYKoXDEy9A3J7yLIQnxf3+W6rXwvRzAFeKDqkXvq0OaNwsLoUaRwQPOYuEwzdcyhHMib4hbR+exxPnLKZgFoLaSWpuo87FFLcNdz9am5CoRVNMkgzw0NwOaB/J5DKBKKyeW9lKTHszw7Gj3UCpsQcwGuKUSDeyYu5rSTIiYrtTbw7Akr7od5GLbiA5wWc9NaVBbS32P09Is4ild2jutfYSzpg0yV1+iZV66LiZl+uwgy6Z4TkbKrWUFKxUt8vtQc1r0pgb0JEnzgb9qQt83hn8BWEaJXui3kh/HGbIFJpiduX0cr5Ul8YpRqnCUm8Hzjg8L+FSCagHLJCisR309EOl/tPJiOrxUQ49AUliBxuGlgftd28rmPPzPlkRtaBrOBem7RAxVrhrYLMZpOC9EcXIh5O9hCxbBnU1+hpcLhkFaYy9C/W74JatzlE4QZt53gwCPk/BW/Ig==~-1~-1~-1',
    'mf_utms': '%7B%22modelCode%22%3A%22SM-A366ELVKINS%22%7D',
    's_pv': 'in%3Amobile%3Asmartphones%3Agalaxy%20a%3Agalaxy%20a36%3Abuy',
    '_cs_mk_aa': '0.6200639281722897_1755253275932',
    'AKA_A2': 'A',
    'mboxEdgeCluster': '41',
    'kndctr_80163DBE5A3CC3DC0A495EC2_AdobeOrg_cluster': 'ind1',
    'BVBRANDSID': 'cb0363a4-145e-4497-8032-9b6d3ceccb71',
    '_ba_rand': '9',
    '_ba_initial_refer': '',
    '_ba_ssid': 'q8L6avzP',
    '_ba_page_seq': '0',
    '_ba_parent_seq': '0',
    '_ba_page_ct': '2025-08-15T10%3A24%3A48.940Z',
    '_ba_last_url': 'https%3A%2F%2Fwww.samsung.com%2Fin%2Fsmartphones%2Fgalaxy-a36%2Fbuy%2F%3FmodelCode%3DSM-A366ELVKINS',
    '_ba_initial_refer': '',
    'fw_se': '{%22value%22:%22fws2.e191abd1-8ef2-415e-9e06-3e425a2f52dc.2.1755253516508%22%2C%22createTime%22:%222025-08-15T10:25:16.508Z%22}',
    'FPGSID': '1.1755253305.1755254341.G-5H9H1K0GSH.X8z3MsoJdzP7lV3m6LsGfA',
    'mbox': 'session%2340647209780920150572609104903293249546%2DQRTvzW%231755256251',
    'bm_sv': '8F5D5B49BCF05EB3E572061750A544E8~YAAQ5hzFFwk3UKyYAQAAdoZQrRxVpcFZ37UGqb2pmfwunQYiExy5cQxWhGaVS4icju/kPA0CKD0OJySyShguDlF8BAkysZaNBaH2xXoTElDaXWs/hQrWEf1qc49o8+lhEewlj3CoOQv4wy2r6jYMzK3pt8IyBLXd2zhvum4ofoePUal5QxYXTqjb/NPmNKkYNpIQxuG0GECz5nvvh+9dgQdKNUN51UgX+HEMaClCA/OOvF7zqmDB3Ke4Xdnzd9igGcs=~1',
    '_ba_reload_count': '1',
    's_ppvl': 'in%253Amobile%253Asmartphones%253Agalaxy%2520a%253Agalaxy%2520a36%253Abuy%2C71%2C71%2C5843%2C1366%2C303%2C1366%2C768%2C1%2CP',
    's_ppv': 'in%253Amobile%253Asmartphones%253Agalaxy%2520a%253Agalaxy%2520a36%253Abuy%2C48%2C48%2C5843%2C1366%2C303%2C1366%2C768%2C1%2CP',
    'RT': '"z=1&dm=samsung.com&si=21a8d77e-ac59-4844-b030-03e65280f92a&ss=mecolfme&sl=1&tt=4ir&bcn=%2F%2F684d0d43.akstat.io%2F&ld=ja12"',
    'kampyleUserSession': '1755254367323',
    'kampyleUserSessionsCount': '3',
    'kampyleUserPercentile': '4.574008493144211',
    'kampyleSessionPageCounter': '1',
    'da_sid': 'BBCB33898E26AEA02094AA13ACFB3B61A6.0|4|0|3',
    'da_lid': '629A96239A79EA3AAAA1BB99EEF938EBBB|0|0|0',
    'da_intState': '0',
    'fw_uid': '{%22value%22:%22338dc8d8-e1b1-4a06-b788-e22d56a6ec62%22%2C%22createTime%22:%222025-08-15T10:39:28.680Z%22}',
    'fw_bid': '{%22value%22:%22oNjWyo%22%2C%22createTime%22:%222025-08-15T10:39:28.853Z%22}',
    '_uetsid': '7f60596079b911f0a66da5e997957423',
    '_uetvid': '7f607fd079b911f08547f5343f6d9200',
    'mf_visitid': 'szgyoe.1755254369657',
    '_scid_r': 'JP8dkzbznNvc1NloTMFWFjCE2RPgO2pGB7ljWg',
    '_clsk': 'yjidvb%7C1755254370343%7C3%7C0%7Cl.clarity.ms%2Fcollect',
    '_ga_5H9H1K0GSH': 'GS2.1.s1755253212$o2$g1$t1755254371$j60$l0$h385612038',
    'cto_bundle': 'zyE8QF9RdzJGUWJvN1NrbXAxJTJGVnNvejMlMkI4Q2JudVQzenU1VVFnU3BuemtCJTJGQ3NBcW8lMkZuJTJCTjhHQWdSdkdDMFY5bDZINGN3JTJGaE83UXI5OHlrYnFWTFoybGdEZnF1R2cxTWJ2eDdYWWclMkJrNnIyVTZGMVRaVTZDWXVPN0pOcWMlMkJyS1h1WHl2aFRYNUdqUE0wWGpmbExHUCUyRlhMUVQ4c0taamxPeklIc1lEUW15amtnJTJGa2QlMkZLdkhsNm5xSHo5emFhSmVLbktHQ2x1UDY4cVlpM2Jmc2ZZWlVtQ29RZyUzRCUzRA',
    '_ba_click': 'true',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'priority': 'u=1, i',
    'referer': 'https://www.samsung.com/in/smartphones/galaxy-a36/buy/?modelCode=SM-A366ELVKINS',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': 'recent_list=[{"familyCode":"539175","modelCode":"SM-A566EZGZ","tellsomeYn":"N","updated":"2025-08-15 09:23:18"},{"familyCode":"539188","modelCode":"SM-A366ELVK","tellsomeYn":"N","updated":"2025-08-15 10:39:22"}]; deliveryPincode=682042; country_region=CA-ON; s_fpid=3df65fcd-0b41-4c45-8cb6-cdd5afdd4739; country_codes=in; device_type=pc; __COM_SPEED=H; cookie_country=in; home_pnz=Mobile; ak_bmsc=B298B4A8ABD7861471BB42ABD05554FB~000000000000000000000000000000~YAAQt/Q3FyzhNquYAQAA+d8KrRzGyiSsTtu6cdYlYC0UxX3xqspbKi7kQeIjy89jX1ot6+YWwba+smFVl7GX80yLEePhMY0lENG3xNGT+TVEcsSbDgDLXqKm9rbh1RW7f7S96QRFx0Sej7tzgh4xZPuSo5SYhV0aF/e2msZx1qR4L7HjKtwCDoEckIE1sZlmwH7/WCvRaiIRumSOjSCU+GwngA7wfrd9KiWXdmqEy12/ITPGiM852RqGHKzxhIWZf4KFbnTZy2X7HAxcZAkghzTsUg63rW7+y5OnhmIhoeG2lSzVXaQYvdQmQUKFtWfbbEMkBPr3TMpRImTOCqgwef88NXfV+jwtsIZo8HJI1aPVMgTOugH8s5hTjN2s6/irrDyQT2XSeSox2Krm; bm_sz=F3C920C6A7CF44E0C4C97BC2893A075B~YAAQt/Q3Fy3hNquYAQAA+d8KrRwRlrYgyqmFzH4+8liwgAlE31syv7p2jmDi5szW5bG493TQsqACds9OnLideJXfDZqFgpHrOevyVjbmbTIVbfox7eQTKEb7BAARA2ENqof19OcWZ6Eh6hnMAb+4QAEBaVoMp1I60dWFoN2utQxNqMgM7kpM/lFPQkibvrzI7vSlUik2JZ+T7KB1trG1UWKN9HkZuvAI1lkagfWbjU4jc4tsPCi/5qLcKgXF8w+ZB8o/hk8TfGSuc87ejOVOWL1DcBVLNp6TisI1MfuSriv3Y7/J+kjhTVOsJdsmI3bj2e1UNBCPiO5EJvTlQt9z9Mk9A0jtRSGSTrsnaRf2U20lrBrQJg==~3360051~3355461; cmapi_cookie_privacy=permit%201%2C2%2C3%2C4; notice_gdpr_prefs=0%2C1%2C2%2C3::implied%2Ceu; directCallFlAA=undefined; AMCVS_80163DBE5A3CC3DC0A495EC2%40AdobeOrg=1; AMCV_80163DBE5A3CC3DC0A495EC2%40AdobeOrg=179643557%7CMCIDTS%7C20316%7CMCMID%7C40647209780920150572609104903293249546%7CMCAAMLH-1755854600%7C12%7CMCAAMB-1755854600%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1755257000s%7CNONE%7CvVersion%7C5.5.0; kndctr_80163DBE5A3CC3DC0A495EC2_AdobeOrg_identity=CiY0MDY0NzIwOTc4MDkyMDE1MDU3MjYwOTEwNDkwMzI5MzI0OTU0NlIRCJDKq%2DiKMxgBKgRJTkQxMAOgAZTKq%2DiKM7ABAPABkMqr6Ioz; BVBRANDID=22dd61bc-9825-47f3-af0d-36a8d336008a; _gcl_gs=2.1.k1$i1755249796$u180406437; _ga=GA1.1.837507620.1755249802; _ba_exist=true; FPGCLAW=2.1.kCjwKCAjwtfvEBhAmEiwA-DsKjjhL4FjjOpAmVKnbh7zmGjSktvNKt4vtbTqQ8RK-lkp4ra-Gj8ouXxoC2fcQAvD_BwE$i1755249832; FPGCLGS=2.1.k1$i1755249825$u180406437; FPAU=1.2.2125246221.1755249832; kampyle_userid=2420-a76e-4979-1b46-2501-408c-4845-92b7; _fbp=fb.1.1755249804920.505874056674959550; _gcl_au=1.1.1430124959.1755249805; _scid=Fn8dkzbznNvc1NloTMFWFjCE2RPgO2pG; _ScCbts=%5B%5D; _clck=1tzrrot%7C2%7Cfyh%7C0%7C2053; spr-chat-token-60b09fbd4a12a35df6a54193_app_943747=; mfKey=xjpegm.1755249807708; _sctr=1%7C1755196200000; _gcl_aw=GCL.1755249820.CjwKCAjwtfvEBhAmEiwA-DsKjjhL4FjjOpAmVKnbh7zmGjSktvNKt4vtbTqQ8RK-lkp4ra-Gj8ouXxoC2fcQAvD_BwE; cookiesaccepted-countries=in; cookiesaccepted=true; _abck=ADCAFB8E522F21641B755D6E0859A1B4~-1~YAAQ7xzFF+nknqSYAQAAyqcOrQ42lg8N2j8jsYKoXDEy9A3J7yLIQnxf3+W6rXwvRzAFeKDqkXvq0OaNwsLoUaRwQPOYuEwzdcyhHMib4hbR+exxPnLKZgFoLaSWpuo87FFLcNdz9am5CoRVNMkgzw0NwOaB/J5DKBKKyeW9lKTHszw7Gj3UCpsQcwGuKUSDeyYu5rSTIiYrtTbw7Akr7od5GLbiA5wWc9NaVBbS32P09Is4ild2jutfYSzpg0yV1+iZV66LiZl+uwgy6Z4TkbKrWUFKxUt8vtQc1r0pgb0JEnzgb9qQt83hn8BWEaJXui3kh/HGbIFJpiduX0cr5Ul8YpRqnCUm8Hzjg8L+FSCagHLJCisR309EOl/tPJiOrxUQ49AUliBxuGlgftd28rmPPzPlkRtaBrOBem7RAxVrhrYLMZpOC9EcXIh5O9hCxbBnU1+hpcLhkFaYy9C/W74JatzlE4QZt53gwCPk/BW/Ig==~-1~-1~-1; mf_utms=%7B%22modelCode%22%3A%22SM-A366ELVKINS%22%7D; s_pv=in%3Amobile%3Asmartphones%3Agalaxy%20a%3Agalaxy%20a36%3Abuy; _cs_mk_aa=0.6200639281722897_1755253275932; AKA_A2=A; mboxEdgeCluster=41; kndctr_80163DBE5A3CC3DC0A495EC2_AdobeOrg_cluster=ind1; BVBRANDSID=cb0363a4-145e-4497-8032-9b6d3ceccb71; _ba_rand=9; _ba_initial_refer=; _ba_ssid=q8L6avzP; _ba_page_seq=0; _ba_parent_seq=0; _ba_page_ct=2025-08-15T10%3A24%3A48.940Z; _ba_last_url=https%3A%2F%2Fwww.samsung.com%2Fin%2Fsmartphones%2Fgalaxy-a36%2Fbuy%2F%3FmodelCode%3DSM-A366ELVKINS; _ba_initial_refer=; fw_se={%22value%22:%22fws2.e191abd1-8ef2-415e-9e06-3e425a2f52dc.2.1755253516508%22%2C%22createTime%22:%222025-08-15T10:25:16.508Z%22}; FPGSID=1.1755253305.1755254341.G-5H9H1K0GSH.X8z3MsoJdzP7lV3m6LsGfA; mbox=session%2340647209780920150572609104903293249546%2DQRTvzW%231755256251; bm_sv=8F5D5B49BCF05EB3E572061750A544E8~YAAQ5hzFFwk3UKyYAQAAdoZQrRxVpcFZ37UGqb2pmfwunQYiExy5cQxWhGaVS4icju/kPA0CKD0OJySyShguDlF8BAkysZaNBaH2xXoTElDaXWs/hQrWEf1qc49o8+lhEewlj3CoOQv4wy2r6jYMzK3pt8IyBLXd2zhvum4ofoePUal5QxYXTqjb/NPmNKkYNpIQxuG0GECz5nvvh+9dgQdKNUN51UgX+HEMaClCA/OOvF7zqmDB3Ke4Xdnzd9igGcs=~1; _ba_reload_count=1; s_ppvl=in%253Amobile%253Asmartphones%253Agalaxy%2520a%253Agalaxy%2520a36%253Abuy%2C71%2C71%2C5843%2C1366%2C303%2C1366%2C768%2C1%2CP; s_ppv=in%253Amobile%253Asmartphones%253Agalaxy%2520a%253Agalaxy%2520a36%253Abuy%2C48%2C48%2C5843%2C1366%2C303%2C1366%2C768%2C1%2CP; RT="z=1&dm=samsung.com&si=21a8d77e-ac59-4844-b030-03e65280f92a&ss=mecolfme&sl=1&tt=4ir&bcn=%2F%2F684d0d43.akstat.io%2F&ld=ja12"; kampyleUserSession=1755254367323; kampyleUserSessionsCount=3; kampyleUserPercentile=4.574008493144211; kampyleSessionPageCounter=1; da_sid=BBCB33898E26AEA02094AA13ACFB3B61A6.0|4|0|3; da_lid=629A96239A79EA3AAAA1BB99EEF938EBBB|0|0|0; da_intState=0; fw_uid={%22value%22:%22338dc8d8-e1b1-4a06-b788-e22d56a6ec62%22%2C%22createTime%22:%222025-08-15T10:39:28.680Z%22}; fw_bid={%22value%22:%22oNjWyo%22%2C%22createTime%22:%222025-08-15T10:39:28.853Z%22}; _uetsid=7f60596079b911f0a66da5e997957423; _uetvid=7f607fd079b911f08547f5343f6d9200; mf_visitid=szgyoe.1755254369657; _scid_r=JP8dkzbznNvc1NloTMFWFjCE2RPgO2pGB7ljWg; _clsk=yjidvb%7C1755254370343%7C3%7C0%7Cl.clarity.ms%2Fcollect; _ga_5H9H1K0GSH=GS2.1.s1755253212$o2$g1$t1755254371$j60$l0$h385612038; cto_bundle=zyE8QF9RdzJGUWJvN1NrbXAxJTJGVnNvejMlMkI4Q2JudVQzenU1VVFnU3BuemtCJTJGQ3NBcW8lMkZuJTJCTjhHQWdSdkdDMFY5bDZINGN3JTJGaE83UXI5OHlrYnFWTFoybGdEZnF1R2cxTWJ2eDdYWWclMkJrNnIyVTZGMVRaVTZDWXVPN0pOcWMlMkJyS1h1WHl2aFRYNUdqUE0wWGpmbExHUCUyRlhMUVQ4c0taamxPeklIc1lEUW15amtnJTJGa2QlMkZLdkhsNm5xSHo5emFhSmVLbktHQ2x1UDY4cVlpM2Jmc2ZZWlVtQ29RZyUzRCUzRA; _ba_click=true',
}



params = {
    'skus': 'SM-A366ELVK',
    'postal_code': '560085',

}

response1 = requests.get(
    'https://www.samsung.com/in/api/v4/configurator/serviceability',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response1.status_code)

result=[]
df=pd.read_csv(r'C:\Users\Madri.Gadani\PycharmProjects\PythonProject\oppo_cod_service\zipcode.csv', encoding='latin1')
# print(df)

zip_list=df.iloc[:, 0].tolist()
print(zip_list)
print(len(zip_list))

url='https://www.samsung.com/in/smartphones/galaxy-a36/buy/?modelCode=SM-A366ELVKINS'

for i in zip_list:
    params = {
        'skus': 'SM-A366ELVK',
        'postal_code': i,

    }
    response = requests.get(
        'https://www.samsung.com/in/api/v4/configurator/serviceability',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(response.status_code)
    data = json.loads(response.text)
    # print(data)

    with open(f'D:\madri_new_codes\samsung\samsung_json\pincode_{i}.json','w',encoding='utf-8') as f:
        f.write(response.text)

    external_attrs = data[0].get('external_attributes', {})

    # Handle local_dealers safely
    local_dealers = external_attrs.get('local_dealers', [])
    if local_dealers and 'serviceable' in local_dealers[0]:
        service_availability = 1 if local_dealers[0]['serviceable'] else 0
    else:
        service_availability = 0
    print('service_availability', service_availability)

    # Postal code (safe)
    postal_code = external_attrs.get('postal_code', None)
    print('postal_code', postal_code)

    # COD availability (safe)
    cod_availability = 1 if external_attrs.get('is_cod_available', False) else 0
    print('cod_availability', cod_availability)



    # service_availability = data[0]['external_attributes']['local_dealers'][0]['serviceable']
    # print('service_availability', service_availability)
    # if service_availability == 'true':
    #     service_availability = 1
    # else:
    #     service_availability = 0
    # print(f'service_availability: {service_availability}')
    # postal_code = data[0]['external_attributes']['postal_code']
    # print('postal_code', postal_code)
    # cod_availability = data[0]['external_attributes']['is_cod_available']
    # print('cod_availability', cod_availability)
    #
    # if cod_availability == 'true':
    #     cod_availability = 1
    # else:
    #     cod_availability = 0
    #
    # print(f'cod_availability: {cod_availability}')

    # exit(0)
    result.append({
        'pincode':i,
        'url':url,
        'service_availability':service_availability,
        'postal_code':postal_code,
        'cod_availability':cod_availability,

    })
output_df=pd.DataFrame(result)
print(output_df)

samsung_output_csv='D:\madri_new_codes\samsung\samsung_csv\samsung_output_csv\samsung_output_csv.csv'
output_df.to_csv(samsung_output_csv,index=False)

exit(0)

