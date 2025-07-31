# url='https://www.meesho.com/search?q=mobile&searchType=manual&searchIdentifier=text_search'

import requests
import json

cookies = {
    'ORDER_BLOCK_EXPERIMENT_COOKIE': '0.27',
    'ANONYMOUS_USER_CONFIG': 'j%3A%7B%22clientId%22%3A%22547fe4d6-4e5f-4ea6-9e29-012dc7d8%22%2C%22instanceId%22%3A%22547fe4d6-4e5f-4ea6-9e29-012dc7d8%22%2C%22xo%22%3A%22eyJ0eXBlIjoiY29tcG9zaXRlIn0%3D.eyJqd3QiOiJleUpvZEhSd2N6b3ZMMjFsWlhOb2J5NWpiMjB2ZG1WeWMybHZiaUk2SWpFaUxDSm9kSFJ3Y3pvdkwyMWxaWE5vYnk1amIyMHZhWE52WDJOdmRXNTBjbmxmWTI5a1pTSTZJa2xPSWl3aVlXeG5Jam9pU0ZNeU5UWWlmUS5leUpwWVhRaU9qRTNORGt4TURjNU5ERXNJbVY0Y0NJNk1Ua3dOamM0TnprME1Td2lhSFIwY0hNNkx5OXRaV1Z6YUc4dVkyOXRMMmx1YzNSaGJtTmxYMmxrSWpvaU5UUTNabVUwWkRZdE5HVTFaaTAwWldFMkxUbGxNamt0TURFeVpHTTNaRGdpTENKb2RIUndjem92TDIxbFpYTm9ieTVqYjIwdllXNXZibmx0YjNWelgzVnpaWEpmYVdRaU9pSTBaREF3T0daa05pMWlZekJtTFRRelpHRXRZV1l4TnkxaVpqazVNakZtWTJWbU16SWlmUS42Mkdqc3dSeWU2bmh4emcxeldvZENFOEdtZFFFVG4wOUFlVkdMVTAxbzY0IiwieG8iOm51bGx9%22%2C%22createdAt%22%3A%222025-06-05T07%3A19%3A01.197Z%22%7D',
    'bm_ss': 'ab8e18ef4e',
    '_gcl_au': '1.1.694162653.1749107923',
    '_ga': 'GA1.1.1860454926.1749107923',
    'bm_s': 'YAAQT63OF8+2GjiXAQAA0aj2PgOoQ26SyKj8IdO0SK21KNYyxFjkTZSzQZ6xsU+8mERxNyQDfk1IZO26QXThfxSub6gJq3braU+kBHKSYp5eHT6U3jatC92BfhfTWIMh4zMujZq55eLK8Fw28AWCs8Y4L+20HZ9dv3nevfjsnHP5lF3hEsUuGiX31Tz5OgvD0iyTlII0q4n56elVltic1YAfkj5YOKD11VlCW3Q+IF41Aw4v2VNzUDDMs+UoNBTAORuu2JFQwd1xeUG5srnrtEG2L1ZDYJ9NQ9c3PoDtor0nkJ8V2Wy5yvi861dai+nS8D2tHmisNXOJU7ZasBHv5RyMEGP0bEasVJPE5phLuiDfqhTWcahHtoasWNS2S5LylWetXmpSxflPQM4Sx8q/WkKqcbiW0kte/Ex+vFrxdcFJEyiH4hLo5nTuiFB1WVbiL8OJnqR3qQdqAMDL5tE2iA+Hwuk3DIfk22wlxwcdf+VrEOxVTtOkjbDW+Crl8um0jNl2PcgmSi1HOv1dou4XG3l2pJz0IeKsi2XplGeEUuC07QxR1a4l',
    'bm_mi': '3CEEC8BC6C9AAFA9B44AE375A8FAEFF8~YAAQFq3OFyPnNDqXAQAAEpr3PhzU+6K2zBWs8F2s5CZkFZn6ZVcVQS/VmhJIuoe1bbGqLz4gW1QaOEc4QrzeZhanVL26RHNHmtYwhm70tyd5ap8GfJ5bRMELiUrGnOJlHKpmAOUjwZDUwVqJdyVBbmBq/iDS3icZ0N5nz09y869FgiubJ/Tp9e7vpq0BDnXXV9p9V8EjZxJ07Ywd6/QNItasf9JfAoT7nfmw67Y0FAoV19UKncYd0v112uO6YpfjHcgIoYDjKxA4yBhgM3y0kGRvttOSUE37mXSTHkS3FGz/pw14lemNJegEM+c2ahKfJXvT~1',
    'bm_sv': 'C76CFDAC34961EDA25DD2DEDD549562A~YAAQFq3OFyTnNDqXAQAAEpr3PhwyZE/wo+pzGiab+aP4/fHnwnXY20x0/HDSr+GgkYmokZxti6TJ34kkflL7vOOyOvfSFtZonCfMP7XoF2AdkbbkUDh4Mfupen+D2lyloqMGkew5LKqZhOX+P80i//ogNuLTnF0NHQW4yNkxtJdxt2OfjplPH90udmSz/Bc8LNc0fCwU0mfavbqUdxZElO2DusCJZ/EPDUWGTsEQU4bYYpTF1iT42DswOljSBe0+dg==~1',
    'bm_sz': '2B2A74E00B49016B88C387DC3DF54839~YAAQFq3OFyXnNDqXAQAAEpr3PhwMsUBIfUFnOz5JGDl5xOwi1s2I3MAq7VJpYMqJtoRNmfs0ODgjpx+lqCs5tlFsHq470oQghAFy5r6ZTtneE2Mau2IwZG16VoGXQimCTw/SU2PeSmfUbvSRqsMJ/xj6GkUlR7TICsxl4k0lQAs4hcmsntrzU9SqGhjjo1eEiZ4+mHBa7QT7RbzIBtmWNLe4PwoFT+W2kHAsaSLyIjAWV9pRiqC2w5ipyfQfLjW/zMOphaInJOkt8t6KdKoNaG5K822OiRQeBF3laWas9iP44ltVsTAD87R+hSoUvhaNzRJtgUdGm2ovsBpgsIoSJ9VG4pKtB2YP7YSgCudXdlmVCrIZDp3bSt3b+6f0Lwpx5k+muCmiaZW5CHIet7Y1vjqwXMaZLZQEKic403xYQCWZqo2mNnOxN3eVBwMpNUnKZkM=~4600132~3162438',
    '_ga_NEH2MEG9CT': 'GS2.1.s1749107923$o1$g1$t1749108075$j60$l0$h0',
    'ak_bmsc': '1C0F2247C74A0696B2D621B48121F3F6~000000000000000000000000000000~YAAQLa3OFzyc7i6XAQAAF5z3PhygOVUYZqb63dnSi8V/xsl6Q2X1WW/7RSyAPSuGkenwJhd+GguoiOrji6HuvUp+kzqVxz7Rzg9A1zaHUr6e1JotMeWsTo8oQhXedO9a+NY0XGx4lUHQcimBs/oM8kiKvhjrB211zni0LPFxkCY+gKS9Hb8Iu8mzjIzHh5njh6O0mvxkpupEjKaaAR/RS2gbcipIvuhkd+5BCAs9i6ZzuTc84g7xB0L9EcSTAlnTqgwAyfBCI2N3gcNc9l+luV70by6jk8Tw23dYn92ZxWI2GgeRRfceMasxHcRUHHDY7inoJB7qrJidv2FcputrhBABwcl5l4ujVJ5SjO9m8x26eMRziO8SH/AVRc5RTGHF6Uq8aUWvDblo7EFHyGA5EXV6mAOHqTnPbL72lhgQfvZVSYSF/EiSejzWkEBdcY20IkC5Crxcon/VOoNL+QpoQxM=',
    'mp_60483c180bee99d71ee5c084d7bb9d20_mixpanel': '%7B%22distinct_id%22%3A%20%221973ef4c6ec1d4-0e5d7abb16f6e8-26011e51-100200-1973ef4c6ed136%22%2C%22%24device_id%22%3A%20%221973ef4c6ec1d4-0e5d7abb16f6e8-26011e51-100200-1973ef4c6ed136%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22%24user_id%22%3A%20%221973ef4c6ec1d4-0e5d7abb16f6e8-26011e51-100200-1973ef4c6ed136%22%2C%22Is%20Anonymous%22%3A%20%22True%22%2C%22Instance_Id%22%3A%20%22547fe4d6-4e5f-4ea6-9e29-012dc7d8%22%2C%22Session%20ID%22%3A%20%22037a57ce-178d-4e55-92a3-4fd17b5e%22%2C%22last%20event%20time%22%3A%201749108052935%7D',
    '_abck': 'CD2BD69AD7342E6124BFBEF0C63ADA1A~-1~YAAQLa3OFxed7i6XAQAAkq73Pg45Oh6kCz/0q/WnBXtEhKSHG520l25EDaECID7P+lhAEyBChWcTk8/A2ksd9D7UTovQRDRoDpFuoJc+XtclZEDcCiu9AISxC0VTrlpdIW0SQ9/7zr5QjO3eN5NB5OUcnSRZMQ6a6ci6XBPIIlhXaR5zMwu06PjGDoh7IkYFcMG2GVdnCiPCmfmFMZiCsjMj9almDIeeLYpcVTI45TiqbMve8b7ks6D5ppw/XAVLPdEU8iR3yV8JCI7kf5DhdKPj/IkscJmIQPklX4xffGqZ4Ruqqguhp2jzAg45i1KZsrqLJG+PYPXlCG9SYsER+KgjjxiuNAb4LJ9pSQJUz99nb8WGFXO+XW6jNVQ/1NHkrApMxv49CFcfbjhsU28DgyPbusttYGGJ0FflWyFgpmZ1kfVrmgfFprh5EdNoBItxL7NTy5csBdk7ekh9dXJU6x1lK+9wRHjYpi4h2nZz3IswuSvGMpjk9oaNw2F5Puyd6/tl7/Vk1+Dy+jOXO6/PWTkGT8cshNpIZRIolHd7QLMp05KocdWviv7vKPJ+b/tUD9+5WfRRvA1YZ/90mUklalDs0qYoJubRmRCjaQnc+GBnvpD+AElWSu+2RAjqf0WxZL0vUNZlWc5fLuNPrMx9BKMCdMFgPur/ZFsZMDULUNO3ybU7UvJipgkkMLB9sOIVm16OiH2mBu3Ln436HV2x0FNzKoELKKsJGzNxqIN+Q8I8vRvBIjOqA+6vPmKLcLoT9cQ+WALG5oDuJCEr1C2i6KyF08oRwn/Ae6JSyHXmrFBtKusW+N9Mr0DXgesiOUTFAeaBm5sEmDmo67JxeDZ0C8y0y6ofWKmH4HNemjs46uvl+SEHxxDHp7IOznWXlyUYGlgrQlMuEvm8ez3FTzgRjICEnhEMSDCbi3mdf7is84zYP9OKOyGLRQtanIXYPoBbl3cC1Hz34r0iGGwqbJipZWuW8N6KmWFF18YphaW6u83LmFny~-1~||0||~1749111546',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'meesho-iso-country-code': 'IN',
    'origin': 'https://www.meesho.com',
    'priority': 'u=1, i',
    'referer': 'https://www.meesho.com/search?q=mobile&searchType=manual&searchIdentifier=text_search',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': 'ORDER_BLOCK_EXPERIMENT_COOKIE=0.27; ANONYMOUS_USER_CONFIG=j%3A%7B%22clientId%22%3A%22547fe4d6-4e5f-4ea6-9e29-012dc7d8%22%2C%22instanceId%22%3A%22547fe4d6-4e5f-4ea6-9e29-012dc7d8%22%2C%22xo%22%3A%22eyJ0eXBlIjoiY29tcG9zaXRlIn0%3D.eyJqd3QiOiJleUpvZEhSd2N6b3ZMMjFsWlhOb2J5NWpiMjB2ZG1WeWMybHZiaUk2SWpFaUxDSm9kSFJ3Y3pvdkwyMWxaWE5vYnk1amIyMHZhWE52WDJOdmRXNTBjbmxmWTI5a1pTSTZJa2xPSWl3aVlXeG5Jam9pU0ZNeU5UWWlmUS5leUpwWVhRaU9qRTNORGt4TURjNU5ERXNJbVY0Y0NJNk1Ua3dOamM0TnprME1Td2lhSFIwY0hNNkx5OXRaV1Z6YUc4dVkyOXRMMmx1YzNSaGJtTmxYMmxrSWpvaU5UUTNabVUwWkRZdE5HVTFaaTAwWldFMkxUbGxNamt0TURFeVpHTTNaRGdpTENKb2RIUndjem92TDIxbFpYTm9ieTVqYjIwdllXNXZibmx0YjNWelgzVnpaWEpmYVdRaU9pSTBaREF3T0daa05pMWlZekJtTFRRelpHRXRZV1l4TnkxaVpqazVNakZtWTJWbU16SWlmUS42Mkdqc3dSeWU2bmh4emcxeldvZENFOEdtZFFFVG4wOUFlVkdMVTAxbzY0IiwieG8iOm51bGx9%22%2C%22createdAt%22%3A%222025-06-05T07%3A19%3A01.197Z%22%7D; bm_ss=ab8e18ef4e; _gcl_au=1.1.694162653.1749107923; _ga=GA1.1.1860454926.1749107923; bm_s=YAAQT63OF8+2GjiXAQAA0aj2PgOoQ26SyKj8IdO0SK21KNYyxFjkTZSzQZ6xsU+8mERxNyQDfk1IZO26QXThfxSub6gJq3braU+kBHKSYp5eHT6U3jatC92BfhfTWIMh4zMujZq55eLK8Fw28AWCs8Y4L+20HZ9dv3nevfjsnHP5lF3hEsUuGiX31Tz5OgvD0iyTlII0q4n56elVltic1YAfkj5YOKD11VlCW3Q+IF41Aw4v2VNzUDDMs+UoNBTAORuu2JFQwd1xeUG5srnrtEG2L1ZDYJ9NQ9c3PoDtor0nkJ8V2Wy5yvi861dai+nS8D2tHmisNXOJU7ZasBHv5RyMEGP0bEasVJPE5phLuiDfqhTWcahHtoasWNS2S5LylWetXmpSxflPQM4Sx8q/WkKqcbiW0kte/Ex+vFrxdcFJEyiH4hLo5nTuiFB1WVbiL8OJnqR3qQdqAMDL5tE2iA+Hwuk3DIfk22wlxwcdf+VrEOxVTtOkjbDW+Crl8um0jNl2PcgmSi1HOv1dou4XG3l2pJz0IeKsi2XplGeEUuC07QxR1a4l; bm_mi=3CEEC8BC6C9AAFA9B44AE375A8FAEFF8~YAAQFq3OFyPnNDqXAQAAEpr3PhzU+6K2zBWs8F2s5CZkFZn6ZVcVQS/VmhJIuoe1bbGqLz4gW1QaOEc4QrzeZhanVL26RHNHmtYwhm70tyd5ap8GfJ5bRMELiUrGnOJlHKpmAOUjwZDUwVqJdyVBbmBq/iDS3icZ0N5nz09y869FgiubJ/Tp9e7vpq0BDnXXV9p9V8EjZxJ07Ywd6/QNItasf9JfAoT7nfmw67Y0FAoV19UKncYd0v112uO6YpfjHcgIoYDjKxA4yBhgM3y0kGRvttOSUE37mXSTHkS3FGz/pw14lemNJegEM+c2ahKfJXvT~1; bm_sv=C76CFDAC34961EDA25DD2DEDD549562A~YAAQFq3OFyTnNDqXAQAAEpr3PhwyZE/wo+pzGiab+aP4/fHnwnXY20x0/HDSr+GgkYmokZxti6TJ34kkflL7vOOyOvfSFtZonCfMP7XoF2AdkbbkUDh4Mfupen+D2lyloqMGkew5LKqZhOX+P80i//ogNuLTnF0NHQW4yNkxtJdxt2OfjplPH90udmSz/Bc8LNc0fCwU0mfavbqUdxZElO2DusCJZ/EPDUWGTsEQU4bYYpTF1iT42DswOljSBe0+dg==~1; bm_sz=2B2A74E00B49016B88C387DC3DF54839~YAAQFq3OFyXnNDqXAQAAEpr3PhwMsUBIfUFnOz5JGDl5xOwi1s2I3MAq7VJpYMqJtoRNmfs0ODgjpx+lqCs5tlFsHq470oQghAFy5r6ZTtneE2Mau2IwZG16VoGXQimCTw/SU2PeSmfUbvSRqsMJ/xj6GkUlR7TICsxl4k0lQAs4hcmsntrzU9SqGhjjo1eEiZ4+mHBa7QT7RbzIBtmWNLe4PwoFT+W2kHAsaSLyIjAWV9pRiqC2w5ipyfQfLjW/zMOphaInJOkt8t6KdKoNaG5K822OiRQeBF3laWas9iP44ltVsTAD87R+hSoUvhaNzRJtgUdGm2ovsBpgsIoSJ9VG4pKtB2YP7YSgCudXdlmVCrIZDp3bSt3b+6f0Lwpx5k+muCmiaZW5CHIet7Y1vjqwXMaZLZQEKic403xYQCWZqo2mNnOxN3eVBwMpNUnKZkM=~4600132~3162438; _ga_NEH2MEG9CT=GS2.1.s1749107923$o1$g1$t1749108075$j60$l0$h0; ak_bmsc=1C0F2247C74A0696B2D621B48121F3F6~000000000000000000000000000000~YAAQLa3OFzyc7i6XAQAAF5z3PhygOVUYZqb63dnSi8V/xsl6Q2X1WW/7RSyAPSuGkenwJhd+GguoiOrji6HuvUp+kzqVxz7Rzg9A1zaHUr6e1JotMeWsTo8oQhXedO9a+NY0XGx4lUHQcimBs/oM8kiKvhjrB211zni0LPFxkCY+gKS9Hb8Iu8mzjIzHh5njh6O0mvxkpupEjKaaAR/RS2gbcipIvuhkd+5BCAs9i6ZzuTc84g7xB0L9EcSTAlnTqgwAyfBCI2N3gcNc9l+luV70by6jk8Tw23dYn92ZxWI2GgeRRfceMasxHcRUHHDY7inoJB7qrJidv2FcputrhBABwcl5l4ujVJ5SjO9m8x26eMRziO8SH/AVRc5RTGHF6Uq8aUWvDblo7EFHyGA5EXV6mAOHqTnPbL72lhgQfvZVSYSF/EiSejzWkEBdcY20IkC5Crxcon/VOoNL+QpoQxM=; mp_60483c180bee99d71ee5c084d7bb9d20_mixpanel=%7B%22distinct_id%22%3A%20%221973ef4c6ec1d4-0e5d7abb16f6e8-26011e51-100200-1973ef4c6ed136%22%2C%22%24device_id%22%3A%20%221973ef4c6ec1d4-0e5d7abb16f6e8-26011e51-100200-1973ef4c6ed136%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22%24user_id%22%3A%20%221973ef4c6ec1d4-0e5d7abb16f6e8-26011e51-100200-1973ef4c6ed136%22%2C%22Is%20Anonymous%22%3A%20%22True%22%2C%22Instance_Id%22%3A%20%22547fe4d6-4e5f-4ea6-9e29-012dc7d8%22%2C%22Session%20ID%22%3A%20%22037a57ce-178d-4e55-92a3-4fd17b5e%22%2C%22last%20event%20time%22%3A%201749108052935%7D; _abck=CD2BD69AD7342E6124BFBEF0C63ADA1A~-1~YAAQLa3OFxed7i6XAQAAkq73Pg45Oh6kCz/0q/WnBXtEhKSHG520l25EDaECID7P+lhAEyBChWcTk8/A2ksd9D7UTovQRDRoDpFuoJc+XtclZEDcCiu9AISxC0VTrlpdIW0SQ9/7zr5QjO3eN5NB5OUcnSRZMQ6a6ci6XBPIIlhXaR5zMwu06PjGDoh7IkYFcMG2GVdnCiPCmfmFMZiCsjMj9almDIeeLYpcVTI45TiqbMve8b7ks6D5ppw/XAVLPdEU8iR3yV8JCI7kf5DhdKPj/IkscJmIQPklX4xffGqZ4Ruqqguhp2jzAg45i1KZsrqLJG+PYPXlCG9SYsER+KgjjxiuNAb4LJ9pSQJUz99nb8WGFXO+XW6jNVQ/1NHkrApMxv49CFcfbjhsU28DgyPbusttYGGJ0FflWyFgpmZ1kfVrmgfFprh5EdNoBItxL7NTy5csBdk7ekh9dXJU6x1lK+9wRHjYpi4h2nZz3IswuSvGMpjk9oaNw2F5Puyd6/tl7/Vk1+Dy+jOXO6/PWTkGT8cshNpIZRIolHd7QLMp05KocdWviv7vKPJ+b/tUD9+5WfRRvA1YZ/90mUklalDs0qYoJubRmRCjaQnc+GBnvpD+AElWSu+2RAjqf0WxZL0vUNZlWc5fLuNPrMx9BKMCdMFgPur/ZFsZMDULUNO3ybU7UvJipgkkMLB9sOIVm16OiH2mBu3Ln436HV2x0FNzKoELKKsJGzNxqIN+Q8I8vRvBIjOqA+6vPmKLcLoT9cQ+WALG5oDuJCEr1C2i6KyF08oRwn/Ae6JSyHXmrFBtKusW+N9Mr0DXgesiOUTFAeaBm5sEmDmo67JxeDZ0C8y0y6ofWKmH4HNemjs46uvl+SEHxxDHp7IOznWXlyUYGlgrQlMuEvm8ez3FTzgRjICEnhEMSDCbi3mdf7is84zYP9OKOyGLRQtanIXYPoBbl3cC1Hz34r0iGGwqbJipZWuW8N6KmWFF18YphaW6u83LmFny~-1~||0||~1749111546',
}

