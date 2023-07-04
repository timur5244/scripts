import time
import requests


def oneTest(func: str) -> str:
    def wrapper() -> str:
        result = ''
        start = time.time()
        func()
        end = time.time()
        result = '[*] Время выполнения: {} секунд.'.format(end-start)
        return result
    return wrapper

def averageSpeedTest(iters = 10) -> str:
    
    def actual_decorator(func: str) -> str:

        def wrapper_ad(*args: tuple, **kwargs: dict):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total/iters))
            return return_value

        return wrapper_ad
    
    return actual_decorator

def normalize_url(text: str) -> str:
  if text[:8] == 'https://':
    return text.strip()
  elif text[:7] == 'http://':
    return (text[:4] + 's' + text[4:]).strip()
  else:
    return ('https://' + text).strip()

if __name__== '__main__':
    inputNum = int(input('Введите количество итераций: '))
    input_url = normalize_url(input('Введите url-адрес: '))

    @averageSpeedTest(iters=inputNum)
    def fetch_webpage_aST(url):
        webpage = requests.get(url)
        return webpage.text
    
    if input_url == 'https://' or input_url == None or len(input_url) <= 8:
      webpage = fetch_webpage_aST('https://google.com')
    else:
      webpage = fetch_webpage_aST(input_url)
    #print(webpage)


    @oneTest
    def fetch_webpage():
        webpage = requests.get('https://google.com')
    #print(fetch_webpage())

    