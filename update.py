import requests
import json

f = open("./movie/fixtures/movie.json",'w',encoding='utf8')
key_file = open("tmdb_api.txt",'r')
API_KEY = key_file.read()
print(API_KEY)
json_content = []

for page_num in range(1,11):
    API_URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&page={page_num}'
    data = requests.get(API_URL)
    res = json.loads(data.text)
    for result in res['results']:
        model = 'movie.movie'
        fields = dict()
        fields['title'] = result['title']
        fields['overview']= result['overview']
        fields['poster_path'] = 'https://image.tmdb.org/t/p/w500'+result['poster_path']
        fields['genres'] = result['genre_ids']
        movie_data = dict()
        movie_data['model'] = model
        movie_data['fields'] = fields
        json_content.append(movie_data)
        print(result['title'])
json.dump(json_content,f,ensure_ascii=False)

f.close()
key_file.close()