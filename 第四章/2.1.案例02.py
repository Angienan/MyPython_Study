"""获取高分电影的榜单数据,保存在csv文件当中
1.明确网站的robot.txt中的抓取规则
2.查看网页结构,拆解具体操作步骤:
    a.获取高分列表的数据
    b.遍历电影列表,获取每一部电影的详细信息,并提取
    c.保存电影信息到csv文件中
"""
import requests
import csv
from lxml import html
import  re

#常量
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL_1 = "https://www.themoviedb.org/movie/top-rated"
TMDB_TOP_URL_2 = "https://www.themoviedb.org/movie/top-rated?page=2"

MOVIE_LIST_FILE = "csv.data/movie_list.csv"





def get_movie_info(movie_info_url):
    response = requests.get(movie_info_url,timeout=20)
    document = html.fromstring(response.text)

    movie_names = document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div[1]/div/a/h2/text()")
    movie_years = document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div[4]/div/span[@class='release']/text()")
    movie_tags = document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div[4]/div/span[3]/text()")
    movie_cost_limes = document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div[4]/div/span[4]/text()")
    movie_scores = document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div[2]/div[1]/div[1]/div/div/div/@data_percent")

    movie_info = {
        "movie_name": movie_names[0] if movie_names else None,
        "movie_year": get_movie_years(movie_years),
        "movie_tag": movie_tags[0] if movie_tags else None,
        "movie_cost_lime": movie_cost_limes[0] if movie_cost_limes else None,
        "movie_score": movie_scores[0] if movie_scores else None
    }
    return movie_info
#保存所有电影信息到csv文件中
def save_all_movies(all_movies):
    with open(MOVIE_LIST_FILE,"w",encoding="utf-8",newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["movie_name", "movie_year", "movie_tag", "movie_cost_lime", "movie_score"])
        writer.writerows(all_movies)
#

def get_movie_years(movie_years):
     movie_year =  movie_years[0].strip() if movie_years else ''
     return movie_year.replace("(","").replace(")","")


def get_movie_publish_date(moive_dates):
    movie_date = moive_dates[0].strip() if moive_dates else ''
    return re.search(r"\d{4}-\d{2}-\d{2}",movie_date).group()
#主函数
def main():
    all_movies = []
    for page_num in range(1,6):
        # 1.发送请求
        if page_num ==1:
            response = requests.get(TMDB_TOP_URL_1, timeout=20)
        else:
            response = requests.get(TMDB_TOP_URL_2,f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-01-22&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400", timeout=20)
        # 2.解析数据
        document = html.fromstring(response.text)
        movie_list = document.xpath(f"//*[@id='page_{page_num}']/div[contains(@class, 'media-card-list')]")

        # 3.遍历电影列表,获取电影信息
        for movie in movie_list:
            movie_urls = movie.xpath("./div/div/div/a/@href")
            if movie_urls:
                # 电影详情URL
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                print(movie_info_url)

                # 发送请求,获取电影详细数据
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)


    #保存信息
    save_all_movies(all_movies)

if __name__ == '__main__':
    main()


