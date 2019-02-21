# Cato_scraper

미국의 씽크탱크인 Cato institute의 자료들(Survey Reports을 제외한 나머지)을 받아오기 위한 크롤러입니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py 그리고 parser.py 총 세가지로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리합니다.
scraper는 util.py내의 사이트내의 url 링크들을 get_soup함수를 통해 모아줍니다.
parser는 이렇게 만들어진 url리스트를 통해서 각 분석들의 제목/일자/내용을 모아줍니다.

```
python scraping_latest_news.py
```
특정한 페이지를 parse하기 위해서는 yield_latest_report를 사용하세요.
```
[1 / 10] (20190214) Building an Effective and Practical National Approach to Terrorism Prevention
[2 / 10] (20190214) Educator Access to and Use of Data Systems
[3 / 10] (February 20, 2019) Opioids and a Crisis of Unintended Consequences
[4 / 10] (February 19, 2019) Book Review: 'The Woman Who Smashed Codes' by Jason Fagone
[5 / 10] (20190220) Public Acceptability of Health and Social Care Funding Options
[6 / 10] (20190219) Functional Limitations and Employment Among Disability Benefit Recipients with Musculoskeletal Conditions
[7 / 10] (20190218) Science-Based Scenario Design
[8 / 10] (20190218) Assessing Retention and Special and Incentive Pays for Army and Navy Commissioned Officers in the Special Operations Forces
[9 / 10] (20190215) Market Power and Price Discrimination in the US Market for Higher Education
[10 / 10] (20190215) Organising for excellence

```

## 참고 코드

본 코드는 https://github.com/lovit/whitehouse_scraper를 참조하여 만들어졌습니다.
