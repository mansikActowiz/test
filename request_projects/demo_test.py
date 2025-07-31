import requests

cookies = {
    '__cf_bm': 'jmBU5ypMwlAOcRYmAluEFTVIdAdHRWBeJuR3y4.B2BI-1748500758-1.0.1.1-H352XxqqTrERWLm4v1jcDh8eSb3tU7peyyUXsU9KeyuJ41uiZHnFLjJeJEEMGhIC0d6L49LpLKhc_qttbz86bboRACdlWyvDHx.yumzmODU',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Mon, 26 May 2025 03:25:24 GMT',
    'if-none-match': '"05113d7f85a53229a052c07c4f10a4e4"-gzip',
    'priority': 'u=0, i',
    'referer': 'https://locations.starbucks.sa/directory',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    # 'cookie': '__cf_bm=jmBU5ypMwlAOcRYmAluEFTVIdAdHRWBeJuR3y4.B2BI-1748500758-1.0.1.1-H352XxqqTrERWLm4v1jcDh8eSb3tU7peyyUXsU9KeyuJ41uiZHnFLjJeJEEMGhIC0d6L49LpLKhc_qttbz86bboRACdlWyvDHx.yumzmODU',
}

response = requests.get('https://locations.starbucks.sa/directory/abha', cookies=cookies, headers=headers)