json_data = {
    'query': 'mobile',
    'type': 'text_search',
    'page': 1,
    'offset': 0,
    'limit': 20,
    'cursor': None,
    'isDevicePhone': False,
}

response = requests.post('https://www.meesho.com/api/v1/products/search', cookies=cookies, headers=headers, json=json_data)

print(response.status_code)
print(response.text)
print(response.json())


json_path = r'C:\Users\Madri.Gadani\Desktop\madri\meesho\meesho_json.json'
with open(json_path, 'w', encoding='utf-8') as json_file:
    json.dump(response.json(), json_file, indent=4, ensure_ascii=False)
print(f"JSON content saved to {json_path}")
# json_path = r'C:\Users\Madri.Gadani\Desktop\madri\swiggy\swiggy_raw_try2.json'

with open(json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
print(data.keys())


catalogs=data.get('catalogs', [])
print(catalogs)
print(len(catalogs))
# print(catalogs.keys())
# print(catalogs.items)
for i in catalogs:
    print(i)
    print('///////////////////////////////')





# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"query":"mobile","type":"text_search","page":1,"offset":0,"limit":20,"cursor":null,"isDevicePhone":false}'
#response = requests.post('https://www.meesho.com/api/v1/products/search', cookies=cookies, headers=headers, data=data)