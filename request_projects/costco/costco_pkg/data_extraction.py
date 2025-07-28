import os, json, pymongo, threading, time, hashlib
import re
import urllib.parse
from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from scrapy import Selector
# from curl_cffi import requests
import requests

counter = 1

#TODO:: Mongo Connection string
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "costco_US_feasiblity"
COLLECTION_INPUT = "sitemaps_inputs_20250610"
COLLECTION_OUTPUT = "sitemaps_output_20250610"

#TODO:: Pagesave conection path
try:
    # PAGESAVE_PATH = Path("D:/Sharma Danesh/Pagesave/Woolworth_AU_feasiblity/product_page_data/20_03_2025")
    PAGESAVE_PATH = Path("D:/Sharma Danesh/Pagesave/costco_feasibility/product_page_data")
    PAGESAVE_PATH.mkdir(parents=True, exist_ok=True)
except Exception as e:
    print(e)

#TODO:: Url headers
cookies = {
    'invCheckPostalCode': '98101',
    'invCheckStateCode': 'WA',
    'invCheckCity': 'Times%20Square',
    'C_WHLOC': 'USWA',
    'selectedLanguage': '-1',
    'akaas_AS01': '2147483647~rv=48~id=d9e8dd2fcbef019857c39f6179f898d1',
    'BCO': 'pm2',
    'WC_SESSION_ESTABLISHED': 'true',
    'WC_PERSISTENT': 'PlrjwO2d1WPCtUeoBg6Sn0vIKO9bJC36bOQZj1vJzyQ%3D%3B2025-06-10+01%3A41%3A12.906_1749544834699-1021966_10301_-1002%2C-1%2CUSD%2CvVX5azFQXG11WAi%2BSLU6yk2CV1PkSjrlL%2FWy90A4kqThzRMSgiKcmJKN%2F5ssd1%2BYLglkSRomzGpVY%2FfjIF2aHg%3D%3D_10301',
    'WC_AUTHENTICATION_-1002': '-1002%2CtMlGzWl0cXkJgxNmSw2bN88J4PwPTaLQto2HrkgAI8Q%3D',
    'WC_ACTIVEPOINTER': '-1%2C10301',
    'WC_USERACTIVITY_-1002': '-1002%2C10301%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1898306536%2C7KBFh0dHPSQNvOfR5dt45n6aQd%2FaYnxADpZTJiYebs05SZMQNvvLZVWRyVwuQf%2ByHVQhlKX0eOmagKR%2BsPzbi1aKxh%2BZDucVcI7%2BObdgfsFYmPtcsr8mGA%2Bs050b0y%2B9icB%2B3lK%2FosLzJ9tkAVoftg3S59QkNU2a24GzcVwwGbxNYWIo2%2Bgfw9HRls3Lj%2BTV3XYHJdGcxjVQKYB2nmciieeCp5soOJz15RrhMR01t%2F8Abjgzzbw0l0k7ekCf5v%2Be',
    'WC_GENERIC_ACTIVITYDATA': '[45652832112%3Atrue%3Afalse%3A0%3A17ObQdMovfxw31GzeA2zWttzfYZQ5IigeEPvDFj8lvQ%3D][com.ibm.commerce.context.entitlement.EntitlementContext|120577%253B120572%253B120591%253B120563%253B120565%253B120570%253B120571%253B120568%253B120569%253B120757%253B120754%253B120752%253B120758%253B120753%253B120756%253B120755%253B120751%253B120765%253B120926%253B121112%253B120762%253B120763%253B120761%253B120933%253B120920%253B120573%253B120574%253B4000000000000101005%253B60501%253B4000000000000001002%26null%26null%26-2000%26null%26null%26null][com.ibm.commerce.context.audit.AuditContext|1749544834699-1021966][com.ibm.commerce.context.globalization.GlobalizationContext|-1%26USD%26-1%26USD][com.ibm.commerce.store.facade.server.context.StoreGeoCodeContext|null%26null%26null%26null%26null%26null][com.ibm.commerce.context.experiment.ExperimentContext|null][com.ibm.commerce.context.ExternalCartContext|null][com.costco.commerce.member.context.ProfileApiTokenCustomContext|null][com.ibm.commerce.giftcenter.context.GiftCenterContext|null%26null%26null][com.costco.pharmacy.commerce.common.context.PharmacyCustomContext|null%26null%26null%26null%26null%26null][com.ibm.commerce.catalog.businesscontext.CatalogContext|10701%26null%26false%26false%26false][CTXSETNAME|Store][com.ibm.commerce.context.base.BaseContext|10301%26-1002%26-1002%26-1]',
    'STORELOCATION': '{%22storeLocation%22:{%22city%22:%22Seattle%22%2C%22zip%22:%2298134%22}}',
    'WAREHOUSEDELIVERY_WHS': '{%22distributionCenters%22:[%221250-3pl%22%2C%221321-wm%22%2C%221456-3pl%22%2C%22283-wm%22%2C%22561-wm%22%2C%22725-wm%22%2C%22731-wm%22%2C%22758-wm%22%2C%22759-wm%22%2C%22847_0-cor%22%2C%22847_0-cwt%22%2C%22847_0-edi%22%2C%22847_0-ehs%22%2C%22847_0-membership%22%2C%22847_0-mpt%22%2C%22847_0-spc%22%2C%22847_0-wm%22%2C%22847_1-cwt%22%2C%22847_1-edi%22%2C%22847_d-fis%22%2C%22847_lg_n1f-edi%22%2C%22847_lux_us01-edi%22%2C%22847_NA-cor%22%2C%22847_NA-pharmacy%22%2C%22847_NA-wm%22%2C%22847_ss_u362-edi%22%2C%22847_wp_r458-edi%22%2C%22951-wm%22%2C%22952-wm%22%2C%229847-wcs%22]%2C%22groceryCenters%22:[%22115-bd%22]%2C%22pickUpCenters%22:[]%2C%22nearestWarehouse%22:{%22catalog%22:%221-wh%22}}',
    'CriteoSessionUserId': '567ef4b9ffb44538922465d34fcffddc',
    'kndctr_97B21CFE5329614E0A490D45_AdobeOrg_identity': 'CiYxMjQzMjAyMDQ4MzU0ODMwMzU5MjEzNjE3NDY4OTU5MDQ4MzkxMVIQCN7_jsn1MhgBKgNWQTYwAfAB3v-OyfUy',
    'AMCV_97B21CFE5329614E0A490D45%40AdobeOrg': 'MCMID|12432020483548303592136174689590483911',
    'BVBRANDID': 'e5d02bd4-50a1-47b1-8967-ae58d9d0f8ac',
    'bm_ss': 'e919a75364',
    'bm_so': '0D39B8ADCF8FCA826D318E5A49942BCFDB5C0E40D02FC11FB20774A788D7F1CA~YAAQJBEoF+3tRy6XAQAAuY3IWQOeiRJoeIluAl6NtVIv2sOT0xPhZRVBzViBbyghs2q9zmcy5rv3HJPjHsRQ3zPcJw3kZoz2bzbM7v4rFRbKJ9vLQxsr6TQxm4sJgPq/x4RHd2K8acfuMgY3ISkMnv2GEDdZdJpd36CNfr0b8w9eVcUwuhk3flwToHQ6lXiGsMK0tO4WwqBp1JdTsNhqauKuVP9a+GhHNtjC9oAE9U0hRsahA+5n3PSF4ytlzAQUP7U1cZafLaoseI8uEI7btKspBsc1KvAe9flTF8edA/eS90of6aTvbrUsqC5p8zSJP6WOfWxCIr0RYl1zCINQ1LAD0nb6w0QBP8VyyCDsL+3VtxfhrGGD+Olg6XfuNESK9iiZueJKu8ch4EDUQ3aI+U5drC70hn+Yu305kQCVkvs9lciFmX+cli4+xGiLohFSVaVs+WSa29IMzgM9ibTDLg==',
    'client-zip-short': '08601',
    'C_LOC': 'NJ',
    'bm_lso': '0D39B8ADCF8FCA826D318E5A49942BCFDB5C0E40D02FC11FB20774A788D7F1CA~YAAQJBEoF+3tRy6XAQAAuY3IWQOeiRJoeIluAl6NtVIv2sOT0xPhZRVBzViBbyghs2q9zmcy5rv3HJPjHsRQ3zPcJw3kZoz2bzbM7v4rFRbKJ9vLQxsr6TQxm4sJgPq/x4RHd2K8acfuMgY3ISkMnv2GEDdZdJpd36CNfr0b8w9eVcUwuhk3flwToHQ6lXiGsMK0tO4WwqBp1JdTsNhqauKuVP9a+GhHNtjC9oAE9U0hRsahA+5n3PSF4ytlzAQUP7U1cZafLaoseI8uEI7btKspBsc1KvAe9flTF8edA/eS90of6aTvbrUsqC5p8zSJP6WOfWxCIr0RYl1zCINQ1LAD0nb6w0QBP8VyyCDsL+3VtxfhrGGD+Olg6XfuNESK9iiZueJKu8ch4EDUQ3aI+U5drC70hn+Yu305kQCVkvs9lciFmX+cli4+xGiLohFSVaVs+WSa29IMzgM9ibTDLg==^1749558007028',
    'AKA_A2': 'A',
    'bm_mi': '74D9A9E8FC5C20B1568057FA6A3B2193~YAAQJBEoFwLuRy6XAQAA0prIWRwo8526muVjKfBi9OIKOFyW5dI9L7PSWorita/t0+Y5FOtrzWLkuAL5vET2jXmprak+AxHHaFY+d13WxneexJE2LFDc3/aT3IoNi+c5XS7nQMUwZ9PEG0NKKxQXdaYgIot5GwajQvoiEimoYvC+k6nyXSWPxrsYI7g3W8ctUGeTTA7JYGmkxA6laSd+V9obIBMGZTviC6UCRcWza/WlX4xxmb3l4ofBRO0hBh6eYJ50vz7Ag89K9ZUKWsvw6cHEUhFS3EeB9eqePQ8uV0WHbkDqxzB6+wCjs1ZIkxDCXxbHTolGXTwqxAD6QKJQvJDP2LEmYTvyg4yKRp2OE6msg0kUaDfdfquynDtRU8cKZpUwGD+JOw+IjWoN3xpVTe+VD3ecZl76XkRg~1',
    'bm_sc': '4~1~2667809~YAAQJBEoFwTuRy6XAQAA0prIWQRifeSReiilBNlvID4MarmQOZ/QD5BP4UM5OExMXRqyaVaegcNKYN8/5FTeQwr6HGXFnuElSHP7HUZ7Ly/LZjTMSgjMdXkBKE2/dgSVbBNOsykM8hpo8EjfL4P4Kdq4Va+T0iaZS9NGFOak87G4HY6eebOd9zBGfHIunryPjCixVaDJFwLF0U9kmUqMd1wjg9i6S/G2/v/HD6JWDKznUQ+clGFwnzLEUc/Yx/VjnIku309lPaUOn+my6+w3LABrP1DRqJ+bl1Gcbm7ANYJBkugPeXjqMO1JzkW/HRCA7aaMX79G9R8ZK06VdCQPd+algHS/Xt9Bpw5g65AupotXXXiVoFicRTayoSLzQCXGTtAdTnKfhCJF2frKD+5iqd/SXFwz5qurhCoU92pJZEkmG01lql1OruJx+l+HXQ7d0Zn0Cglf1BEb8aBLIhg11JBV5FUIzutBTAMH7rbhgPTB5wncCoJ6zM3MzAvhBZAiU0Q+KkvFq0w5X6zUZ4oUha08k3INKAVY5PbiGxMKJAHK+EH4h3kn39nihBc=',
    'bm_sz': '53726D57FE20B2DD39A20AE465B6149F~YAAQJBEoFwbuRy6XAQAA0prIWRw1Bb6ehZbcJkX7FyBqALNZX4rYgh/nP6XeoP9xdoDmiFeZHK4RMNVw03eRwgHBucqy9cjq/MyCEAjK/EeYrM8/Jv19PJQ6QxhUz4/+jrX1ikqHZXfVE+xfoPBlRzAAYmu8RvU8M7HZiJ2kaEcKMCMbiqc9D5HJoxEOPdb1V2jZhdUNkSdkYsrnupiMNPy+QaQXgh+IZlpvj1ImOUnBg49pdgwie2j5bzEJMDGHTx1L2TFur09TcidK+0cs/aUng3W+BKIn/2zDOG4pOwKx6rnnH4hBArCpEkpbYgTwnKU17SkFwml+yd/fXInAgyJtNpY84ebShA1E76dR0W8TMMyBrrwx3VJmkdolQ6eTc50oUYpqQvrsTfAPjh99NDg7uj0PVfl8/2tX0NKBcTY3zLrZ7IIa/6270PJAJn32+CuJkbFABYNTQ5h8EbYy+jw0GkZ1leNggHJNi2lLqRqLRb/3ytwlkFM3ypwwFADTn0cY1cB6Vi6KgBYPC1VhL0WhitxO52cyCdidqNIWEaJUogDkGvEvs0u20dnktl91QQFyj1Rayg==~3225911~4343349',
    'RT': '"z=1&dm=www.costco.com&si=7de5692b-975a-426b-bdaf-d23dd44f71da&ss=mbqdwd48&sl=0&tt=0&bcn=%2F%2F173bf10e.akstat.io%2F"',
    '_abck': 'E9B9F3313CF6EB20E6314F1B7FEFBC8D~0~YAAQJBEoFwvuRy6XAQAAwJ7IWQ7wmZf4XxBlwzyKpmRDeSpF2wcUAPZY3+VW1ciehk7K5kZmP/zRt3WJ2mORbhbGjhS7Odo1yaU+6TsOi2TXnnBBNfvPqFUfvwqgi78/ev29zQlPJv4p2nRNijraVJDYIncANo9m+QkZCW5sn3gB7ftved3C5zq1lphEswIo46E4ztbY4dHNQjhXATM+y2Ts7mIBzgGM6yeU3Gyb3qRlaBuxhy8wLz7jg4/F/mrziy1f9NXROS8Kbify+T9/5aGeCkTI52Exlb7eGmOrMHHc0pQ6VrcLr6KN1OWx5zSqpnwT7sEU2iwtN64WPFJ3POjQv7EDsO2o+m8CNCezuODVZX1+hyqS13FldmJ/1HmqPQRRTQ0ZDuOrd0LOUsBDNozgsCBlolGS7QZRR0bao8FZ5XWnlMif686bY8jNncKZmKpyM1/MZjlUiW8L2PIMPxRpLBoFWbixcxqVjByVz/o46fQANy8i6kXR+iYb3KUfCUpUN2LDXa+ynXZcihBlXGvKzE++j49tAYyJX+Px1qgpyuhmcvsn7afFD9iMoTjJdG0k/NYs/blwpowp6t+X/eOuji7Ej2d5bAR3l18Mao6RbztNIZ+GgttTrbDrQFb8DFDJso+j0mlhE9EIH+K6wbf1zlRAe9LrN623D0EXlctL2s1IqHD1NJuifg==~-1~-1~1749558701',
    'kndctr_97B21CFE5329614E0A490D45_AdobeOrg_cluster': 'va6',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Jun+10+2025+17%3A50%3A10+GMT%2B0530+(India+Standard+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=00b5d08e-b6c6-49f9-ab46-ce17a77797c1&interactionCount=1&landingPath=NotLandingPage&groups=BG117%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CSPD_BG%3A1%2CC0004%3A1&AwaitingReconsent=false',
    'ak_bmsc': 'EC50F957ABF2CEB6F820DF7E2A58926A~000000000000000000000000000000~YAAQJBEoF0XuRy6XAQAAaKTIWRyzcFzsaAUaLLJb9dKlbOGcPXj7NhSosru1VdsWIn3NO6dWK1likkqn71Q//OxDrIvBz+dDBHM2GAGcesZVWjlqITaY2QGhAtFTLcyMQfiqzwSh+c8VWqzj9tVwLT2WZ76+41DAsnME8yyjmJEInunlIIi/rVsn09eXMHDWMMDjpoSyVJtDB+dmcu97cWhHvQhv/wT+aqUE92WpnFpGHz58gOA3/rR+YJY+TnszaNd0nqAVsI5DPl2jTl48D6yKSd9Px4iCs5N1Rzi948hXaAJ5tQR2XBrCt3PrE2FGDqHfSGSpRuvNSExG0xiKYffB6aG1zr+S9pN0rjh0dYqNROFA/cl20mdkZrR5n2ejTvnhJWLPQy9FxEVaTPjqPUBOS/59QnKMYnwQz3gsNGGsXtXz4R/HySwdb+cSPxaWRAUFP4anS1jvrtrCTjJjSgG1aWFzzkhfDtIDaVFTr7AyP100UZgta/vJ7A/U+k4BVUxKDVU29+mAOvQCoPohpUZafPbLoB0WqOx2lxa5snoHH4BpD6DKkA9KUYVHT8vlpSpVs1AgRxJ5OGt1eQ0=',
    'JSESSIONID': '0000nbUKzJgmwS3G4YzO6pzgDu2:1g39ofch8',
    'bm_s': 'YAAQJBEoF1PuRy6XAQAAtKbIWQPB0W6njB+niaWjhyIwmMVy9hVUOaecYGygpjpA2CxgXkrjFsekEvOXGV0MzW+TNs0cHxOaSRqZluTI0fy36TPebpgioOsxO0estRG8VZLnbicUu2PWDSfP/figPT9fZD+7puW02B1oJbT/nA2ji2TzW1SUd/IddHPTxNyQJ5ukyAYR/G6/kTTk7ujGNSwNgWd28y9BYZP2w16mWEzlQYAOXKrZ7HmHDxVP4n9ujiNwsM3vAji1Gt/jGekwCiEP3MGasPr9ltg7hGaEjtxva14sjhBtjXdE29aXu1zeEM/4fCaKMmTUFxAP1uErZDK6vUaJe5hUaPeSQ8WYnzyb3jUZinZfL+102z3v7HjKRORm8xUsTFYSNjfqeoXCyMWlDl9kKoWyFPjyEKA/5p6y787/NRPG+97obJAWcLR+FzDpdAMPL5S1vdYQguYZRsIWlFfZItCkULQ6Pp0orgj4l/COaK4BIn30Atkfc9inOiu4PX1qrPg4S3Sv+psEUMGvjdfzXijNo12BwLMzYLVhOCxg5+ZPECfD7FsfY1CjwfxhbVR6u63PZA==',
    'bm_sv': '146AC8F8840CFACDB62A6C6FBF8BD234~YAAQJBEoF1TuRy6XAQAAtKbIWRx+z8JJNfMLLkciWO7u+xE6ENh6o3A6WfIt4zIqJmuF7ylPedF38DbotzCY312N9F5GyLJz1LTet9IgF5K+Y9wjczMUac3KdEmAeE/nvoWf5lQ01F7NBmtLEZLzwDAqAwd84IocvwEylkfayCoAR+DiLOIG+hs3FdSaHRSX5DlnOZm+eEywmpfb6NN9KMNh5ajT+MCW0ljm/XdJVsXEMFBzJ/A0XZcltQ6beVHq~1',
    'mboxEdgeCluster': '34',
    'mbox': 'session%2312432020483548303592136174689590483911%2DWFCsMN%231749559872',
    'cto_bundle': 'R94Xz19JTFZSWmpHSEo4V3AxN3IlMkZMbVNDJTJGRjdOcjNXT3hHN2kzSUp6bWx2SkNBZGpxZUJTaG9jMlI5cVNDN1FWZ3pBUnJRbnBrdVBodnM2VldaVUdpUmtSMVJiOSUyQjQ5QWJLVFhlZjFYQkFSVlVEcGJ0RWhtJTJGQ1c1b013a3clMkJnSzNWRkQzSG1ZYlE5SWd6RXUlMkJLMUhUM0hZV3clM0QlM0Q',
    '_lr_tabs_-costco%2Fproduction-vrwno': '{%22recordingID%22:%226-019759c8-87b3-72b5-82cb-c452689e0e7a%22%2C%22sessionID%22:0%2C%22lastActivity%22:1749558013302%2C%22hasActivity%22:false%2C%22recordingConditionThreshold%22:%2226.87061060358502%22}',
    '_lr_hb_-costco%2Fproduction-vrwno': '{%22heartbeat%22:1749558013303}',
    'akavpau_zezxapz5yf': '1749558315~id=e159556d089cd59b8271f90b027bb85b',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.costco.com/the-cake-bake-shop-8-round-carrot-cake-16-22-servings.product.4000181373.html',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': 'invCheckPostalCode=98101; invCheckStateCode=WA; invCheckCity=Times%20Square; C_WHLOC=USWA; selectedLanguage=-1; akaas_AS01=2147483647~rv=48~id=d9e8dd2fcbef019857c39f6179f898d1; BCO=pm2; WC_SESSION_ESTABLISHED=true; WC_PERSISTENT=PlrjwO2d1WPCtUeoBg6Sn0vIKO9bJC36bOQZj1vJzyQ%3D%3B2025-06-10+01%3A41%3A12.906_1749544834699-1021966_10301_-1002%2C-1%2CUSD%2CvVX5azFQXG11WAi%2BSLU6yk2CV1PkSjrlL%2FWy90A4kqThzRMSgiKcmJKN%2F5ssd1%2BYLglkSRomzGpVY%2FfjIF2aHg%3D%3D_10301; WC_AUTHENTICATION_-1002=-1002%2CtMlGzWl0cXkJgxNmSw2bN88J4PwPTaLQto2HrkgAI8Q%3D; WC_ACTIVEPOINTER=-1%2C10301; WC_USERACTIVITY_-1002=-1002%2C10301%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1898306536%2C7KBFh0dHPSQNvOfR5dt45n6aQd%2FaYnxADpZTJiYebs05SZMQNvvLZVWRyVwuQf%2ByHVQhlKX0eOmagKR%2BsPzbi1aKxh%2BZDucVcI7%2BObdgfsFYmPtcsr8mGA%2Bs050b0y%2B9icB%2B3lK%2FosLzJ9tkAVoftg3S59QkNU2a24GzcVwwGbxNYWIo2%2Bgfw9HRls3Lj%2BTV3XYHJdGcxjVQKYB2nmciieeCp5soOJz15RrhMR01t%2F8Abjgzzbw0l0k7ekCf5v%2Be; WC_GENERIC_ACTIVITYDATA=[45652832112%3Atrue%3Afalse%3A0%3A17ObQdMovfxw31GzeA2zWttzfYZQ5IigeEPvDFj8lvQ%3D][com.ibm.commerce.context.entitlement.EntitlementContext|120577%253B120572%253B120591%253B120563%253B120565%253B120570%253B120571%253B120568%253B120569%253B120757%253B120754%253B120752%253B120758%253B120753%253B120756%253B120755%253B120751%253B120765%253B120926%253B121112%253B120762%253B120763%253B120761%253B120933%253B120920%253B120573%253B120574%253B4000000000000101005%253B60501%253B4000000000000001002%26null%26null%26-2000%26null%26null%26null][com.ibm.commerce.context.audit.AuditContext|1749544834699-1021966][com.ibm.commerce.context.globalization.GlobalizationContext|-1%26USD%26-1%26USD][com.ibm.commerce.store.facade.server.context.StoreGeoCodeContext|null%26null%26null%26null%26null%26null][com.ibm.commerce.context.experiment.ExperimentContext|null][com.ibm.commerce.context.ExternalCartContext|null][com.costco.commerce.member.context.ProfileApiTokenCustomContext|null][com.ibm.commerce.giftcenter.context.GiftCenterContext|null%26null%26null][com.costco.pharmacy.commerce.common.context.PharmacyCustomContext|null%26null%26null%26null%26null%26null][com.ibm.commerce.catalog.businesscontext.CatalogContext|10701%26null%26false%26false%26false][CTXSETNAME|Store][com.ibm.commerce.context.base.BaseContext|10301%26-1002%26-1002%26-1]; STORELOCATION={%22storeLocation%22:{%22city%22:%22Seattle%22%2C%22zip%22:%2298134%22}}; WAREHOUSEDELIVERY_WHS={%22distributionCenters%22:[%221250-3pl%22%2C%221321-wm%22%2C%221456-3pl%22%2C%22283-wm%22%2C%22561-wm%22%2C%22725-wm%22%2C%22731-wm%22%2C%22758-wm%22%2C%22759-wm%22%2C%22847_0-cor%22%2C%22847_0-cwt%22%2C%22847_0-edi%22%2C%22847_0-ehs%22%2C%22847_0-membership%22%2C%22847_0-mpt%22%2C%22847_0-spc%22%2C%22847_0-wm%22%2C%22847_1-cwt%22%2C%22847_1-edi%22%2C%22847_d-fis%22%2C%22847_lg_n1f-edi%22%2C%22847_lux_us01-edi%22%2C%22847_NA-cor%22%2C%22847_NA-pharmacy%22%2C%22847_NA-wm%22%2C%22847_ss_u362-edi%22%2C%22847_wp_r458-edi%22%2C%22951-wm%22%2C%22952-wm%22%2C%229847-wcs%22]%2C%22groceryCenters%22:[%22115-bd%22]%2C%22pickUpCenters%22:[]%2C%22nearestWarehouse%22:{%22catalog%22:%221-wh%22}}; CriteoSessionUserId=567ef4b9ffb44538922465d34fcffddc; kndctr_97B21CFE5329614E0A490D45_AdobeOrg_identity=CiYxMjQzMjAyMDQ4MzU0ODMwMzU5MjEzNjE3NDY4OTU5MDQ4MzkxMVIQCN7_jsn1MhgBKgNWQTYwAfAB3v-OyfUy; AMCV_97B21CFE5329614E0A490D45%40AdobeOrg=MCMID|12432020483548303592136174689590483911; BVBRANDID=e5d02bd4-50a1-47b1-8967-ae58d9d0f8ac; bm_ss=e919a75364; bm_so=0D39B8ADCF8FCA826D318E5A49942BCFDB5C0E40D02FC11FB20774A788D7F1CA~YAAQJBEoF+3tRy6XAQAAuY3IWQOeiRJoeIluAl6NtVIv2sOT0xPhZRVBzViBbyghs2q9zmcy5rv3HJPjHsRQ3zPcJw3kZoz2bzbM7v4rFRbKJ9vLQxsr6TQxm4sJgPq/x4RHd2K8acfuMgY3ISkMnv2GEDdZdJpd36CNfr0b8w9eVcUwuhk3flwToHQ6lXiGsMK0tO4WwqBp1JdTsNhqauKuVP9a+GhHNtjC9oAE9U0hRsahA+5n3PSF4ytlzAQUP7U1cZafLaoseI8uEI7btKspBsc1KvAe9flTF8edA/eS90of6aTvbrUsqC5p8zSJP6WOfWxCIr0RYl1zCINQ1LAD0nb6w0QBP8VyyCDsL+3VtxfhrGGD+Olg6XfuNESK9iiZueJKu8ch4EDUQ3aI+U5drC70hn+Yu305kQCVkvs9lciFmX+cli4+xGiLohFSVaVs+WSa29IMzgM9ibTDLg==; client-zip-short=08601; C_LOC=NJ; bm_lso=0D39B8ADCF8FCA826D318E5A49942BCFDB5C0E40D02FC11FB20774A788D7F1CA~YAAQJBEoF+3tRy6XAQAAuY3IWQOeiRJoeIluAl6NtVIv2sOT0xPhZRVBzViBbyghs2q9zmcy5rv3HJPjHsRQ3zPcJw3kZoz2bzbM7v4rFRbKJ9vLQxsr6TQxm4sJgPq/x4RHd2K8acfuMgY3ISkMnv2GEDdZdJpd36CNfr0b8w9eVcUwuhk3flwToHQ6lXiGsMK0tO4WwqBp1JdTsNhqauKuVP9a+GhHNtjC9oAE9U0hRsahA+5n3PSF4ytlzAQUP7U1cZafLaoseI8uEI7btKspBsc1KvAe9flTF8edA/eS90of6aTvbrUsqC5p8zSJP6WOfWxCIr0RYl1zCINQ1LAD0nb6w0QBP8VyyCDsL+3VtxfhrGGD+Olg6XfuNESK9iiZueJKu8ch4EDUQ3aI+U5drC70hn+Yu305kQCVkvs9lciFmX+cli4+xGiLohFSVaVs+WSa29IMzgM9ibTDLg==^1749558007028; AKA_A2=A; bm_mi=74D9A9E8FC5C20B1568057FA6A3B2193~YAAQJBEoFwLuRy6XAQAA0prIWRwo8526muVjKfBi9OIKOFyW5dI9L7PSWorita/t0+Y5FOtrzWLkuAL5vET2jXmprak+AxHHaFY+d13WxneexJE2LFDc3/aT3IoNi+c5XS7nQMUwZ9PEG0NKKxQXdaYgIot5GwajQvoiEimoYvC+k6nyXSWPxrsYI7g3W8ctUGeTTA7JYGmkxA6laSd+V9obIBMGZTviC6UCRcWza/WlX4xxmb3l4ofBRO0hBh6eYJ50vz7Ag89K9ZUKWsvw6cHEUhFS3EeB9eqePQ8uV0WHbkDqxzB6+wCjs1ZIkxDCXxbHTolGXTwqxAD6QKJQvJDP2LEmYTvyg4yKRp2OE6msg0kUaDfdfquynDtRU8cKZpUwGD+JOw+IjWoN3xpVTe+VD3ecZl76XkRg~1; bm_sc=4~1~2667809~YAAQJBEoFwTuRy6XAQAA0prIWQRifeSReiilBNlvID4MarmQOZ/QD5BP4UM5OExMXRqyaVaegcNKYN8/5FTeQwr6HGXFnuElSHP7HUZ7Ly/LZjTMSgjMdXkBKE2/dgSVbBNOsykM8hpo8EjfL4P4Kdq4Va+T0iaZS9NGFOak87G4HY6eebOd9zBGfHIunryPjCixVaDJFwLF0U9kmUqMd1wjg9i6S/G2/v/HD6JWDKznUQ+clGFwnzLEUc/Yx/VjnIku309lPaUOn+my6+w3LABrP1DRqJ+bl1Gcbm7ANYJBkugPeXjqMO1JzkW/HRCA7aaMX79G9R8ZK06VdCQPd+algHS/Xt9Bpw5g65AupotXXXiVoFicRTayoSLzQCXGTtAdTnKfhCJF2frKD+5iqd/SXFwz5qurhCoU92pJZEkmG01lql1OruJx+l+HXQ7d0Zn0Cglf1BEb8aBLIhg11JBV5FUIzutBTAMH7rbhgPTB5wncCoJ6zM3MzAvhBZAiU0Q+KkvFq0w5X6zUZ4oUha08k3INKAVY5PbiGxMKJAHK+EH4h3kn39nihBc=; bm_sz=53726D57FE20B2DD39A20AE465B6149F~YAAQJBEoFwbuRy6XAQAA0prIWRw1Bb6ehZbcJkX7FyBqALNZX4rYgh/nP6XeoP9xdoDmiFeZHK4RMNVw03eRwgHBucqy9cjq/MyCEAjK/EeYrM8/Jv19PJQ6QxhUz4/+jrX1ikqHZXfVE+xfoPBlRzAAYmu8RvU8M7HZiJ2kaEcKMCMbiqc9D5HJoxEOPdb1V2jZhdUNkSdkYsrnupiMNPy+QaQXgh+IZlpvj1ImOUnBg49pdgwie2j5bzEJMDGHTx1L2TFur09TcidK+0cs/aUng3W+BKIn/2zDOG4pOwKx6rnnH4hBArCpEkpbYgTwnKU17SkFwml+yd/fXInAgyJtNpY84ebShA1E76dR0W8TMMyBrrwx3VJmkdolQ6eTc50oUYpqQvrsTfAPjh99NDg7uj0PVfl8/2tX0NKBcTY3zLrZ7IIa/6270PJAJn32+CuJkbFABYNTQ5h8EbYy+jw0GkZ1leNggHJNi2lLqRqLRb/3ytwlkFM3ypwwFADTn0cY1cB6Vi6KgBYPC1VhL0WhitxO52cyCdidqNIWEaJUogDkGvEvs0u20dnktl91QQFyj1Rayg==~3225911~4343349; RT="z=1&dm=www.costco.com&si=7de5692b-975a-426b-bdaf-d23dd44f71da&ss=mbqdwd48&sl=0&tt=0&bcn=%2F%2F173bf10e.akstat.io%2F"; _abck=E9B9F3313CF6EB20E6314F1B7FEFBC8D~0~YAAQJBEoFwvuRy6XAQAAwJ7IWQ7wmZf4XxBlwzyKpmRDeSpF2wcUAPZY3+VW1ciehk7K5kZmP/zRt3WJ2mORbhbGjhS7Odo1yaU+6TsOi2TXnnBBNfvPqFUfvwqgi78/ev29zQlPJv4p2nRNijraVJDYIncANo9m+QkZCW5sn3gB7ftved3C5zq1lphEswIo46E4ztbY4dHNQjhXATM+y2Ts7mIBzgGM6yeU3Gyb3qRlaBuxhy8wLz7jg4/F/mrziy1f9NXROS8Kbify+T9/5aGeCkTI52Exlb7eGmOrMHHc0pQ6VrcLr6KN1OWx5zSqpnwT7sEU2iwtN64WPFJ3POjQv7EDsO2o+m8CNCezuODVZX1+hyqS13FldmJ/1HmqPQRRTQ0ZDuOrd0LOUsBDNozgsCBlolGS7QZRR0bao8FZ5XWnlMif686bY8jNncKZmKpyM1/MZjlUiW8L2PIMPxRpLBoFWbixcxqVjByVz/o46fQANy8i6kXR+iYb3KUfCUpUN2LDXa+ynXZcihBlXGvKzE++j49tAYyJX+Px1qgpyuhmcvsn7afFD9iMoTjJdG0k/NYs/blwpowp6t+X/eOuji7Ej2d5bAR3l18Mao6RbztNIZ+GgttTrbDrQFb8DFDJso+j0mlhE9EIH+K6wbf1zlRAe9LrN623D0EXlctL2s1IqHD1NJuifg==~-1~-1~1749558701; kndctr_97B21CFE5329614E0A490D45_AdobeOrg_cluster=va6; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Jun+10+2025+17%3A50%3A10+GMT%2B0530+(India+Standard+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=00b5d08e-b6c6-49f9-ab46-ce17a77797c1&interactionCount=1&landingPath=NotLandingPage&groups=BG117%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1%2CSPD_BG%3A1%2CC0004%3A1&AwaitingReconsent=false; ak_bmsc=EC50F957ABF2CEB6F820DF7E2A58926A~000000000000000000000000000000~YAAQJBEoF0XuRy6XAQAAaKTIWRyzcFzsaAUaLLJb9dKlbOGcPXj7NhSosru1VdsWIn3NO6dWK1likkqn71Q//OxDrIvBz+dDBHM2GAGcesZVWjlqITaY2QGhAtFTLcyMQfiqzwSh+c8VWqzj9tVwLT2WZ76+41DAsnME8yyjmJEInunlIIi/rVsn09eXMHDWMMDjpoSyVJtDB+dmcu97cWhHvQhv/wT+aqUE92WpnFpGHz58gOA3/rR+YJY+TnszaNd0nqAVsI5DPl2jTl48D6yKSd9Px4iCs5N1Rzi948hXaAJ5tQR2XBrCt3PrE2FGDqHfSGSpRuvNSExG0xiKYffB6aG1zr+S9pN0rjh0dYqNROFA/cl20mdkZrR5n2ejTvnhJWLPQy9FxEVaTPjqPUBOS/59QnKMYnwQz3gsNGGsXtXz4R/HySwdb+cSPxaWRAUFP4anS1jvrtrCTjJjSgG1aWFzzkhfDtIDaVFTr7AyP100UZgta/vJ7A/U+k4BVUxKDVU29+mAOvQCoPohpUZafPbLoB0WqOx2lxa5snoHH4BpD6DKkA9KUYVHT8vlpSpVs1AgRxJ5OGt1eQ0=; JSESSIONID=0000nbUKzJgmwS3G4YzO6pzgDu2:1g39ofch8; bm_s=YAAQJBEoF1PuRy6XAQAAtKbIWQPB0W6njB+niaWjhyIwmMVy9hVUOaecYGygpjpA2CxgXkrjFsekEvOXGV0MzW+TNs0cHxOaSRqZluTI0fy36TPebpgioOsxO0estRG8VZLnbicUu2PWDSfP/figPT9fZD+7puW02B1oJbT/nA2ji2TzW1SUd/IddHPTxNyQJ5ukyAYR/G6/kTTk7ujGNSwNgWd28y9BYZP2w16mWEzlQYAOXKrZ7HmHDxVP4n9ujiNwsM3vAji1Gt/jGekwCiEP3MGasPr9ltg7hGaEjtxva14sjhBtjXdE29aXu1zeEM/4fCaKMmTUFxAP1uErZDK6vUaJe5hUaPeSQ8WYnzyb3jUZinZfL+102z3v7HjKRORm8xUsTFYSNjfqeoXCyMWlDl9kKoWyFPjyEKA/5p6y787/NRPG+97obJAWcLR+FzDpdAMPL5S1vdYQguYZRsIWlFfZItCkULQ6Pp0orgj4l/COaK4BIn30Atkfc9inOiu4PX1qrPg4S3Sv+psEUMGvjdfzXijNo12BwLMzYLVhOCxg5+ZPECfD7FsfY1CjwfxhbVR6u63PZA==; bm_sv=146AC8F8840CFACDB62A6C6FBF8BD234~YAAQJBEoF1TuRy6XAQAAtKbIWRx+z8JJNfMLLkciWO7u+xE6ENh6o3A6WfIt4zIqJmuF7ylPedF38DbotzCY312N9F5GyLJz1LTet9IgF5K+Y9wjczMUac3KdEmAeE/nvoWf5lQ01F7NBmtLEZLzwDAqAwd84IocvwEylkfayCoAR+DiLOIG+hs3FdSaHRSX5DlnOZm+eEywmpfb6NN9KMNh5ajT+MCW0ljm/XdJVsXEMFBzJ/A0XZcltQ6beVHq~1; mboxEdgeCluster=34; mbox=session%2312432020483548303592136174689590483911%2DWFCsMN%231749559872; cto_bundle=R94Xz19JTFZSWmpHSEo4V3AxN3IlMkZMbVNDJTJGRjdOcjNXT3hHN2kzSUp6bWx2SkNBZGpxZUJTaG9jMlI5cVNDN1FWZ3pBUnJRbnBrdVBodnM2VldaVUdpUmtSMVJiOSUyQjQ5QWJLVFhlZjFYQkFSVlVEcGJ0RWhtJTJGQ1c1b013a3clMkJnSzNWRkQzSG1ZYlE5SWd6RXUlMkJLMUhUM0hZV3clM0QlM0Q; _lr_tabs_-costco%2Fproduction-vrwno={%22recordingID%22:%226-019759c8-87b3-72b5-82cb-c452689e0e7a%22%2C%22sessionID%22:0%2C%22lastActivity%22:1749558013302%2C%22hasActivity%22:false%2C%22recordingConditionThreshold%22:%2226.87061060358502%22}; _lr_hb_-costco%2Fproduction-vrwno={%22heartbeat%22:1749558013303}; akavpau_zezxapz5yf=1749558315~id=e159556d089cd59b8271f90b027bb85b',
}

def pagesave_portion(join_path, fetch_Product_URL):
    try:
        attempts = 0
        max_attempts = 3
        my_selector = ''

        while attempts < max_attempts and not my_selector:
            try:
                # scrape_do_token = "f42a5b59aec3467e97a8794c611c436b91589634343"
                # scrap_do_url = f"https://api.scrape.do?token={scrape_do_token}&url={urllib.parse.quote(fetch_Product_URL)}&customHeaders=TRUE&super=True"
                response = requests.get(url=fetch_Product_URL,headers=headers,cookies=cookies)
                # response = requests.get(url=scrap_do_url)
                print(response.status_code)
                # response = requests.get(url=fetch_Product_URL, headers=headers)

                if response.status_code == 200 and 'automation-id="productName"' in response.text:
                    try:
                        with open(join_path, "w", encoding="utf-8") as file:
                            file.write(response.text)
                        my_selector = response.text
                    except Exception as e:
                        print(f"File write error: {e}")

                if response.status_code == 404:
                    try:
                        with open(join_path, "w", encoding="utf-8") as file:
                            file.write(response.text)
                        my_selector = response.text
                    except Exception as e:
                        print(f"File write error: {e}")

                    # Create a new MongoDB client for this thread
                    client = pymongo.MongoClient(MONGO_URI)
                    db = client[DB_NAME]
                    collection_ip = db[COLLECTION_INPUT]

                    # TODO::updating portion
                    try:
                        collection_ip.update_one({"url": fetch_Product_URL}, {"$set": {"status": "Not Found"}})
                        print("input status update as Not Found")
                        max_attempts = 3
                        my_selector = ''
                    except Exception as e:
                        print(e)

                    client.close()
            except Exception as e:
                print(f"Request error: {e}")
            attempts += 1
            if not my_selector:
                time.sleep(2)
        return my_selector
    except Exception as e:
        return ""

def process_task(fetch_Product_URL):
    fetch_Product_ID = fetch_Product_URL.split(".product.")[-1].split(".html")[0]
    page_name = f"{fetch_Product_ID}.html"
    join_path = PAGESAVE_PATH / page_name

    if os.path.exists(join_path):
        my_selector = open(join_path, "r", encoding="utf-8").read()
    else:
        my_selector = pagesave_portion(join_path, fetch_Product_URL)

    if my_selector:
        # TODO::Contain selector
        my_common_selector = Selector(text=my_selector)
        """
        url
product_id
product_name
brand
images
ingredients
nutritional_data
store_id
price
location
Description
        """

        item = {}

        # TODO:: Product Url // Product ID
        item['url'] = fetch_Product_URL
        item['product_id'] = fetch_Product_ID

        # TODO:: Product Name
        try:
            product_Name_check = my_common_selector.xpath('//h1[@itemprop="name"]/text()').get()
            product_Name = product_Name_check.strip() if product_Name_check else ""
            item['product_name'] = product_Name
        except:
            ...

        # TODO:: Brand Name
        try:
            Product_Brand_check = my_common_selector.xpath('//div[@class="product-info-specs body-copy"]//div[contains(text(),"Brand")]/following-sibling::*/text()').get()
            Product_Brand = Product_Brand_check.strip() if Product_Brand_check else ""
            item['brand'] = Product_Brand
        except:
            ...

        #TODO:: images
        try:
            images_check = my_common_selector.xpath("//script[contains(text(), 'cdn_url')]/text()").get()
            if images_check:
                # Regex pattern to match cdn_url values
                pattern = r"cdn_url\s*:\s*'([^']+)'"
                images_check = re.findall(pattern, images_check)
            if not images_check:
                images_check = my_common_selector.xpath('//img[@class="thumbnail-image MuiBox-root css-14fu01j"]/@src').getall()
                if not images_check:
                    images_check = my_common_selector.xpath('//div[@data-testid="Clickzoom_image_container"]/img/@src').get()
                    if not images_check:
                        images_check = my_common_selector.xpath('//div[@id="productImageOverlay"]/img/@src').get()
            images = images_check if images_check else ""
            item["images"] = images
        except:...

        #TODO:: ingredients
        try:
            text_nodes = my_common_selector.xpath("//div[@class='nutrition-facts-row other-ingredients']//span//text()").getall()
            ingredients = ' '.join(t.strip() for t in text_nodes if t.strip())
            item["ingredients"] = ingredients
        except:...

        #TODO:: nutritional_data
        try:
            nutrition_dict = {}
            # Check if serving info section exists and extract data
            serving_info = my_common_selector.xpath(
                '//div[contains(@class, "serving-info") and contains(@class, "nutrition-subsection")]')
            if serving_info:
                # Extract serving size and servings per container
                serving_size = serving_info.xpath('.//h4[contains(text(), "Serving Size:")]/span/text()').get()
                servings_per_container = serving_info.xpath(
                    './/h4[contains(text(), "Servings per Container:")]/span/text()').get()

                if serving_size:
                    nutrition_dict['Serving Size'] = serving_size.strip()
                if servings_per_container:
                    nutrition_dict['Servings per Container'] = servings_per_container.strip()

            # Extract nutrition values from the table
            nutrition_rows = my_common_selector.xpath('//tr[contains(@class, "aps-label-row")]')
            for row in nutrition_rows:
                # Get the nutrient name (remove colon if present)
                nutrient = row.xpath('.//td[1]/text()').get('').strip().rstrip(':')

                # Get the amount value
                amount = row.xpath('.//td[1]/span[contains(@class, "no-bold")]/text()').getall()
                # Get the daily value percentage
                daily_value = row.xpath(
                    './/td[contains(@class, "right-column")]//span[contains(@class, "no-bold")]/text()').get('')

                if nutrient:
                    nutrition_dict[nutrient] = {
                        'amount': ' '.join(x.strip() for x in amount if x.strip()),
                        'daily_value': daily_value.strip() if daily_value else 'Not specified'
                    }

            nutrition = nutrition_dict if nutrition_dict else ""
            item["nutritional_data"] = nutrition
        except:...

        #TODO:: Store_id
        try:
            Store_id_check = my_common_selector.xpath('//*[@name="storeId"]//@value').get()
            Store_id = Store_id_check.strip() if Store_id_check else ""
            item['store_id'] = Store_id
        except:...

        #TODO:: price
        try:
            price_check = my_common_selector.xpath("//script[contains(text(), 'priceTotal: initialize(')]/text()").re_first(r"priceTotal\s*:\s*initialize\(([\d.]+)\)")
            if not price_check:
                price_check = my_common_selector.xpath("//script[contains(text(), 'priceMax')]/text()").re_first(r"priceMax\s*:\s*'([^']+)'")
            # price_check = my_common_selector.xpath('//span[@automation-id="productPriceOutput"]/text()').get()
            price = price_check.strip() if price_check else ""
            item['price'] = price
        except:...

        #TODO:: location
        try:
            location_check1 = my_common_selector.xpath('//span[@id="notfound_deliveryWarehouse"]//text()').get()
            location_check2 = my_common_selector.xpath('//span[@id="notfound_deliveryLocation"]//text()').get()
            location = f"{location_check1.strip()},{location_check2.strip()}" if location_check1 and location_check2 else ""
            item['location'] = location
        except:...

        #TODO:: Description
        try:
            # Description_check = my_common_selector.xpath('//div[@class="product-info-description"]//span[@id="productDescriptions1"]//text()').getall()
            Description_check = my_common_selector.xpath('//span[@id="productDescriptions1"]/ul/li/text()').getall()
            allergens = my_common_selector.xpath('//span[@id="productDescriptions1"]/span/text()').getall()

            # Join main description
            Description = ", ".join(Description_check) if Description_check else ""

            # Check if any allergen info is present and contains 'may contain'
            for allergen in allergens:
                if 'may contain' in allergen.lower():
                    Description += f", {allergen.strip()}"
                    break  # optional: break if you only want to add the first match

            item['Description'] = Description
        except:...
        #weight
        try:
            weight = my_common_selector.xpath("//div[text()[normalize-space()='Package Net Weight']]/following-sibling::div[1]/text()").get()
            if weight:
                weight = weight.strip()
            else:
                weight = "N/A"
            item['net_weight'] = weight
        except:...
        #calories
        try:
            calories = 'N/A'
            if isinstance(nutrition, dict):
                calories = nutrition.get('Calories', {}).get('amount', 'N/A')
            item['calories'] = calories

        except:...

        #package size 
        try:
            pattern = r'(?:(\d+)[-–—]count|(\d+)-pack|(\d+)-ct|(\d+)-piece|(\d+)-servings|(\d+)-cake|(\d+)-cookies|(\d+)-bites|(\d+)-balls|(\d+)-total|(\d+)---count|(\d+)-per-cake|(\d+)-lbs|(\d+)-oz|(\d+)-in|(\d+)-lb)'
            pack_size = 'N/A'
            match = re.search(pattern, fetch_Product_URL)
            if match:
                # Extract the first non-None group
                pack_size = next((g for g in match.groups() if g is not None), None)
                
            item['pack_size'] = pack_size
        except:...

        #allergens
        try:
            item['allergens'] = "N/A"
        except:...
        #TODO:: hashlib
        unique_string = f"{fetch_Product_ID}-{product_Name_check}-{fetch_Product_URL}"
        hashed_id = hashlib.sha256(unique_string.encode()).hexdigest()
        item['_id'] = hashed_id
        #
        # Create a new MongoDB client for this thread
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection_op = db[COLLECTION_OUTPUT]
        collection_ip = db[COLLECTION_INPUT]


        #TODO:: Insert the item
        try:
            collection_op.insert_one(item)
            print("Item inserted successfully!")
        except Exception as e:
            print(f"Error: {e}")
        #
        # # TODO::updating portion
        # try:
        #     collection_ip.update_one({"url": fetch_Product_URL}, {"$set": {"status": "Done"}})
        #     print("input status update sucessfully")
        # except Exception as e:
        #     print(e)
        #
        client.close()
#


MAX_THREADS = 10
def main():
    # client = pymongo.MongoClient(MONGO_URI)
    # db = client[DB_NAME]
    # collection_ip = db[COLLECTION_INPUT]
    # pending_tasks = list(collection_ip.find({"status": "Pending"}))
    # # pending_tasks = list(collection_ip.find({"Status": "Pending", "ID":6}))
    #
    # if not pending_tasks:
    #     print("No pending tasks found.")
    #     return
    urls = [
    "https://www.costco.com/the-cake-bake-shop-8-round-carrot-cake-16-22-servings.product.4000181373.html",
    "https://www.costco.com/collin-street-bakery-mini-pecan-cake-bundle-9-oz-per-cake.product.4000275908.html",
    "https://www.costco.com/davids-cookies-mile-high-peanut-butter-cake-68-lbs-14-servings.product.100338715.html",
    "https://www.costco.com/st-michel-madeleine-classic-french-sponge-cake-100---count.product.100517831.html",
    "https://www.costco.com/davids-cookies-mango--strawberry-cheesecake-2-count-28-slices-total.product.100496548.html",
    "https://www.costco.com/austin-cake-ball-catering-assortment-48-cake-balls.product.4000035726.html",
    "https://www.costco.com/davids-cookies-no-sugar-added-cheesecake--marble-truffle-cake-2-pack-28-slices-total.product.100494269.html",
    "https://www.costco.com/davids-cookies-premier-chocolate-cake-72-lbs-serves-14.product.100338718.html",
    "https://www.costco.com/davids-cookies-chocolate-fudge-birthday-cake-375-lbs--includes-party-pack-16-servings.product.100431056.html",
    "https://www.costco.com/collin-street-bakery-cake-bites-bundle-deluxe-fruitcake--pineapple-pecan-cake-2-pack-24-bites-total.product.4000284537.html",
    "https://www.costco.com/mary-macleods-gluten-free-shortbread-cookies-mixed-assortment-8-pack.product.100799668.html",
    "https://www.costco.com/ferraras-bakery-new-york-cheesecake-2-pack.product.100760705.html",
    "https://www.costco.com/the-cake-bake-shop-8-round-pixie-fetti-cake-16-22-servings.product.4000181454.html",
    "https://www.costco.com/mary-macleods-shortbread-variety-tin-3-pack-24-cookies-per-tin.product.4000159297.html",
    "https://www.costco.com/ferraras-bakery-8-in-tiramisu-cake-2-pack.product.4000233634.html",
    "https://www.costco.com/the-cake-bake-shop-8-round-chocolate-cake-16-22-servings.product.4000181494.html",
    "https://www.costco.com/davids-cookies-10-rainbow-cake--12-servings.product.100498608.html",
    "https://www.costco.com/davids-cookies-variety-cheesecakes-2-pack-28-slices-total.product.100158259.html",
    "https://www.costco.com/davids-cookies-brownie-and-cookie-combo-pack.product.100130229.html",
    "https://www.costco.com/davids-cookies-90-piece-gourmet-chocolate-chunk-frozen-cookie-dough.product.100651546.html",
    "https://www.costco.com/collin-street-bakery-cinnamon-coffee-cake-379-lb.product.4000275903.html",
    "https://www.costco.com/davids-cookies-butter-pecan-meltaways-3-pack-6-lb-total.product.4000315234.html",
    "https://www.costco.com/hostess-cupcakes--twinkies-32-count.product.4000153042.html",
    "https://www.costco.com/la-grande-galette-french-butter-cookies-13-lb-6-pack.product.100302567.html"
]
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for task in urls:
            url = task
            future = executor.submit(process_task, url)
            futures.append(future)

        for future in as_completed(futures):
            try:
                future.result()  # If process_task returns something or raises errors
            except Exception as e:
                print(f"Error processing task: {e}")

    print("All tasks completed.")


if __name__ == "__main__":
    main()
