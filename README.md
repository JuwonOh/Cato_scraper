# Cato_scraper

미국의 씽크탱크인 카토 연구소(Cato institute, https://www.cato.org)의 자료들(Survey Reports이외 전부)을 받아오기 위한 크롤러입니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py, parser.py 그리고 scraping_latest_news.py 총 네가지로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리하는 등 scraper가 필요한 기본적인 기능을 가지고 있습니다.
parser.py는 모아진 url리스트를 통해서 각 분석들의 제목/일자/내용 등의 문자, 시간 데이터들을 parsing 합니다.
scraper.py는 사이트내의 url 링크들을 get_soup함수를 통해 모아주고, parser를 통해서 json형식으로 변환시킵니다.
scraping_latest_news.py는 scraper.py를 통해 만들어진 json파일을 저장시켜줍니다. scraping_latest_news.py파일의 parameter는 다음과 같습니다.

Using Python script with arguments

| Argument name | Default Value | Note |
| --- | --- | --- |
| begin_date | 2018-07-01 | datetime YYYY-mm-dd |
| directory | ./output/ | Output directory |
| max_num | 1000 | Maximum number of news to be scraped |
| sleep | 1.0 | Sleep time for each news |
| verbose | False, store_true | If True use verbose mode |

만일 2018년 7월 1일부터 작성된 자료를 1000개까지 받고 싶다면 다음과 같이 실행코드를 입력해주시면 됩니다.

```
scraping_latest_news.py --begin_date 2018/07/01 --directory ./output --max_num 1000 --sleep 1.0

```

최근 순서대로 크롤링한 파일을 살펴보고 싶을때는 usage.ipynb를 사용하세요.

```
[1 / 10] (January 23, 2019) Temporary Protected Status and Immigration to the United States
[2 / 10] (January 22, 2019) How ‘Market Failure’ Arguments Lead to Misguided Policy
[3 / 10] (January 16, 2019) Do 40-Year-Old Facts Still Matter?: Long-Run Effects of Federal Oversight under the Voting Rights Act
[4 / 10] (January 15, 2019) Do Immigrants Import Terrorism?
[5 / 10] (January 15, 2019) The Myth of the Cyber Offense: The Case for Restraint
[6 / 10] (January 9, 2019) More Legislation, More Violence? The Impact of Dodd-Frank in the Democratic Republic of the Congo
[7 / 10] (January 8, 2019) The Case for an Immigration Tariff: How to Create a Price-Based Visa Category
[8 / 10] (January 2, 2019) The Spread of Deposit Insurance and the Global Rise in Bank Asset Risk since the 1970s
[9 / 10] (December 19, 2018) How Legalizing Marijuana Is  Securing the Border: The Border Wall, Drug Smuggling, and Lessons for Immigration Policy
[10 / 10] (December 19, 2018) Militarization Fails to Enhance Police Safety or Reduce Crime but May Harm Police Reputation
특정한 페이지를 parse하기 위해서는 yield_latest_report를 사용하세요.
```

## 참고 코드

본 코드는 https://github.com/lovit/whitehouse_scraper를 참조하여 만들어졌습니다.
