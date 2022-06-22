from requests import get, utils

def currency_rates(tiket):
    target_url1 = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(target_url1.headers)
    server_data = target_url1.headers['Set-Cookie'].split(',')[1]
    print(f'дата сервера: {server_data}')

    target_content = target_url1.content.decode(encoding=encodings)

    key_words = ['Nominal', 'Name', 'Value']

    target_str = target_content[target_content.find(str(tiket).upper()):]

    if len(target_str) > 2:
        target_str = target_str[:target_str.find('</Valute>')]

        currency_info = list(map(lambda x: str(target_str.split(x)[1])[1:-2], key_words))
        currency_info[0] = int(currency_info[0])
        currency_info[2] = float('.'.join(currency_info[2].split(',')))

        print(f'За {currency_info[0]} {currency_info[1]} дают {currency_info[2]} рублей')
    else:
        print(None)


if __name__ == "__main__":
    currency_rates(input('введите тикет нужной валюты: '))
