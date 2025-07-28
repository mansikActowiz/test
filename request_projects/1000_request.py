import requests

# cookies = {
#     'klk_currency': 'USD',
#     'kepler_id': '46c1fb69-fbba-4784-8d42-83cb0982a8a1',
#     'klk_rdc': 'US',
#     'klk_ga_sn': '4369251097..1750656023256',
#     '__lt__cid': '859a5a17-361e-4362-a223-514270b633c3',
#     '__lt__cid.c83939be': '859a5a17-361e-4362-a223-514270b633c3',
#     '__lt__sid': 'eae094cd-7f4bcfe7',
#     '__lt__sid.c83939be': 'eae094cd-7f4bcfe7',
#     '_fwb': '154tD823EygGdllvmlju7Gx.1750656024022',
#     'wcs_bt': 's_2cb388a4aa34:1750656024',
#     'dable_uid': '63778019.1750656049950',
#     '_gcl_au': '1.1.345839410.1750656025',
#     '_gid': 'GA1.2.1331656445.1750656025',
#     '_ga': 'GA1.1.1722000750.1750656025',
#     'JSESSIONID': 'AD96FA028DC1EF220246F1C6C3426363',
#     'KOUNT_SESSION_ID': 'AD96FA028DC1EF220246F1C6C3426363',
#     '_uetsid': 'c4b06cb04ff111f0b220776fe0b02243',
#     '_uetvid': 'c4b0a5704ff111f0abae4b6d368b4c98',
#     '_yjsu_yjad': '1750656025.aa0dfc5f-2db3-4ebc-af3d-5ff4ed820a53',
#     '_tt_enable_cookie': '1',
#     '_ttp': '01JYDKP13JT92NFDS454SMDT98_.tt.1',
#     '_ga_FW3CMDM313': 'GS2.1.s1750656025$o1$g0$t1750656025$j60$l0$h0',
#     '_ga_HSY7KJ18X2': 'GS2.1.s1750656025$o1$g0$t1750656025$j60$l0$h0',
#     'ttcsid_C1SIFQUHLSU5AAHCT7H0': '1750656025718::R0xBXkd8U_530e_zu1PZ.1.1750656026222',
#     'ttcsid': '1750656025719::q3nSSV3R8IcEt1uTh7Gb.1.1750656026222',
#     '_ga_V8S4KC8ZXR': 'GS2.1.s1750656024$o1$g1$t1750656026$j58$l0$h1914087761',
#     'clientside-cookie': 'f4d8f7c9f351bf2052ac4313e2252aa32f5b0aeeb84b01066bd193a116f4f7fe4351f9eef2342423cad9a536a5cb0d994badbc64819ab42a70db8d460ea226eb801aca8c60148780db44a1210c00e7f3de30a0d8d1553492915d1d325d46319b3e5a91ee4afb3cf88247c38c2227d9aab0811630ba913fe89cf1dc3a396bad086046017706fa03fab05ff8991aa58c4479637525e64ec7591656',
#     'forterToken': '90a7e02e059a46afaaaaf97eea415c9a_1750656024891__UDF43-m4_21ck_',
#     'datadome': 'yQdjl~nc0WWnMCA2mTGmNbHEmQ6NaHsENYVpxMo~gL9JqFp4ojrboQGjGajlG6WY8DSiRVgDYDAH3qbM0MP4psVjD6CSbJxpIEspK_FRFI67Nw8RI6Qmw3cYEopW3h~I',
#     'klk_i_sn': '0921297714..1750656475391',
# }

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'if-none-match': 'W/"1e741-ZnHA+75pKaKK5zBmq4PR9UybvQE"',
    'priority': 'u=0, i',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="137.0.7151.104", "Chromium";v="137.0.7151.104", "Not/A)Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': 'klk_currency=USD; kepler_id=46c1fb69-fbba-4784-8d42-83cb0982a8a1; klk_rdc=US; klk_ga_sn=4369251097..1750656023256; __lt__cid=859a5a17-361e-4362-a223-514270b633c3; __lt__cid.c83939be=859a5a17-361e-4362-a223-514270b633c3; __lt__sid=eae094cd-7f4bcfe7; __lt__sid.c83939be=eae094cd-7f4bcfe7; _fwb=154tD823EygGdllvmlju7Gx.1750656024022; wcs_bt=s_2cb388a4aa34:1750656024; dable_uid=63778019.1750656049950; _gcl_au=1.1.345839410.1750656025; _gid=GA1.2.1331656445.1750656025; _ga=GA1.1.1722000750.1750656025; JSESSIONID=AD96FA028DC1EF220246F1C6C3426363; KOUNT_SESSION_ID=AD96FA028DC1EF220246F1C6C3426363; _uetsid=c4b06cb04ff111f0b220776fe0b02243; _uetvid=c4b0a5704ff111f0abae4b6d368b4c98; _yjsu_yjad=1750656025.aa0dfc5f-2db3-4ebc-af3d-5ff4ed820a53; _tt_enable_cookie=1; _ttp=01JYDKP13JT92NFDS454SMDT98_.tt.1; _ga_FW3CMDM313=GS2.1.s1750656025$o1$g0$t1750656025$j60$l0$h0; _ga_HSY7KJ18X2=GS2.1.s1750656025$o1$g0$t1750656025$j60$l0$h0; ttcsid_C1SIFQUHLSU5AAHCT7H0=1750656025718::R0xBXkd8U_530e_zu1PZ.1.1750656026222; ttcsid=1750656025719::q3nSSV3R8IcEt1uTh7Gb.1.1750656026222; _ga_V8S4KC8ZXR=GS2.1.s1750656024$o1$g1$t1750656026$j58$l0$h1914087761; clientside-cookie=f4d8f7c9f351bf2052ac4313e2252aa32f5b0aeeb84b01066bd193a116f4f7fe4351f9eef2342423cad9a536a5cb0d994badbc64819ab42a70db8d460ea226eb801aca8c60148780db44a1210c00e7f3de30a0d8d1553492915d1d325d46319b3e5a91ee4afb3cf88247c38c2227d9aab0811630ba913fe89cf1dc3a396bad086046017706fa03fab05ff8991aa58c4479637525e64ec7591656; forterToken=90a7e02e059a46afaaaaf97eea415c9a_1750656024891__UDF43-m4_21ck_; datadome=yQdjl~nc0WWnMCA2mTGmNbHEmQ6NaHsENYVpxMo~gL9JqFp4ojrboQGjGajlG6WY8DSiRVgDYDAH3qbM0MP4psVjD6CSbJxpIEspK_FRFI67Nw8RI6Qmw3cYEopW3h~I; klk_i_sn=0921297714..1750656475391',
}

params = {
    'spm': 'Home.SearchSuggest_LIST',
    'clickId': '049c826980',
}

response = requests.get(
    'https://www.klook.com/activity/143928-dunia-fantasi-ancol/',
    params=params,
    # cookies=cookies,
    headers=headers,
)

# print(response.status_code)
final_url=response.url


# print(final_url)

for i in range(1000):
    multiple_response=requests.get(final_url,params=params,
                                   # cookies=cookies,
                                   headers=headers)

    raw_html=multiple_response.text
    if 'Dunia Fantasi' in raw_html:
        print(f"{i + 1}: Status Code = {multiple_response.status_code}")

    # print(raw_html)
    # exit(0)

